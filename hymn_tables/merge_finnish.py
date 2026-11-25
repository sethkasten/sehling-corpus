# -*- coding: utf-8 -*-
"""Fold into hymns.db the gradual hymns of three Finnish church handbooks (Käsikirja): Sorolainen's
of 1614, the handbook of 1629 (Elimaeus 1629.pdf) and the Carolinian handbook of 1694
(Karoliininen Käsi-kiria 1694.pdf). The scans are in "Hymnal Index/Hymnal PDFs for hotd"; the
lists are transcribed in Sorolainen_1614_Gradual_Hymns.csv, Elimaeus_1629_Gradual_Hymns.csv and
Karoliininen_1694_Gradual_Hymns.csv. Run it after merge_sbh.py.

In these handbooks the hymn that changes Sunday by Sunday is the gradual hymn, sung between the
Epistle and the Gospel ("Graduale mahta olla jocu Psalmi eli kijtos wirsi", 1614). Olavi
Rimpiläinen's study of the service in the diocese of Viipuri (1980) led to them: his appendices
give the 1629 list and set the 1614 and 1694 lists side by side. The lists here are read from
the prints, which correct his table in places; the notes say where. The handbook of 1614 gives
one hymn to a day, now and then two; that of 1629 the same, with a 27th Sunday after Trinity;
that of 1694 three or four to most days and twelve at Pentecost. Each handbook is one witness,
and all its hymns for a day count for it, as the several hymns of one day do for any witness.

Each row of a transcription gives the hymn as printed, a literal English gloss of it, the day,
and the German or Latin hymn the Finnish one translates, where it can be told: 'certain' (the
incipit is a translation of the original's), 'probable' (it agrees in sense, or is the same
psalm's hymn on a day that suits it) or 'possible'. Only certain and probable identifications
name the hymn (canonical(), for export_xlsx.py); a possible one stays a note, and its row, like
an unidentified one, is named by its Finnish title. common_english is the received English title
of an identified hymn, literal_english the gloss of the Finnish.

The days take this database's labels. The handbooks keep the Transfiguration on the 7th Sunday
after Trinity, and that Sunday's hymns are the Transfiguration's; the 1614 and 1629 handbooks give
Septuagesima and Sexagesima one heading; the 1694 handbook's sixth Sunday after the Epiphany has
its hymns by a cross-reference to the 27th after Trinity. Days new to the database are listed in
NEW_DAYS, so that a misspelt label stops the build.
"""
import csv, os, re, sqlite3, sys
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import lexicon
from resolve import resolve
from merge_sources import provenance

# (witness, transcription)
LISTS = [
 ('Finnish handbook (Sorolainen, 1614)', 'Sorolainen_1614_Gradual_Hymns.csv'),
 ('Finnish handbook (Elimaeus, 1629)', 'Elimaeus_1629_Gradual_Hymns.csv'),
 ('Finnish handbook (1694)', 'Karoliininen_1694_Gradual_Hymns.csv'),
]
WITNESSES = [w for w, _f in LISTS]
VIA = 'its gradual hymns'
# a possible identification is a note, not an identity
NAMED = ('certain', 'probable')
NEW_DAYS = {
 'St Matthias (24 Feb)', 'St Andrew (30 Nov)', 'St Thomas (21 Dec)', 'Ss Philip and James (1 May)',
 'St Bartholomew (24 Aug)', 'Rogation days', 'Days of public thanksgiving, fasting and prayer',
}

def entries(fn):
    return list(csv.DictReader(open(os.path.join(HERE, fn), encoding='utf-8')))

def source(witness, e):
    return f'{witness} (via {VIA}; item {e["seq"]}, PDF p. {e["pdf_page"]})'

def named(e):
    """the lexicon's hymn of a transcribed row, or None"""
    return e['lexicon'] if e['confidence'] in NAMED and e['lexicon'] else None

_CANON = {}
def canonical(src):
    """the lexicon's hymn of a row whose source is one of these lists' ('...; item 47, PDF p. 34)'),
    or None for a hymn not identified: export_xlsx.py names these rows by their Finnish titles"""
    if not _CANON:
        for w, fn in LISTS:
            for e in entries(fn):
                _CANON[source(w, e)] = named(e)
    return _CANON[src]

def rows(known):
    out, report = [], []
    names = {e[0] for e in lexicon.L} | set(lexicon.LATIN_EN)
    for w, fn in LISTS:
        for e in entries(fn):
            if e['day'] not in known and e['day'] not in NEW_DAYS:
                raise SystemExit(f'merge_finnish: {fn} item {e["seq"]}: no such day {e["day"]!r}')
            canon = named(e)
            if e['lexicon'] and e['lexicon'] not in names:
                raise SystemExit(f'merge_finnish: {fn} item {e["seq"]}: {e["lexicon"]!r} is not in the lexicon')
            com = resolve(canon)[2] if canon else None
            out.append((e['day'], e['title'], e['literal_english'], com, source(w, e)))
            report.append((w, e['seq'], e['day'], e['title'], canon, e['confidence']))
    return out, report

def main():
    db = sqlite3.connect(os.path.join(HERE, '..', 'hymns.db'))
    c = db.cursor()
    if c.execute('SELECT 1 FROM hymn_prescriptions WHERE source LIKE ?', ('Finnish handbook (%',)).fetchone():
        raise SystemExit('merge_finnish: hymns.db has these rows already; rebuild it first '
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
            print(f'  {w[18:]:<20} {seq:>3} {day:<38} {title:<42} {canon or "-"} ({conf or "unidentified"})')
    for w in WITNESSES:
        mine = [r for r in report if r[0] == w]
        print(f'{w:<37}: {len(mine)} on {len({r[2] for r in mine})} occasions, '
              f'{sum(1 for r in mine if r[4])} named by the lexicon')
    print(f'  days new to the db    : {sorted({r[2] for r in report} - known)}')
    print(f'  hymns new to the db   : {len(new)}  {new}')
    print(f'  total rows now        : {c.execute("SELECT COUNT(*) FROM hymn_prescriptions").fetchone()[0]}')
    db.close()

if __name__ == '__main__':
    main()
