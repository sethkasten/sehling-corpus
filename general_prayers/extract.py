"""Curation aid: locate a known prayer text (e.g. the Württemberg 1553
archetype) inside another witness and print the witness's own wording, with

  ‹x›        a letter that looks like a siglum glued to a word (check it),
  ⟦...⟧      words in the witness that the archetype lacks (variant wording,
             or Sehling's apparatus / footnotes / running heads -- decide),
  ⟨-word⟩    archetype words the witness lacks.

The output is reviewed by hand before it goes into a witness file; nothing
is taken over automatically.
    python3 extract.py DOC module:witness_key:seq [field]
"""
import re, sys, importlib, sqlite3
import verify

WORD = re.compile(r"[A-Za-zÄÖÜäöüßſÿæœÆŒ]+")


def raw_tokens(did):
    """Tokens of the raw text with their character spans; hyphenated line
    breaks and folio markers inside a word are bridged."""
    t = sqlite3.connect(verify.DB).execute('SELECT text FROM documents WHERE id=?', (did,)).fetchone()[0]
    toks = []
    i = 0
    for m in WORD.finditer(t):
        s, e = m.span()
        if toks:
            ps, pe, pw = toks[-1]
            gap = t[pe:s]
            if re.fullmatch(r'-\s*(\|[^|]{0,12}\|\s*)?', gap) and ('\n' in gap or '|' in gap) and m.group()[0].islower():
                toks[-1] = (ps, e, pw + m.group())
                continue
        toks.append((s, e, m.group()))
    return t, toks


def extract(did, text, pad=0):
    ct = verify.norm_tokens(text)
    raw, rt = raw_tokens(did)
    nt = [verify.norm_tokens(w)[0] if verify.norm_tokens(w) else '' for _, _, w in rt]
    # locate region via verify's machinery (its token stream == nt, modulo page markers)
    verify._cache[('x', did)] = nt
    idx = {}
    for i, t in enumerate(nt): idx.setdefault(t, []).append(i)
    verify._idx[('x', did)] = idx
    best = (-1, None)
    for lo, hi in verify._regions(('x', did), ct):
        l, back = verify._lcs(ct, nt[lo:hi])
        if l > best[0]: best = (l, lo, hi, back)
    l, lo, hi, back = best
    # backtrack to matched pairs
    pairs, i, j = [], len(ct) - 1, hi - lo
    while i >= 0 and j > 0:
        if back[i][j] == back[i][j - 1]: j -= 1
        elif (back[i - 1][j] if i > 0 else 0) == back[i][j]: i -= 1
        else: pairs.append((i, lo + j - 1)); i -= 1; j -= 1
    pairs.reverse()
    matched = dict((dj, ci) for ci, dj in pairs)
    out = []
    first, last = pairs[0][1], pairs[-1][1]
    ci_prev = -1
    j = first
    while j <= last:
        if j in matched:
            ci = matched[j]
            for k in range(ci_prev + 1, ci):
                out.append(f'⟨-{ct[k]}⟩')
            ci_prev = ci
            s, e, w = rt[j]
            a, b = ct[ci], nt[j]
            if a != b and (b.startswith(a) or b.endswith(a)) and len(b) - len(a) <= 2:
                w = f'{w[:len(a)]}‹{w[len(a):]}›' if b.startswith(a) else f'‹{w[:len(b)-len(a)]}›{w[len(b)-len(a):]}'
            # punctuation following the word, up to the next word
            nxt = rt[j + 1][0] if j + 1 < len(rt) else e
            tail = raw[e:nxt]
            tail = re.sub(r'\|[^|]{0,12}\|', ' ', tail)
            tail = re.sub(r'\[p\. \d+\]', ' ', tail)
            punct = ''.join(ch for ch in tail if ch in ',.;:!?()[]')
            out.append(w + punct)
            j += 1
        else:
            k = j
            while k <= last and k not in matched: k += 1
            run = raw[rt[j][0]:rt[k - 1][1]]
            run = re.sub(r'\s+', ' ', run)
            out.append(f'⟦{run}⟧' if len(run) < 400 else f'⟦{run[:120]} … {run[-120:]}⟧')
            j = k
    return l / len(ct), ' '.join(out)


