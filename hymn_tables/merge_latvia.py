# -*- coding: utf-8 -*-
"""Fold into hymns.db the Sunday hymns of the Latvian Lutheran Proprium of 2006, "PROPRIUM
ekumēniskajām perikopēm: Rokasgrāmata dievkalpošanai LELB un LELBāL draudzēs", vol. 2, part 1
(Riga: the liturgy and music department of the church, October 2006; "Hymnal Index/Hymnal PDFs for
hotd/Latvia 2006.pdf"), as transcribed in Latvia_2006_Sunday_Hymns.csv. Run it after
merge_tasbh.py.

The book is the pastor's book of propers of the Evangelical Lutheran Church of Latvia (LELB) and
the Latvian Evangelical Lutheran Church Abroad (LELBāL), made by their joint liturgical commission
(Juris Cālītis, Sarma Eglīte and Vilis Kolms) for the three-year Revised Common Lectionary. For
each Sunday and feast it gives the readings of years A, B and C, the colour, the introit, the psalm,
the prayer, the Gospel verse and the preface, and, on 28 days from Advent 1 to Trinity Sunday, a
hymn: "Dziesma", by its first line and its number in a hymnal the book does not name. The foreword
puts the Gospel verse "after the Alleluia and before the Sunday hymn and the Gospel reading", so
that this is the hymn of the day, sung before the Gospel. The Epiphany and the Sundays after it,
the Transfiguration, Lent 1 and 2, the third Sunday of Easter and the Sundays after Pentecost have
none.
Misericordia Domini has two, the second after a slash; both are loaded.

Each row gives the first line, a literal English gloss, and, where the first line tells it, the
hymn it translates: 'certain' (word for word: "Es dziļās bēdās nosaucos" is "Aus tiefer Not schrei
ich zu dir") or 'probable' (it agrees in sense, on a day that suits it); a 'possible' original is
a note. The book gives only the first line and the number, so the original is told from the first
line alone. A hymn is then named by the lexicon, if the original is one of its hymns; else by the
Lutheran Hymn Index's title for the original's row (index_ref, a hymnal number on it), as the
modern lists that name their hymns by number are; else by its Latvian first line. A hymn the
lexicon names must be the lexicon's hymn of its index row.

The days take this database's labels. The book follows the Revised Common Lectionary, but names the
Lenten and Easter Sundays as of old: its fourth Sunday of Easter is Misericordia Domini, the fifth
Jubilate, the sixth Cantate and the seventh Exaudi (Rogate falls out: the foreword); they take
those days' labels here. The second Christmas
day (Otrie Ziemsvētki) has the readings of Christmas Day, not St Stephen's. New to the database is
New Year's Eve (Vecgads, 31 December).
"""
import csv, os, sqlite3, sys
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import index_rows, index_titles, lexicon
from resolve import resolve
from merge_sources import provenance

LIST = 'Latvia_2006_Sunday_Hymns.csv'
WITNESS = 'Latvian Lutheran Proprium (2006)'
VIA = 'its Sunday hymns'
NAMED = ('certain', 'probable')
NEW_DAYS = {"New Year's Eve (31 Dec)"}

def entries():
    return list(csv.DictReader(open(os.path.join(HERE, LIST), encoding='utf-8')))

def source(e):
    return f'{WITNESS} (via {VIA}; item {e["seq"]}, no. {e["number"]}, PDF p. {e["pdf_page"]})'

_BY_SOURCE = {}
def _entry(src):
    if not _BY_SOURCE:
        for e in entries():
            _BY_SOURCE[source(e)] = e
    return _BY_SOURCE[src]

def canonical(src):
    """the lexicon's hymn of a row whose source is this list's, or None: export_xlsx.py then names
    it by name(src), else by its Latvian first line"""
    e = _entry(src)
    return e['lexicon'] if e['lexicon'] and e['confidence'] in NAMED else None

def name(src):
    """the index's title for the original's row, else the original's title, or None"""
    e = _entry(src)
    if e['index_title']:
        return e['index_title']
    return e['original'] if e['original'] and e['confidence'] in NAMED else None

def check(es, known):
    names = {e[0] for e in lexicon.L} | set(lexicon.LATIN_EN)
    for e in es:
        where = f'merge_latvia: item {e["seq"]} (no. {e["number"]})'
        if e['day'] not in known and e['day'] not in NEW_DAYS:
            raise SystemExit(f'{where}: no such day {e["day"]!r}')
        if e['lexicon'] and e['lexicon'] not in names:
            raise SystemExit(f'{where}: {e["lexicon"]!r} is not in the lexicon')
        if (e['lexicon'] or e['index_ref']) and e['confidence'] not in NAMED:
            raise SystemExit(f'{where}: an identification that is not certain or probable names the hymn')
        if e['index_ref']:
            hid = index_titles.row(e['index_ref'])
            if e['index_title'] != index_titles.title_of_row(hid):
                raise SystemExit(f'{where}: the row of {e["index_ref"]} is not "{e["index_title"]}"')
            led = index_rows.hymn(hid)[0]
            if (led or '') != e['lexicon']:
                raise SystemExit(f'{where}: the row of {e["index_ref"]} is {led!r} in the lexicon')

def rows(known):
    es = entries()
    check(es, known)
    out = [(e['day'], e['first_line'], e['literal_english'], e['index_title'] or None, source(e)) for e in es]
    return out, es

def main():
    db = sqlite3.connect(os.path.join(HERE, '..', 'hymns.db'))
    c = db.cursor()
    if c.execute('SELECT 1 FROM hymn_prescriptions WHERE source LIKE ?', (WITNESS + ' (via%',)).fetchone():
        raise SystemExit('merge_latvia: hymns.db has these rows already; rebuild it first '
                         '(build_hymn_db.py and the merges before this one)')
    known = {o for (o,) in c.execute('SELECT DISTINCT occasion FROM hymn_prescriptions')}
    rs, loaded = rows(known)
    c.executemany('INSERT INTO hymn_prescriptions (occasion,original_title,literal_english,'
                  'common_english,source) VALUES (?,?,?,?,?)', rs)
    have = {t for (t,) in c.execute('SELECT canonical_title FROM hymns')}
    new = sorted({e['lexicon'] for e in loaded if e['lexicon'] and e['confidence'] in NAMED} - have)
    for t in new:
        canon, lit, com, _alt, ok = resolve(t)
        assert ok and canon == t, t
        c.execute('INSERT INTO hymns VALUES (?,?,?,?)',
                  (t, lit, com, 'Latin' if t in lexicon.LATIN_EN else 'German'))
    c.executemany('INSERT INTO translation_candidates VALUES (?,?,?,?,?)', provenance(new))
    db.commit()
    if '--list' in sys.argv:
        for e in loaded:
            print(f'  {e["seq"]:>3} {e["day"]:<34} {e["number"]:>3} {e["first_line"][:32]:<32} '
                  f'{e["lexicon"] or e["index_title"] or "-"} ({e["confidence"] or "unidentified"})')
    print(f'{WITNESS:<36}: {len(rs)} on {len({r[0] for r in rs})} occasions')
    print(f'  named by the lexicon  : {sum(1 for e in loaded if e["lexicon"])}')
    print(f'  by the index          : {sum(1 for e in loaded if e["index_ref"] and not e["lexicon"])}')
    print(f'  days new to the db    : {sorted({r[0] for r in rs} - known)}')
    print(f'  hymns new to the db   : {len(new)}  {new}')
    print(f'  total rows now        : {c.execute("SELECT COUNT(*) FROM hymn_prescriptions").fetchone()[0]}')
    db.close()

if __name__ == '__main__':
    main()
