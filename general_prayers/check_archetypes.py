"""Round-trip check of the archetype collation: from every collated field,
read each witness's text back out of the brackets and compare it, word by
word (spelling-tolerant, as in the collation), with that witness's own text.

    python3 general_prayers/check_archetypes.py      # after build_gp_db.py
"""
import os, re, sys, sqlite3
from collections import defaultdict
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import archetypes as A


def split_top(s, sep):
    """Split s on sep outside brackets."""
    out, depth, i, start = [], 0, 0, 0
    while i < len(s):
        c = s[i]
        if c == '[': depth += 1
        elif c == ']': depth -= 1
        elif depth == 0 and s.startswith(sep, i):
            out.append(s[start:i]); i += len(sep); start = i; continue
        i += 1
    out.append(s[start:])
    return out


def nodes(s):
    """-> list of ('text', str) and ('br', inner str)."""
    out, depth, start = [], 0, 0
    for i, c in enumerate(s):
        if c == '[':
            if depth == 0:
                out.append(('text', s[start:i])); start = i + 1
            depth += 1
        elif c == ']':
            depth -= 1
            if depth == 0:
                out.append(('br', s[start:i])); start = i + 1
    out.append(('text', s[start:]))
    return out


def readings(parts):
    """['W1, W2: text', ...] -> [(set of sigla, text)]"""
    res = []
    for p in parts:
        sig, _, txt = p.partition(': ')
        res.append((set(sig.split(', ')), '' if txt == 'om.' else txt))
    return res


def reconstruct(s, wit):
    out = []
    for kind, v in nodes(s):
        if kind == 'text':
            out.append(v); continue
        if v.startswith('+ '):
            for sigs, txt in readings(split_top(v[2:], ' | ')):
                if wit in sigs:
                    out.append(reconstruct(txt, wit))
        elif v.startswith('om. ') or ' instead: ' in split_top(v, ' | ')[0]:
            continue
        else:
            parts = split_top(v, ' | ')
            base, alts = parts[0], readings(parts[1:])
            txt = next((t for sigs, t in alts if wit in sigs), base)
            out.append(reconstruct(txt, wit))
    return ' '.join(' '.join(out).split())


def same(a, b, canon):
    x = [canon(t) for t in A.tokens(a)]; y = [canon(t) for t in A.tokens(b)]
    x = [t for t in x if t]; y = [t for t in y if t]
    return len(x) == len(y) and all(A.tok_eq(p, q) for p, q in zip(x, y))


def main():
    db = sqlite3.connect(os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'general_prayers.db'))
    fam, wit = defaultdict(list), {}
    for k, fc in db.execute('SELECT key, family_code FROM witnesses ORDER BY year, key'):
        fam[fc].append(k); wit[k] = fc
    pets = defaultdict(lambda: defaultdict(list))
    for k, cat, *f in db.execute('SELECT witness_key, category, rubric_original, bid_original, prayer_original, '
                                 'rubric_english, bid_english, prayer_english FROM petitions ORDER BY witness_key, seq'):
        pets[(wit[k], cat)][k].append(tuple(f))
    checked = bad = 0
    for (fc, cat), P in pets.items():
        for c in A.clusters(fam[fc], P):
            for name, io, ie in A.FIELDS:
                have = [(k, p) for k, p in c if p[io]]
                if not have:
                    continue
                items = [(A.siglum(k), p[io], p[ie]) for k, p in have]
                groups = []
                for it in items:
                    for g in groups:
                        if A.similar(g[0][1], it[1]):
                            g.append(it); break
                    else:
                        groups.append([it])
                for g in groups:
                    o, differ = A.collate(g[0][1], [(s, x) for s, x, _ in g[1:]], A.canon_de)
                    e, _ = A.collate(g[0][2], [(s, y) for s, x, y in g[1:] if s in differ and y], A.canon_en)
                    for s, x, y in g:
                        tests = [('de', o, x, A.canon_de)]
                        if s == g[0][0] or s in differ:      # English variants are recorded only for these
                            tests.append(('en', e, y, A.canon_en))
                        for lang, col, want, canon in tests:
                            checked += 1
                            if not same(reconstruct(col, s), want, canon):
                                bad += 1
                                print(f'{fc} {cat} {name} {lang} {s}:\n  got  {reconstruct(col, s)[:200]}\n  want {" ".join(A.tokens(want))[:200]}')
    # representative texts: filled exactly where the critical text is, and clean
    cols = ('prayer_original', 'prayer_english', 'bid_original', 'bid_english')
    for fc, cat, *v in db.execute('SELECT family_code, category, ' + ', '.join(cols) + ', '
                                  + ', '.join('rep_' + c for c in cols) + ' FROM archetypes'):
        for c, crit, rep in zip(cols, v[:4], v[4:]):
            checked += 1
            if (crit is None) != (rep is None) or (rep and re.search(r'[\[\]⟨⟩]', rep)):
                bad += 1
                print(f'{fc} {cat} rep_{c}: critical {"empty" if crit is None else "filled"}, '
                      f'representative {rep[:80] if rep else "empty"}')
    print(f'{checked} texts checked (witnesses read back from the collation, representative layout), {bad} problems')
    sys.exit(1 if bad else 0)


if __name__ == '__main__':
    main()
