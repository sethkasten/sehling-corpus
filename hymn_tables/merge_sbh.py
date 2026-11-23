# -*- coding: utf-8 -*-
"""Fold into hymns.db the Hymn of the Week of the Service Book and Hymnal (1958), as the American
Lutheran Church set it out in 1965: from the index of hymns on the sleeve of its three records,
"a Time for Singing: around the year with the Hymn-of-the-Week" (a photograph of the sleeve is in
the owner's Google Drive, Hymnal Project/Large PDFs/Hymn of the week - a songbook (SBH
Companion).jpg), as transcribed in SBH_Hymn_of_the_Week.csv. Run it after merge_lbw.py.

The sleeve lists the 62 hymns of the records side by side, under the seasons, "in the order of
their appropriateness for the seasons of the church year": one hymn to a Sunday or festival, in
the order of the year. Each title has two numbers: before it, its page in The Hymn-of-the-Week
Songbook (Augsburg, 1965), and after it, its number in the Service Book and Hymnal (SBH). The
pages do not follow the order of the year; the order of the records does. (Pages 12 and 46
stand twice and 11, 33, 55 and 63 are wanting, it seems by the songbook's layout rather than by
misprint: two short hymns share each of 12 and 46, and four long hymns run across an opening,
10-11, 32-33, 54-55 and 62-63; see HYMN_GUIDE.md.) The records are stacked, so that sides
1-3 play and then 4-6; the sleeve prints sides 4, 5 and 6 from right to left, under sides 3, 2
and 1. Read in that order, the hymns fall on the days of the transcription's `day` column:

- Advent 1-4; Christmas, the Sunday after Christmas and the second Sunday after Christmas
  (Christmas 2, the modern lists' label), the Sundays of the Christmas weeks;
- the Epiphany, Epiphany 1-4, and the Transfiguration, which the SBH keeps on the last Sunday
  after the Epiphany ("God's Word Is Our Great Heritage": "hear him");
- Septuagesima, Sexagesima and Quinquagesima ("Alleluia, Song of Sweetness", the farewell to the
  Alleluia before Lent); Lent 1-5; Palm Sunday; Good Friday;
- Easter, Easter 1-5, the Ascension and Exaudi ("The King of Love My Shepherd Is" on the Sunday
  of the Good Shepherd, Misericordias Domini);
- Pentecost; the Holy Trinity ("Father Most Holy") and Trinity 1-27, the sleeve's four "cycles"
  of the Trinity season, the last "Wake, Awake" (Wachet auf), as the old series has it;
- the Reformation and All Saints' Day.

Each hymn is found by its SBH number in the Lutheran Hymn Index (index_rows.hymn, as LBW's,
Te Laudamus's and Krusemark's), where the SBH's hymns of two tunes are numbered 8a and 8b: the
lexicon's hymn on that row, else a hymn the lexicon lacks, which keeps the index's English title
as its identity. common_english is the index's title for the row; original_title is the title as
the sleeve prints it.
"""
import csv, os, re, sqlite3, sys
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import index_rows, index_titles, lexicon
from resolve import resolve
from merge_sources import provenance

LIST = os.path.join(HERE, 'SBH_Hymn_of_the_Week.csv')
WITNESS = 'Hymn of the Week (SBH, 1965)'
VIA = 'a Time for Singing'
# the least agreement of a printed title with a title of its numbered row (index_rows.agreement),
# so that a misread number stops the build: every number of the transcription agrees fully
AGREE = 0.6

def entries():
    return list(csv.DictReader(open(LIST, encoding='utf-8')))

def identify(number, printed=None):
    """(canonical title or None, how, index row) of the hymn that bears the SBH number"""
    rows = index_rows.rows('SBH', number) or index_rows.rows_lettered('SBH', number)
    if len(rows) != 1:
        raise SystemExit(f'merge_sbh: SBH {number} is on {len(rows)} rows of the index')
    hid = rows.pop()
    if printed and index_rows.agreement(printed, hid) < AGREE:
        raise SystemExit(f'merge_sbh: SBH {number} is not "{printed}" in the index')
    return index_rows.hymn(hid) + (hid,)

_CANON = {}
def canonical(source):
    """the lexicon's hymn of a row whose source is this list's ('...; SBH 98, songbook p. 25)'),
    or None for a hymn the lexicon lacks: export_xlsx.py names these rows by their numbers"""
    if source not in _CANON:
        _CANON[source] = identify(re.search(r'; SBH (\d+)', source).group(1))[0]
    return _CANON[source]

def rows():
    out, report = [], []
    days = set()
    for e in entries():
        if e['day'] in days:
            raise SystemExit(f'merge_sbh: two hymns for {e["day"]}')
        days.add(e['day'])
        canon, how, hid = identify(e['sbh'], e['title'])
        com = index_titles.title_of_row(hid)
        if canon and canon in index_titles.INDEX:
            assert com == index_titles.english(canon)[0], (canon, com)
        out.append((e['day'], e['title'], None, com,
                    f'{WITNESS} (via {VIA}, side {e["side"]}; SBH {e["sbh"]}, songbook p. {e["songbook_page"]})'))
        report.append((e['track'], e['day'], e['sbh'], e['title'], canon, how))
    return out, report

def main():
    db = sqlite3.connect(os.path.join(HERE, '..', 'hymns.db'))
    c = db.cursor()
    if c.execute('SELECT 1 FROM hymn_prescriptions WHERE source LIKE ?', (WITNESS + ' (via%',)).fetchone():
        raise SystemExit('merge_sbh: hymns.db has these rows already; rebuild it first '
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
        for track, day, sbh, title, canon, how in report:
            print(f'  {track:>2} {day:<38} SBH {sbh:>3} {title:<44} {canon or "-"}')
    print(f'SBH Hymn of the Week   : {len(rs)} on {len({r[0] for r in rs})} occasions')
    print(f'  in the lexicon        : {sum(1 for r in report if r[4])}')
    print(f'  hymns new to the db   : {len(new)}  {new}')
    print(f'  total rows now        : {c.execute("SELECT COUNT(*) FROM hymn_prescriptions").fetchone()[0]}')
    db.close()

if __name__ == '__main__':
    main()
