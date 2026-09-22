"""Hof 1592, Nördlingen 1579, Heilbronn 1543: Latin office propers.
Only the HYMN field (H: / Hymnus:) is taken -- introits, antiphons and
responsories are propers but not hymns."""
import re, sys
sys.path.insert(0, '/home/user/sehling-corpus/hymn_tables')
import extract
from canon_latin import canon

SOURCES = {
 294:  ('Sehling 11, IV.20 (Hof, Ordo ecclesiasticus, 1592), pp. 407-477',
        'Ordo ecclesiasticus in Hof'),
 375:  ('Sehling 12, VIII.7 (Nördlingen, Kirchenordnung, 1579), pp. 335-393',
        'Verzaichnus der lateinischen gesang'),
 782:  ('Sehling 17, II/17 (Heilbronn, Ordnung des Kirchengesangs, 1543), pp. 320-326',
        'Ordnung des Kirchengesangs'),
}

OCC = re.compile(r'(?P<occ>'
  r'Dominica\s+[IVXL0-9]{1,6}\.?\s*(?:post\s+)?(?:Trinitat\w*|Adventus|Advent|post\s+Epiphanias?|Epiphan\w*)?'
  r'|Dominica\s+(?:Quasimodogeniti|Misericordia\w*|Jubilate|Cantate|Vocem\s+[ij]ucunditatis|Exaudi|'
  r'Invocavit|Reminiscere|Oculi|Laetare|Letare|Judica|Iudica|Palmarum|Septuagesima\w*|Sexagesima\w*|'
  r'Quinquagesima\w*|Rogate)'
  r'|(?:In\s+)?[Ff]est(?:o|um|i)\s+(?:Nativitatis|Epiphaniae|Ascensionis|Pentecostes|Trinitatis|'
  r'Purificationis|Annunciationis|Visitationis|Michaelis|Joannis)\w*'
  r'|De\s+festo\s+\w+'
  r'|In\s+vigilia\s+\w+'
  r'|Am\s+h\.?\s*Christabend|Am\s+Christtag|Am\s+abend\s+des\s+Obersten|Am\s+Obersten'
  r'|Samstags?\s+und\s+Sonntags?\s+[^.]{2,40}'
  r')', re.I)

HYMN = re.compile(r'(?<![A-Za-zÄÖÜäöüß])(?:Hymnus|Hymnum|H)\s*:\s*(?P<h>[^.;|]{4,70})')

# editorial / apparatus text that is not a hymn incipit
JUNK = re.compile(r'(Original|verloren|Antiphonale|Nocturnale|Liber Usualis|Wackernagel|'
                  r'Analecta|HDEKM|StadtA|Abdruck|Textvorlage|am Rand|Magnificat mit|'
                  r'sonst wie oben|manet usque|Collect|mit seinem? Antiphon|'
                  r'die Psalmen|^S\.|^\d)', re.I)

SKIP = re.compile(r'^(ut supra|ut in praecedenti|wie oben|idem|ut sup)', re.I)

ROM = {'i':1,'ii':2,'iii':3,'iv':4,'iiii':4,'v':5,'vi':6,'vii':7,'viii':8,'ix':9,'x':10,
       'xi':11,'xii':12,'xiii':13,'xiv':14,'xv':15,'xvi':16,'xvii':17,'xviii':18,'xix':19,
       'xx':20,'xxi':21,'xxii':22,'xxiii':23,'xxiv':24,'xxv':25,'xxvi':26,'xxvii':27}

def norm_occ(raw):
    r = re.sub(r'\s+', ' ', raw.strip().lower()).rstrip('.')
    m = re.match(r'dominica\s+([ivxl0-9]+)\.?\s*(?:post\s+)?(trinitat\w*|advent\w*|(?:post\s+)?epiphan\w*)?$', r)
    if m:
        n = m.group(1); n = ROM.get(n, n)
        season = m.group(2) or ''
        if 'trinitat' in season: return f'Trinity {n}'
        if 'advent'  in season: return f'Advent {n}'
        if 'epiphan' in season: return f'Epiphany {n}'
        return f'Dominica {n}'
    for pat, lab in [
      (r'quasimodogeniti','Easter 1 (Quasimodogeniti)'),(r'misericordia','Easter 2 (Misericordias Domini)'),
      (r'[ij]ubilate','Easter 3 (Jubilate)'),(r'cantate','Easter 4 (Cantate)'),
      (r'vocem|rogate','Easter 5 (Rogate/Vocem jucunditatis)'),(r'exaudi','Sunday after Ascension (Exaudi)'),
      (r'invocavit','Lent 1 (Invocavit)'),(r'reminiscere','Lent 2 (Reminiscere)'),(r'oculi','Lent 3 (Oculi)'),
      (r'l[ae]tare','Lent 4 (Laetare)'),(r'[ij]udica','Lent 5 (Judica)'),(r'palmarum','Palm Sunday'),
      (r'septuagesima','Septuagesima'),(r'sexagesima','Sexagesima'),(r'quinquagesima','Quinquagesima'),
      (r'nativitatis|christtag|christabend','Christmas'),(r'epiphani|obersten','Epiphany'),
      (r'ascensionis','Ascension'),(r'pentecostes','Pentecost'),(r'trinitatis','Trinity Sunday'),
      (r'purificationis','Purification of Mary (2 Feb)'),(r'annunciationis','Annunciation (25 March)'),
      (r'visitationis','Visitation of Mary (2 July)'),(r'michaelis','St Michael (29 Sept)'),
      (r'joannis','St John the Baptist (24 June)'),
    ]:
        if re.search(pat, r): return lab
    return raw.strip().rstrip('.')

def parse(doc_id):
    src, _ = SOURCES[doc_id]
    cit, vol, ps, pe, text = extract.load(doc_id)
    f = extract.flow(text)
    marks = list(OCC.finditer(f))
    rows, seen = [], set()
    for i, m in enumerate(marks):
        occ = norm_occ(m.group('occ'))
        body = f[m.end(): marks[i+1].start() if i+1 < len(marks) else len(f)]
        if len(body) > 600: body = body[:600]
        for hm in HYMN.finditer(body):
            raw = hm.group('h')
            for part in re.split(r'\s*(?:,\s*)?\bvel\b\s*:?\s*|\s+oder\s+|\s+dann\s+', raw):
                h = re.sub(r'\d+\s*$', '', part)             # trailing footnote markers
                h = re.sub(r'\s*\([^)]*\)?\s*$', '', h)      # trailing editorial parens
                h = re.sub(r'^(de\s+\w+\s*:?\s*)', '', h, flags=re.I)
                h = extract.clean_title(h)
                if not h or SKIP.match(h) or len(h) < 5: continue
                if JUNK.search(h): continue
                c = canon(h)
                if not c: continue          # not a recognised office hymn
                h = c
                key = (occ, h.lower())
                if key in seen: continue
                seen.add(key)
                rows.append((occ, h, src))
    return rows

if __name__ == '__main__':
    for did in SOURCES:
        r = parse(did)
        print(f'\n### doc {did}: {len(r)} rows -- {SOURCES[did][1]}')
        for o,h,s in r[:18]: print(f'   {o:<36} | {h}')
