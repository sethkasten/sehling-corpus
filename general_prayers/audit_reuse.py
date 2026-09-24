"""Audit re-used translations (tr_from): for each petition that borrows a
translation, list the words in which its original differs from the original
of the source petition (spelling variants ignored).  Every such difference
should be reflected in a tr_sub or be translation-neutral."""
import re, sys
sys.path.insert(0, '.')
import build_gp_db as B, verify

def canon(t):
    t = t.replace('ß', 's').replace('ä', 'e').replace('ö', 'o').replace('ü', 'u').replace('y', 'i')
    t = re.sub(r'(?<=[^aeiou])h', '', t)
    t = t.replace('dt', 't').replace('th', 't').replace('ck', 'k').replace('w', 'u').replace('v', 'f').replace('p', 'b').replace('d', 't')
    t = re.sub(r'(.)\1+', r'\1', t)
    return t

def diff(a, b):
    A = [canon(x) for x in verify.norm_tokens(a)]; Bt = [canon(x) for x in verify.norm_tokens(b)]
    n, m = len(A), len(Bt)
    L = [[0] * (m + 1) for _ in range(n + 1)]
    for i in range(n - 1, -1, -1):
        for j in range(m - 1, -1, -1):
            L[i][j] = L[i + 1][j + 1] + 1 if verify.tok_eq(A[i], Bt[j]) else max(L[i + 1][j], L[i][j + 1])
    i = j = 0; onlyA, onlyB = [], []
    while i < n and j < m:
        if verify.tok_eq(A[i], Bt[j]): i += 1; j += 1
        elif L[i + 1][j] >= L[i][j + 1]: onlyA.append(A[i]); i += 1
        else: onlyB.append(Bt[j]); j += 1
    onlyA += A[i:]; onlyB += Bt[j:]
    return onlyA, onlyB

W = B.load(); by = {w['key']: w for w in W}
for w in W:
    for i, p in enumerate(w['petitions'], 1):
        if not p.get('tr_from'): continue
        k, n = p['tr_from']; q = by[k]['petitions'][n - 1]
        for f in ('r', 'b', 'p'):
            if not p.get(f) or not q.get(f) or p.get(f + '_en') and (f in (p.get('_explicit') or ())): continue
            a, b = diff(p[f], q[f])
            if a or b:
                print(f"{w['key']}#{i}.{f} <- {k}#{n}  subs={len(p.get('tr_sub') or [])}\n    +{' '.join(a)}\n    -{' '.join(b)}")
