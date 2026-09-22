# -*- coding: utf-8 -*-
"""Ludecus, Ordo cantionum Germanicarum (1589).

The docx alternates occasion headings (German paragraph, then its English
translation) with a two-column table of hymns (transcription | translation).
Paragraphs and tables must be read in document order, which python-docx
does not do by default.
"""
import re, os, json
import docx
from docx.table import Table
from docx.text.paragraph import Paragraph

HERE = os.path.dirname(os.path.abspath(__file__))
WITNESS = 'Ludecus, Ordo cantionum Germanicarum (1589)'
COMPILATION = WITNESS

ORD = {'ersten':1,'andern':2,'anderen':2,'dritten':3,'vierten':4,'fünfften':5,'fünften':5,
       'sechsten':6,'siebenden':7,'achten':8,'neunden':9,'zehenden':10,
       'first':1,'second':2,'third':3,'fourth':4,'fifth':5,'sixth':6,'seventh':7,
       'eighth':8,'ninth':9,'tenth':10,
       # early-modern roman numerals with terminal long-i
       'i':1,'ij':2,'ii':2,'iij':3,'iii':3,'iiij':4,'iiii':4,'iv':4,'v':5,'vj':6,'vi':6,
       'vij':7,'vii':7,'viij':8,'viii':8,'ix':9,'x':10,'xj':11,'xi':11,'xij':12,'xii':12}

def blocks(doc):
    body = doc.element.body
    for child in body.iterchildren():
        if child.tag.endswith('}p'):   yield Paragraph(child, doc)
        elif child.tag.endswith('}tbl'): yield Table(child, doc)

def num(tok):
    t = tok.strip().lower().rstrip('.')
    if t in ORD: return ORD[t]
    m = re.match(r'^(\d+)(?:st|nd|rd|th)?$', t)   # "10th" -> 10
    if m: return int(m.group(1))
    return tok

def norm_occ(s):
    r = re.sub(r'\s+', ' ', s.strip().lower()).rstrip('.')
    if re.search(r'hochzeit ward|there was a wedding', r):
        return None                      # the Cana gospel incipit, not an occasion heading
    m = re.search(r'am (\d+)\. vnd (\d+)\. sontag nach trinitatis|'
                  r'on the (\d+)(?:st|nd|rd|th) and (\d+)(?:st|nd|rd|th) sunday after trinity', r)
    if m: return f'Trinity {m.group(1) or m.group(3)} & {m.group(2) or m.group(4)}'
    m = re.search(r'am (\w+) sontag des aduents|on the (\w+) sunday of advent', r)
    if m: return f'Advent {num(m.group(1) or m.group(2))}'
    m = re.search(r'am (\d+)\. vnd (\d+)\. sontag des aduents|on the (\d+)(?:rd|th) and (\d+)(?:rd|th) sunday of advent', r)
    if m: return f'Advent {m.group(1) or m.group(3)} & {m.group(2) or m.group(4)}'
    m = re.search(r'am (\w+) sontag nach epiphani|on the (\w+) sunday after epiphany', r)
    if m: return f'Epiphany {num(m.group(1) or m.group(2))}'
    m = re.search(r'am (\d+)\. sontag nach epiphani|on the (\d+)(?:st|nd|rd|th) sunday after epiphany', r)
    if m: return f'Epiphany {m.group(1) or m.group(2)}'
    m = re.search(r'am ([ivxj]+)\. sontag nach trinitatis', r)
    if m: return f'Trinity {num(m.group(1))}'
    m = re.search(r'am (\w+) sontag nach trinitatis|on the (\w+) sunday after trinity', r)
    if m: return f'Trinity {num(m.group(1) or m.group(2))}'
    m = re.search(r'am (\d+)\. sontag nach trinitatis|on the (\d+)(?:st|nd|rd|th) sunday after trinity', r)
    if m: return f'Trinity {m.group(1) or m.group(2)}'
    for pat, lab in [
      (r'weyhenachten|holy christmas', 'Christmas'),
      (r'newen jarstage|new year', 'New Year (Circumcision)'),
      (r'drey k[oö]nige|epiphany of christ', 'Epiphany'),
      (r'septuagesima', 'Septuagesima'), (r'sexagesima', 'Sexagesima'),
      (r'esto\s?mihi', 'Quinquagesima (Esto mihi)'),
      (r'[ij]nuocauit|invocavit', 'Lent 1-3 (Invocavit, Reminiscere, Oculi)'),
      (r'mitfasten|l[ae]tare|mid-lent', 'Lent 4 (Laetare)'),
      (r'judica|stillenfreitag|passion psalm', 'Lent 5 (Judica), Palm Sunday & Good Friday'),
      (r'ostertag|easter day', 'Easter'),
      (r'quasimodogeniti', 'Easter 1-4 (Quasimodogeniti to Cantate)'),
      (r'vocem [ij]ucunditatis', 'Easter 5 (Rogate/Vocem jucunditatis)'),
      (r'himelsfarth|ascension', 'Ascension'), (r'exaudi', 'Sunday after Ascension (Exaudi)'),
      (r'pfingst|pentecost', 'Pentecost'), (r'^(auff|am|on)?\s*(die|the)?\s*(heilige[nr]?\s*)?(dreifaltigkeit|trinitatis|trinity sunday)$', 'Trinity Sunday'),
      (r'johannis|john the baptist', 'St John the Baptist (24 June)'),
      (r'visitation|heimsuchung', 'Visitation of Mary (2 July)'),
      (r'michael', 'St Michael (29 Sept)'),
      (r'annunciat|verk[uü]ndigung|mari[ae] bodschaft', 'Annunciation (25 March)'),
      (r'purificat|liechtmess|lichtmess|reinigung mari', 'Purification of Mary (2 Feb)'),
      (r'kirchweihu|church dedication', 'Church Dedication'),
      (r'begr[aä]bnis|begrebnis|for burial', 'Burial'),
      (r'pauli bekerung|paul.s conversion', 'Conversion of St Paul (25 Jan)'),
      (r'mari[aæ] magdalen|mary magdalene', 'St Mary Magdalene (22 July)'),
      (r'laurentij|lawrence', 'St Lawrence (10 Aug)'),
      (r'auffnehmung mari|assumption of mary', 'Assumption of Mary (15 Aug)'),
      # must precede the St Matthew test: this heading lists the apostles by name,
      # so "Matthiæ" occurs inside it
      (r'an der apostel tage|days of the apostles', 'Common of Apostles'),
      (r'matthi[aæ] apostels|st\.? matthew', 'St Matthew (21 Sept)'),
      (r'aller heiligen|all saints', 'All Saints (1 Nov)'),
      (r'martini|st\.? martin', 'St Martin (11 Nov)'),
      (r'catharinen|st\.? catherine', 'St Catherine (25 Nov)'),
      (r'^(auff|am|an|on|jn|in)?\s*(die|the)?\s*(heilige[nr]?\s*)?trinity$', 'Trinity Sunday'),
    ]:
        if re.search(pat, r): return lab
    return None

