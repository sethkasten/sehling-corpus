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
