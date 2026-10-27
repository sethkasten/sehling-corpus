"""Extract per-occasion hymn prescriptions from the Sehling corpus hymn tables."""
import sqlite3, re, json, unicodedata

DB = 'eko.db'

def load(doc_id):
    c = sqlite3.connect(DB).cursor()
    c.execute('SELECT citation, volume_id, page_start, page_end, text FROM documents WHERE id=?', (doc_id,))
    return c.fetchone()

def flow(text):
    """Strip page furniture, join wrapped lines into one flow."""
    out = []
    for ln in text.split('\n'):
        s = ln.strip()
        if not s: continue
        if re.match(r'^\[p\.\s*\d+\]$', s): continue
        if re.match(r'^\d{1,4}$', s): continue                      # bare page numbers
        if re.match(r'^\d{1,4}\s+Die Kirchenordnungen', s): continue # running heads
        if re.match(r'^(Die Kirchenordnungen|Nördlingen|Pfalz-Zweibrücken|Weissenfels)\b', s): continue
        if re.match(r'^\d+\s*(Vgl\.|Siehe|Wackernagel|Liber Usualis|Antiphonale)', s): continue
        out.append(s)
    t = ' '.join(out)
    t = re.sub(r'\s+', ' ', t)
    t = t.replace('- ', '')          # rejoin hyphenated line breaks
    return t

FOOTNOTE = re.compile(r'^\d{1,2}\s+(?![.\d])\S')      # "13 Die folgenden ..."; an item is "13. ..."

def lines(doc_id, start, end, furniture=()):
    """The printed lines of a list, from START up to END, without page furniture or
    footnotes. A footnote runs from its number to the first line that ends a sentence."""
    text = load(doc_id)[4]
    i = text.index(start)
    text = text[i: text.index(end, i)]
    out, in_note = [], False
    for ln in text.split('\n'):
        s = ln.strip()
        if not s: continue
        if re.match(r'^\[p\.\s*\d+\]$', s):
            in_note = False; continue
        if re.match(r'^\d{1,4}\s*\*?$', s): continue                 # page numbers, signatures
        if any(re.match(p, s) for p in furniture): continue          # running heads
        if in_note or FOOTNOTE.match(s):
            in_note = not re.search(r'[.!)]$', s)
            continue
        if out and re.search(r'[a-zäöüß]-$', out[-1]):
            out[-1] = out[-1][:-1] + s                               # a hyphenated break
        else:
            out.append(s)
    return out

def clean_title(s):
    s = s.strip()
    s = re.sub(r'\s*\betc\.?\s*$', '', s, flags=re.I)
    s = re.sub(r'^[:\-–\s]+', '', s)
    s = re.sub(r'\s*[.,;]\s*$', '', s)
    s = re.sub(r'\s+', ' ', s)
    return s.strip()

def split_titles(s):
    """One cell may hold several alternative hymns."""
    parts = re.split(r'\betc\.\s*(?=[A-ZÄÖÜ])|\s+und:\s+|\s*\|\s*|\s+oder\s+|'
                     r'\s*Das deutsche lied, nach der epistel:\s*|\s+und das deutsche benedictus', s)
    res = []
    for p in parts:
        p = clean_title(p)
        if p and len(p) > 3 and not re.match(r'^(figuraliter|choraliter|deutsch|ut supra)$', p, re.I):
            res.append(p)
    return res
