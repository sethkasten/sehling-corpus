"""Check that every curated original-language segment actually occurs in the
corpus document it is attributed to, in order, allowing for (a) Sehling's
footnotes and variant apparatus interleaved in the running text, (b) sigla
glued onto words (dienerq, bestendigs), and (c) small OCR repairs made during
curation.  A segment passes when >= 90% of its words are found in sequence."""
import re, sqlite3, os, difflib, unicodedata
DB = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'eko.db')
_cache, _idx, _eqc = {}, {}, {}


def norm_tokens(s):
    s = unicodedata.normalize('NFC', s)
    s = re.sub(r'-\s*\n\s*', '', s)            # re-join hyphenated line breaks
    s = re.sub(r'\|\s*[^|]{0,12}\|', ' ', s)    # folio markers |155v|
    s = re.sub(r'\[p\. \d+\]', ' ', s)
    s = s.lower().replace('ſ', 's').replace('ÿ', 'y')
    return re.findall(r'[a-zäöüßæœ]+', s)


def doc_tokens(did):
    if did not in _cache:
        t = sqlite3.connect(DB).execute('SELECT text FROM documents WHERE id=?', (did,)).fetchone()[0]
        _cache[did] = norm_tokens(t)
    return _cache[did]


def _index(did):
    if did not in _idx:
        d = {}
        for i, t in enumerate(doc_tokens(did)):
            d.setdefault(t, []).append(i)
        _idx[did] = d
    return _idx[did]


def tok_eq(a, b):
    if a == b: return True
    k = (a, b)
    if k in _eqc: return _eqc[k]
    r = False
    if len(a) >= 3 and b.startswith(a) and len(b) - len(a) <= 2: r = True   # glued siglum
    elif len(b) >= 3 and a.startswith(b) and len(a) - len(b) <= 2: r = True
    elif len(a) >= 3 and b.endswith(a) and len(b) - len(a) == 1: r = True   # siglum prefix
    elif len(a) >= 4 and len(b) >= 4 and abs(len(a) - len(b)) <= 3 and \
            difflib.SequenceMatcher(None, a, b).ratio() >= 0.8: r = True
    _eqc[k] = r
    return r


def _walk(ct, dt, st, skip):
    """Greedy in-order match; short words may only look a little ahead so
    that they cannot drag the cursor past the real text."""
    j, hits = st, []
    for c in ct:
        lim = skip if len(c) > 4 else 60
        k = next((x for x in range(j, min(len(dt), j + lim)) if tok_eq(c, dt[x])), None)
        hits.append(k)
        if k is not None: j = k + 1
    return hits


def _lcs(ct, reg):
    """Length of the longest common subsequence under tok_eq, plus the
    matched region indices (for debugging)."""
    n, m = len(ct), len(reg)
    prev = [0] * (m + 1)
    back = []
    for i in range(n):
        cur = [0] * (m + 1)
        c = ct[i]
        for j in range(m):
            if (c[0] == reg[j][0] or len(c) < 4) and tok_eq(c, reg[j]):
                cur[j + 1] = prev[j] + 1
            else:
                cur[j + 1] = cur[j] if cur[j] > prev[j + 1] else prev[j + 1]
        back.append(cur)
        prev = cur
    return prev[m], back


def _regions(did, ct, extra=600):
    dt, idx = doc_tokens(did), _index(did)
    order = sorted(range(len(ct)), key=lambda i: len(idx.get(ct[i], [])) or 10**9)
    pts = []
    for i in order[:8]:
        occ = idx.get(ct[i], [])
        if 0 < len(occ) <= 60:
            pts += [p - i for p in occ]
    if not pts and order and idx.get(ct[order[0]]):
        pts = [p - order[0] for p in idx[ct[order[0]]]]
    pts.sort()
    regs, span = [], 3 * len(ct) + extra
    for p in pts:
        if regs and p - regs[-1][0] < len(ct): continue
        lo = max(0, p - len(ct) - 40)
        regs.append((p, lo, min(len(dt), p + span)))
    return [(lo, hi) for _, lo, hi in regs] or [(0, min(len(dt), span))]


def coverage(did, text, skip=None):
    """(fraction of curated tokens matched in order, region start).  Candidate
    regions sit around exact occurrences of the rarest curated tokens; each is
    scored by a fuzzy longest-common-subsequence alignment."""
    ct = norm_tokens(text)
    if not ct: return 1.0, None
    dt = doc_tokens(did)
    best = (0, None)
    for extra in (600, 4000):   # second pass: text split by a long interleaved column
        for lo, hi in _regions(did, ct, extra):
            l, _ = _lcs(ct, dt[lo:hi])
            if l > best[0]: best = (l, lo)
            if l == len(ct): break
        if best[0] >= 0.9 * len(ct): break
    return best[0] / len(ct), best[1]


def missing(did, text, skip=None):
    """Curated tokens left unmatched by the best alignment (for debugging)."""
    ct = norm_tokens(text)
    dt = doc_tokens(did)
    best = (-1, None, None)
    for lo, hi in _regions(did, ct):
        l, back = _lcs(ct, dt[lo:hi])
        if l > best[0]: best = (l, lo, (back, dt[lo:hi]))
    l, lo, (back, reg) = best
    out, i, j = [], len(ct) - 1, len(reg)
    while i >= 0:
        if j > 0 and back[i][j] == back[i][j - 1]: j -= 1
        elif i > 0 and back[i][j] == back[i - 1][j] or (i == 0 and back[i][j] == 0):
            out.append(ct[i]); i -= 1
        else: i -= 1; j -= 1
    return l / len(ct), lo, out[::-1]
