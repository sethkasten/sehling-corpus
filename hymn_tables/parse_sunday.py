"""Naumburg 1537/38, Nördlingen 1544/1555, Anhalt 1551, Pirna (1555-1569) and
Nördlingen 1579: the German hymn sung after the epistle, before the gospel, set out
Sunday by Sunday or feast by feast. Only that slot is taken; the hymns these orders
set before or after the sermon or at vespers are not.

An entry "Idem" repeats the hymn of the entry before it. A reference to a whole other
order of service ("the same is kept at the Circumcision, Epiphany and Purification")
is not followed."""
import re, sys
sys.path.insert(0, '/home/user/sehling-corpus/hymn_tables')
import extract

ROMAN = {'I': 1, 'II': 2, 'III': 3, 'IV': 4, 'V': 5, 'VI': 6, 'VII': 7, 'VIII': 8, 'IX': 9,
         'X': 10, 'XI': 11, 'XII': 12, 'XIII': 13, 'XIV': 14, 'XV': 15, 'XVI': 16, 'XVII': 17,
         'XVIII': 18, 'XIX': 19, 'XX': 20, 'XXI': 21, 'XXII': 22, 'XXIII': 23, 'XXIV': 24,
         'XXV': 25, 'XXVI': 26, 'XXVII': 27}

LENT = {'septuagesima': 'Septuagesima', 'sexagesima': 'Sexagesima',
        'quinquagesima': 'Quinquagesima (Estomihi)', 'quadragesima': 'Lent 1 (Invocavit)',
        'invocavit': 'Lent 1 (Invocavit)', 'reminiscere': 'Lent 2 (Reminiscere)',
        'oculi': 'Lent 3 (Oculi)', 'laetare': 'Lent 4 (Laetare)', 'judica': 'Lent 5 (Judica)',
        'palmarum': 'Palm Sunday'}
LENT_RE = r'(?i:(Septuagesima|Sexagesima|Quinquagesima|Quadragesima|Invocavit|Reminiscere|Oculi|Laetare|Judica|Palmarum))e?'

# alternatives ("oder", "item") and one title per sentence
SPLIT = re.compile(r'\s*\b(?:oder|Oder|item)\b\s*[:.,]?\s*|(?<=[a-zäöüß]{2}[.?!])\s+(?=[*A-ZÄÖÜ])|\n')

def titles(body, skip=None):
    out = []
    for piece in SPLIT.split(body):
        t = re.sub(r'(?<=[a-zäöüß.])\d{1,2}\)?(?=[\s.:,]|$)', '', piece)  # footnote markers
        t = re.sub(r'^\[[^\]]*\]\s*:?\s*', '', t)                          # "[2. Febr.]:"
        t = re.sub(r'\s*\betc\b.*$', '', t)                                # "etc." and what follows
        t = re.sub(r',?\s*\balternatim\b\.?\s*$', '', t, flags=re.I)
        t = extract.clean_title(t).lstrip('*').rstrip('?').strip()
        if len(t) < 6 or (skip and skip.search(t)): continue
        out.append(t)
    return out

def entries(lines, labels, seasons=(), joiner=' '):
    """[(occasion, body)] from a list of label lines, each followed by its hymns. A label
    is matched at the start of a line, and any text after it on that line is its body.
    Under a season heading, numbered lines "1. ..." are that season's Sundays."""
    out, cur, season = [], None, None
    for s in lines:
        hd = next((name for pat, name in seasons if re.fullmatch(pat, s)), None)
        if hd:
            season, cur = hd, None
            continue
        m = re.match(r'(\d{1,2})\.\s+(.*)$', s) if season else None
        if m:
            cur = [f'{season} {int(m.group(1))}', [m.group(2)]]
            out.append(cur)
            continue
        for pat, occ in labels:
            m = re.match(pat, s)
            if m:
                season = None
                cur = [occ(m) if callable(occ) else occ, [s[m.end():].strip()]]
                out.append(cur)
                break
        else:
            if cur: cur[1].append(s)
    return [(occ, joiner.join(b).strip()) for occ, b in out if occ]

