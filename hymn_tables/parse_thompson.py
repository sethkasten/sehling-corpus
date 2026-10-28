# -*- coding: utf-8 -*-
"""Jason Thompson's transcriptions of eight Sunday-and-feast hymn lists (his dissertation,
Appendix 2), in the text files of this folder: one file to a list, the list's name and year on
its first line and then one line to a hymn, "Occasion, Hymn". A hymn whose place in the service
is not given in parentheses is the chief hymn; "(introit)", "(before sermon)", "(after
sermon)", "(postlude)" and "(distribution)" name the other places.

Five of the lists are not in Sehling's edition: Andorff (Antwerp) 1567, Annaberg 1579, Eler
1588 and Magdeburg 1613 and 1632. Their chief hymns are loaded by merge_thompson.py; Magdeburg
1613 has none, only hymns for after the sermon. The other three, Naumburg 1538, Anhalt 1551
and Pirna (before 1569), are Sehling orders that parse_sunday.py reads from the corpus itself.
They are parsed here only to check that reading (--compare), and are not loaded twice.

The files are kept as Thompson gives them. Their slips are mended here: misspelt occasions
("Triniyt 2") and titles ("halleuljah"), and a few readings set out in FIX. A reference to the
hymns of another day ("as on Trinity 4") is not followed, as parse_sunday.py does not follow
one; nor are "Latin introit", "Latin sequence", the litany, the Nicene Creed and the like,
which are not hymns.

    py hymn_tables/parse_thompson.py            write rows_thompson.json and list the rows
    py hymn_tables/parse_thompson.py --compare  set the three Sehling orders beside our reading
"""
import json, os, re, sys, collections
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)

FILES = ['naumburg 1538.txt', 'anhalt 1551.txt', 'pirna pre-1569.txt', 'andorff 1567.txt',
         'annaberg 1579.txt', 'eler 1588.txt', 'magdeburg 1613.txt', 'magdeburg 1632.txt']
# the list's first line -> the witness in hymns.db, and the Sehling order already read from
# the corpus where the list is one
WITNESS = {
 'Naumburg 1538': ('Naumburg (1538)', 'Sehling 2, Nr. 13 (Naumburg'),
 'Anhalt 1551': ('Anhalt (1551)', 'Sehling 2, Nr. 116 (Anhalt'),
 'Pirna pre-1569': ('Pirna (before 1569)', 'Sehling 1, Nr. 128 (Pirna'),
 'Andorff 1567': ('Antwerp (Andorff, 1567)', None),
 'Annaberg 1579': ('Annaberg (1579)', None),
 'Eler 1588': ('Eler, Cantica sacra (1588)', None),
 'Magdeburg 1613': ('Magdeburg (1613)', None),
 'Magdeburg 1632': ('Magdeburg (1632)', None),
}
VIA = 'Thompson, diss. App. 2'

# Thompson's occasions -> those of hymns.db
OCC = {
 'Advent': 'Advent', 'Christmastide': 'Christmas season', 'Christmas day': 'Christmas',
 'Stephen': 'St Stephen (26 Dec)', 'John Evangelist': 'St John the Evangelist (27 Dec)',
 'Christmas 1': 'Sunday after Christmas', 'Circumcision': 'New Year (Circumcision)',
 'Epiphany 0': 'Epiphany', 'Septuagesima': 'Septuagesima', 'Sexagesima': 'Sexagesima',
 'Quinquagesima': 'Quinquagesima (Estomihi)', 'Lent': 'Lent', 'Lent 1': 'Lent 1 (Invocavit)',
 'Lent 2': 'Lent 2 (Reminiscere)', 'Lent 3': 'Lent 3 (Oculi)', 'Lent 4': 'Lent 4 (Laetare)',
 'Lent 5': 'Lent 5 (Judica)', 'Palmarum': 'Palm Sunday', 'Maundy Thursday': 'Maundy Thursday',
 'Good Friday': 'Good Friday', 'Holy Saturday': 'Holy Saturday', 'Easter': 'Easter',
 'Easter 0': 'Easter', 'Eastertide': 'Easter season', 'Easter 1': 'Easter 1 (Quasimodogeniti)',
 'Easter 2': 'Easter 2 (Misericordias Domini)', 'Easter 3': 'Easter 3 (Jubilate)',
 'Easter 4': 'Easter 4 (Cantate)', 'Easter 5': 'Easter 5 (Rogate)', 'Ascension': 'Ascension',
 'Exaudi': 'Sunday after Ascension (Exaudi)', 'Pentecost': 'Pentecost',
 'Pentecost Mon/Tues': 'Pentecost Monday & Tuesday', 'Trinity': 'Trinity Sunday',
 'Trinity 0': 'Trinity Sunday', 'Trinitytide': 'Trinity season',
 'Common of Mary': 'Feasts of the Virgin Mary', 'Purification': 'Purification of Mary (2 Feb)',
 'Annunciation': 'Annunciation (25 March)', 'Visitation': 'Visitation of Mary (2 July)',
 'Apostles': 'Common of Apostles', 'Conversion of Paul': 'Conversion of St Paul (25 Jan)',
 'Philip and James': 'Sts Philip and James (1 May)',
 'Nativity of John': 'St John the Baptist (24 June)', 'Mary Magdalene': 'St Mary Magdalene (22 July)',
 'Anne': 'St Anne (26 July)', 'Michael': 'St Michael (29 Sept)',
}
SPELL = {'Tirinyt': 'Trinity', 'Triniyt': 'Trinity', 'Triinyt': 'Trinity', 'Triinty': 'Trinity',
         'Tirinty': 'Trinity', 'Tirintyitde': 'Trinitytide', 'Triintytide': 'Trinitytide',
         'Epihpany': 'Epiphany', 'Seputagesima': 'Septuagesima', 'Quinquagesiam': 'Quinquagesima',
         'Quinquagelima': 'Quinquagesima', 'Micahel': 'Michael', 'Christmas Day': 'Christmas day'}