# The one table that a column switch moves to a different occasion than the
# heading above it; its contents are unambiguously the Christmas hymns.
COLUMN_OVERRIDE = {'Omnis mundus iucundetur': 'Christmas'}

SKIP = re.compile(r'^(transcription|translation|page \d+|right column|left column|'
                  r'.*header:|von dieser zeit|so kan man|welcher hymnus|in addition|'
                  r'from this time|one may|hierzu|wie oben|as above)', re.I)

def parse():
    doc = docx.Document(os.path.join(HERE, 'src_ludecus_1589.docx'))
    rows, occ, col_switch = [], None, False
    for b in blocks(doc):
        if isinstance(b, Paragraph):
            o = norm_occ(b.text)
            if o:
                occ = o; col_switch = False
            elif re.search(r'right column|left column', b.text, re.I):
                col_switch = True          # a page-number marker is only a continuation
        else:
            if not occ: continue
            if col_switch:
                first = b.rows[1].cells[0].text.strip() if len(b.rows) > 1 else ''
                occ = COLUMN_OVERRIDE.get(first.rstrip('.'), occ)
                col_switch = False
            for r in b.rows:
                cells = [c.text.strip() for c in r.cells]
                if len(cells) < 2: continue
                ger, eng = cells[0], cells[1]
                if SKIP.match(ger) or SKIP.match(eng): continue
                ger = re.sub(r'\s*\(oder\)\s*$', '', ger).strip(' .')
                eng = re.sub(r'\s*\(or\)\s*$', '', eng).strip(' .')
                if len(ger) < 5 or len(ger) > 80: continue
                rows.append({'occasion': occ, 'german': ger, 'english': eng,
                             'literal_only': True, 'witness': WITNESS,
                             'compilation': COMPILATION, 'note': None})
    # de-dup identical (occasion, incipit) pairs from merged table cells
    seen, out = set(), []
    for r in rows:
        k = (r['occasion'], r['german'].lower())
        if k in seen: continue
        seen.add(k); out.append(r)
    return out

if __name__ == '__main__':
    r = parse()
    print(f'{len(r)} rows, {len({x["occasion"] for x in r})} occasions')
    json.dump(r, open(os.path.join(HERE,'rows_ludecus.json'),'w'), ensure_ascii=False, indent=1)
    for x in r[:10]: print(' ', x['occasion'],'|',x['german'][:44],'|',x['english'][:40])
