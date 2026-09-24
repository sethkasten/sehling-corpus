"""Build general_prayers.db -- the general prayers (Prayers of the Church /
"gemein gebet") of the Sunday service in the Sehling corpus.

    python3 general_prayers/build_gp_db.py          # needs ../eko.db for verification
    python3 general_prayers/build_gp_db.py --no-verify

Sources are the curated witness files w_*.py (one list W per family).  Each
witness is one church order's general prayer; each petition row holds the
marginal/heading rubric, the bidding addressed to the people, and the prayer
addressed to God, in the original language and in a formal-equivalence
(Jacobean) English translation, plus a standardized category.
"""
import os, sys, sqlite3, importlib, re
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
from categories import CATEGORIES, ORDER, normalize
from families import FAMILIES, code as family_code

MODULES = ['w_brenz', 'w_wtb', 'w_bugenhagen', 'w_other', 'w_reformed']
OUT = os.path.join(HERE, '..', 'general_prayers.db')


def load():
    W = []
    for m in MODULES:
        try:
            mod = importlib.import_module(m)
        except ModuleNotFoundError:
            continue
        W += mod.W
    keys = [w['key'] for w in W]
    dup = {k for k in keys if keys.count(k) > 1}
    assert not dup, f'duplicate witness keys {dup}'
    return W


def resolve(W):
    """Fill tr_from / tr_sub translations; returns list of problems."""
    by = {w['key']: w for w in W}
    errs, done = [], set()
    for w in W:
        done.add(w['key'])
        for i, p in enumerate(w['petitions'], 1):
            src = p.get('tr_from')
            p['_tr_src'] = None
            if src:
                k, n = src
                q = by[k]['petitions'][n - 1]
                if k not in done:
                    errs.append(f"{w['key']}#{i}: tr_from {k} must come earlier in the witness lists")
                p['_tr_src'] = f'{k}#{n}'
                for f in ('r', 'b', 'p'):
                    if p.get(f) and not p.get(f + '_en'):
                        if not q.get(f + '_en'):
                            errs.append(f"{w['key']}#{i}: no {f}_en in {k}#{n}")
                            continue
                        p[f + '_en'] = q[f + '_en']
                        p.setdefault('_inherited', set()).add(f)
            for old, new in p.get('tr_sub') or []:
                hit = False
                for f in ('r_en', 'b_en', 'p_en'):
                    if p.get(f) and old in p[f]:
                        p[f] = p[f].replace(old, new); hit = True
                if not hit:
                    errs.append(f"{w['key']}#{i}: tr_sub text not found: {old[:50]!r}")
            for f in ('r', 'b', 'p'):
                if p.get(f) and not p.get(f + '_en'):
                    errs.append(f"{w['key']}#{i}: {f} has no translation")
                if p.get(f + '_en') and not p.get(f):
                    errs.append(f"{w['key']}#{i}: {f}_en without original")
            if not (p.get('r') or p.get('b') or p.get('p')):
                errs.append(f"{w['key']}#{i}: empty petition")
            try:
                normalize(p['cat'])
            except KeyError:
                errs.append(f"{w['key']}#{i}: unknown category {p['cat']!r}")
            for s in (p.get('sub') or '').split(';'):
                s = s.strip()
                if s:
                    try: normalize(s)
                    except KeyError: errs.append(f"{w['key']}#{i}: unknown sub-category {s!r}")
    return errs


SCHEMA = '''
CREATE TABLE categories (
  code TEXT PRIMARY KEY, label TEXT, sort INTEGER, description TEXT);
CREATE TABLE families (
  code TEXT PRIMARY KEY, name TEXT, archetype TEXT, description TEXT,
  n_witnesses INTEGER);
CREATE TABLE witnesses (
  key TEXT PRIMARY KEY, year INTEGER, order_title TEXT, territory TEXT,
  citation TEXT, eko_doc_id TEXT, family TEXT,
  family_code TEXT REFERENCES families(code), form TEXT, tradition TEXT,
  position TEXT, heading_original TEXT, heading_english TEXT, notes TEXT,
  n_petitions INTEGER, categories_sequence TEXT);
CREATE TABLE petitions (
  id INTEGER PRIMARY KEY, witness_key TEXT REFERENCES witnesses(key), seq INTEGER,
  category TEXT REFERENCES categories(code), subcategories TEXT,
  rubric_original TEXT, rubric_english TEXT,
  bid_original TEXT, bid_english TEXT,
  prayer_original TEXT, prayer_english TEXT,
  note TEXT, translation_reused_from TEXT, verify_coverage REAL);
CREATE VIEW prayers_of_the_church AS
SELECT w.year, w.order_title, w.territory, p.seq,
       p.prayer_original                                   AS prayer_original,
       p.prayer_english                                    AS prayer_english,
       w.citation                                          AS source,
       TRIM(COALESCE(p.rubric_original, '') || CASE WHEN p.rubric_original IS NOT NULL AND p.bid_original IS NOT NULL THEN ' ' ELSE '' END || COALESCE(p.bid_original, ''))
                                                           AS bid_rubric_original,
       TRIM(COALESCE(p.rubric_english, '') || CASE WHEN p.rubric_english IS NOT NULL AND p.bid_english IS NOT NULL THEN ' ' ELSE '' END || COALESCE(p.bid_english, ''))
                                                           AS bid_rubric_english,
       c.label                                             AS category,
       p.subcategories, w.family, w.form, w.tradition, w.key AS witness_key
FROM petitions p JOIN witnesses w ON w.key = p.witness_key
JOIN categories c ON c.code = p.category
ORDER BY w.year, w.key, p.seq;
CREATE VIEW category_matrix AS
SELECT w.year, w.key AS witness_key, w.territory, w.family, w.categories_sequence
FROM witnesses w ORDER BY w.year, w.key;
CREATE VIEW category_usage AS
SELECT c.sort, c.code, c.label,
       (SELECT COUNT(*) FROM petitions p WHERE p.category = c.code) AS petitions_primary,
       (SELECT COUNT(DISTINCT p.witness_key) FROM petitions p WHERE p.category = c.code
          OR ('; ' || p.subcategories || '; ') LIKE '%; ' || c.code || '; %') AS witnesses_any
FROM categories c ORDER BY c.sort;
'''


