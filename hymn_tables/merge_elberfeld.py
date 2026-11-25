# -*- coding: utf-8 -*-
"""Fold into hymns.db the table of hymns for the Sundays and festivals in the Gesangbuch für die
Evangelisch-Lutherische Kirche (Elberfeld: Verlag des Lutherischen Büchervereins, 1898), which
the Gießen University Library's record gives to the Evangelisch-Lutherische Kirche Altpreußens, as
transcribed in Elberfeld_1898_Liedertafel.csv. Run it after merge_slovak.py.

The hymnal is in "Hymnal Index/Hymnal PDFs for hotd" as the text and ALTO XML of the library's
digitization of its copy, Gb 195 (urn:nbn:de:hebis:26-digisam-123435; the image numbers here are
the library's, at digisam.ub.uni-giessen.de). The table is the fifth part of the appendix,
"Verzeichnis der Episteln und Evangelien mit Liedertafel" (appendix pp. 79-82, images 751-754):
for each of 77 Sundays and festivals, Advent 1 to the 27th Sunday after Trinity, the Reformation
and the dedication of a church, a psalm, the Epistle and the Gospel, and against each reading
three hymn numbers ("Liedernummer"), six hymns to a day. The order of service at the front of
the book does not say where these hymns are sung (it names only the creed hymn, no. 192 or 193,
and the Amen after a spoken creed, no. 246), so all six count for the day, as the several hymns
of one day do for any witness. The text's OCR loses the numbers of the table and of the alphabetical register of first
lines (appendix pp. 83-92, images 755-764), so both were read from the page images; each row
gives the first line as the register prints it, cut short, and a literal English gloss.

Each hymn is named, in this order, by:
- the lexicon, where the first line, or the hymn's row in the Lutheran Hymn Index, is a hymn it
  has (the `lexicon` column, reviewed: a first line that only begins like a lexicon hymn, as
  Paul Gerhardt's Psalm 1 does the older "Wohl dem Menschen, der wandelt nicht", is not taken);
- else the hymn's row in the Lutheran Hymn Index (`index_row`), whose title (index_titles.
  title_of_row) is then its identity, as for the modern lists that name their hymns by number,
  so that the same hymn in this book and in an American hymnal is one hymn;
- else its first line.
common_english is the lexicon's received English title, else the index's title when that is
English (for some hymns the index's title is the German one). The notes say why a hymn is not
the one that a first line or an index row would suggest. A hymn named by the lexicon must be the
lexicon's hymn of its index row, if index_rows.hymn gives one, and a hymn the lexicon does not
name must have none.
"""
import csv, difflib, os, sqlite3, sys
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import bridge, index_rows, index_titles, lexicon
from resolve import resolve
from merge_sources import provenance

LIST = 'Elberfeld_1898_Liedertafel.csv'
WITNESS = 'Elberfeld hymnal (1898)'
VIA = 'its Liedertafel'
NEW_DAYS = {'Christmas (Second Day, 26 Dec)', 'Christmas (Third Day, 27 Dec)'}
# the least agreement of a first line with a title of its index row (agreement), so that a
# misread number or a wrong row stops the build
AGREE = 0.6

def entries():
    return list(csv.DictReader(open(os.path.join(HERE, LIST), encoding='utf-8')))

def source(e):
    return f'{WITNESS} (via {VIA}; item {e["seq"]}, no. {e["number"]}, p. {e["page"]})'

_BY_SOURCE = {}
def _entry(src):
    if not _BY_SOURCE:
        for e in entries():
            _BY_SOURCE[source(e)] = e
    return _BY_SOURCE[src]

def canonical(src):
    """the lexicon's hymn of a row whose source is this list's, or None: export_xlsx.py then names
    it by index_title(src), else by its first line"""
    return _entry(src)['lexicon'] or None

def index_title(src):
    """the Lutheran Hymn Index's title for the hymn of a row the lexicon lacks, or None"""
    e = _entry(src)
    return e['index_title'] or None

def agreement(first, hid):
    """how near a first line is to a title the index records for its row, German or English
    (index_rows.agreement compares the English ones): 1.0 where one begins the other, else the
    best ratio of their words"""
    k, best = bridge.keyify(first), index_rows.agreement(first, hid)
    for o in index_rows.originals(hid):
        ko = bridge.keyify(o)
        if not ko: continue
        if k.startswith(ko) or ko.startswith(k): return 1.0
        best = max(best, difflib.SequenceMatcher(None, k, ko).ratio())
    return best

