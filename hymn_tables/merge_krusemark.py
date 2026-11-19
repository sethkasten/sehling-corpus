# -*- coding: utf-8 -*-
"""Fold Krusemark's Hymn-of-the-Day rows into hymns.db.

Only the entries Krusemark marks as Hymn of the Day are inserted. His lists
also carry opening, distribution, offering and closing hymns; those are real
data but they are not chief hymns, and mixing them in would wreck the
meaning of the table. The full extraction is kept in rows_krusemark_raw.json.

Note on his Easter numbering: Krusemark counts Easter Day as Easter 1, so
his 'Easter 2, Quasimodo Geniti' is the Sunday this database already calls
'Easter 1 (Quasimodogeniti)'. The mapping below shifts them back.

His Thompson column is not loaded. It is not one witness's list: it sets out
the hymns of Ludecus and twelve other lists that Jason Thompson collates in
his dissertation (Appendix 2), and underlines those that three or more of the
lists give (Krusemark, p. 95). Ludecus is loaded in his own right, and of
Thompson's transcriptions of the other lists (rows_thompson.json) four are
loaded by merge_thompson.py and three are Sehling orders read from the corpus.
Counting the column as well would count these lists twice.

He gives each hymn by its English title and its number in a hymnal (LSB, TLH,
WH, ELH, LW), which the source keeps: "Gehrke (via Krusemark, Hymns ABC (2018);
TLH 383)". export_xlsx.py names his hymns by those numbers (identify, below),
as it names Te Laudamus's: the number's row in the Lutheran Hymn Index, and the
lexicon's hymn on that row (index_rows.hymn). A row the lexicon lacks is named
by the index's title for it (index_title), as Te Laudamus's are, so that his
lists join where they print different hymnals' wordings of one hymn; it cannot
then be taken for a lexicon hymn of a like title ("O Lord, we welcome Thee",
TLH 93, is "Ich freue mich in dir", not "Wie soll ich dich empfangen"). The title decides where the number cannot: a row
without one, or with a page of the liturgy (LSB 198), and his two misprinted
numbers, whose rows do not bear his titles (LSB 566 for 556, "Dear Christians,
One and All, Rejoice"; LSB 906 for 942, "Kyrie! God, Father").

His lists of the old usage (HISTORICAL) give a German hymn by the number of a
modern hymnal. Where that number is a translation of the Latin hymn, the hymn
is its German version, which Liliencron's English column gives the same title:
the c. 1700 plan's "Come, Holy Ghost, Creator blest" (LSB 498/9) is Luther's
"Komm, Gott Schöpfer, Heiliger Geist", which the Leipzig hymnals of 1605, 1627
and 1694 give for Pentecost, and Carpzov's "O Christ, who art the Light and
Day" (LSB 882) is "Christe, der du bist Tag und Licht", which they give for
Invocavit.
"""
import re, os, json, sqlite3, collections, sys
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import bridge, index_rows, index_titles, lexicon
from resolve import resolve
from merge_sources import provenance

COMPILATION = 'Krusemark, Hymns ABC (2018)'

# his lists of the old usage, which give each German hymn by the number of a modern hymnal
HISTORICAL = {'Carpzov', 'Bach’s Leipzig usage', 'Stiller (Leipzig/Weissenfels/Dresden, via Stiller)',
              'Liliencron de tempore plan (c. 1700, via Graff)'}
# the hymnal number at the end of a source ("; LSB 498/9)" is read as LSB 498)
REF = re.compile(r'; ([A-Z]+) (\d+)([a-z]?)(?:/\d+)?\)$')
# the least agreement of a printed title with a title of its numbered row (index_rows.agreement):
# his misprinted numbers agree 0.3 or so, every other number 0.69 or more
AGREE = 0.5