# the places in the service; anything else in parentheses is a note
SLOT = [(r'intr?oi?r?i?t', 'Introit'), (r'before sermon', 'Before the sermon'),
        (r'after sermon', 'After the sermon'), (r'p\w*tl\w*de|postlude', 'Postlude'),
        (r'distribution', 'Distribution')]
# not hymns
NOT_HYMN = re.compile(r'^(Lat(in)? (introit|intoirt|tract|sequence|chants)|Latin Intoirt|Litany|'
                      r'Nicene creed|Eben dieselben)$', re.I)
# readings that need mending: Thompson's text -> the incipit (with the reason in a comment)
FIX = {
 'Komm Gott schpopfer': 'Komm Gott Schöpfer',
 'Fröhlich wollen wir halleuljah singen': 'Fröhlich wollen wir Halleluja singen',
 'Mensch willstud leben seliglich': 'Mensch willstu leben seliglich',
 'Es wird sicher der letzte Tag herkommen': 'Es wird schier der letzte Tag herkommen',
 'Dies sind die heiligne': 'Dies sind die heiligen', 'Dies sind de hieligen': 'Dies sind die heiligen',
 'Herr Christ der eigin': 'Herr Christ der einig', 'Herr Christ der eignig': 'Herr Christ der einig',
 'Ein Kinedelin so lobelich': 'Ein Kindelein so löbelich',
 'Nun hπoret zu ihr Christenleut': 'Nun höret zu ihr Christenleut',
 'Wo Gott der Herr nicht beit': 'Wo Gott der Herr nicht bei',
 'Mitten wir im Leben isnd': 'Mitten wir im Leben sind', 'Aus tiefre not': 'Aus tiefer Not',
 'Jessu CHristus unser heiland der von uns': 'Jesus Christus unser Heiland der von uns',
 'Jesus CHristus unser Heiland der den Tod': 'Jesus Christus unser Heiland der den Tod',
 'Hilf mir gotts gute preisen': 'Helft mir Gotts Güte preisen',
 'Wenn mein Stundlein vordanden ist': 'Wenn mein Stündlein vorhanden ist',
 'O Herr eGott dein göttlich Wort': 'O Herre Gott dein göttlich Wort',
 'Ein vaste borch': 'Ein feste Burg',                       # Low German
 'Was fürchst du Feind Herodes': 'Was fürchtst du Feind Herodes',
 'Hilf Gott das mirs gelinge': 'Hilf Gott dass mir gelinge',
 'Wenn wir im höchsten Noten': 'Wenn wir in höchsten Nöten',
 'Komm Heiliger Geist erfull': 'Komm Heiliger Geist erfüll',
 # Thompson's own query: Magdeburg 1632 has "Allein zu dir" on seven other Sundays
 'Allein nach dir Herr Jesu Christ': 'Allein zu dir Herr Jesu Christ',
 # the second line of Alber's Ascension hymn, set down as a hymn of its own
 'Der Herr fährt auf mit grossem Schall': 'Nun freut euch Gottes Kinder all',
 # openings cut short: the Christmas hymn, and Luther's baptism hymn on St John the Baptist's day
 'Der Tag der ist so': 'Der Tag der ist so freudenreich',
 'Christ unser Herr': 'Christ unser Herr zum Jordan kam',
 'Dies est laetitae': 'Dies est laetitiae',
}

