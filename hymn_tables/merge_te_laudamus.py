# -*- coding: utf-8 -*-
"""Fold into hymns.db the chief hymns of Te Laudamus (2024), from its table of chief hymns as
transcribed in TL_Chief_Hymns.md. Run it after merge_thompson.py.

The table gives each Sunday and feast a hymn by its number in Te Laudamus (TL), one line to an
occasion: "Advent 1: 151". A number may carry TL's letters for the parts or settings it prints
("159a/b", "203a/b"); two numbers of one hymn are joined by a slash ("202/203a/b", which TL
prints as 202 and 203), and alternatives by OR ("274 OR 275"), each a chief hymn of the day.

Each number is read in TL's index of hymn titles (Hymnal Index/.../te_laudamus_index.csv), which
gives the row its original_title, as TL prints it, and found in the Lutheran Hymn Index
(Hymnal Index/hymnal.db), whose row names the hymn: the hymn of the lexicon matched to that row
(index_titles.INDEX), else the hymn the row's German or Latin original resolves to
(index_rows.hymn, which merge_krusemark.py shares). A hymn the
lexicon lacks keeps its English title as its identity, like the English titles of the other
modern lists. common_english is the hymn's title in the index (index_titles.title), which is
the lexicon's English title where the hymn is there.

The source is "Te Laudamus (2024) (via its chief-hymn table; TL n)". The occasions are the
labels the modern lists of this database use (Krusemark's), and an entry for two services
keeps them together ("Easter Evening & Easter Monday"). One hymn given twice on a day (202 and
203) is counted once.
"""
import csv, os, re, sqlite3, sys
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import index_rows, index_titles, lexicon
from resolve import resolve
from merge_sources import provenance

LIST = os.path.join(HERE, 'TL_Chief_Hymns.md')
TL_INDEX = os.path.join(HERE, '..', 'Hymnal Index', 'Hymnary Tables and PDFs', 'Te Laudamus',
                        'te_laudamus_index.csv')
WITNESS = 'Te Laudamus (2024)'
VIA = 'its chief-hymn table'

# TL's occasions -> this database's labels
OCCASION = {
 'Christmas Midnight/Dawn': 'Christmas (Midnight & Dawn)', 'Christmas Day': 'Christmas',
 'St. Stephen': 'St Stephen (26 Dec)', 'St. John': 'St John the Evangelist (27 Dec)',
 'Holy Innocents': 'Holy Innocents (28 Dec)', 'Christmas 1': 'Sunday after Christmas',
 "Circumcision and Name of Jesus (New Year's Day)": 'New Year (Circumcision)',
 'Baptism of our Lord': 'Baptism of Christ (Octave of Epiphany)',
 'Presentation of our Lord and Purification of Mary': 'Purification of Mary (2 Feb)',
 # the historic Gospel of the sixth Sunday after the Epiphany is the Transfiguration
 'Epiphany 6 (Transfiguration)': 'Epiphany 6',
 'Quinquagesima': 'Quinquagesima (Estomihi)', 'Lent 1': 'Lent 1 (Invocavit)',
 'Lent 2': 'Lent 2 (Reminiscere)', 'Lent 3': 'Lent 3 (Oculi)', 'Lent 4': 'Lent 4 (Laetare)',
 'Lent 5': 'Lent 5 (Judica)', 'Lent 6 (Palmarum)': 'Palm Sunday',
 'Annunciation': 'Annunciation (25 March)', 'Holy Saturday (Matins)': 'Holy Saturday',
 'Easter Dawn': 'Easter (Sunrise)', 'Easter Day': 'Easter',
 'Easter Evening/Easter Monday': 'Easter Evening & Easter Monday',
 'Easter 1': 'Easter 1 (Quasimodogeniti)', 'Easter 2': 'Easter 2 (Misericordias Domini)',
 'Easter 3': 'Easter 3 (Jubilate)', 'Easter 4': 'Easter 4 (Cantate)',
 'Easter 5 (Rogate)': 'Easter 5 (Rogate/Vocem jucunditatis)',
 'Easter 6': 'Sunday after Ascension (Exaudi)',
 'Pentecost Evening/Pentecost Monday': 'Pentecost Evening & Pentecost Monday',
 'Trinity': 'Trinity Sunday', 'Nativity of John the Baptist': 'St John the Baptist (24 June)',
 'Saint Peter and Saint Paul': 'St Peter and St Paul (29 June)',
 'Visitation': 'Visitation of Mary (2 July)', 'Reformation': 'Reformation (31 Oct)',
 "All Saints' Day": 'All Saints (1 Nov)',
}
KEEP = re.compile(r'^(Advent \d|Christmas Eve|Christmas 2|Epiphany( \d)?|Septuagesima|Sexagesima|'
                  r'Ash Wednesday|Maundy Thursday|Good Friday|Easter Tuesday|Ascension|Pentecost|'
                  r'Pentecost Tuesday|Trinity \d+|Thanksgiving)$')

def occasion(raw):
    if raw in OCCASION: return OCCASION[raw]
    if KEEP.match(raw): return raw
    raise SystemExit(f'merge_te_laudamus: no label for the occasion {raw!r}')

