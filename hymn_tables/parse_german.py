"""Mansfeld, Pfalz-Zweibrücken 1565, Hohenlohe 1596: German hymn orders
organised by season / liturgical slot rather than strictly per-Sunday."""
import re, sys
sys.path.insert(0, '/home/user/sehling-corpus/hymn_tables')
import extract

PROSE = re.compile(r'(wird bei uns|zweierlei|durch tegliche|jugent|fodert|ubung|gesangbüchlein|'
                   r'sol im anfange|Die vier Harzgrafschaften|verzeichnet ist|erheischunge|'
                   r'gehalten werden|prediget|monat|vesper zeit|abbrechen|geprediget|'
                   r'Textvorlage|Reinschrift|Konzept|Der hymnus|Der himnus|Oder$|'
                   r'siehe|vgl\.|Anm\.|^S\. \d|Schulmaister|schuelmeister|pfarrherr|'
                   r'Bedenken|frühere Ordnung|Fehlt|Wie Anm)', re.I)

def rows_mansfeld():
    SRC = 'Sehling 2, Grafschaft Mansfeld (Kirchenordnung), pp. 210-247'
    cit, vol, ps, pe, text = extract.load(1241)
    f = extract.flow(text)
    i = f.find('Ordnung gemeiner deutscher kirchen gesenge')
    seg = f[i: f.find('Zum andern, wird der catechismus bei uns sonderlich', i)]
    LAB = [
      (r'Im advent', 'Advent'),
      (r'Umb,? und nach weinachten, bis auf festum purificationis', 'Christmas to Purification'),
      (r'Auf purificationis', 'Purification of Mary (2 Feb)'),
      (r'In der fasten', 'Lent'),
      (r'In der marterwoche', 'Holy Week'),
      (r'Umb und nach ostern', 'Easter season'),
      (r'Umb,? und nach pfingsten', 'Pentecost season'),
      (r'Auf trinitatis', 'Trinity Sunday'),
    ]
    pat = re.compile('(' + '|'.join(p for p, _ in LAB) + r')\s*\.\s*', re.I)
    marks = list(pat.finditer(seg))
    out = []
    for k, m in enumerate(marks):
        occ = next(lab for p, lab in LAB if re.match(p, m.group(1), re.I))
        body = seg[m.end(): marks[k+1].start() if k+1 < len(marks) else len(seg)]
        for piece in re.split(r'\.\s*|\bOder\b\s*\.?\s*', body):
            t = extract.clean_title(piece).lstrip('*').strip()
            t = re.sub(r',?\s*J\.\s*S\.?\s*$', '', t).strip()
            if not t or len(t) < 8 or len(t) > 70 or PROSE.search(t): continue
            out.append((occ, t, SRC))
    return out

