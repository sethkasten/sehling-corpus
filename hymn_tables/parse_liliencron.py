# -*- coding: utf-8 -*-
"""Liliencron, de tempore hymn concordance (pp. 61-77), English translation.

Entry format:  German incipit — English title[°]: Sigla. Sigla. ...
Each siglum is a separate hymnal witness, so one entry expands to one row
per hymnal. '°' marks the translator's own literal rendering, i.e. no
established English title exists.
"""
import re, os, json

HERE = os.path.dirname(os.path.abspath(__file__))
COMPILATION = 'Liliencron, Liturgisch-musikalische Geschichte, de tempore concordance, pp. 61-77'

SIGLA = {
 'A.':  'Augsburg hymnal (1619)',
 'D.':  'Darmstadt Cantional (1687)',
 'E.':  'Erhardi, Frankfurt hymnal (1659)',
 'Ge.': 'Gesius, Geistliche Lieder (1601)',
 'Go.': 'Goslar hymnal (1687)',
 'H.':  'Helmstedt hymnal (1626)',
 'K.':  'Keuchenthal, Kirchengesänge (1573)',
 'L.':  'Liegnitz choir hymnal (1625-30)',
 'LK.': 'Leipzig Kirchenandachten (1694)',
 'LL.': 'Leipzig Geistliche Lieder (1605)',
 'Sch.':'Schein, Cantional (1627)',
 'Se.': 'Selnecker',
 'SH.': 'Schleswig-Holstein church book (1665)',
 'Sp.': 'Spangenberg, Cantiones (1545)',
 'St.': 'Stiphelius, Libellus scholasticus (1607)',
}
SIG_RE = re.compile(r'\b(LK|LL|SH|Sch|Ge|Go|Se|Sp|St|A|D|E|G|H|K|L)\.')

# The translator's footnotes resolve two printer's slips of the undefined siglum "G.":
#   fn.1  "G." at Vom Himmel hoch  -> "Go." (Goslar)
#   fn.3  "G. LL." at Cantate      -> "Ge." (Gesius)
def resolve_G(occasion, german):
    return 'Ge.' if occasion.startswith('Easter 4') else 'Go.'

# Stated in prose rather than tabulated (p. 68): the one coincidence at Quasimodogeniti.
PROSE_ENTRIES = [
 ('Easter 1 (Quasimodogeniti)', 'Ich ruf zu dir, Herr Jesu Christ',
  'I Call to Thee, Lord Jesus Christ', False, ['Go.', 'LK.'],
  'Liliencron tabulates nothing for this day; only Go. and LK. coincide, stated in prose'),
]

OCC = {
 r'^(\d)\. Advent$':            lambda m: f'Advent {m.group(1)}',
 r'^(\d)\. after Epiphany$':    lambda m: f'Epiphany {m.group(1)}',
 r'^(\d+)\. after Trinity$':    lambda m: f'Trinity {m.group(1)}',
 r'^25th, 26th, and 27th after Trinity$': lambda m: 'Trinity 25-27',
}
OCC_FIXED = {
 'Christmas':'Christmas', 'Sunday after Christmas':'Sunday after Christmas',
 'New Year':'New Year (Circumcision)', 'Sunday after New Year':'Sunday after New Year',
 'Epiphany':'Epiphany', 'Septuagesima':'Septuagesima', 'Sexagesima':'Sexagesima',
 'Estomihi':'Quinquagesima (Estomihi)', 'Quinquagesima':'Quinquagesima (Estomihi)',
 'Invocavit':'Lent 1 (Invocavit)', 'Reminiscere':'Lent 2 (Reminiscere)',
 'Oculi':'Lent 3 (Oculi)', 'Laetare':'Lent 4 (Laetare)', 'Judica':'Lent 5 (Judica)',
 'Palmarum':'Palm Sunday', 'Good Friday':'Good Friday', 'Easter':'Easter',
 'Quasimodogeniti':'Easter 1 (Quasimodogeniti)', 'Misericordias':'Easter 2 (Misericordias Domini)',
 'Jubilate':'Easter 3 (Jubilate)', 'Cantate':'Easter 4 (Cantate)',
 'Rogate':'Easter 5 (Rogate/Vocem jucunditatis)', 'Ascension':'Ascension',
 'Exaudi':'Sunday after Ascension (Exaudi)', 'Pentecost':'Pentecost', 'Trinity':'Trinity Sunday',
 'Purification of Mary':'Purification of Mary (2 Feb)',
 'Annunciation of Mary':'Annunciation (25 March)',
 'St. John the Baptist':'St John the Baptist (24 June)',
 'St. Michael':'St Michael (29 Sept)',
}

