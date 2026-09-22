import re, sys
sys.path.insert(0, '/home/user/sehling-corpus/hymn_tables')
import extract

SRC = 'Sehling 4, Pommern (Agenda, 1569), pp. 425-480'

ORD = {'ersten':1,'andern':2,'andren':2,'drüdden':3,'drudden':3,'veerden':4,'vöfften':5,'vofften':5,
       'sösten':6,'sosten':6,'söven':7,'soven':7,'achten':8,'negenden':9,'teinden':10,'elfften':11,
       'twölfften':12,'dörteinden':13,'veerteinden':14,'föffteinden':15,'sösteinden':16,
       'söventeinden':17,'achteinden':18,'negenteinden':19,'twintigsten':20}
ROM = {'i':1,'ii':2,'iii':3,'iiii':4,'iv':4,'v':5,'vi':6,'vii':7,'viii':8,'ix':9,'x':10,'xi':11,
       'xii':12,'xiii':13,'xiiii':14,'xiv':14,'xv':15,'xvi':16,'xvii':17,'xviii':18,'xix':19,
       'xx':20,'xxi':21,'xxii':22,'xxiii':23,'xxiiii':24,'xxiv':24,'xxv':25,'xxvi':26,'xxvii':27}

# only treat as an occasion label if it names a Sunday/feast
OCCWORD = re.compile(r'(sondage|sondach|winachten|nien jars|kinder dage|köninge|apenbaringe|'
                     r'purificationis|septuagesima|esto mihi|invocavit|reminiscere|oculi|letare|'
                     r'[ij]udica|palmarum|pasche|osteren|quasimodogeniti|misericordia|[ij]ubilate|'
                     r'cantate|rogate|vocem|hemmelva?e?rt|hemmelfart|exaudi|pinge?sten|trinitatis|drefoldicheit|'
                     r'johannis|visitationis|michaelis|annunciationis|bodeschop|pasche|'
                     r'mitfasten|passion psalme|stillen fridach)', re.I)
MARK = re.compile(r'(?P<occ>(?:Am|An|Up|Im|In)\s+[^.]{3,90}?)\s*\.\s*', re.I)

# rubric prose to discard (not hymn incipits)
PROSE = re.compile(r'(kan men|schal men|is gut|umme der lere willen|alse dar sint|jedoch|'
                   r'bet up|desülvigen|averein|willen singe|de leste vers|men singe|'
                   r'Das Herzogthum|in der weke|edder ock$|gesenge van der)', re.I)

def num(tok):
    t = tok.strip().lower().rstrip('.')
    if t in ORD: return ORD[t]
    if t in ROM: return ROM[t]
    if t.isdigit(): return int(t)
    return tok

