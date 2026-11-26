# -*- coding: utf-8 -*-
"""Fold into hymns.db the chief hymns of the 2022 Supplement of the Augustana Service Book and
Hymnal (TASBH), as a review of it lists them, transcribed in TASBH_2022_Chief_Hymns.csv. Run it
after merge_zavorka.py.

The review is "Tacky Hymns 103" on the blog A Fort Made of Books (RobbieFish, 12 November 2023;
https://afortmadeofbooks.blogspot.com/2023/11/tacky-hymns-103.html). The Supplement (Malone,
Texas: Repristination Press, 2022) is the first part of the hymnal the Evangelical Lutheran
Diocese of North America (ELDoNA) is preparing, and the review lists its Office Hymns: the chief
hymn of each Sunday and feast of the one-year series in the order of the year, numbered 1-65
(Advent 1 to Trinity 27), and of some saints' days (67-109), whose numbers leave gaps, it seems
for the days the full hymnal will add. Neither the Supplement nor an index of it has been seen:
the review gives each hymn's number, day and first line, and names the tune it is set to (the
Supplement prints no tune names, but often the German original's first line). It is a modern
witness, which Appendix 8.A leaves out.

Each hymn is found by the number of the same text in another hymnal of the Lutheran Hymn Index
(the transcription's `ref`: TLH 95 for "Savior of the heathen, come"), whose row must bear the
first line (index_rows.agreement), and named as Te Laudamus's and LBW's are (index_rows.hymn):
the lexicon's hymn on that row, else a hymn the lexicon lacks, which keeps the index's English
title as its identity. A hymn the index lacks is named by the lexicon (`lexicon`): Trinity 15's
"Why art thou thus cast down, my heart" is "Warum betrübst du dich, mein Herz". common_english is
the index's title for the row, else the lexicon's English title; original_title is the first line
as the review gives it.

The days take this database's labels, the modern lists' (as Te Laudamus's): Lent 6 is Palm
Sunday, Easter 1-5 are Quasimodogeniti to Rogate, the Sunday after the Ascension is Exaudi, the
Presentation of our Lord is the Purification (2 Feb); four saints' days are new: St Lucy (13
Dec), St Henry of Finland (19 Jan, as the review's list of the book's festivals dates it), St
Titus (26 Jan) and St Patrick (17 March). Trinity 19 repeats Trinity Sunday's hymn (38 and 57).
109, "Jesus calls us; o'er the tumult", has no day in the list; it is loaded as St Andrew's (30
Nov), for which Cecil Frances Alexander wrote it and which stands there if the saints' days run
from December to November (the project owner's decision).
"""
import csv, os, sqlite3, sys
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import index_rows, index_titles, lexicon
from resolve import resolve
from merge_sources import provenance

LIST = os.path.join(HERE, 'TASBH_2022_Chief_Hymns.csv')
WITNESS = 'Augustana Service Book and Hymnal, Supplement (2022)'
VIA = 'A Fort Made of Books, Tacky Hymns 103, 2023'
# the least agreement of a first line with a title of its ref's row (index_rows.agreement), so that
# a wrong number stops the build: every ref agrees 0.85 or more ("Look down, O Lord, from heav'n,
# behold", TLH 260's "O Lord, look down from heaven, behold")
AGREE = 0.8
NEW_DAYS = {'St Lucy (13 Dec)', 'St Henry of Finland (19 Jan)', 'St Titus (26 Jan)', 'St Patrick (17 March)'}

def entries():
    return list(csv.DictReader(open(LIST, encoding='utf-8')))

def source(e):
    return f'{WITNESS} (via {VIA}; TASBH {e["number"]})'

_BY_SOURCE = {}
def _entry(src):
    if not _BY_SOURCE:
        for e in entries():
            _BY_SOURCE[source(e)] = e
    return _BY_SOURCE[src]