def entries():
    """(TL's occasion, [[TL reference of one hymn, ...] for each alternative]) per line"""
    out = []
    for line in open(LIST, encoding='utf-8'):
        line = line.strip()
        if not line: continue
        occ, refs = (x.strip() for x in line.rsplit(':', 1))
        alts = []
        for alt in re.split(r'\s+OR\s+', refs):
            parts, number = [], None
            for p in alt.split('/'):
                m = re.fullmatch(r'(\d+)?([a-z]?)', p.strip())
                if not m or not (m.group(1) or number):
                    raise SystemExit(f'merge_te_laudamus: cannot read {refs!r} ({line})')
                number = m.group(1) or number
                parts.append((number, m.group(2)))
            alts.append((alt, parts))
        out.append((occ, alts))
    return out

def tl_titles():
    """TL number as its index gives it ('159', '157a') -> TL's title"""
    out = {}
    for r in csv.DictReader(open(TL_INDEX, encoding='utf-8')):
        if r['alternate'] == '0':
            out.setdefault(r['number'], r['title'])
    return out

def identify(number):
    """(TL number as the index has it, TL title, canonical title or None, how) for one part"""
    titles = tl_titles()
    n, letter = number
    key = n + letter if n + letter in titles else n   # TL's index numbers 159a and 159b as 159
    if key not in titles:
        raise SystemExit(f'merge_te_laudamus: TL {n}{letter} is not in TL\'s index')
    rows = index_rows.rows('TL', n, key[len(n):])
    if len(rows) != 1:
        raise SystemExit(f'merge_te_laudamus: TL {key} is on {len(rows)} rows of the index')
    return (key, titles[key]) + index_rows.hymn(rows.pop())

_CANON = {}
def canonical(source):
    """the lexicon's hymn of a row whose source is this list's ('... (via ...; TL 202/203a/b)'), or
    None for a hymn the lexicon lacks: export_xlsx.py names TL's rows by their numbers, since an
    English title can stand for two hymns (Luther's and Jonas's Psalm 124 hymns)"""
    if source not in _CANON:
        printed = re.search(r'; TL ([^)]+)\)$', source).group(1)
        n, letter = re.fullmatch(r'(\d+)([a-z]?)', re.split(r'/', printed)[0]).groups()
        _CANON[source] = identify((n, letter))[2]
    return _CANON[source]

def rows():
    out, seen, report = [], set(), []
    for raw, alts in entries():
        occ = occasion(raw)
        for printed, parts in alts:
            hymns = [identify(p) for p in parts]
            idents = {h[2] or h[1] for h in hymns}
            if len(idents) != 1:
                raise SystemExit(f'merge_te_laudamus: {raw}: {printed} names {idents}')
            key, title, canon, how = hymns[0]
            if (occ, canon or title) in seen:
                continue
            seen.add((occ, canon or title))
            com = index_titles.title(f'TL {key}')
            if canon and canon in index_titles.INDEX:
                assert com == index_titles.english(canon)[0], (canon, com)
            out.append((occ, title, None, com, f'{WITNESS} (via {VIA}; TL {printed})'))
            report.append((raw, occ, printed, title, canon, how))
    return out, report

def main():
    db = sqlite3.connect(os.path.join(HERE, '..', 'hymns.db'))
    c = db.cursor()
    if c.execute('SELECT 1 FROM hymn_prescriptions WHERE source LIKE ?', (WITNESS + ' (via%',)).fetchone():
        raise SystemExit('merge_te_laudamus: hymns.db has these rows already; rebuild it first '
                         '(build_hymn_db.py and the merges before this one)')
    rs, report = rows()
    c.executemany('INSERT INTO hymn_prescriptions (occasion,original_title,literal_english,'
                  'common_english,source) VALUES (?,?,?,?,?)', rs)
    have = {t for (t,) in c.execute('SELECT canonical_title FROM hymns')}
    new = sorted({r[4] for r in report if r[4]} - have)
    for t in new:
        canon, lit, com, _alt, ok = resolve(t)
        assert ok and canon == t, t
        c.execute('INSERT INTO hymns VALUES (?,?,?,?)',
                  (t, lit, com, 'Latin' if t in lexicon.LATIN_EN else 'German'))
    c.executemany('INSERT INTO translation_candidates VALUES (?,?,?,?,?)', provenance(new))
    db.commit()
    if '--list' in sys.argv:
        for raw, occ, printed, title, canon, how in report:
            print(f'  {raw:<48} {printed:<11} {title:<44} {canon or "-":<44} {how}')
    print(f'Te Laudamus chief hymns: {len(rs)} on {len({r[0] for r in rs})} occasions')
    print(f'  in the lexicon        : {sum(1 for r in report if r[4])}')
    print(f'  hymns new to the db   : {len(new)}  {new}')
    print(f'  total rows now        : {c.execute("SELECT COUNT(*) FROM hymn_prescriptions").fetchone()[0]}')
    db.close()

if __name__ == '__main__':
    main()