def norm_occ(raw):
    r = re.sub(r'\s+', ' ', raw.strip().lower())
    m = re.search(r'am\s+(\w+)\s+sondage\s+(?:na|nah)\s+trinitat', r)
    if m: return f'Trinity {num(m.group(1))}'
    m = re.search(r'am\s+([ivxl]+)\.?\s*sondage\s+(?:na|nah)\s+trinitat', r)
    if m: return f'Trinity {num(m.group(1))}'
    m = re.search(r'am\s+(\w+)\s+sondage\s+des\s+advent', r)
    if m: return f'Advent {num(m.group(1))}'
    m = re.search(r'am\s+(\w+)\s+unde\s+(\w+)\s+sondage\s+des\s+advent', r)
    if m: return f'Advent {num(m.group(1))} & {num(m.group(2))}'
    m = re.search(r'am\s+(\w+)\s+sondage\s+na\s+epiphan', r)
    if m: return f'Epiphany {num(m.group(1))}'
    for pat, lab in [
        (r'invocavit,\s*reminiscere,\s*oculi', 'Lent 1-3 (Invocavit, Reminiscere, Oculi)'),
        (r'mitfasten', 'Lent 4 (Mid-Lent / Laetare)'),
        (r'passion psalme.*(iudica|judica)', 'Lent 5 (Judica), Palm Sunday & Good Friday'),
        (r'hiligen paschefest|paschefest', 'Easter'),
        (r'hiligen winachten', 'Christmas / New Year'), (r'unschüldigen kinder', 'Holy Innocents'),
        (r'dre köninge|apenbaringe christi', 'Epiphany'), (r'purificationis', 'Purification of Mary (2 Feb)'),
        (r'septuagesima', 'Septuagesima & Sexagesima'), (r'esto mihi', 'Quinquagesima (Esto mihi)'),
        (r'invocavit', 'Lent 1 (Invocavit)'), (r'reminiscere', 'Lent 2 (Reminiscere)'),
        (r'oculi', 'Lent 3 (Oculi)'), (r'letare|laetare', 'Lent 4 (Laetare)'),
        (r'sondach [ij]udica,\s*palmdach', 'Lent 5 (Judica), Palm Sunday & Good Friday'),
        (r'[ij]udica', 'Lent 5 (Judica)'), (r'palmarum|palmen', 'Palm Sunday'),
        (r'paschen|osteren|hilige[nm]? oster', 'Easter'), (r'quasimodogeniti', 'Easter 1 (Quasimodogeniti)'),
        (r'misericordia', 'Easter 2 (Misericordias Domini)'), (r'[ij]ubilate', 'Easter 3 (Jubilate)'),
        (r'cantate', 'Easter 4 (Cantate)'), (r'rogate|vocem', 'Easter 5 (Rogate)'),
        (r'hemmelva?e?rt|hemmelfart|ascensio', 'Ascension'), (r'exaudi', 'Sunday after Ascension (Exaudi)'),
        (r'pinge?sten|pfingst', 'Pentecost'), (r'trinitatis$|hilige[nm]? drefoldicheit', 'Trinity Sunday'),
        (r'johannis des döpers', 'St John the Baptist (24 June)'),
        (r'visitationis', 'Visitation of Mary (2 July)'), (r'michaelis', 'St Michael (29 Sept)'),
        (r'annunciationis|mariae bodeschop', 'Annunciation (25 March)'),
    ]:
        if re.search(pat, r): return lab
    return raw.strip()

def parse():
    cit, vol, ps, pe, text = extract.load(1865)
    f = extract.flow(text)
    start = f.find('Wat men vor düdische psalmen singen schal')
    seg = f[start:]
    for stop in ('[Es folgen drei Symbole', 'Consistorial-Instruction', 'Der erste theil'):
        k = seg.find(stop)
        if k > 0: seg = seg[:k]
    # "Am XXIII. sondage" -> the period would otherwise end the occasion label
    seg = re.sub(r'\b(Am\s+[IVXL]{1,7})\.\s*(?=sondage)', r'\1 ', seg)
    # source omits the period after this feast label, which would swallow the first hymn
    seg = re.sub(r'(hiligen pinge?sten)\s+(?=[A-ZÄÖÜ])', r'\1. ', seg)
    VALID = re.compile(r'^(Trinity|Advent|Epiphany|Easter|Lent|Christmas|Holy|Purification|'
                       r'Septuagesima|Quinquagesima|Palm|Ascension|Sunday after|Pentecost|St |'
                       r'Visitation|Annunciation)')
    marks = [m for m in MARK.finditer(seg)
             if OCCWORD.search(m.group('occ')) and VALID.match(norm_occ(m.group('occ')))]
    rows = []
    for i, m in enumerate(marks):
        occ = norm_occ(m.group('occ'))
        body = seg[m.end(): marks[i+1].start() if i+1 < len(marks) else len(seg)]
        for piece in body.split('.'):
            if ':' in piece:          # rubric introduces the hymn after a colon
                piece = piece.rsplit(':', 1)[1]
            t = extract.clean_title(piece)
            t = re.sub(r'^(edder ock|so kan men up disen sondach singen|alse dar sint)[:\s]*', '', t, flags=re.I)
            t = extract.clean_title(t)
            if not t or len(t) < 8 or len(t) > 70: continue
            if PROSE.search(t): continue
            rows.append((occ, t, SRC))
    return rows

if __name__ == '__main__':
    rows = parse()
    print(f'{len(rows)} rows')
    seen=set()
    for o,t,s in rows:
        if o not in seen: print(f'--- {o}'); seen.add(o)
        print(f'      {t}')