def check(es, known):
    names = {e[0] for e in lexicon.L} | set(lexicon.LATIN_EN)
    by_number = {}
    for e in es:
        where = f'merge_elberfeld: item {e["seq"]} (no. {e["number"]})'
        if e['day'] not in known and e['day'] not in NEW_DAYS:
            raise SystemExit(f'{where}: no such day {e["day"]!r}')
        if e['lexicon'] and e['lexicon'] not in names:
            raise SystemExit(f'{where}: {e["lexicon"]!r} is not in the lexicon')
        hymn = tuple(e[k] for k in ('first_line', 'literal_english', 'lexicon', 'index_row',
                                    'index_title', 'common_english'))
        if by_number.setdefault(e['number'], hymn) != hymn:
            raise SystemExit(f'{where}: the number is not the same hymn as before')
        if e['index_row']:
            hid = int(e['index_row'])
            if agreement(e['first_line'], hid) < AGREE:
                raise SystemExit(f'{where}: "{e["first_line"]}" is not index row {hid}')
            if e['index_title'] != index_titles.title_of_row(hid):
                raise SystemExit(f'{where}: index row {hid} is not "{e["index_title"]}"')
            led = index_rows.hymn(hid)[0]
            if led and led != e['lexicon']:
                raise SystemExit(f'{where}: index row {hid} is {led!r} in the lexicon')

def rows(known):
    es = entries()
    check(es, known)
    out = [(e['day'], e['first_line'], e['literal_english'], e['common_english'] or None, source(e))
           for e in es]
    return out, es

def main():
    db = sqlite3.connect(os.path.join(HERE, '..', 'hymns.db'))
    c = db.cursor()
    if c.execute('SELECT 1 FROM hymn_prescriptions WHERE source LIKE ?', (WITNESS + ' (via%',)).fetchone():
        raise SystemExit('merge_elberfeld: hymns.db has these rows already; rebuild it first '
                         '(build_hymn_db.py and the merges before this one)')
    known = {o for (o,) in c.execute('SELECT DISTINCT occasion FROM hymn_prescriptions')}
    rs, es = rows(known)
    c.executemany('INSERT INTO hymn_prescriptions (occasion,original_title,literal_english,'
                  'common_english,source) VALUES (?,?,?,?,?)', rs)
    have = {t for (t,) in c.execute('SELECT canonical_title FROM hymns')}
    new = sorted({e['lexicon'] for e in es if e['lexicon']} - have)
    for t in new:
        canon, lit, com, _alt, ok = resolve(t)
        assert ok and canon == t, t
        c.execute('INSERT INTO hymns VALUES (?,?,?,?)',
                  (t, lit, com, 'Latin' if t in lexicon.LATIN_EN else 'German'))
    c.executemany('INSERT INTO translation_candidates VALUES (?,?,?,?,?)', provenance(new))
    db.commit()
    hymns = {e['number']: e for e in es}
    if '--list' in sys.argv:
        for e in es:
            print(f'  {e["seq"]:>3} {e["day"]:<32} {e["reading"]:<7} {e["number"]:>3} '
                  f'{e["first_line"]:<36} {e["lexicon"] or e["index_title"] or "-"}')
    print(f'{WITNESS:<26}: {len(rs)} on {len({r[0] for r in rs})} occasions, '
          f'{len(hymns)} hymns')
    print(f'  named by the lexicon  : {sum(1 for e in hymns.values() if e["lexicon"])}')
    print(f'  by the index alone    : {sum(1 for e in hymns.values() if e["index_row"] and not e["lexicon"])}')
    print(f'  by their first lines  : {sum(1 for e in hymns.values() if not e["index_row"] and not e["lexicon"])}')
    print(f'  days new to the db    : {sorted({e["day"] for e in es} - known)}')
    print(f'  hymns new to the db   : {len(new)}  {new}')
    print(f'  total rows now        : {c.execute("SELECT COUNT(*) FROM hymn_prescriptions").fetchone()[0]}')
    db.close()

if __name__ == '__main__':
    main()
