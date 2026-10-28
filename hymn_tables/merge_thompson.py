# -*- coding: utf-8 -*-
"""Fold into hymns.db the chief hymns of the lists that Jason Thompson transcribes in his
dissertation (Appendix 2) and that are not in Sehling: Antwerp (Andorff) 1567, Annaberg 1579,
Eler's Cantica sacra 1588 and Magdeburg 1632. Run it after merge_krusemark.py.

The rows come from rows_thompson.json (parse_thompson.py). Only the chief hymns are taken,
the hymns a list gives without naming another place in the service. The hymns Thompson marks
for the introit, the sermon, the distribution or the postlude stay in rows_thompson.json, and so
does Magdeburg 1613, whose hymns are all for after the sermon. Naumburg 1538, Anhalt 1551 and
Pirna are Sehling orders, read from the corpus by parse_sunday.py; Thompson's transcriptions of
them only check that reading.

Each row's source is "Witness (via Thompson, diss. App. 2)". Its title is Thompson's, with the
slips that parse_thompson.py mends; its English titles are the lexicon's. A list that gives
one hymn twice on a day is counted once.
"""
import json, os, sqlite3, sys, collections
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import lexicon
from resolve import resolve, by_occasion
from merge_sources import provenance
from parse_thompson import VIA

def rows():
    out, seen = [], set()
    for r in json.load(open(os.path.join(HERE, 'rows_thompson.json'), encoding='utf-8')):
        if not r['title'] or r['sehling'] or r['slot'] != 'Chief hymn':
            continue
        canon, lit, com, _alt, ok = resolve(r['title'])
        assert ok, (r['witness'], r['line'], r['title'])
        canon, lit, com = by_occasion(canon, r['occasion'], r['title'])
        key = (r['witness'], r['occasion'], canon)
        if key in seen: continue
        seen.add(key)
        out.append({'occasion': r['occasion'], 'printed': r['title'], 'canonical': canon,
                    'literal': lit, 'common': com, 'source': f"{r['witness']} (via {VIA})"})
    return out

def main():
    db = sqlite3.connect(os.path.join(HERE, '..', 'hymns.db'))
    c = db.cursor()
    rs = rows()
    c.executemany('INSERT INTO hymn_prescriptions (occasion,original_title,literal_english,'
                  'common_english,source) VALUES (?,?,?,?,?)',
                  [(r['occasion'], r['printed'], r['literal'], r['common'], r['source']) for r in rs])
    have = {t for (t,) in c.execute('SELECT canonical_title FROM hymns')}
    new = sorted({r['canonical'] for r in rs} - have)
    c.executemany('INSERT INTO hymns VALUES (?,?,?,?)',
                  [(t,) + next((r['literal'], r['common']) for r in rs if r['canonical'] == t)
                   + ('Latin' if t in lexicon.LATIN_EN else 'German',) for t in new])
    c.executemany('INSERT INTO translation_candidates VALUES (?,?,?,?,?)', provenance(new))
    db.commit()
    print(f'Thompson chief hymns   : {len(rs)}')
    for w, n in sorted(collections.Counter(r['source'].split(' (via')[0] for r in rs).items()):
        print(f'   {n:>4}  {w}')
    print(f'  hymns new to the db   : {len(new)}  {new}')
    print(f'  total rows now        : {c.execute("SELECT COUNT(*) FROM hymn_prescriptions").fetchone()[0]}')
    db.close()

if __name__ == '__main__':
    main()
