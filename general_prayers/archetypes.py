"""Family archetypes: the witnesses of each text family collated, category by
category, into one archetypal text with the other witnesses' variants
interleaved in square brackets.

The archetype is the family's earliest witness, taken verbatim. Every other
witness is aligned to it word by word, with spelling differences ignored, and
its substantive differences are written in at the point where they occur:

    plain text                   the archetype's own reading
    [a | W1, W2: b | W3: om.]    variation unit: archetype reading first, then
                                 the other witnesses' readings (om. = lacking)
    [+ W1, W2: b]                words that W1 and W2 add at this point
    [W1, W2 instead: …]          (after a field) W1 and W2 have a different text
                                 here in place of the archetype's (their own
                                 variants nested)
    [om. W1, W2]                 (after a field) witnesses of the family that
                                 lack this petition, bid or rubric altogether
    [+ W1, W2: …]                (a whole block) a petition, bid or rubric the
                                 archetype lacks: the earliest witness that has
                                 it is the base, with its own variants nested

Every text family gets one row per standard category. A petition counts for
the category that is its chief intention (petitions.category). Several
petitions of one category in a family are collated separately: a witness's
petition joins the archetype petition it most resembles, and a petition that
resembles none stands as an addition ([+ …]). The English is collated in the
same way from each witness's own translation. A witness's English variants
are shown only where its original differs from the base, so that two
renderings of the same original do not appear as variants.
Square brackets in the source texts (Sehling's editorial additions) are
changed to ⟨ ⟩.
"""
import re, sqlite3, difflib, os
from collections import defaultdict

# a petition joins a cluster when the aligned words cover >= SIM_MAX of the
# longer text, or >= SIM_MIN of the shorter and >= SIM_FLOOR of the longer
SIM_MAX, SIM_MIN, SIM_FLOOR = 0.3, 0.45, 0.2
FIELD_SIM = 0.35   # below this a whole field is one variation unit
GLUE = 2           # variation units separated by <= GLUE agreeing words are merged

# ---- sigla -----------------------------------------------------------------
_SIGLA = {
    'moers_1581': 'Moers 1581', 'frankfurt_poullain_1554': 'Frankfurt 1554 (Poullain)',
    'london_micron_1554': 'London 1554 (Micron)', 'nuernberg_veit_dietrich_1545': 'Nürnberg 1545',
    'wild_rheingrafschaft_1603': 'Wild- und Rheingrafschaft 1603', 'strassburg_1598': 'Strassburg 1598',
    'schwaebisch_hall_1526': 'Schwäbisch Hall 1526', 'schwaebisch_hall_1543': 'Schwäbisch Hall 1543',
}


def siglum(key):
    if key in _SIGLA:
        return _SIGLA[key]
    parts = [p for p in key.split('_') if p not in ('long', 'short', 'lp')]
    name = '-'.join(p.capitalize() for p in parts[:-1])
    for a, b in (('ae', 'ä'), ('oe', 'ö'), ('ue', 'ü'), ('Oe', 'Ö')):
        name = name.replace(a, b)
    return f'{name} {parts[-1]}'


# ---- token comparison ------------------------------------------------------
def canon_de(tok):
    t = re.sub(r'[^a-zäöüßſæœ]', '', tok.lower().replace('ſ', 's'))
    t = t.replace('ß', 's').replace('ä', 'e').replace('ö', 'o').replace('ü', 'u').replace('y', 'i').replace('j', 'i')
    t = re.sub(r'^v(?=[^aeiou])', 'u', t).replace('ai', 'ei')
    t = t[:1] + t[1:].replace('h', '')
    t = t.replace('ie', 'i')
    t = t.replace('dt', 't').replace('th', 't').replace('ck', 'k').replace('w', 'u').replace('v', 'f').replace('p', 'b').replace('d', 't')
    t = re.sub(r'(.)\1+', r'\1', t)
    if len(t) > 2 and t.endswith('e'):
        t = t[:-1]
    return t


def canon_en(tok):
    return re.sub(r'[^a-z]', '', tok.lower())


_eq_cache = {}


def tok_eq(a, b):
    if a == b:
        return True
    if min(len(a), len(b)) < 4:
        return False
    k = (a, b)
    if k not in _eq_cache:
        _eq_cache[k] = abs(len(a) - len(b)) <= 3 and difflib.SequenceMatcher(None, a, b).ratio() >= 0.8
    return _eq_cache[k]


def tokens(text):
    return text.replace('[', '⟨').replace(']', '⟩').split()


def align(A, B):
    """Fuzzy LCS of two canonical token lists -> matched index pairs."""
    n, m = len(A), len(B)
    L = [[0] * (m + 1) for _ in range(n + 1)]
    for i in range(n - 1, -1, -1):
        Li, Li1, a = L[i], L[i + 1], A[i]
        for j in range(m - 1, -1, -1):
            Li[j] = Li1[j + 1] + 1 if (a and tok_eq(a, B[j])) else (Li1[j] if Li1[j] >= Li[j + 1] else Li[j + 1])
    pairs, i, j = [], 0, 0
    while i < n and j < m:
        if A[i] and tok_eq(A[i], B[j]) and L[i][j] == L[i + 1][j + 1] + 1:
            pairs.append((i, j)); i += 1; j += 1
        elif L[i + 1][j] >= L[i][j + 1]:
            i += 1
        else:
            j += 1
    return pairs


