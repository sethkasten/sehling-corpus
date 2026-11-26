# -*- coding: utf-8 -*-
"""Fold into hymns.db the hymns of B. S. Ingemann's "Høimesse-Psalmer til Kirkeaarets Helligdage"
(Copenhagen: Andreas Seidelin, 1825; "Hymnal Index/Hymnal PDFs for hotd/Ingemann 1825.pdf", a
Google Books scan of the copy in the National Library of Scotland), as transcribed in
Ingemann_1825_High_Mass_Hymns.csv. Run it after merge_latvia.py.

The book is one poet's cycle of hymns for the High Mass (Høimesse) of each Sunday and holy day of
the Danish church year, 73 in all: each is headed by its number, its day, the Gospel of the day
(chapter and verse, and the matter of the reading) and the melody it is sung to, and most are on
the day's Gospel. It is not a list of hymns chosen from a hymnal, but it gives each day its hymn,
and it is loaded as a witness of the Danish church's year in 1825. The hymns are Ingemann's own,
none a translation, and each is named by its Danish first line, which the transcription takes from
the text and the book's register, checked against the scan where the two disagree. A modern
witness, which Appendix 8.A leaves out.

The days are those of the Danish church after the reduction of its holy days in 1770, with this
database's labels. St Stephen's Day is the second day of Christmas, and has two hymns, as Easter
Day has; the contents head the second of each "Samme Dag" (the same day). The Annunciation stands
before Palm Sunday, where the Danish church kept it, in the place of Judica, which the book does
not have; All Saints stands between the 21st and 22nd Sundays after Trinity, on the first Sunday
of November; Epiphany itself has no hymn. Five Passion hymns, printed between Maundy
Thursday and Good Friday for no day, are `Passiontide`; the General Prayer Day (Almindelig
Bededag, Store Bededag, the fourth Friday after Easter) is new to the database. The Sundays after
Easter are Quasimodogeniti to Rogate, the sixth Exaudi.
"""
import csv, os, sqlite3, sys
HERE = os.path.dirname(os.path.abspath(__file__))

LIST = 'Ingemann_1825_High_Mass_Hymns.csv'
WITNESS = 'Ingemann, Høimesse-Psalmer (1825)'
VIA = 'its hymns'
NEW_DAYS = {'General Prayer Day (Store Bededag)'}

def entries():
    return list(csv.DictReader(open(os.path.join(HERE, LIST), encoding='utf-8')))

def source(e):
    return f'{WITNESS} (via {VIA}; no. {e["number"]}, p. {e["page"]}, PDF p. {e["pdf_page"]})'

def canonical(_src):
    """no hymn of this list is in the lexicon: export_xlsx.py names each by its Danish first line"""
    return None

def rows(known):
    es = entries()
    for e in es:
        if e['day'] not in known and e['day'] not in NEW_DAYS:
            raise SystemExit(f'merge_ingemann: no. {e["number"]}: no such day {e["day"]!r}')
    return [(e['day'], e['first_line'], e['literal_english'], None, source(e)) for e in es], es

def main():
    db = sqlite3.connect(os.path.join(HERE, '..', 'hymns.db'))
    c = db.cursor()
    if c.execute('SELECT 1 FROM hymn_prescriptions WHERE source LIKE ?', (WITNESS + ' (via%',)).fetchone():
        raise SystemExit('merge_ingemann: hymns.db has these rows already; rebuild it first '
                         '(build_hymn_db.py and the merges before this one)')
    known = {o for (o,) in c.execute('SELECT DISTINCT occasion FROM hymn_prescriptions')}
    rs, es = rows(known)
    c.executemany('INSERT INTO hymn_prescriptions (occasion,original_title,literal_english,'
                  'common_english,source) VALUES (?,?,?,?,?)', rs)
    db.commit()
    if '--list' in sys.argv:
        for e in es:
            print(f'  {e["number"]:>7} {e["day"]:<36} {e["first_line"]}')
    print(f'{WITNESS:<36}: {len(rs)} on {len({r[0] for r in rs})} occasions')
    print(f'  days new to the db    : {sorted({r[0] for r in rs} - known)}')
    print(f'  total rows now        : {c.execute("SELECT COUNT(*) FROM hymn_prescriptions").fetchone()[0]}')
    db.close()

if __name__ == '__main__':
    main()
