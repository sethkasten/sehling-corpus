# -*- coding: utf-8 -*-
"""Fold into hymns.db the hymns of the Mass that the "Rubryka" of Tobiáš Závorka Lipenský's hymnal
gives for the Sundays and feasts of the year, as transcribed in Zavorka_1602_Rubryka.csv. Run it
after merge_ingria.py.

The book is "Písně chval božských" (Prague: Jiří Jakub Dačický), the hymnal of Závorka, Utraquist
dean of Doubravník, in Czech; its title page is dated 1602, and the printing is said to have been
finished in 1606. It is read here from the National Library of the Czech Republic's copy, 54 B 38,
in Manuscriptorium's images (IIIF manifest AIPDIG-NKCR__54_B_38_____2HE0NZ0-cs; CC BY-NC 4.0); the
leaves are those of the images' labels. The Rubryka (ff. 7r-15r, in two columns) is the book's
order for the year: for each Sunday and feast it names, by incipit and by leaf of the book (its
gatherings run A-T), what is sung at the early service ("Ráno"), at the High Mass ("na Summě"),
after the noon meal, at Vespers and at the weekday Masses. At the High Mass it gives the Introit,
Kyrie, Gloria, Alleluia, the sequence ("Proza"), the Creed hymn ("Patrem"), a hymn after the Gospel
("po Ewangelium") and one after the sermon ("po kázanj"), and the Sanctus; the hymns of the day
are these:

- the sequence, or the hymn sung instead of it (and on a few days a hymn given after it), and the
  hymns sung after the tract, after the Alleluia, after the Passion or as an antiphon before the
  Introit, which take the place of the sequence on those days;
- the hymn after the Gospel and the hymn after the sermon, with their alternatives;
- the songs the Rubryka gives for a Sunday as such ("Pjsničky"), on four Sundays.

They are loaded as one witness. The morning songs, the hymns after the noon meal and at Vespers,
the weekday Masses' and the Ordinary's are kept in the transcription, which has the morning songs,
but are not loaded.

Each row gives the incipit as the Rubryka prints it, often cut short, the title in modern spelling,
and a literal English gloss. Where the Rubryka gives a sequence by its leaf alone, the transcription
names it from that leaf, where one begins (`from_leaf`), and says so. The book prints over a hymn
translated from the Latin the Latin's incipit; where the hymn so headed was read and is the Latin's
in Czech, the transcription names the original, 'certain' or 'probable' (a free version is
'probable'; a new text on a Latin melody is not named by it). A hymn is then named by the lexicon,
if the original is one of its hymns; else by the original's title; else by its Czech title.

The days take this database's labels; three saints' days are new: Jan Hus (6 July), St Margaret
(13 July) and the Dispersion of the Apostles (15 July). The Sunday before Advent, the last of the
year, is the 27th after Trinity.
"""
import csv, os, sqlite3, sys
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import lexicon
from resolve import resolve
from merge_sources import provenance

LIST = 'Zavorka_1602_Rubryka.csv'
WITNESS = 'Závorka, Písně chval božských (1602-06)'
VIA = 'its Rubryka'
NAMED = ('certain', 'probable')
NEW_DAYS = {'Jan Hus (6 July)', 'St Margaret (13 July)', 'Dispersion of the Apostles (15 July)'}

def entries():
    return list(csv.DictReader(open(os.path.join(HERE, LIST), encoding='utf-8')))

def source(e):
    return f'{WITNESS} (via {VIA}; item {e["seq"]}, f. {e["rubryka_leaf"]})'

_BY_SOURCE = {}
def _entry(src):
    if not _BY_SOURCE:
        for e in entries():
            _BY_SOURCE[source(e)] = e
    return _BY_SOURCE[src]

def canonical(src):
    """the lexicon's hymn of a row whose source is this list's, or None: export_xlsx.py then names
    it by name(src), else by its Czech title"""
    e = _entry(src)
    return e['lexicon'] if e['lexicon'] and e['confidence'] in NAMED else None

def name(src):
    """the original's title, if certain or probable, or None"""
    e = _entry(src)
    return e['original'] if e['original'] and e['confidence'] in NAMED else None

def check(es, known):
    names = {e[0] for e in lexicon.L} | set(lexicon.LATIN_EN)
    for e in es:
        if e['loaded'] != 'yes': continue
        where = f'merge_zavorka: item {e["seq"]} ({e["title"]})'
        if e['day'] not in known and e['day'] not in NEW_DAYS:
            raise SystemExit(f'{where}: no such day {e["day"]!r}')
        if not e['title']:
            raise SystemExit(f'{where}: no title')
        if e['lexicon'] and e['lexicon'] not in names:
            raise SystemExit(f'{where}: {e["lexicon"]!r} is not in the lexicon')
        if (e['lexicon'] or e['original']) and e['confidence'] not in NAMED:
            raise SystemExit(f'{where}: an identification that is not certain or probable names the hymn')

def rows(known):
    es = entries()
    check(es, known)
    out, loaded = [], []
    for e in es:
        if e['loaded'] != 'yes':
            continue
        com = resolve(e['lexicon'])[2] if e['lexicon'] else None
        out.append((e['day'], e['title'], e['literal_english'], com, source(e)))
        loaded.append(e)
    return out, loaded

def main():
    db = sqlite3.connect(os.path.join(HERE, '..', 'hymns.db'))
    c = db.cursor()
    if c.execute('SELECT 1 FROM hymn_prescriptions WHERE source LIKE ?', (WITNESS + ' (via%',)).fetchone():
        raise SystemExit('merge_zavorka: hymns.db has these rows already; rebuild it first '
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
    titles = {e['title']: e for e in loaded}
    if '--list' in sys.argv:
        for e in loaded:
            print(f'  {e["seq"]:>3} {e["day"]:<34} {e["slot"]:<28} {e["title"][:34]:<34} '
                  f'{e["lexicon"] or (e["original"] if e["confidence"] in NAMED else "") or "-"}')
    print(f'{WITNESS:<40}: {len(rs)} on {len({r[0] for r in rs})} occasions, {len(titles)} hymns')
    print(f'  named by the lexicon  : {sorted({e["lexicon"] for e in loaded if e["lexicon"]})}')
    print(f'  by the original       : {sorted({e["original"] for e in loaded if e["original"] and not e["lexicon"]})}')
    print(f'  days new to the db    : {sorted({e["day"] for e in loaded} - known)}')
    print(f'  hymns new to the db   : {len(new)}  {new}')
    print(f'  total rows now        : {c.execute("SELECT COUNT(*) FROM hymn_prescriptions").fetchone()[0]}')
    db.close()

if __name__ == '__main__':
    main()