def rows_from(ents, src, skip=None):
    rows, prev = [], []
    for occ, body in ents:
        found = prev if re.match(r'Idem\b', body) else titles(body, skip)
        rows += [(occ, t, src) for t in found]
        prev = found
    return rows

def feasts(text, src, pats):
    """The hymn(s) of the slot after the epistle, one pattern per feast."""
    rows = []
    for pat, occs in pats:
        m = re.search(pat, text)
        assert m, pat
        for occ in occs:
            rows += [(occ, t, src) for t in titles(m.group('h'))]
    return rows

# ---- Naumburg, St Wenzel, 1537/38 -------------------------------------------------------------
NAUMBURG = 'Sehling 2, Nr. 13 (Naumburg, Kirchen-Ordnung für St. Wenzel, 1537/38), pp. 76-77'

def rows_naumburg():
    ls = extract.lines(1219, 'An den hohen festen werden die gesenge', 'Das magnificat mag man singen',
                       furniture=[r'\d+\. Kirchen-Ordnung für die St\. Wenzelskirche'])
    k = next(i for i, s in enumerate(ls) if s.startswith('Was man an einem jedem sontage'))
    rows = feasts(' '.join(ls[:k]), NAUMBURG, [
        (r'Zue weinachten\..*?Nach der epistel, (?P<h>.+?), zum anfang', ['Christmas']),
        (r'Zu ostern\..*?Nach der epistel, (?P<h>.+?)\. Die predigt', ['Easter']),
        (r'Zue pfingsten\..*?Nach der epistel, (?P<h>.+?)\. Nach der predigt', ['Pentecost']),
        (r'In festis beatae virginis\..*?\. (?P<h>[^.]+?), nach der\s+epistel', ['Feasts of the Virgin Mary']),
        (r'In festis apostolorum et Johan\. baptistae\.\s*(?P<h>[^.]+?), nach der\s+epistel',
         ['Common of Apostles', 'St John the Baptist (24 June)']),
    ])
    labels = [(r'Was man an einem jedem sontage|Post trinitatis\.', None),
              (r'(?:Dominica )?' + LENT_RE + r'\.', lambda m: LENT[m.group(1).lower()])]
    return rows + rows_from(entries(ls[k:], labels,
                                    [(r'Dominica\.', 'Trinity'), (r'In adventu dominica\.', 'Advent')]),
                            NAUMBURG)

# ---- Nördlingen, St George's, Löner 1544, revised by Runtzler 1555 ------------------------------
NOERDLINGEN_1555 = ('Sehling 12, VIII.5 (Nördlingen, Ordnung der Ceremonien zu St. Georgen, '
                    '1544/1555), pp. 321-323')

def rows_noerdlingen_1555():
    ls = extract.lines(373, 'Zum tageampt aber an den hohen festen', 'Nach gelegenhait der zeit, nachdem',
                       furniture=[r'Nördlingen$', r'Ordnung der ceremonien \.\.\. zu', r'\d+ Sehling, Bd\.'])
    k = next(i for i, s in enumerate(ls) if s.startswith('Was man an ain jeden sontag'))
    rows = feasts(' '.join(ls[:k]), NOERDLINGEN_1555, [
        (r'Zu Weihnachten\..*?Nach der epistel (?P<h>.+?)\. 3\.', ['Christmas']),
        (r'Zu Ostern .*?Nach der epistel (?P<h>.+?)\. 3\.', ['Easter']),
        # "Discumbentibus" and "Omnes gentes" are figural pieces; the hymn is the alternative
        (r'Ascensionis Domini\..*?nicht figurirt, (?P<h>.+?)\. Sonst', ['Ascension']),
        (r'Sontag post Ascensionis\..*?Post epistolam (?P<h>.+?)\. Zu Pfingsten',
         ['Sunday after Ascension (Exaudi)']),
        (r'Zu Pfingsten\..*?Nach der epistel (?P<h>.+?)\. 4\.', ['Pentecost']),
        (r'In festis Beatae Virginis\..*?\d\.\s*(?P<h>[^.]+?) nach der epistel', ['Feasts of the Virgin Mary']),
        (r'In festis apostolorum et Joannis baptistae\.\s*1\.\s*(?P<h>[^.]+?) nach der\s+epistel',
         ['Common of Apostles', 'St John the Baptist (24 June)']),
    ])
    labels = [(r'Was man an ain jeden sontag', None),
              (r'Judica et Palmarum\.', 'Lent 5 (Judica) & Palm Sunday'),
              (r'(?:Dominica )?' + LENT_RE + r'\.', lambda m: LENT[m.group(1).lower()]),
              (r'Folgende sontage singet man', None)]   # "the Christmas songs, as Christ lag ..."
    skip = re.compile(r'singet der cantor|kinderpredigt')
    return rows + rows_from(entries(ls[k:], labels,
                                    [(r'Dominica \[post\] Trinitatis\.', 'Trinity'),
                                     (r'In Adventu dominica', 'Advent')]),
                            NOERDLINGEN_1555, skip)