def parse(path):
    lines = open(path, encoding='utf-8').read().split('\n')
    name = lines[0].strip()
    wit, sehling = WITNESS[name]
    rows = []
    for n, raw in enumerate(lines[1:], 2):
        s = raw.strip()
        if not s: continue
        occ_raw, _, text = s.partition(',')
        occ_raw, text = occ_raw.strip(), text.strip()
        word = occ_raw.split()[0]
        occ_key = SPELL.get(occ_raw) or ' '.join([SPELL.get(word, word)] + occ_raw.split()[1:])
        occ = OCC.get(occ_key) or (occ_key if re.fullmatch(r'(Advent|Epiphany|Trinity) \d{1,2}', occ_key)
                                   else None)
        assert occ, (path, n, occ_raw)
        slot, note = 'Chief hymn', None
        for m in re.finditer(r'\s*[\[(]([^)\]]*)[)\]]', text):
            inner = m.group(1).strip()
            sl = next((name_ for pat, name_ in SLOT if re.fullmatch(pat, inner, re.I)), None)
            if sl: slot = sl
            else: note = inner
        title = re.sub(r'\s*[\[(][^)\]]*[)\]]', '', text).strip().strip('"')
        if re.match(r'as on ', title):
            rows.append(dict(witness=wit, occasion=occ, title=None, slot=slot, note=title, line=n)); continue
        if NOT_HYMN.match(title):
            rows.append(dict(witness=wit, occasion=occ, title=None, slot=slot, note=title, line=n)); continue
        m = re.match(r'Latin introit or (.+)$', title)          # Naumburg's Christmas introit
        if m: title = m.group(1)
        fixed = FIX.get(title)
        rows.append(dict(witness=wit, occasion=occ, title=fixed or title, slot=slot,
                         note=note if not fixed else (note or f'Thompson: {title}'), line=n,
                         thompson=title, sehling=sehling))
    return name, rows

def parse_all():
    out = []
    for f in FILES:
        out += parse(os.path.join(HERE, f))[1]
    return out

def identity(title, occasion):
    from resolve import resolve, by_occasion
    c, _lit, _com, _alt, ok = resolve(title)
    return by_occasion(c, occasion, title)[0] if ok else title

# a season of Thompson's is the feast that parse_sunday.py reads at its head
SEASON_DAY = {'Christmas season': 'Christmas', 'Easter season': 'Easter'}

def compare(rows):
    """Thompson's chief hymns for the three Sehling orders, day by day, beside the hymns that
    parse_sunday.py reads from the corpus (rows_sunday.json)."""
    ours = collections.defaultdict(set)
    for occ, title, src in json.load(open(os.path.join(HERE, 'rows_sunday.json'), encoding='utf-8')):
        ours[(src, occ)].add(identity(title, occ))
    for name, (wit, sehling) in WITNESS.items():
        if not sehling: continue
        src = next(s for s, _o in ours if s.startswith(sehling))
        his = collections.defaultdict(set)
        for r in rows:
            if r['witness'] == wit and r['title'] and r['slot'] == 'Chief hymn':
                occ = SEASON_DAY.get(r['occasion'], r['occasion'])
                his[occ].add(identity(r['title'], occ))
        days = sorted(set(his) | {o for s, o in ours if s == src})
        same = [d for d in days if his.get(d) == ours.get((src, d))]
        print(f'\n{name}: {len(same)} of {len(days)} days agree')
        for d in days:
            a, b = his.get(d, set()), ours.get((src, d), set())
            if a != b:
                print(f'  {d:<32} Thompson: {"; ".join(sorted(a)) or "-"}\n'
                      f'  {"":<32} corpus:   {"; ".join(sorted(b)) or "-"}')

if __name__ == '__main__':
    rows = parse_all()
    if '--compare' in sys.argv:
        compare(rows); sys.exit()
    json.dump(rows, open(os.path.join(HERE, 'rows_thompson.json'), 'w', encoding='utf-8'),
              ensure_ascii=False, indent=1)
    by = collections.Counter((r['witness'], r['slot'] if r['title'] else '(not a hymn)') for r in rows)
    for k, v in sorted(by.items()): print(f'{v:>4}  {k[0]:<28} {k[1]}')