if __name__ == '__main__':
    did = int(sys.argv[1])
    mod, key, seq = sys.argv[2].split(':')
    fld = sys.argv[3] if len(sys.argv) > 3 else 'p'
    W = {w['key']: w for w in importlib.import_module(mod).W}
    p = W[key]['petitions'][int(seq) - 1]
    cov, s = extract(did, p[fld])
    print(f'coverage {cov:.2f}\n{s}')


def _pairs(ct, did):
    raw, rt = raw_tokens(did)
    nt = [(verify.norm_tokens(w) or [''])[0] for _, _, w in rt]
    key = ('x', did)
    if key not in verify._cache:
        verify._cache[key] = nt
        idx = {}
        for i, t in enumerate(nt): idx.setdefault(t, []).append(i)
        verify._idx[key] = idx
    best = (-1,)
    for lo, hi in verify._regions(key, ct):
        l, back = verify._lcs(ct, nt[lo:hi])
        if l > best[0]: best = (l, lo, hi, back)
    l, lo, hi, back = best
    pairs, i, j = [], len(ct) - 1, hi - lo
    while i >= 0 and j > 0:
        if back[i][j] == back[i][j - 1]: j -= 1
        elif (back[i - 1][j] if i > 0 else 0) == back[i][j]: i -= 1
        else: pairs.append((i, lo + j - 1)); i -= 1; j -= 1
    pairs.reverse()
    # trim stray matches at the edges: split at doc gaps > 25 tokens and drop
    # edge clusters of <= 3 matches
    cl = [[pairs[0]]]
    for a, b in zip(pairs, pairs[1:]):
        if b[1] - a[1] > 25: cl.append([])
        cl[-1].append(b)
    while len(cl) > 1 and len(cl[0]) <= 3: cl.pop(0)
    while len(cl) > 1 and len(cl[-1]) <= 3: cl.pop()
    pairs = [p for c in cl for p in c]
    return raw, rt, nt, pairs, l / len(ct)


def clean(did, text):
    """Witness wording aligned to `text`, apparatus heuristically removed.
    Returns (coverage, clean_text, notes) -- notes list every judgement made."""
    ct = verify.norm_tokens(text)
    raw, rt, nt, pairs, cov = _pairs(ct, did)
    matched = dict((dj, ci) for ci, dj in pairs)
    out, notes = [], []
    first, last = pairs[0][1], pairs[-1][1]
    j = first
    if pairs[0][0] > 0: notes.append('MISSING-START: ' + ' '.join(ct[:pairs[0][0]]))
    if pairs[-1][0] < len(ct) - 1: notes.append('MISSING-END: ' + ' '.join(ct[pairs[-1][0] + 1:]))
    prev_ci = pairs[0][0] - 1
    while j <= last:
        if j in matched:
            ci = matched[j]
            if ci > prev_ci + 1: notes.append('LACKS: ' + ' '.join(ct[prev_ci + 1:ci]))
            prev_ci = ci
            s, e, w = rt[j]
            a, b = ct[ci], nt[j]
            if a != b and len(b) == len(a) + 1 and (b.startswith(a) or b.endswith(a)):
                x = b[-1] if b.startswith(a) else b[0]
                near = raw[e:e + 6000]
                if re.search(rf'(?m)^{x}(-{x})? ', near):
                    notes.append(f'SIGLUM? {w} -> ' + (w[:-1] if b.startswith(a) else w[1:]))
                    w = w[:-1] if b.startswith(a) else w[1:]
            nxt = rt[j + 1][0] if j + 1 < len(rt) else e
            tail = re.sub(r'\|[^|]{0,12}\||\[p\. \d+\]', ' ', raw[e:nxt])
            if '\n' in tail and j + 1 not in matched:
                tail = tail.split('\n')[0]
            punct = ''.join(ch for ch in tail if ch in ',.;:!?')
            out.append(w + punct)
            j += 1
        else:
            k = j
            while k <= last and k not in matched: k += 1
            run = re.sub(r'\s+', ' ', raw[rt[j][0]:rt[k - 1][1]])
            run = re.sub(r'-\s(?=[a-zäöü])', '', run)
            n = k - j
            if n <= 6 and not re.search(r'\d|\[p\.|Fehlt|KO |[A-Z][a-z]+ 1[56]\d\d', run):
                notes.append(f'KEPT: {run}')
                out.append(run)
            else:
                notes.append(f'DROPPED({n}): {run[:100]}{" …" if len(run) > 100 else ""}')
            j = k
    s = ' '.join(out)
    s = re.sub(r'\s+([,.;:])', r'\1', s)
    return cov, s, notes
