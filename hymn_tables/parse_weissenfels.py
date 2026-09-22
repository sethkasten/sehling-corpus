import re, sys
sys.path.insert(0, '/home/user/sehling-corpus/hymn_tables')
import extract

SRC = 'Sehling 1, Nr. 159 (Weissenfels, Ordnung der geseng, 1578), pp. 693-696'

MARK = re.compile(
    r'(?P<occ>'
    r'Dominica\s+(?:\d{1,2}\.?\s*(?:und\s+\d\.?)?\s*(?:adventus|post\s+trinitatis)?|'
    r'septuagesimae|sexagesimae|quinquagesimae|invocavit|reminiscere|oculi|laetare|judica|palmarum|'
    r'quasimodogeniti|misericordia|jubilate|cantate|vocem\s+jucunditatis|exaudi)(?:\s+etc\.)?'
    r'|Domina\s+quinquagesimae'
    r'|Christag|Sontag nach dem christag|Neu jahrs tag|Heiligen drei konig tag'
    r'|Pfingsten\.\s*Figuraliter\.\s*Deutsche lieder'
    r'|De sancta trinitate\.\s*Figuraliter\.\s*Deutsch'
    r'|De ascensione domini figuraliter und'
    r'|De nativitate Joannis Baptistae\.\s*Figuraliter\.\s*Deutsch'
    r'|In festa visitationis Mariae figuraliter'
    r'|Die S\. Michaelis etc\.\s*Figuraliter'
    r')\s*:?\s*', re.I)

NORM = {
 'dominica 2. und 3. adventus': 'Advent 2 & 3', 'dominica 4. adventus': 'Advent 4',
 'christag': 'Christmas Day', 'sontag nach dem christag': 'Sunday after Christmas',
 'neu jahrs tag': 'New Year (Circumcision)', 'heiligen drei konig tag': 'Epiphany',
 'dominica septuagesimae': 'Septuagesima', 'dominica sexagesimae': 'Sexagesima',
 'domina quinquagesimae': 'Quinquagesima (Estomihi)',
 'dominica invocavit': 'Lent 1 (Invocavit)', 'dominica reminiscere': 'Lent 2 (Reminiscere)',
 'dominica oculi': 'Lent 3 (Oculi)', 'dominica laetare': 'Lent 4 (Laetare)',
 'dominica judica': 'Lent 5 (Judica)', 'dominica palmarum': 'Palm Sunday', 'dominica judica': 'Lent 5 (Judica)',
 'dominica quasimodogeniti': 'Easter 1 (Quasimodogeniti)',
 'dominica misericordia': 'Easter 2 (Misericordias Domini)',
 'dominica jubilate': 'Easter 3 (Jubilate)', 'dominica cantate': 'Easter 4 (Cantate)',
 'dominica vocem jucunditatis': 'Easter 5 (Rogate/Vocem jucunditatis)',
 'dominica exaudi': 'Sunday after Ascension (Exaudi)',
 'pfingsten. figuraliter. deutsche lieder': 'Pentecost',
 'de sancta trinitate. figuraliter. deutsch': 'Trinity Sunday',
 'de ascensione domini figuraliter und': 'Ascension',
 'de nativitate joannis baptistae. figuraliter. deutsch': 'St John the Baptist (24 June)',
 'in festa visitationis mariae figuraliter': 'Visitation of Mary (2 July)',
 'die s. michaelis etc. figuraliter': 'St Michael (29 September)',
}

def norm_occ(raw):
    k = re.sub(r'\s+', ' ', raw.strip().lower()).rstrip(':').strip()
    k = re.sub(r'\s*etc\.$', '', k).strip()
    if k in NORM: return NORM[k]
    m = re.match(r'dominica\s+(\d{1,2})\.?\s*(post\s+trinitatis)?$', k)
    if m: return f'Trinity {m.group(1)}'
    return raw.strip().rstrip(':')

def parse():
    cit, vol, ps, pe, text = extract.load(145)
    f = extract.flow(text)
    end = f.find('Wochentlich werden zwo predigten')
    seg = f[f.find('Dominica 2. und 3. adventus'):end]
    rows = [('Advent 1', 'Nun kom der heiden heiland', SRC)]   # stated as the rubric's worked example
    marks = list(MARK.finditer(seg))
    for i, m in enumerate(marks):
        body = seg[m.end(): marks[i+1].start() if i+1 < len(marks) else len(seg)]
        body = re.split(r'(?:Uf die fest|Uf die hohen fest|Die deutschen lieder vom fest|'
                        r'Nach dem evangelio|Ostern figural)', body)[0]
        for t in extract.split_titles(body):
            if re.match(r'^(die (lateinische|deutsche) passion|das deutsche benedictus|'
                        r'historiam resurrectionis|domine non secundum|eine mutet|das symbolum)', t, re.I):
                continue
            rows.append((norm_occ(m.group('occ')), t, SRC))
    return rows

if __name__ == '__main__':
    rows = parse()
    print(f'{len(rows)} rows\n')
    for o, t, s in rows: print(f'{o:<38} | {t}')