def identify(source, printed):
    """(the lexicon's hymn or None, how) for one of his rows. how is None where the number
    cannot decide and the printed title must; the hymn is None where the number's row is a hymn
    the lexicon lacks, which index_title names"""
    m = REF.search(source)
    if not m: return None, None
    rows = index_rows.rows(*m.groups())
    if len(rows) != 1: return None, None
    hid = rows.pop()
    if index_rows.agreement(printed, hid) < AGREE: return None, None
    canon, how = index_rows.hymn(hid)
    if canon in lexicon.LATIN_EN and source.split(' (via')[0] in HISTORICAL:
        german, *_ = bridge.identify(None, printed)
        if german and german not in lexicon.LATIN_EN:
            return german, how + '; the German version, in the old usage'
    return canon, how

def index_title(source):
    """the index's title for the row of the number a source gives (export_xlsx.py names by it a
    hymn the lexicon lacks), as index_titles.title gives it"""
    code, number, suffix = REF.search(source).groups()
    return index_titles.title(f'{index_rows.CODES.get(code, code)} {number}{suffix}')

_CANON = {}
def canonical(source, printed):
    """identify, kept for each row of his: export_xlsx.py asks it for every one"""
    if (source, printed) not in _CANON:
        _CANON[(source, printed)] = identify(source, printed)
    return _CANON[(source, printed)]

FIXED = {
 'Advent 1, Ad Te Levavi':'Advent 1','Advent 2, Populus Zion':'Advent 2',
 'Advent 3, Gaudete':'Advent 3','Advent 4, Rorate Coeli':'Advent 4',
 'All Saints’':'All Saints (1 Nov)','Annunciation Lord':'Annunciation (25 March)',
 'Ascension Lord':'Ascension','Ash Wednesday':'Ash Wednesday',
 'Baptism Lord':'Baptism of Christ (Octave of Epiphany)',
 'Christmas 1':'Sunday after Christmas','Christmas 2':'Christmas 2',
 'Christmastide':'Christmas','Circumcision Lord Name of Jesus':'New Year (Circumcision)',
 'Day of Thanksgiving':'Thanksgiving','Dormition Mary':'Assumption of Mary (15 Aug)',
 'Easter 2, Quasimodo Geniti':'Easter 1 (Quasimodogeniti)',
 'Easter 3, Misericordias Domini':'Easter 2 (Misericordias Domini)',
 'Easter 4, Jubilate':'Easter 3 (Jubilate)','Easter 5, Cantate':'Easter 4 (Cantate)',
 'Easter 6, Rogate':'Easter 5 (Rogate/Vocem jucunditatis)',
 'Easter 7, Exaudi':'Sunday after Ascension (Exaudi)',
 'Easter Monday':'Easter Monday','Easter Tuesday':'Easter Tuesday','Eastertide':'Easter',
 'Epiphany Lord':'Epiphany','Good Friday':'Good Friday','Holy Trinity':'Trinity Sunday',
 'Lent 1, Invocavit':'Lent 1 (Invocavit)','Lent 2, Reminiscere':'Lent 2 (Reminiscere)',
 'Lent 3, Oculi':'Lent 3 (Oculi)','Lent 4, Laetare':'Lent 4 (Laetare)',
 'Lent 5, Judica Passion Sunday':'Lent 5 (Judica)',
 'Lent 6, Palmarum Palm Sunday':'Palm Sunday','Maundy Thursday':'Maundy Thursday',
 'Michaelmas':'St Michael (29 Sept)','Nativity Lord Dawn':'Christmas (Dawn)',
 'Nativity Lord Day':'Christmas','Nativity Lord Eve Divine Service':'Christmas Eve',
 'Nativity Lord Eve Lessons and Carols':'Christmas Eve (Lessons and Carols)',
 'Nativity Lord Midnight':'Christmas (Midnight)',
 'Nativity St. John Baptist':'St John the Baptist (24 June)',
 'Pentecost Day':'Pentecost','Pentecost Monday':'Pentecost Monday',
 'Pentecost Tuesday':'Pentecost Tuesday','Pentecost Vigil':'Pentecost Vigil',
 'Purification Mary/Presentation Lord':'Purification of Mary (2 Feb)',
 'Quinquagesima':'Quinquagesima (Estomihi)','Reformation Day':'Reformation (31 Oct)',
 'Resurrection Lord, Easter Day':'Easter','Resurrection Lord, Easter Sunrise':'Easter (Sunrise)',
 'Resurrection Lord, Vigil of Easter':'Easter Vigil','Septuagesima':'Septuagesima',
 'Sexagesima':'Sexagesima','St. Peter and St. Paul':'St Peter and St Paul (29 June)',
 'Transfiguration Lord':'Transfiguration','Visitation Mary':'Visitation of Mary (2 July)',
 'St. Joseph':'St Joseph (19 March)', 'Holy Innocents':'Holy Innocents (28 Dec)',
}