def identify(e):
    """(canonical title or None, how, common English title) of an entry's hymn"""
    where = f'merge_tasbh: TASBH {e["number"]} ("{e["first_line"]}")'
    if e['ref']:
        code, number = e['ref'].split()
        rows = index_rows.rows(code, number)
        if len(rows) != 1:
            raise SystemExit(f'{where}: {e["ref"]} is on {len(rows)} rows of the index')
        hid = rows.pop()
        if index_rows.agreement(e['first_line'], hid) < AGREE:
            raise SystemExit(f'{where}: the row of {e["ref"]} does not bear that first line')
        canon, how = index_rows.hymn(hid)
        if e['lexicon'] and e['lexicon'] != canon:
            raise SystemExit(f'{where}: the row of {e["ref"]} is {canon!r}, not {e["lexicon"]!r}')
        return canon, f'{e["ref"]}: {how}', index_titles.title(e['ref'])
    if not e['lexicon']:
        raise SystemExit(f'{where}: neither a ref nor the lexicon names it')
    english = index_titles.english(e['lexicon'])
    return e['lexicon'], 'the lexicon', english[0] if english else resolve(e['lexicon'])[2]

_CANON = {}
def canonical(src):
    """the lexicon's hymn of a row whose source is this list's, or None for a hymn the lexicon lacks:
    export_xlsx.py then names it by the index's title for its row, as TL's and LBW's"""
    if src not in _CANON:
        _CANON[src] = identify(_entry(src))[0]
    return _CANON[src]

def check(es, known):
    names = {e[0] for e in lexicon.L} | set(lexicon.LATIN_EN)
    for e in es:
        if e['loaded'] != 'yes':
            continue
        where = f'merge_tasbh: TASBH {e["number"]} ("{e["first_line"]}")'
        if e['occasion'] not in known and e['occasion'] not in NEW_DAYS:
            raise SystemExit(f'{where}: no such day {e["occasion"]!r}')
        if e['lexicon'] and e['lexicon'] not in names:
            raise SystemExit(f'{where}: {e["lexicon"]!r} is not in the lexicon')

def rows(known):
    es = entries()
    check(es, known)
    out, report = [], []
    for e in es:
        if e['loaded'] != 'yes':
            continue
        canon, how, com = identify(e)
        if canon and canon in index_titles.INDEX:
            assert com == index_titles.english(canon)[0], (canon, com)
        out.append((e['occasion'], e['first_line'], None, com, source(e)))
        report.append((e, canon, how))
    return out, report

def main():
    db = sqlite3.connect(os.path.join(HERE, '..', 'hymns.db'))
    c = db.cursor()
    if c.execute('SELECT 1 FROM hymn_prescriptions WHERE source LIKE ?', (WITNESS + ' (via%',)).fetchone():
        raise SystemExit('merge_tasbh: hymns.db has these rows already; rebuild it first '
                         '(build_hymn_db.py and the merges before this one)')
    known = {o for (o,) in c.execute('SELECT DISTINCT occasion FROM hymn_prescriptions')}
    rs, report = rows(known)
    c.executemany('INSERT INTO hymn_prescriptions (occasion,original_title,literal_english,'
                  'common_english,source) VALUES (?,?,?,?,?)', rs)
    have = {t for (t,) in c.execute('SELECT canonical_title FROM hymns')}
    new = sorted({canon for _e, canon, _how in report if canon} - have)
    for t in new:
        canon, lit, com, _alt, ok = resolve(t)
        assert ok and canon == t, t
        c.execute('INSERT INTO hymns VALUES (?,?,?,?)',
                  (t, lit, com, 'Latin' if t in lexicon.LATIN_EN else 'German'))
    c.executemany('INSERT INTO translation_candidates VALUES (?,?,?,?,?)', provenance(new))
    db.commit()
    if '--list' in sys.argv:
        for e, canon, how in report:
            print(f'  {e["number"]:>3} {e["occasion"]:<38} {e["first_line"][:40]:<40} {canon or "-":<38} {how}')
    print(f'{WITNESS}: {len(rs)} on {len({r[0] for r in rs})} occasions')
    print(f'  in the lexicon        : {sum(1 for _e, canon, _how in report if canon)}')
    print(f'  days new to the db    : {sorted({r[0] for r in rs} - known)}')
    print(f'  hymns new to the db   : {len(new)}  {new}')
    print(f'  total rows now        : {c.execute("SELECT COUNT(*) FROM hymn_prescriptions").fetchone()[0]}')
    db.close()

if __name__ == '__main__':
    main()
