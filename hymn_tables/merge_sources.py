# -*- coding: utf-8 -*-
"""Fold the hymnal/compilation sources into hymns.db alongside the Sehling orders.

Each row is one witness's appointment of one hymn to one occasion. A witness
attested by more than one compilation is recorded once, with every attesting
compilation named in the source -- so Selnecker, who appears in his own
account, in Liliencron (as 'Se.') and in the HotD table (as 'S'), is not
counted three times.
"""
import json, os, sys, re, sqlite3, collections
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import bridge
from resolve import norm

FILES = ['rows_liliencron.json', 'rows_ludecus.json', 'rows_hotd.json', 'rows_selnecker.json']

def load():
    rows = []
    for fn in FILES:
        rows += json.load(open(os.path.join(HERE, fn), encoding='utf-8'))
    return rows

def identity(r):
    """Stable key for 'the same hymn', across German- and English-citing sources."""
    c, lit, com, how = bridge.identify(r.get('german'), r.get('english'))
    if c: return c, lit, com, how
    if r.get('german'):  return 'DE:' + norm(r['german']), None, None, 'unmatched-german'
    return 'EN:' + bridge.keyify(r['english']), None, None, 'unmatched-english'

def build_rows():
    merged = collections.OrderedDict()
    for r in load():
        ident, lit, com, how = identity(r)
        key = (r['occasion'], ident, r['witness'])
        # the printed form: German incipit where a source gives one, else its English title
        printed = r.get('german') or r.get('english')
        literal = lit
        common = com
        if r['compilation'].startswith('Liliencron'):
            # Liliencron's own English rendering: '°' marked ones are literal, not received titles
            if r['literal_only'] and not literal: literal = r['english']
            elif not r['literal_only'] and not common: common = r['english']
        elif not r.get('german'):
            # an English-only source: its title is a received English title by definition
            common = common or r['english']
        elif not literal:
            literal = r.get('english')
        if key in merged:
            m = merged[key]
            m['compilations'].add(r['compilation'])
            m['literal'] = m['literal'] or literal
            m['common'] = m['common'] or common
        else:
            merged[key] = {'occasion': r['occasion'], 'printed': printed, 'identity': ident,
                           'witness': r['witness'], 'literal': literal, 'common': common,
                           'compilations': {r['compilation']}, 'how': how}
    return list(merged.values())

SHORT = {
 'Liliencron, Liturgisch-musikalische Geschichte, de tempore concordance, pp. 61-77':
   'Liliencron concordance',
 'Hymn of the Day conflation table (modern compilation)': 'Hymn of the Day table',
 'Selnecker, own account of his hymn scheme (English translation)': 'Selnecker’s own account',
 'Ludecus, Ordo cantionum Germanicarum (1589)': None,   # witness == compilation
}

def source_string(m):
    vias = sorted(SHORT.get(c, c) for c in m['compilations'] if SHORT.get(c, c))
    vias = [v for v in vias if v and v != m['witness']]
    return f"{m['witness']} (via {'; '.join(vias)})" if vias else m['witness']

def main():
    db = sqlite3.connect(os.path.join(HERE, '..', 'hymns.db'))
    c = db.cursor()
    rows = build_rows()
    before = c.execute('SELECT COUNT(*) FROM hymn_prescriptions').fetchone()[0]
    c.executemany('INSERT INTO hymn_prescriptions (occasion,original_title,literal_english,'
                  'common_english,source) VALUES (?,?,?,?,?)',
                  [(m['occasion'], m['printed'], m['literal'], m['common'], source_string(m))
                   for m in rows])
    # lexicon rows for hymns these sources introduce
    have = {r[0] for r in c.execute('SELECT canonical_title FROM hymns')}
    new = {}
    for m in rows:
        t = m['identity']
        if t.startswith(('DE:', 'EN:')) or t in have or t in new: continue
        new[t] = (t, m['literal'], m['common'], 'German')
    c.executemany('INSERT OR IGNORE INTO hymns VALUES (?,?,?,?)', list(new.values()))
    db.commit()
    after = c.execute('SELECT COUNT(*) FROM hymn_prescriptions').fetchone()[0]
    print(f'merged rows added : {after - before}  (total {after})')
    print(f'distinct witnesses: {len({m["witness"] for m in rows})}')
    dups = sum(len(m["compilations"]) - 1 for m in rows)
    print(f'overlaps collapsed: {dups} duplicate attestations folded into existing rows')
    for w, n in collections.Counter(m['witness'] for m in rows).most_common(8):
        print(f'   {n:>4}  {w}')
    db.close()

if __name__ == '__main__':
    main()