def norm_occ(raw):
    raw = raw.strip()
    if raw in FIXED: return FIXED[raw]
    m = re.match(r'^(Trinity|Epiphany|Advent|Christmas)\s+(\d+)$', raw)
    if m: return f'{m.group(1)} {m.group(2)}'
    return raw

# his lists that are not loaded (see above)
NOT_LOADED = {'Thompson'}

# witnesses Krusemark shares with sources already in the database
SHARED = {
 'Gehrke, Planning the Service':'Gehrke',
 'Carpzov':'Carpzov',
 'Bach’s cantata chorales':'Bach’s Leipzig usage',
 'Zion, Detroit (2013-14)':'Zion',
 'SELK hymnal':'SELK hymnal',
}

def main():
    raw = json.load(open(os.path.join(HERE, 'rows_krusemark_raw.json'), encoding='utf-8'))
    hod = [x for x in raw if x['hod'] and x['list'] not in NOT_LOADED]
    db = sqlite3.connect(os.path.join(HERE, '..', 'hymns.db'))
    c = db.cursor()

    existing = set()
    for occ, src in c.execute('SELECT occasion, source FROM hymn_prescriptions'):
        existing.add((occ, src.split(' (via')[0]))

    rows, seen, folded = [], set(), 0
    for x in hod:
        occ = norm_occ(x['occasion_raw'])
        wit = SHARED.get(x['witness'], x['witness'])
        title = x['title']
        key = (occ, wit, title.lower())
        if key in seen: continue
        seen.add(key)
        if (occ, wit) in existing: folded += 1
        ref = f"{x['book']} {x['number']}" if x['book'] and x['number'] else None
        rows.append((occ, title, None, title,
                     f"{wit} (via {COMPILATION}{'; ' + ref if ref else ''})"))
    c.executemany('INSERT INTO hymn_prescriptions (occasion,original_title,literal_english,'
                  'common_english,source) VALUES (?,?,?,?,?)', rows)
    # the lexicon's hymns that his numbers name, for the lexicon table and its provenance
    ids = [identify(r[4], r[1]) for r in rows]
    have = {t for (t,) in c.execute('SELECT canonical_title FROM hymns')}
    new = sorted({h for h, how in ids if h} - have)
    for t in new:
        canon, lit, com, _alt, ok = resolve(t)
        assert ok and canon == t, t
        c.execute('INSERT INTO hymns VALUES (?,?,?,?)',
                  (t, lit, com, 'Latin' if t in lexicon.LATIN_EN else 'German'))
    c.executemany('INSERT INTO translation_candidates VALUES (?,?,?,?,?)', provenance(new))
    db.commit()
    by_number = [h for h, how in ids if how]
    print(f'Krusemark entries      : {len(raw)}')
    print(f'  marked Hymn of the Day: {len(hod)}')
    print(f'  inserted (deduped)    : {len(rows)}')
    print(f'  named by number       : {len(by_number)} ({sum(1 for h in by_number if h)} hymns '
          f'of the lexicon, {sum(1 for h in by_number if not h)} that it lacks)')
    print(f'  named by title        : {len(rows) - len(by_number)}')
    print(f'  hymns new to the db   : {len(new)}  {new}')
    print(f'  witnesses             : {len({r[4].split(" (via")[0] for r in rows})}')
    print(f'  occasions             : {len({r[0] for r in rows})}')
    print(f'  total rows now        : {c.execute("SELECT COUNT(*) FROM hymn_prescriptions").fetchone()[0]}')
    db.close()

if __name__ == '__main__':
    main()
