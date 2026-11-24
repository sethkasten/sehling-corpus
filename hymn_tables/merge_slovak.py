# -*- coding: utf-8 -*-
"""Fold into hymns.db two Slovak Lutheran lists of hymns for the Sundays after Trinity, from Table 2
of Peter Ruščin, "Postilové piesne a rozpisy spevov na nedele cirkevného roka v slovenských
evanjelických prameňoch obdobia baroka", in Pramene slovenskej hudby XI: Hudba a liturgia
(Bratislava, 2023), pp. 133-154 (the volume is in "Hymnal Index/Hymnal PDFs for hotd"; the table
is on pp. 146-151, PDF pp. 148-153), as transcribed in Ruscin_Slovak_Trinity_Songs.csv. Run it
after merge_finnish.py.

The Slovak Lutherans sang in Czech. Ruščin's table sets side by side, Sunday by Sunday, the songs
that five sources give for the Sundays after Trinity:

- the register of the Cithara Sanctorum printed at Levoča in 1674, "Poznamenání písní některých
  k obecným nedělím po sv. Trojici případných", four hymns for each of 25 Sundays, from which the
  cantor chose the hymns of the day ("de tempore") for after the Epistle and after the sermon;
- the manuscript hymnal B III-107 of the Literary Archive of the Slovak National Library in
  Martin (c. 1674-1720), with the songs a congregation of central Slovakia sang before and after
  the sermon on these Sundays;
- and three collections of songs on the Sunday Gospels, each the work of one author: Eliáš
  Mlynárových (1707), Matej Bodó (1743) and Ján Blasius (1741, 1745).

The first two are lists of hymns of the day and are loaded here, each as one witness. The three
collections are not: each gives a new text of its author's for each Gospel, which no other witness
can share, and Ruščin finds that they were sung little in church. The transcription keeps them,
with the tunes they name.

As with the Finnish lists, each row gives the hymn as printed, a literal English gloss of it, and
the German or Latin hymn it translates where that can be told, 'certain', 'probable' or
'possible'; only certain and probable identifications name the hymn (canonical(), for
export_xlsx.py), and a hymn not so named keeps its Czech title.
"""
import csv, os, sqlite3, sys
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import lexicon
from resolve import resolve
from merge_sources import provenance

LIST = 'Ruscin_Slovak_Trinity_Songs.csv'
# the transcription's sources that are loaded -> their witnesses
LOADED = {
 'Cithara Sanctorum 1674': 'Cithara Sanctorum (Levoča, 1674)',
 'B III-107': 'Slovak manuscript B III-107 (c. 1674-1720)',
}
WITNESSES = list(LOADED.values())
VIA = "Ruščin's table"
NAMED = ('certain', 'probable')

def entries():
    return list(csv.DictReader(open(os.path.join(HERE, LIST), encoding='utf-8')))

def source(e):
    return f'{LOADED[e["source"]]} (via {VIA}; item {e["seq"]}, PDF p. {e["pdf_page"]})'

def named(e):
    """the lexicon's hymn of a transcribed row, or None"""
    return e['lexicon'] if e['confidence'] in NAMED and e['lexicon'] else None

_CANON = {}
def canonical(src):
    """the lexicon's hymn of a row whose source is one of these lists', or None for a hymn not
    identified: export_xlsx.py names these rows by their Czech titles"""
    if not _CANON:
        for e in entries():
            if e['source'] in LOADED:
                _CANON[source(e)] = named(e)
    return _CANON[src]

def rows(known):
    out, report = [], []
    names = {e[0] for e in lexicon.L} | set(lexicon.LATIN_EN)
    for e in entries():
        if e['source'] not in LOADED:
            continue
        if e['day'] not in known:
            raise SystemExit(f'merge_slovak: item {e["seq"]}: no such day {e["day"]!r}')
        if e['lexicon'] and e['lexicon'] not in names:
            raise SystemExit(f'merge_slovak: item {e["seq"]}: {e["lexicon"]!r} is not in the lexicon')
        canon = named(e)
        com = resolve(canon)[2] if canon else None
        out.append((e['day'], e['title'], e['literal_english'], com, source(e)))
        report.append((LOADED[e['source']], e['seq'], e['day'], e['title'], canon, e['confidence']))
    return out, report

def main():
    db = sqlite3.connect(os.path.join(HERE, '..', 'hymns.db'))
    c = db.cursor()
    if c.execute('SELECT 1 FROM hymn_prescriptions WHERE source LIKE ?', (f'% (via {VIA};%',)).fetchone():
        raise SystemExit('merge_slovak: hymns.db has these rows already; rebuild it first '
                         '(build_hymn_db.py and the merges before this one)')
    known = {o for (o,) in c.execute('SELECT DISTINCT occasion FROM hymn_prescriptions')}
    rs, report = rows(known)
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
        for w, seq, day, title, canon, conf in report:
            print(f'  {w[:22]:<22} {seq:>3} {day:<12} {title:<44} {canon or "-"} ({conf or "unidentified"})')
    for w in WITNESSES:
        mine = [r for r in report if r[0] == w]
        print(f'{w:<44}: {len(mine)} on {len({r[2] for r in mine})} occasions, '
              f'{sum(1 for r in mine if r[4])} named by the lexicon')
    print(f'  hymns new to the db   : {len(new)}  {new}')
    print(f'  total rows now        : {c.execute("SELECT COUNT(*) FROM hymn_prescriptions").fetchone()[0]}')
    db.close()

if __name__ == '__main__':
    main()