# ---- Anhalt, Ordnung der deutschen Gesänge, before 8 February 1551 ------------------------------
ANHALT = 'Sehling 2, Nr. 116 (Anhalt, Ordnung der deutschen Gesänge, 1551), pp. 555-556'

def rows_anhalt():
    ls = extract.lines(1262, 'In der advent.', 'Diese nachfolgende geistliche',
                       furniture=[r'Das Fürstenthum Anhalt\.$'])
    text = ' '.join(ls)
    rows = feasts(text, ANHALT, [
        (r'In der advent\..*?In der mess vor dem evangelio: (?P<h>.+?)\. Vor der vesper', ['Advent']),
        (r'Am christag\..*?in der messen vor dem evangelio singe man: (?P<h>.+?) gar aus\.', ['Christmas']),
        (r'In der fasten\..*?vor dem evangelio: (?P<h>.+?)\. Vor der vesperpredig', ['Lent']),
        (r'Am ostertag und etzliche .*?die sequentia, (?P<h>.+?), darnach', ['Easter']),
        (r'Am ostertag und etzliche .*?darnach vor dem evangelio: (?P<h>.+?), vor der vesperpredig',
         ['Easter']),
        (r'Am himelfartstag\..*?Vor dem evangelio in der messen: (?P<h>.+?), vor der vesperpredig',
         ['Ascension']),
        (r'Am pfingstag\..*?in der mess vor dem evangelio die sequentia und\s*:\s*(?P<h>.+?), vor der vesper',
         ['Pentecost']),
        (r'Am tage der heiligen dreiheit\..*?In der mess vor dem evangelio die sequentia und\s*:\s*'
         r'(?P<h>.+?)\. Vor der vesper', ['Trinity Sunday']),
    ])
    # after Trinity: a rotation, each hymn kept for about four Sundays, not tied to a Sunday
    m = re.search(r'Nach Trinitatis\..*?behalde:\s*(?P<h>.+?)\s+und dergleichen\.', text)
    for t in re.split(r',\s*(?=[A-ZÄÖÜ])', m.group('h')):
        t = extract.clean_title(re.sub(r',\s*etvan halb.*$', '', t))
        rows.append(('Trinity season', t, ANHALT))
    return rows

# ---- Pirna, Kirchenordnung of Anton Lauterbach: undated; probably after the recess of 1555, which it uses,
# and before Lauterbach's death in 1569 (Sehling 1, p. 635) ----------------------------------------
PIRNA = 'Sehling 1, Nr. 128 (Pirna, Kirchenordnung of Anton Lauterbach, 1555-1569), pp. 642-643'

