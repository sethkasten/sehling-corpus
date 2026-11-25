# -*- coding: utf-8 -*-
"""Fold into hymns.db the de tempore series of Lutheran Book of Worship (1978), from its
"Hymns for the Church Year" (pp. 929-931; the pages are in Hymnal Index/LBW-hotd), as
transcribed in LBW_Hymns_Church_Year.csv. Run it after merge_te_laudamus.py.

The table gives three to five hymns for each Sunday and festival. A star marks the hymns "which
constitute a contemporary adaptation of the traditional Lutheran de tempore series", and only
these are the day's chief hymns here, as only Krusemark's Hymns of the Day are. The letters A, B
and C tie a hymn to the year of the three-year lectionary whose readings it suits: of the starred
hymns, those without letters serve every year, the others the years they name ("When in the hour
of deepest need* (C)"). LBW is one witness, and its hymns for a day are those of all three years;
the source keeps LBW's day and letters: "Lutheran Book of Worship (1978) (via its Hymns for the
Church Year, 13 Pentecost; LBW 303, A)". The transcription keeps the unstarred hymns too.

LBW's days follow the three-year lectionary, whose Sundays bear other Gospels than the old
series'. They are given the labels of this database by their place in the church year: Easter
Day is the first Sunday of Easter, so 2 Easter is Quasimodogeniti and 7 Easter Exaudi; the Holy
Trinity is the first Sunday after Pentecost, so 2 Pentecost is Trinity 1 and 27 Pentecost Trinity
26; Christ the King, the last Sunday after Pentecost, is Trinity 27, the last Sunday of the
year; the Baptism of Our Lord and the Transfiguration take the labels of the modern one-year lists
(Krusemark's), and the Sunday of the Passion is Palm Sunday. 7 and 8 Epiphany, which the old
series lacks, are Epiphany 7 and 8.

Each hymn is found by its LBW number in the Lutheran Hymn Index (index_rows.hymn, as Te
Laudamus's and Krusemark's): the lexicon's hymn on that row, else a hymn the lexicon lacks, which
keeps its English title as its identity. common_english is the index's title for the row
(index_titles.title); original_title is LBW's title as printed.
"""
import csv, os, re, sqlite3, sys
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import index_rows, index_titles, lexicon
from resolve import resolve
from merge_sources import provenance

LIST = os.path.join(HERE, 'LBW_Hymns_Church_Year.csv')
WITNESS = 'Lutheran Book of Worship (1978)'
VIA = 'its Hymns for the Church Year'
# the least agreement of a printed title with a title of its numbered row (index_rows.agreement),
# so that a misread number stops the build: every number of the transcription agrees 0.75 or more
AGREE = 0.6

# LBW's days -> this database's labels (N Epiphany, N Pentecost: occasion())
OCCASION = {
 'Christmas': 'Christmas', '1 Christmas': 'Sunday after Christmas', '2 Christmas': 'Christmas 2',
 'Epiphany': 'Epiphany', 'Baptism of Our Lord': 'Baptism of Christ (Octave of Epiphany)',
 'Transfiguration': 'Transfiguration', 'Ash Wednesday': 'Ash Wednesday',
 '1 Lent': 'Lent 1 (Invocavit)', '2 Lent': 'Lent 2 (Reminiscere)', '3 Lent': 'Lent 3 (Oculi)',
 '4 Lent': 'Lent 4 (Laetare)', '5 Lent': 'Lent 5 (Judica)', 'Sunday of the Passion': 'Palm Sunday',
 'Monday in Holy Week': 'Monday in Holy Week', 'Tuesday in Holy Week': 'Tuesday in Holy Week',
 'Wednesday in Holy Week': 'Wednesday in Holy Week', 'Maundy Thursday': 'Maundy Thursday',
 'Good Friday': 'Good Friday', 'Easter Day': 'Easter',
 '2 Easter': 'Easter 1 (Quasimodogeniti)', '3 Easter': 'Easter 2 (Misericordias Domini)',
 '4 Easter': 'Easter 3 (Jubilate)', '5 Easter': 'Easter 4 (Cantate)',
 '6 Easter': 'Easter 5 (Rogate/Vocem jucunditatis)', '7 Easter': 'Sunday after Ascension (Exaudi)',
 'Ascension': 'Ascension', 'Pentecost': 'Pentecost', 'Holy Trinity': 'Trinity Sunday',
 'Christ the King': 'Trinity 27',
}