# Tesseract misreads umlauts in the Fraktur-derived German incipits.
OCR_FIX = [
 (r'\bfiir', 'für'), (r'fiircht', 'fürcht'), (r'Siinden', 'Sünden'), (r'betriibst', 'betrübst'),
 (r'Wasserfliissen', 'Wasserflüssen'), (r'Ungliick', 'Unglück'), (r'Stiindlein', 'Stündlein'),
 (r'g[ée]ttlich', 'göttlich'), (r'h[ée]chsten', 'höchsten'), (r'N[oé]+then', 'Nöthen'),
 (r'Fr[ée]lich', 'Fröhlich'), (r'sch6n', 'schön'), (r'Schd[ée]pfer', 'Schöpfer'),
 (r'\bhalt\b', 'hält'), (r'\bWar Gott\b', 'Wär Gott'), (r'Schaar', 'Schar'),
 (r'genaddig', 'gnädig'), (r'tiberwand', 'überwand'), (r'H[Oé]he', 'Höhe'), (r'allmachtgen', 'allmächtgen'),
]

def fix_ocr(s):
    for pat, rep in OCR_FIX:
        s = re.sub(pat, rep, s)
    return s

def norm_occ(line):
    s = line.strip().rstrip('.*').strip()
    for pat, fn in OCC.items():
        m = re.match(pat, s)
        if m: return fn(m)
    s2 = s.rstrip('*').strip()
    return OCC_FIXED.get(s2)

def flow(text):
    """Rejoin entries that OCR wrapped across lines."""
    # cut the translator's note and the footnotes
    start = text.find('[p. 61]')
    end = text.find('Footnotes')
    if end < 0: end = len(text)
    body = text[start:end]
    out, buf = [], ''
    for raw in body.split('\n'):
        ln = raw.rstrip()
        if not ln.strip():
            if buf: out.append(buf); buf = ''
            continue
        if re.match(r'^\[p\. \d+\]', ln.strip()):
            if buf: out.append(buf); buf = ''
            continue
        if norm_occ(ln) and '—' not in ln:   # an occasion heading always stands alone
            if buf: out.append(buf)
            out.append(ln.strip()); buf = ''
        elif '—' in ln and buf:              # a new entry begins
            out.append(buf); buf = ln.strip()
        elif buf:
            buf += ' ' + ln.strip()
        else:
            buf = ln.strip()
    if buf: out.append(buf)
    return out

def parse():
    text = open(os.path.join(HERE, 'src_liliencron_ocr.txt'), encoding='utf-8').read()
    rows, occ = [], None
    for line in flow(text):
        s = line.strip()
        o = norm_occ(s)
        if o and '—' not in s:
            occ = o; continue
        if '—' not in s or not occ:
            continue
        german, rest = s.split('—', 1)
        german = fix_ocr(german.strip(' .'))
        if ':' not in rest: continue
        english, sig = rest.rsplit(':', 1)
        english = english.strip()
        # parenthetical gloss, e.g. "(O lux beata Trinitas)"
        note = None
        pm = re.search(r'\(([^)]*)\)\s*$', english)
        if pm:
            note = pm.group(1); english = english[:pm.start()].strip()
        literal_only = '°' in english or '®' in english   # OCR renders ° as ®
        english = english.replace('°', '').replace('®', '').strip(' ?')
        found = SIG_RE.findall(sig)
        for tag in found:
            if tag == 'G':
                tag = resolve_G(occ, german).rstrip('.')
            wit = SIGLA.get(tag + '.')
            if not wit: continue
            rows.append({'occasion': occ, 'german': german, 'english': english,
                         'literal_only': literal_only, 'witness': wit,
                         'compilation': COMPILATION, 'note': note})
    for occ_, ger, eng, lit, sigs, note in PROSE_ENTRIES:
        for tag in sigs:
            rows.append({'occasion': occ_, 'german': ger, 'english': eng,
                         'literal_only': lit, 'witness': SIGLA[tag],
                         'compilation': COMPILATION, 'note': note})
    return rows

if __name__ == '__main__':
    r = parse()
    print(f'{len(r)} witness rows, {len({(x["occasion"],x["german"]) for x in r})} distinct entries, '
          f'{len({x["occasion"] for x in r})} occasions, {len({x["witness"] for x in r})} witnesses')
    json.dump(r, open(os.path.join(HERE,'rows_liliencron.json'),'w'), ensure_ascii=False, indent=1)
    for x in r[:6]: print(' ', x['occasion'],'|',x['german'],'|',x['english'],'|',x['witness'])