def rows_pirna():
    """Most Sundays have two German hymns: the first in the place of the introit, the second
    after the epistle. The feasts show the order of the two places: the Latin introit comes
    first ("Ascensionis. Viri Galilaei. Kyrie. Graduale. Sequens."), and the German hymn after
    the gradual ("Christ fuhr gen himmel."). Thompson reads the table the same way
    (rows_thompson.json). Only the last hymn of each day is taken."""
    ls = extract.lines(119, 'Cantica per anni curriculum', 'Haec cantica germanica',
                       furniture=[r'der ernestinischen und albertinischen Länder\.$', r'\d+\. Pirna\. Kirchenordnung',
                                  r'\d+ Die Kirchenordnungen\.'])
    labels = [(r'Cantica per anni', None), (r'Natalis domini\.', 'Christmas'),
              (LENT_RE + r'\.', lambda m: LENT[m.group(1).lower()]),
              (r'Annunciationis\.', 'Annunciation (25 March)'), (r'Paschae\.', 'Easter'),
              (r'Ascensionis\.', 'Ascension'), (r'Pentecostes\.', 'Pentecost'),
              (r'Trinitatis\.', 'Trinity Sunday'),
              (r'Dom(?:in)?\.\s*([IVX]+)[.,]', lambda m: f'Trinity {ROMAN[m.group(1)]}'),
              (r'Advent(?:us)?\.?\s*([IVX]+)\.', lambda m: f'Advent {ROMAN[m.group(1)]}')]
    # the Latin propers of the feasts; of these only the sequences are hymns
    skip = re.compile(r'^(Puer natus|Kyrie|Gloria|Graduale|Sequens|Introitus|Latine|Nos autem|Passio|'
                      r'Bona|Sabbato|Resurrexi|Antiphonis|Viri Galilaei|Cantica|Hymni|Responsoria|'
                      r'Benedictus|ad festum)\b', re.I)
    rows = []
    for occ, body in entries(ls, labels, joiner='\n'):     # one hymn to a line
        body = re.sub(r'Grates nunc cum canticis.*$', 'Grates nunc.', body, flags=re.M)
        rows += [(occ, t, PIRNA) for t in titles(body, skip)[-1:]]
    return rows

# ---- Nördlingen, Kirchenordnung, 1579 ------------------------------------------------------------
NOERDLINGEN_1579 = 'Sehling 12, VIII.7 (Nördlingen, Kirchenordnung, 1579), pp. 335-393'

def rows_noerdlingen_1579():
    ls = extract.lines(375, 'Nach verlesung der epistel werden dise psalmen', 'Finis cantionum',
                       furniture=[r'Kirchenordnung von 1579$', r'vel Invocavit\.$'])
    labels = [(r'Nach verlesung der epistel', None), (r'In dem Advent:', 'Advent'),
              (r'Auf Weihenacht und hin bis uf Purificationis Mariae', 'Christmas to Purification'),
              (r'Wo aber den sechsten Januarii', 'Epiphany'),
              (r'Von Purificationis bis uf den sonntag Septuagesima:', 'Purification to Septuagesima'),
              (r'Dominica ' + LENT_RE + r':', lambda m: LENT[m.group(1).lower()]),
              (r'In die Annunciationis Mariae \[25\. März\]:', 'Annunciation (25 March)'),
              (r'Von Ostern bis uf das fest um Ascensionis Domini:', 'Easter to Ascension'),
              (r'Dominica Vocem Jucunditatis:', 'Easter 5 (Rogate/Vocem jucunditatis)'),
              (r'In die Ascensionis Domini:', 'Ascension'),
              (r'Dominica Exaudi:', 'Sunday after Ascension (Exaudi)'),
              (r'Auf Pfingsten und den montag:', 'Pentecost & Pentecost Monday'),
              (r'Dominica Trinitatis:', 'Trinity Sunday'),
              (r'Dominica 1\. et 2\.:', 'Trinity 1 & 2'),
              (r'Dominica 26\. 27:', 'Trinity 26 & 27'),
              (r'Dominica (\d{1,2}):', lambda m: f'Trinity {m.group(1)}')]
    ents = []
    for occ, body in entries(ls, labels):
        m = re.search(r'solle der psalm (.+?) etc\. gesungen werden', body)
        ents.append((occ, m.group(1) if m else body))   # where the baptism of Christ is preached
    return rows_from(ents, NOERDLINGEN_1579)

def parse_all():
    return (rows_naumburg() + rows_noerdlingen_1555() + rows_anhalt() + rows_pirna()
            + rows_noerdlingen_1579())

if __name__ == '__main__':
    for name, fn in [('NAUMBURG', rows_naumburg), ('NOERDLINGEN 1555', rows_noerdlingen_1555),
                     ('ANHALT', rows_anhalt), ('PIRNA', rows_pirna), ('NOERDLINGEN 1579', rows_noerdlingen_1579)]:
        r = fn(); print(f'\n### {name}: {len(r)} rows')
        for o, t, s in r: print(f'   {o:<40} | {t}')