def occasion(day):
    if day in OCCASION: return OCCASION[day]
    m = re.fullmatch(r'(\d+) (Advent|Epiphany|Pentecost)', day)
    if m and m.group(2) == 'Pentecost' and int(m.group(1)) >= 2:
        return f'Trinity {int(m.group(1)) - 1}'
    if m and m.group(2) != 'Pentecost':
        return f'{m.group(2)} {m.group(1)}'
    raise SystemExit(f'merge_lbw: no label for the day {day!r}')

def entries():
    """the starred hymns, as dicts of the transcription's columns"""
    return [r for r in csv.DictReader(open(LIST, encoding='utf-8')) if r['starred']]

def numbers(entry):
    return [n.strip() for n in entry['numbers'].split(',')]

def identify(number, printed=None):
    """(canonical title or None, how, index row) of the hymn that bears LBW's number"""
    rows = index_rows.rows('LBW', number)
    if len(rows) != 1:
        raise SystemExit(f'merge_lbw: LBW {number} is on {len(rows)} rows of the index')
    hid = rows.pop()
    if printed and index_rows.agreement(printed, hid) < AGREE:
        raise SystemExit(f'merge_lbw: LBW {number} is not "{printed}" in the index')
    return index_rows.hymn(hid) + (hid,)

_CANON = {}
def canonical(source):
    """the lexicon's hymn of a row whose source is LBW's ('...; LBW 457/458, B)'), or None for a
    hymn the lexicon lacks: export_xlsx.py names LBW's rows by their numbers"""
    if source not in _CANON:
        _CANON[source] = identify(re.search(r'; LBW (\d+)', source).group(1))[0]
    return _CANON[source]

def rows():
    out, seen, report = [], set(), []
    for e in entries():
        occ = occasion(e['day'])
        nums = numbers(e)
        hymns = [identify(n, e['title']) for n in nums]
        if len({canon or hid for canon, _how, hid in hymns}) != 1:   # 457, 458: one hymn
            raise SystemExit(f'merge_lbw: {e["day"]}: LBW {nums} name {hymns}')
        canon, how, _hid = hymns[0]
        com = index_titles.title(f'LBW {nums[0]}')
        if (occ, canon or com) in seen:
            continue
        seen.add((occ, canon or com))
        if canon and canon in index_titles.INDEX:
            assert com == index_titles.english(canon)[0], (canon, com)
        note = ''.join(f', {x}' for x in (e['series'], e['gospel']) if x)
        out.append((occ, e['title'], None, com,
                    f'{WITNESS} (via {VIA}, {e["day"]}; LBW {"/".join(nums)}{note})'))
        report.append((e['day'], occ, '/'.join(nums) + note, e['title'], canon, how))
    return out, report

def main():
    db = sqlite3.connect(os.path.join(HERE, '..', 'hymns.db'))
    c = db.cursor()
    if c.execute('SELECT 1 FROM hymn_prescriptions WHERE source LIKE ?', (WITNESS + ' (via%',)).fetchone():
        raise SystemExit('merge_lbw: hymns.db has these rows already; rebuild it first '
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
        for day, occ, printed, title, canon, how in report:
            print(f'  {day:<22} {occ:<38} {printed:<16} {title:<46} {canon or "-"}')
    print(f'LBW de tempore hymns   : {len(rs)} on {len({r[0] for r in rs})} occasions')
    print(f'  in the lexicon        : {sum(1 for r in report if r[4])}')
    print(f'  hymns new to the db   : {len(new)}  {new}')
    print(f'  total rows now        : {c.execute("SELECT COUNT(*) FROM hymn_prescriptions").fetchone()[0]}')
    db.close()

if __name__ == '__main__':
    main()
