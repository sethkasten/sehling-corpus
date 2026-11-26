# -*- coding: utf-8 -*-
"""Fold into hymns.db the hymns of the day of the liturgical calendar of the Russian Lutheran Church
(the Evangelical Lutheran Church of Ingria), "Литургический календарь 2025-26" ("Hymnal
Index/Hymnal PDFs for hotd/Ingria liturgical calendar 2025-26.pdf", from elci.ru), as transcribed
in Ingria_2025-26_Hymns_of_the_Day.csv. Run it after merge_elberfeld.py.

The calendar runs through the calendar year 2026, from 29 December 2025 to 3 January 2027, a week
to a page, on the one-year lectionary with the Sundays after Trinity. For each Sunday and feast it
gives the theme, the colour, the introit, the psalm and the readings, and a line of hymn numbers
("Гимны"), with alternatives in parentheses, in the hymnal of the church, the "Сборник гимнов
Евангелическо-Лютеранской Церкви Ингрии" (2015; elci.ru/wp-content/uploads/2020/03/Sbornik-gimnov.pdf).
The line has seven places, which follow the hymnal's order of the Eucharistic service: the opening
hymn, the Gloria ("Laudamus", or in Advent, Lent and at Christmas a hymn in its place), the hymn
between the Epistle and the Gospel, and four more (the creed or sermon, the offering, the
communion, the end). The calendar does not label them; the third is the hymn between the readings,
the gradual hymn of the Finnish order the church keeps, as of the Finnish handbooks loaded by
merge_finnish.py, and it and its alternatives are the hymns of the day loaded here, one witness.
The whole line is kept in the transcription. On Good Friday the calendar gives eleven hymns for
three services without saying which is sung between the readings, and none is loaded. New Year's
Day and the 2nd Sunday after Christmas fall twice, in 2026 and in 2027, with the same hymns, and
each hymn is loaded once.

Each row gives the hymn's first line from the hymnal's table of contents, a literal English gloss,
and the hymnal's credit (author, translator, tune) in English. Most of the hymns are Russian,
Finnish or English; where the credit and the text show the hymn translated, the transcription names
the original, 'certain' or 'probable' (a 'possible' original is a note). A hymn is then named by
the lexicon, if the original is one of its hymns; else by the Lutheran Hymn Index's title for the
original's row (index_ref, a hymnal number on it: a row's id moves as rows are added), as for the
modern lists that name their hymns by number; else by the original's title; else by its Russian
first line. A hymn the lexicon names must be the lexicon's hymn of its index row, if index_rows.hymn
gives one.

The days take this database's labels. The 1st Sunday after the Epiphany is kept as the Baptism of
the Lord, and the last three Sundays of the church year take the old series' days by their Gospels:
the third from the end (Matthew 24:15-27) the 25th Sunday after Trinity, the second-last (Matthew
25:1-13) the 27th, and the last, Judgment Sunday (Matthew 25:31-46), the 26th.
"""
import csv, os, sqlite3, sys
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import index_rows, index_titles, lexicon
from resolve import resolve
from merge_sources import provenance

LIST = 'Ingria_2025-26_Hymns_of_the_Day.csv'
WITNESS = 'Church of Ingria calendar (2025-26)'
VIA = 'its liturgical calendar'
NAMED = ('certain', 'probable')

def entries():
    return list(csv.DictReader(open(os.path.join(HERE, LIST), encoding='utf-8')))

def source(e):
    return f'{WITNESS} (via {VIA}; item {e["seq"]}, no. {e["number"]}, PDF p. {e["pdf_page"]})'

_BY_SOURCE = {}
def _entry(src):
    if not _BY_SOURCE:
        for e in entries():
            if e['number']:
                _BY_SOURCE[source(e)] = e
    return _BY_SOURCE[src]

def canonical(src):
    """the lexicon's hymn of a row whose source is this list's, or None: export_xlsx.py then names
    it by name(src), else by its Russian first line"""
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
        if not e['number']: continue
        where = f'merge_ingria: item {e["seq"]} (no. {e["number"]})'
        if e['day'] not in known:
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
            if led and led != e['lexicon']:
                raise SystemExit(f'{where}: the row of {e["index_ref"]} is {led!r} in the lexicon')

def rows(known):
    es = entries()
    check(es, known)
    out, loaded, seen = [], [], set()
    for e in es:
        if not e['number'] or (e['day'], e['number']) in seen:
            continue                      # Good Friday's line; a day's hymn a second year
        seen.add((e['day'], e['number']))
        out.append((e['day'], e['first_line'], e['literal_english'], e['common_english'] or None, source(e)))
        loaded.append(e)
    return out, loaded

def main():
    db = sqlite3.connect(os.path.join(HERE, '..', 'hymns.db'))
    c = db.cursor()
    if c.execute('SELECT 1 FROM hymn_prescriptions WHERE source LIKE ?', (WITNESS + ' (via%',)).fetchone():
        raise SystemExit('merge_ingria: hymns.db has these rows already; rebuild it first '
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
    hymns = {e['number']: e for e in loaded}
    if '--list' in sys.argv:
        for e in loaded:
            print(f'  {e["seq"]:>3} {e["day"]:<34} {e["position"]:<15} {e["number"]:>3} {e["literal_english"][:40]:<40} '
                  f'{e["lexicon"] or e["index_title"] or e["original"] or "-"}')
    print(f'{WITNESS:<36}: {len(rs)} on {len({r[0] for r in rs})} occasions, {len(hymns)} hymns')
    print(f'  named by the lexicon  : {sum(1 for e in hymns.values() if e["lexicon"])}')
    print(f'  by the index          : {sum(1 for e in hymns.values() if e["index_ref"] and not e["lexicon"])}')
    print(f'  by the original       : {sum(1 for e in hymns.values() if e["original"] and e["confidence"] in NAMED and not e["lexicon"] and not e["index_ref"])}')
    print(f'  hymns new to the db   : {len(new)}  {new}')
    print(f'  total rows now        : {c.execute("SELECT COUNT(*) FROM hymn_prescriptions").fetchone()[0]}')
    db.close()

if __name__ == '__main__':
    main()
