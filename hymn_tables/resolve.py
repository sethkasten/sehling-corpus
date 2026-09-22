import re, sys, unicodedata, json, collections
sys.path.insert(0, '/home/user/sehling-corpus/hymn_tables')
import lexicon, difflib
from canon_latin import canon as latin_canon

def norm(s):
    t = unicodedata.normalize('NFKD', s).lower()
    t = t.replace('ß', 'ss').replace('æ', 'ae')
    t = ''.join(c for c in t if not unicodedata.combining(c))
    t = re.sub(r'[^a-z0-9\s,\[\]]', ' ', t)
    return re.sub(r'\s+', ' ', t).strip()

def fold(s):
    """Collapse early-modern German / OCR spelling variance for matching."""
    t = norm(s)
    t = re.sub(r'\bva[nm]\b', 'vom', t)
    for a, b in [('th','t'),('ck','k'),('c','k'),('ai','ei'),('ay','ei'),('ey','ei'),
                 ('y','i'),('v','f'),('w','f'),('z','s'),('ß','s'),('ue','u'),('oe','o'),('ae','e')]:
        t = t.replace(a, b)
    t = re.sub(r'(.)\1+', r'\1', t)      # collapse doubled letters
    t = re.sub(r'[dt]\b', '', t)          # unstable final d/t
    t = re.sub(r'\s+', ' ', t)
    return t.strip()

_COMPILED = [(c, [re.compile(p) for p in pats], lit, com, alt)
             for c, pats, lit, com, alt in lexicon.L]

PRE = [
 (r'^\s*vel ante Lectionem(?: Capituli)?\s*:\s*', ''),   # rubric prefix
 (r'^\s*Introitus vel ante Lectionem Capituli\s*:\s*', ''),
 (r'^[b¡\^0]\s*(?=[A-Za-zÄÖÜ])', ''),                     # stray OCR sigla
 (r'^.*?Lobwa[ßs]+er den \d+\.? Psalm\s*:\s*', ''),        # Lobwasser psalter reference
 (r'\s*etc\s*A?\s*$', ''),
 (r',\s*die (ander|annder|erst)e? melodi\s*$', ''),        # "the other tune"
 (r'^Der lobgesang Simeonis,\s*', ''),
 (r'\s*\[Christen gemein\]\s*', ' '),
]
JUNK = re.compile(r'^(Agenda von|Johannis des d[oö]pers dach|Sondag Advent|'
                  r'nach Pfingsten unnd Trinitatis)', re.I)

def preclean(s):
    for pat, rep in PRE:
        s = re.sub(pat, rep, s, flags=re.I)
    return re.sub(r'\s+', ' ', s).strip(' ,.:;')

def resolve(raw):
    raw = preclean(raw)
    if JUNK.match(raw) or len(raw) < 5:
        return None, None, None, None, False
    """-> (canonical, literal_en, common_en, alternates, matched?)"""
    lat = latin_canon(raw)
    if lat and lat in lexicon.LATIN_EN:
        lit, com = lexicon.LATIN_EN[lat]
        return lat, lit, com, None, True
    n = norm(raw)
    n2 = norm(raw.replace('ß','ss'))
    for c, pats, lit, com, alt in _COMPILED:
        for p in pats:
            if p.search(n) or p.search(n2):
                return c, lit, com, alt, True
    # truncated incipits ("Vater unser", "Durch Adams fall") -> prefix of a canonical title
    nf = fold(raw)
    best, best_r = None, 0.0
    for c, pats, lit, com, alt in _COMPILED:
        cn, cf = norm(c), fold(c)
        if len(n) >= 8 and (cn.startswith(n) or n.startswith(cn)):
            return c, lit, com, alt, True
        if len(nf) >= 7 and (cf.startswith(nf) or nf.startswith(cf)):
            return c, lit, com, alt, True
        r = max(difflib.SequenceMatcher(None, n, cn).ratio(),
                difflib.SequenceMatcher(None, nf, cf).ratio())
        if r > best_r: best, best_r = (c, lit, com, alt), r
    # dialect / OCR variance -> nearest canonical title
    if best and best_r >= 0.74:
        c, lit, com, alt = best
        return c, lit, com, alt, True
    return raw, None, None, None, False

if __name__ == '__main__':
    rows = []
    for fn in ['weissenfels','pommern','latin','german']:
        rows += json.load(open('hymn_tables/rows_%s.json' % fn))
    miss = collections.Counter()
    hit = 0
    for o,t,s in rows:
        c, lit, com, alt, ok = resolve(t)
        if ok: hit += 1
        else: miss[preclean(t)] += 1
    print(f'rows: {len(rows)}   resolved: {hit} ({hit*100//len(rows)}%)   unresolved: {len(rows)-hit}')
    print(f'distinct unresolved: {len(miss)}\n')
    for t, n in miss.most_common(60): print(f'{n:>3}  {t}')