def units(A, B):
    """Variation units of witness B against base A: (s, e, ws, we)."""
    n, m = len(A), len(B)
    pairs = align(A, B)
    if not pairs or 2 * len(pairs) / (n + m) < FIELD_SIM:
        return [(0, n, 0, m)], {}
    out = []
    for (pi, pj), (qi, qj) in zip([(-1, -1)] + pairs, pairs + [(n, m)]):
        if qi - pi > 1 or qj - pj > 1:
            out.append([pi + 1, qi, pj + 1, qj])
    merged = []
    for u in out:
        if merged and u[0] - merged[-1][1] <= GLUE and u[2] - merged[-1][3] <= GLUE:
            merged[-1][1], merged[-1][3] = u[1], u[3]
        else:
            merged.append(u)
    return [tuple(u) for u in merged], dict(pairs)


def collate(base, others, canon):
    """base: text; others: [(siglum, text)].  Returns (collated text, set of
    sigla whose text differs substantively from the base)."""
    Braw = tokens(base)
    Bk = [canon(t) for t in Braw]
    n = len(Braw)
    wits = []
    for sig, text in others:
        Wraw = tokens(text)
        Wk = [canon(t) for t in Wraw]
        us, mp = units(Bk, Wk)
        wits.append((sig, Wraw, Wk, us, mp))
    spans = sorted((u[0], u[1]) for w in wits for u in w[3])
    merged = []
    for s, e in spans:
        if merged and s <= merged[-1][1]:
            merged[-1][1] = max(merged[-1][1], e)
        else:
            merged.append([s, e])
    differ = set()
    at = {}
    for S, E in merged:
        groups = {}
        base_key = [k for k in Bk[S:E] if k]
        for sig, Wraw, Wk, us, mp in wits:
            whole = len(us) == 1 and us[0][:2] == (0, n) and not mp
            if whole:
                lo, hi = (0, len(Wraw)) if (S, E) == (0, n) else (None, None)
                if lo is None:
                    continue
            else:
                lo = mp[S - 1] + 1 if S > 0 else 0
                hi = mp[E] if E < n else len(Wraw)
            rk = [k for k in Wk[lo:hi] if k]
            if len(rk) == len(base_key) and all(tok_eq(a, b) for a, b in zip(rk, base_key)):
                continue
            groups.setdefault(tuple(rk), [' '.join(Wraw[lo:hi]), []])[1].append(sig)
            differ.add(sig)
        if groups:
            at[S] = (E, list(groups.values()))
    out, i = [], 0
    while i <= n:
        if i in at:
            E, groups = at[i]
            rd = ' | '.join(f"{', '.join(sigs)}: {txt or 'om.'}" for txt, sigs in groups)
            if E == i:
                out.append(f'[+ {rd}]')
            else:
                out.append(f"[{' '.join(Braw[i:E])} | {rd}]")
                i = E
                continue
        if i < n:
            out.append(Braw[i])
        i += 1
    return ' '.join(out), differ


# ---- clustering -------------------------------------------------------------
def _ptoks(p):
    return [canon_de(t) for t in tokens(' '.join(x for x in p[:3] if x))]


def sim(p, q):
    """0 if the petitions are unrelated, else the share of the longer text
    covered by the alignment."""
    a, b = _ptoks(p), _ptoks(q)
    if not a or not b:
        return 0
    n = len(align(a, b))
    lo, hi = n / min(len(a), len(b)), n / max(len(a), len(b))
    return hi if hi >= SIM_MAX or (lo >= SIM_MIN and hi >= SIM_FLOOR) else 0


def clusters(family_wits, pets):
    """family_wits: witness keys in order (base first); pets: {key: [petition]}.
    Returns [ [(key, petition), ...], ... ] main clusters first."""
    cl = []
    for k in family_wits:
        cand = []
        for pi, p in enumerate(pets.get(k, [])):
            for ci, c in enumerate(cl):
                s = max(sim(p, q) for _, q in c)
                if s:
                    cand.append((s, pi, ci))
        used_p, used_c = set(), set()
        for s, pi, ci in sorted(cand, reverse=True):
            if pi in used_p or ci in used_c:
                continue
            cl[ci].append((k, pets[k][pi])); used_p.add(pi); used_c.add(ci)
        for pi, p in enumerate(pets.get(k, [])):
            if pi not in used_p:
                cl.append([(k, p)])
    return cl


FIELDS = (('rubric', 0, 3), ('bid', 1, 4), ('prayer', 2, 5))   # (name, orig idx, en idx)