def pivot_view():
    """witness x category: the petition numbers at which each category occurs,
    primary category bare ("3"), secondary in brackets ("(5)")."""
    cols = []
    for c in ORDER:
        cols.append(
            f"GROUP_CONCAT(CASE WHEN p.category = '{c}' THEN CAST(p.seq AS TEXT) "
            f"WHEN ('; ' || p.subcategories || '; ') LIKE '%; {c}; %' THEN '(' || p.seq || ')' END, ' ') "
            f'AS "{c}"')
    return ('CREATE VIEW category_pivot AS SELECT w.year, w.key AS witness_key, w.territory, '
            'w.family_code, w.n_petitions, ' + ', '.join(cols) +
            ' FROM witnesses w JOIN (SELECT * FROM petitions ORDER BY witness_key, seq) p '
            'ON p.witness_key = w.key GROUP BY w.key ORDER BY w.family_code, w.year, w.key;')


def main():
    do_verify = '--no-verify' not in sys.argv
    W = load()
    errs = resolve(W)
    if errs:
        print('\n'.join(errs)); sys.exit(1)
    cov = {}
    if do_verify:
        import verify
        low = []
        for w in W:
            for i, p in enumerate(w['petitions'], 1):
                cs = [verify.coverage(w['doc'], p[f])[0] for f in ('r', 'b', 'p') if p.get(f)]
                cov[(w['key'], i)] = round(min(cs), 3)
                if min(cs) < 0.9: low.append(f"{w['key']}#{i} {min(cs):.2f}")
        if low:
            print('verification below 0.90:\n  ' + '\n  '.join(low)); sys.exit(1)
    if os.path.exists(OUT): os.remove(OUT)
    db = sqlite3.connect(OUT)
    db.executescript(SCHEMA)
    db.execute(pivot_view())
    fams = {}
    for w in W:
        fc = family_code(w['family'])
        assert fc in FAMILIES, f"{w['key']}: family {fc!r} not in families.py"
        fams.setdefault(fc, [w['family'], 0])[1] += 1
    for fc, (arch, desc) in FAMILIES.items():
        assert fc in fams, f'family {fc} has no witnesses'
        db.execute('INSERT INTO families VALUES (?,?,?,?,?)',
                   (fc, fams[fc][0].split('. ', 1)[1], arch, desc, fams[fc][1]))
    for n, code in enumerate(ORDER, 1):
        label, desc = CATEGORIES[code]
        db.execute('INSERT INTO categories VALUES (?,?,?,?)', (code, label, n, desc))
    for w in W:
        seqcats = []
        for i, p in enumerate(w['petitions'], 1):
            c = normalize(p['cat'])
            subs = '; '.join(normalize(s.strip()) for s in (p.get('sub') or '').split(';') if s.strip()) or None
            seqcats.append(c)
            db.execute('INSERT INTO petitions (witness_key, seq, category, subcategories, rubric_original, rubric_english, bid_original, bid_english, prayer_original, prayer_english, note, translation_reused_from, verify_coverage) VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?)',
                       (w['key'], i, c, subs, p.get('r'), p.get('r_en'), p.get('b'), p.get('b_en'),
                        p.get('p'), p.get('p_en'), p.get('note'), p.get('_tr_src'), cov.get((w['key'], i))))
        db.execute('INSERT INTO witnesses VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)',
                   (w['key'], w['year'], w['order'], w['territory'], w['citation'], w['doc'] if isinstance(w['doc'], int) else ','.join(map(str, w['doc'])),
                    w['family'], family_code(w['family']), w['form'], w['tradition'], w['position'], w.get('heading'),
                    w.get('heading_en'), w.get('notes'), len(w['petitions']), ' > '.join(seqcats)))
    db.commit()
    n = db.execute('SELECT COUNT(*) FROM petitions').fetchone()[0]
    print(f'{OUT}: {len(W)} witnesses, {n} petitions')


if __name__ == '__main__':
    main()
