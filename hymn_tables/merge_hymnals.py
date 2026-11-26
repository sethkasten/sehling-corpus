# -*- coding: utf-8 -*-
"""Fold into hymns.db the hymns that nineteenth-century Scandinavian hymnals give for the Sundays and
holy days, as transcribed in the CSVs of LISTS. Run it after merge_ingemann.py.

- The Icelandic hymnal of 1886, "Sálmabók til kirkju- og heimasöngs" (sixth printing, Reykjavík:
  Prestaekknasjóðurinn, 1899; "Hymnal Index/Hymnal PDFs for hotd/Sálmabók til kirkju- og heimasöngs
  (1886 (1899 reprint)).pdf"): its table "Tilvísun til sálma út af guðspjöllum (og pistlum)
  helgidaganna" (PDF p. 19), the hymns on the Gospels (and Epistles) of the holy days, two or three for
  each, from which the priest chose the hymns of the Mass (the book's order of service: after the
  Epistle, "the hymn which the priest has chosen for it in the book"; then the sermon hymn).
- "Psalmebog for Kirke og Hjem" (Copenhagen, 1905 printing; "Psalmebog for Kirke og Hjem 1905.pdf"):
  its table "Psalmer til Søn- og Helligdags-Evangeliernes første (I.) og anden (II.) Tekstrække" (PDF
  pp. 721-736), the hymns named for each Sunday and holy day under each of the Danish church's two
  series of Gospels; the further numbers each series gives bare, without a first line, are not loaded.

Each row gives the first line, a literal English gloss and, where the text shows it, the hymn it
translates or is: 'certain' (word for word, or line for line in the same metre) or 'probable' (it
agrees in sense, on a day that suits it). A hymn is named by the lexicon, if the original is one of its
hymns; else by the Lutheran Hymn Index's title for the original's row (index_ref, a hymnal number on
it); else by the original's title; else by its own first line. A Danish hymn that is its own original
is named the same way, so that the Icelandic translation of it and the Danish lists group together:
Ingemann's hymns by their first lines as printed in his Høimesse-Psalmer (1825), others by the Danish
book's first line or the index's title for it.
"""
import csv, os, sqlite3, sys
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import index_rows, index_titles, lexicon
from resolve import resolve
from merge_sources import provenance

# (witness, CSV, how its rows were read, days new to the database)
LISTS = [
    ('Icelandic hymnal (1886)', 'Salmabok_1886_Holy_Day_Hymns.csv', 'its table of hymns for the holy days', set()),
    ('Psalmebog for Kirke og Hjem (1905)', 'PfKoH_1905_Sunday_Hymns.csv', 'its table of hymns for the Sundays', set()),
]
WITNESSES = {w for w, _c, _v, _n in LISTS}
NAMED = ('certain', 'probable')

def entries(path):
    return list(csv.DictReader(open(os.path.join(HERE, path), encoding='utf-8')))

def source(witness, via, e):
    series = f'series {e["series"]}, ' if e.get('series') else ''
    return f'{witness} (via {via}; item {e["seq"]}, {series}no. {e["number"]}, PDF p. {e["pdf_page"]})'

_BY_SOURCE = {}
def _entry(src):
    if not _BY_SOURCE:
        for w, path, via, _n in LISTS:
            for e in entries(path):
                _BY_SOURCE[source(w, via, e)] = e
    return _BY_SOURCE[src]

def canonical(src):
    """the lexicon's hymn of a row whose source is one of these lists', or None: export_xlsx.py then
    names it by name(src), else by its first line"""
    e = _entry(src)
    return e['lexicon'] if e['lexicon'] and e['confidence'] in NAMED else None

def name(src):
    """the index's title for the original's row, else the original's title, or None"""
    e = _entry(src)
    if e['index_title']:
        return e['index_title']
    return e['original'] if e['original'] and e['confidence'] in NAMED else None

def check(witness, es, known, new_days):
    names = {e[0] for e in lexicon.L} | set(lexicon.LATIN_EN)
    for e in es:
        where = f'merge_hymnals: {witness}, item {e["seq"]} (no. {e["number"]})'
        if e['day'] not in known and e['day'] not in new_days:
            raise SystemExit(f'{where}: no such day {e["day"]!r}')
        if e['lexicon'] and e['lexicon'] not in names:
            raise SystemExit(f'{where}: {e["lexicon"]!r} is not in the lexicon')
        if (e['lexicon'] or e['index_ref'] or e['original']) and e['confidence'] not in NAMED:
            raise SystemExit(f'{where}: an identification that is not certain or probable names the hymn')
        if e['index_ref']:
            hid = index_titles.row(e['index_ref'])
            if e['index_title'] != index_titles.title_of_row(hid):
                raise SystemExit(f'{where}: the row of {e["index_ref"]} is not "{e["index_title"]}"')
            led = index_rows.hymn(hid)[0]
            if (led or '') != e['lexicon']:
                raise SystemExit(f'{where}: the row of {e["index_ref"]} is {led!r} in the lexicon')

def rows(known):
    out, loaded = [], []
    for w, path, via, new_days in LISTS:
        es = entries(path)
        check(w, es, known, new_days)
        out += [(e['day'], e['first_line'], e['literal_english'], e['index_title'] or None, source(w, via, e))
                for e in es]
        loaded += [(w, e) for e in es]
    return out, loaded

def main():
    db = sqlite3.connect(os.path.join(HERE, '..', 'hymns.db'))
    c = db.cursor()
    for w in WITNESSES:
        if c.execute('SELECT 1 FROM hymn_prescriptions WHERE source LIKE ?', (w + ' (via%',)).fetchone():
            raise SystemExit('merge_hymnals: hymns.db has these rows already; rebuild it first '
                             '(build_hymn_db.py and the merges before this one)')
    known = {o for (o,) in c.execute('SELECT DISTINCT occasion FROM hymn_prescriptions')}
    rs, loaded = rows(known)
    c.executemany('INSERT INTO hymn_prescriptions (occasion,original_title,literal_english,'
                  'common_english,source) VALUES (?,?,?,?,?)', rs)
    have = {t for (t,) in c.execute('SELECT canonical_title FROM hymns')}
    new = sorted({e['lexicon'] for _w, e in loaded if e['lexicon'] and e['confidence'] in NAMED} - have)
    for t in new:
        canon, lit, com, _alt, ok = resolve(t)
        assert ok and canon == t, t
        c.execute('INSERT INTO hymns VALUES (?,?,?,?)',
                  (t, lit, com, 'Latin' if t in lexicon.LATIN_EN else 'German'))
    c.executemany('INSERT INTO translation_candidates VALUES (?,?,?,?,?)', provenance(new))
    db.commit()
    for w, _path, _via, _n in LISTS:
        mine = [(r, e) for r, (ww, e) in zip(rs, loaded) if ww == w]
        named = [e for _r, e in mine if e['confidence'] in NAMED]
        print(f'{w:<36}: {len(mine)} on {len({r[0] for r, _e in mine})} occasions')
        print(f'  named by the lexicon  : {sum(1 for e in named if e["lexicon"])}')
        print(f'  by the index          : {sum(1 for e in named if e["index_ref"] and not e["lexicon"])}')
        print(f'  by the original       : {sum(1 for e in named if not e["index_ref"] and not e["lexicon"])}')
    print(f'  days new to the db    : {sorted({r[0] for r in rs} - known)}')
    print(f'  hymns new to the db   : {len(new)}  {new}')
    print(f'  total rows now        : {c.execute("SELECT COUNT(*) FROM hymn_prescriptions").fetchone()[0]}')
    db.close()

if __name__ == '__main__':
    main()