def similar(a, b):
    A = [canon_de(t) for t in tokens(a)]
    B = [canon_de(t) for t in tokens(b)]
    return bool(A and B) and 2 * len(align(A, B)) / (len(A) + len(B)) >= FIELD_SIM


def collate_field(items):
    """items: [(siglum, original, english)], base first.  Witnesses whose
    text is unrelated to the base form their own 'instead' groups."""
    groups = []
    for it in items:
        for g in groups:
            if similar(g[0][1], it[1]):
                g.append(it); break
        else:
            groups.append([it])
    res = []
    for g in groups:
        (bs, bo, be), rest = g[0], g[1:]
        o, differ = collate(bo, [(s, x) for s, x, _ in rest], canon_de)
        e, _ = collate(be, [(s, y) for s, x, y in rest if s in differ and y], canon_en)
        res.append((', '.join(s for s, _, _ in g), o, e))
    o = res[0][1] + ''.join(f' [{sig} instead: {x}]' for sig, x, _ in res[1:])
    e = res[0][2] + ''.join(f' [{sig} instead: {y}]' for sig, _, y in res[1:])
    return o, e


def render_cluster(c, family_wits, base_key):
    """-> {field: (orig, english)} for one cluster."""
    members = [k for k, _ in c]
    main = members[0] == base_key
    out = {}
    for name, io, ie in FIELDS:
        have = [(k, p) for k, p in c if p[io]]
        if not have:
            continue
        hk = have[0][0]
        orig, en = collate_field([(siglum(k), p[io], p[ie]) for k, p in have])
        if main and hk == base_key:
            lacking = [siglum(k) for k in family_wits if k not in {x for x, _ in have}]
            if lacking:
                tail = f" [om. {', '.join(lacking)}]"
                orig += tail; en += tail
        else:
            sig = ', '.join(siglum(k) for k, _ in have)
            orig, en = f'[+ {sig}: {orig}]', f'[+ {sig}: {en}]'
        out[name] = (orig, en)
    return out


SCHEMA = '''
CREATE TABLE archetypes (
  family_code TEXT REFERENCES families(code), category TEXT REFERENCES categories(code),
  prayer_original TEXT, prayer_english TEXT,
  bid_original TEXT, bid_english TEXT,
  witnesses TEXT, n_texts INTEGER, named_within TEXT,
  PRIMARY KEY (family_code, category));
'''


def build(db):
    db.executescript(SCHEMA)
    wit = {}
    fam = defaultdict(list)
    for k, fc, y in db.execute('SELECT key, family_code, year FROM witnesses ORDER BY year, key'):
        fam[fc].append(k); wit[k] = fc
    pets = defaultdict(lambda: defaultdict(list))   # (fc, cat) -> key -> [petition]
    within = defaultdict(set)
    labels = dict(db.execute('SELECT code, label FROM categories'))
    for k, cat, subs, *f in db.execute(
            'SELECT witness_key, category, subcategories, rubric_original, bid_original, prayer_original, '
            'rubric_english, bid_english, prayer_english FROM petitions ORDER BY witness_key, seq'):
        pets[(wit[k], cat)][k].append(tuple(f))
        for s in (subs or '').split('; '):
            if s and s != cat:
                within[(wit[k], s)].add(cat)
    cats = [c for c, in db.execute('SELECT code FROM categories ORDER BY sort')]
    for fc, ws in fam.items():
        for cat in cats:
            P = pets.get((fc, cat), {})
            named = '; '.join(labels[c] for c in cats if c in within.get((fc, cat), ())) or None
            if not P:
                db.execute('INSERT INTO archetypes VALUES (?,?,?,?,?,?,?,?,?)',
                           (fc, cat, None, None, None, None, None, 0, named))
                continue
            cl = clusters(ws, P)
            main = [c for c in cl if c[0][0] == ws[0]]
            cl = main + sorted([c for c in cl if c[0][0] != ws[0]], key=lambda c: ws.index(c[0][0]))
            parts = [render_cluster(c, ws, ws[0]) for c in cl]
            def join(fields, lang):
                blocks = []
                for pr in parts:
                    lines = [pr[f][lang] for f in fields if f in pr]
                    if lines:
                        blocks.append('\n'.join(lines))
                return '\n\n'.join(blocks) or None
            db.execute('INSERT INTO archetypes VALUES (?,?,?,?,?,?,?,?,?)',
                       (fc, cat, join(['prayer'], 0), join(['prayer'], 1),
                        join(['rubric', 'bid'], 0), join(['rubric', 'bid'], 1),
                        '; '.join(siglum(k) for k in ws if k in P), len(cl), named))


if __name__ == '__main__':
    db = sqlite3.connect(os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'general_prayers.db'))
    db.execute('DROP TABLE IF EXISTS archetypes')
    build(db)
    db.commit()
    print(db.execute('SELECT COUNT(*), SUM(prayer_original IS NOT NULL OR bid_original IS NOT NULL) FROM archetypes').fetchone())