def rows_zweibruecken():
    SRC = 'Sehling 18, I/23 (Pfalz-Zweibrücken, Ordnung der Kirchengesänge, 1565), pp. 337-341'
    cit, vol, ps, pe, text = extract.load(985)
    f = extract.flow(text)
    seg = f[f.find('Die erst wochen'):]
    WEEK = re.compile(r'(Die (?:erst|annder|dridt) [Ww]och\w*[^.]{0,30}?)\s*\.', re.I)
    SLOT = re.compile(r'\b(Nachmittag|Mittwochen?|Freydag|Sambstag zur vesper|'
                      r'Al[sß] am Ostertag morgens|Feyrdag|Hohe fest[^.]{0,40}|'
                      r'Ge?senng? zu den Hochzeiten|Geseng zu den begrebdnussen|'
                      r'Kindertauff[^.]{0,40})\s*\.', re.I)
    FIELD = re.compile(r'\b(Introitus|Post Confessionem|Post Epistolam|Ante Con[ct]ionem|'
                       r'Post Con[ct]ionem|Post Catechismum|Conclussio|Conclusio|'
                       r'Ante Lectionem Capituli|Post Lectionem)\s*:?\s*(?P<v>[^.]{4,80})', re.I)
    out, week, slot = [], None, 'Sunday morning'
    for chunk in re.split(r'(?=Die (?:erst|annder|dridt) [Ww]och)', seg):
        wm = WEEK.match(chunk)
        if wm:
            w = wm.group(1).lower()
            week = 'Week 1' if 'erst' in w else 'Week 2' if 'annder' in w else 'Week 3'
        if not week: continue
        pos, slot = 0, 'Sunday morning'
        marks = list(SLOT.finditer(chunk))
        spans = [(0, marks[0].start() if marks else len(chunk), 'Sunday morning')]
        for j, m in enumerate(marks):
            spans.append((m.end(), marks[j+1].start() if j+1 < len(marks) else len(chunk),
                          re.sub(r'\s+', ' ', m.group(1)).strip()))
        for a, b, sl in spans:
            for fm in FIELD.finditer(chunk[a:b]):
                t = extract.clean_title(fm.group('v'))
                for part in re.split(r'\s+oder\s+|\s*,\s*(?=[A-ZÄÖÜ][a-zäöü])', t):
                    p2 = extract.clean_title(part)
                    if not p2 or len(p2) < 6 or len(p2) > 70 or PROSE.search(p2): continue
                    out.append((f'{week}, {sl} ({fm.group(1)})', p2, SRC))
    return out

def rows_hohenlohe():
    SRC = 'Sehling 15, Nr. 54 (Hohenlohe, Schul- und Gesangsordnung, 1596), pp. 641-660'
    cit, vol, ps, pe, text = extract.load(628)
    f = extract.flow(text)
    i = f.find('Morgens und mittags an den ftirnemesten festen')
    if i < 0: i = f.find('Auf den besondern jarfesten')
    seg = f[i:i+7000]
    FEAST = re.compile(r'\b\d\.\s*(Nativitatis|Wan man den Paßion predigt|Zum Paßion|Ostern|'
                       r'Ascensionis|Pentecostes|Baptistae|Annunciationis[^:]{0,20}Mariae|Adventus)'
                       r'\s*\d*\s*:\s*', re.I)
    MAP = {'nativitatis':'Christmas','wan man den paßion predigt':'Passiontide','zum paßion':'Passiontide',
           'ostern':'Easter','ascensionis':'Ascension','pentecostes':'Pentecost',
           'baptistae':'St John the Baptist (24 June)','adventus':'Advent'}
    out = []
    marks = list(FEAST.finditer(seg))
    for k, m in enumerate(marks):
        key = re.sub(r'\s+', ' ', m.group(1)).strip().lower()
        occ = MAP.get(key, 'Annunciation (25 March)' if 'annunciationis' in key else key.title())
        body = seg[m.end(): marks[k+1].start() if k+1 < len(marks) else m.end()+220]
        body = re.split(r'(?:Nach der lection|wNach der lection|Zun jarfesten|Catechismus|'
                        r'Sontags\b|Freytagspredigten|Vesper\b)', body)[0]
        for part in re.split(r'\s*etc\.\s*,?\s*', body):
            t = extract.clean_title(part)
            t = re.sub(r'^[\^\ds,]+\s*', '', t)                    # stray OCR sigla
            t = re.sub(r'^oder\s*\([^)]*:\s*', '', t, flags=re.I)  # "oder (da man ...: "
            t = re.sub(r'^oder\s*:?\s*', '', t, flags=re.I)
            t = extract.clean_title(t)
            if not t or len(t) < 6 or len(t) > 70 or PROSE.search(t): continue
            out.append((occ, t, SRC))
    return out

def parse_all():
    return rows_mansfeld() + rows_zweibruecken() + rows_hohenlohe()

if __name__ == '__main__':
    for name, fn in [('MANSFELD', rows_mansfeld), ('ZWEIBRUECKEN', rows_zweibruecken), ('HOHENLOHE', rows_hohenlohe)]:
        r = fn(); print(f'\n### {name}: {len(r)} rows')
        for o, t, s in r[:16]: print(f'   {o:<46} | {t}')
