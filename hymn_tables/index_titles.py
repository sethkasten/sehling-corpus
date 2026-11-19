# -*- coding: utf-8 -*-
"""The English titles of the hymns, from the Lutheran Hymn Index (Hymnal Index/hymnal.db).

A hymn that is in the index takes the index's master title (its HYMN TITLE: the title of
Lutheran Service Book, else of The Lutheran Hymnal, else of the Evangelical Lutheran Hymnary,
else of the hymnal that brought the hymn into the index). The index gives some of those titles
without their commas ("O Lord Look Down from Heaven Behold"); these take the punctuation of the
first hymnal title of the same words (TLH's "O Lord, Look Down from Heaven, Behold"). Titles in
sentence case are put in title case. lexicon.py puts these titles in common_english.

INDEX matches each hymn of the lexicon to its row in the index, named by a hymnal number on the
row ('LSB 656'), since a row's id is its row number in the spreadsheet and changes whenever a row
is added before it. The matches were made by the
German, Latin or other original that the index records for each row (KELG's and ELGBS's
German, the originals of TLH, TLHy, TL and Liber Hymnorum), and checked one by one. A hymn
of the lexicon that is not here is not in the index, or only as another text (Schütz's "Sei
Lob und Ehr dem höchsten Gut" is in it; the stanza "Sei Lob und Ehr mit hohem Preis" of "Es
ist das Heil" is not a hymn of its own), or is a canticle or a group of hymns.

    py hymn_tables/index_titles.py          list the hymns with their index rows and titles
"""
import os, re, sqlite3, unicodedata

HERE = os.path.dirname(os.path.abspath(__file__))
DB = os.path.join(HERE, '..', 'Hymnal Index', 'hymnal.db')

# canonical title of the lexicon -> its row of the index, named by a hymnal number on the row
# ('LSB 656'): the rows' ids in hymnal.db are their row numbers in the spreadsheet, which
# change whenever write_back.py adds a row, so the matches keep a number instead
INDEX = {
 'A solis ortus cardine': 'LSB 385', 'Ach bleib bei uns, Herr Jesu Christ': 'LSB 585',
 'Ach Gott und Herr': 'TLH 317', 'Ach Gott, vom Himmel sieh darein': 'TLH 260',
 'Ach, lieben Christen, seid getrost': 'KELG 353', 'Ad coenam agni providi': 'LSB 633',
 'All Ehr und Lob soll Gottes sein': 'LSB 948', 'Allein Gott in der Höh sei Ehr': 'LSB 947',
 'Allein zu dir, Herr Jesu Christ': 'LSB 972', 'Also heilig ist der Tag': 'KELG 96',
 'Auf diesen Tag so denken wir': 'KELG 118', 'Auf meinen lieben Gott': 'LSB 745',
 'Aus tiefer Not schrei ich zu dir': 'LSB 607', 'Christ fuhr gen Himmel': 'KELG 119',
 'Christ ist erstanden': 'LSB 459', 'Christ lag in Todesbanden': 'LSB 458',
 'Christ, unser Herr, zum Jordan kam': 'LSB 406', 'Christe qui lux es et dies': 'LSB 882',
 'Christe, der du bist Tag und Licht': 'KELG 313', 'Christe, du bist der helle Tag': 'KELG 312',
 'Christum wir sollen loben schon': 'LSB 385', 'Conditor alme siderum': 'LSB 351',
 'Corde natus ex parentis': 'LSB 384', 'Da Jesus an dem Kreuze stund': 'TLH 177',
 'Das alte Jahr vergangen ist': 'TLH 125', 'Das neugeborne Kindelein': 'KELG 49',
 'Der du bist drei in Einigkeit': 'LSB 890', 'Der Tag, der ist so freudenreich': 'TLH 78',
 'Der Törichte spricht': 'KELG 170', 'Des Königs Panier gehet hervor': 'LSB 455',
 'Dies absoluti praetereunt': 'LH 31', 'Dies sind die heilgen zehn Gebot': 'LSB 581',
 'Durch Adams Fall ist ganz verderbt': 'LSB 562', 'Ein feste Burg ist unser Gott': 'LSB 656',
 'Ein Kind geborn zu Bethlehem': 'ELH 112', 'Ein Kindelein so löbelich': 'TLHy 189',
 'Ein Lämmlein geht und trägt die Schuld': 'LSB 438',
 'Erhalt uns, Herr, bei deinem Wort': 'LSB 655', 'Erschienen ist der herrlich Tag': 'KELG 103',
 'Es ist das Heil uns kommen her': 'LSB 555', 'Es ist gewisslich an der Zeit': 'LSB 508',
 'Es spricht der Unweisen Mund wohl': 'KELG 170', 'Es wolle Gott uns gnädig sein': 'LSB 823',
 'Festum nunc celebre': 'LH 45', 'Fröhlich soll mein Herze springen': 'LSB 360',
 'Fröhlich wolln wir Halleluja singen': 'TLHy 19', 'Gelobet seist du, Jesu Christ': 'LSB 382',
 'Gloria laus et honor': 'LSB 442', 'Gott der Vater wohn uns bei': 'LSB 505',
 'Gott hat das Evangelium': 'KELG 442', 'Gott sei gelobet und gebenedeiet': 'LSB 617',
 'Gott, heiliger Schöpfer aller Stern': 'LSB 351', 'Gottes Sohn ist kommen': 'LSB 333',
 'Helft mir Gotts Güte preisen': 'TLH 112', 'Herr Christ, der einig Gotts Sohn': 'LSB 402',
 'Herr Gott, dich loben alle wir': 'LSB 522', 'Herr Jesu Christ, du höchstes Gut': 'KELG 216',
 'Herr Jesu Christ, wahr Mensch und Gott': 'KELG 407',
 'Herzlich lieb hab ich dich, o Herr': 'LSB 708', 'Heut triumphieret Gottes Sohn': 'KELG 107',
 'Hostis Herodes impie': 'LSB 399', 'Ich danke dir, lieber Herre': 'KELG 300',
 'Ich hab mein Sach Gott heimgestellt': 'TLHy 481', 'Ich ruf zu dir, Herr Jesu Christ': 'KELG 273',
 'Iesu nostra redemptio': 'LSB 553', 'Ihr lieben Christen, freut euch nun': 'LPC 102',
 'In dich hab ich gehoffet, Herr': 'LSB 734', 'In dulci jubilo': 'LSB 386',
 'Jesaja, dem Propheten, das geschah': 'LSB 960', 'Jesu, meine Freude': 'LSB 743',
 'Jesus Christus, unser Heiland': 'LSB 627',
 'Jesus Christus, unser Heiland, der den Tod überwand': 'KELG 110',
 'Komm, Gott Schöpfer, Heiliger Geist': 'KELG 132', 'Komm, Heiliger Geist, Herre Gott': 'LSB 497',
 'Komm, Heiliger Geist, erfüll die Herzen deiner Gläubigen': 'KELG 133',
 'Kommt her zu mir, spricht Gottes Sohn': 'KELG 276', 'Kyrie, Gott Vater in Ewigkeit': 'LSB 942',
 'Lasset uns mit Jesu ziehen': 'LSB 685', 'Lob sei dem allmächtigen Gott': 'KELG 29',
 'Lobt Gott, ihr Christen, allzugleich': 'LSB 389', 'Mein Seel erhebt den Herren': 'LSB 934',
 'Mensch, willst du leben seliglich': 'KELG 181', 'Menschenkind, merk eben': 'KELG 32',
 'Mir nach, spricht Christus, unser Held': 'LSB 688',
 'Mit Fried und Freud ich fahr dahin': 'LSB 938', 'Mitten wir im Leben sind': 'LSB 755',
 'Nimm von uns, Herr, du treuer Gott': 'KELG 225', 'Nun bitten wir den Heiligen Geist': 'LSB 768',
 'Nun freut euch, Gottes Kinder, all': 'KELG 122',
 'Nun freut euch, lieben Christen gmein': 'LSB 556', 'Nun komm, der Heiden Heiland': 'LSB 332',
 'Nun lasst uns den Leib begraben': 'LSB 759', 'Nun lob, mein Seel, den Herren': 'LSB 820',
 'O filii et filiae': 'LSB 470', 'O Gott, du frommer Gott': 'LSB 696',
 'O Herre Gott, dein göttlich Wort': 'TLH 266', 'O Lamm Gottes, unschuldig': 'LSB 434',
 'O lux beata Trinitas': 'LSB 890', 'O Mensch, bewein dein Sünde groß': 'TL 202',
 'O Traurigkeit, o Herzeleid': 'LSB 448', 'Puer natus in Bethlehem': 'ELH 112',
 'Rex Christe factor omnium': 'LH 40', 'Sei Lob und Ehr dem höchsten Gut': 'LSB 819',
 'Sie ist mir lieb, die werte Magd': 'TL 251', 'So wahr ich leb, spricht Gott der Herr': 'LSB 614',
 'Such, wer da will, ein ander Ziel': 'LSB 557', 'Tröstet, tröstet meine Lieben': 'LSB 347',
 'Valet will ich dir geben': 'TLH 407', 'Vater unser im Himmelreich': 'LSB 766',
 'Veni creator Spiritus': 'LSB 498', 'Verleih uns Frieden gnädiglich': 'LSB 777',
 'Iam maesta quiesce querela': 'TLHy 595', 'Veni redemptor gentium': 'LSB 332',
 'Veni sancte Spiritus': 'TLH 227', 'Veni Sancte Spiritus, deutsch': 'TLH 227',
 'Vexilla regis prodeunt': 'LSB 455', 'Victimae paschali laudes': 'LSB 460',
 'Vita sanctorum decus angelorum': 'LH 42', 'Vom Himmel hoch da komm ich her': 'LSB 358',
 'Vom Himmel kam der Engel Schar': 'TLH 103', 'Von Adam her so lange Zeit': 'KELG 43',
 'Von Gott will ich nicht lassen': 'LSB 713', 'Wachet auf, ruft uns die Stimme': 'LSB 516',
 'Was frag ich nach der Welt': 'LSB 730', 'Was fürchtst du, Feind Herodes, sehr': 'KELG 60',
 'Was mein Gott will, das gscheh allzeit': 'LSB 758',
 'Wenn mein Stündlein vorhanden ist': 'TLH 594', 'Wenn wir in höchsten Nöten sein': 'LSB 615',
 'Wie schön leuchtet der Morgenstern': 'LSB 395', 'Wie soll ich dich empfangen': 'LSB 334',
 'Wir Christenleut habn jetzund Freud': 'TLH 107', 'Wir danken dir, Herr Jesu Christ': 'TLH 223',
 'Wir glauben all an einen Gott': 'LSB 954', 'Wo Gott der Herr nicht bei uns hält': 'KELG 438',
 'Wohl dem, der in Gottes Furcht steht': 'KELG 328', 'Wär Gott nicht mit uns diese Zeit': 'TLH 267',
}

# titles the rules below would not give: Luther's Creed hymn without the word ("..., Maker")
# that tells it in the index from Clausnitzer's; a title the index gives unpunctuated in every
# form
SPECIAL = {'LSB 954': 'We All Believe in One True God', 'LH 40': 'O Christ, Our King, Creator, Lord'}

# the hymnals whose title gives the punctuation, in this order
PREF = ['LSB', 'TLH', 'ELH', 'LW', 'TL', 'TLHy', 'WH', 'ELHB', 'LH', 'ELHal', 'LPC']
# Matthew Carver's books: Walther's Hymnal (2012), numbered as KELG, and Liber Hymnorum (2016)
CARVER_BOOKS = {'WH': ("Walther's Hymnal", 'KELG'), 'LH': ('Liber Hymnorum', 'LH')}
SMALL = {'a', 'an', 'the', 'and', 'but', 'or', 'nor', 'of', 'to', 'in', 'on', 'at', 'by', 'for',
         'from', 'with', 'upon', 'unto', 'into', 'as'}

def words(s):
    s = unicodedata.normalize('NFKC', s).replace('’', "'")
    return re.sub(r"[^\w' -]", ' ', s.lower()).replace('-', ' ').split()

def titlecase(s):
    """capitalise every word but articles, short prepositions and conjunctions, and keep "O" up"""
    toks = re.split(r'(\s+)', s)
    idx = [i for i, t in enumerate(toks) if t.strip()]
    def cap(w, force):
        m = re.match(r'^([^\w]*)(\w)(.*)$', w)
        if not m: return w
        pre, first, rest = m.groups()
        core = (first + rest).rstrip(',.;:!?"\')')
        if not force and core.lower() in SMALL: return pre + first.lower() + rest
        return pre + first.upper() + rest
    for n, i in enumerate(idx):
        force = n in (0, len(idx) - 1)
        toks[i] = '-'.join(cap(p, force or k > 0) for k, p in enumerate(toks[i].split('-')))
    return re.sub(r'\bo\b', 'O', ''.join(toks))

_db = None
def _c():
    global _db
    if _db is None:
        if not os.path.exists(DB):
            raise SystemExit(f'index_titles: {DB} not found (the Lutheran Hymn Index)')
        _db = sqlite3.connect(DB)
    return _db

def row(ref):
    """the id in hymnal.db of the row that bears the hymnal number ref ('LSB 656', 'TL 157a')"""
    code, number, suffix = re.fullmatch(r'(\S+) (\d+)([a-zA-Z]?)', ref).groups()
    rows = {h for (h,) in _c().execute(
        "SELECT hymn_id FROM hymn_numbers WHERE hymnal_code = ? AND number = ? "
        "AND COALESCE(suffix, '') = ? AND is_page = 0", (code, int(number), suffix))}
    if len(rows) != 1:
        raise SystemExit(f'index_titles: {ref} is on {len(rows)} rows of the index, not one')
    return rows.pop()

def _titles(hid):
    out = {}
    for src, t in _c().execute('SELECT source, title FROM hymn_titles WHERE hymn_id = ?', (hid,)):
        out.setdefault(src, t)
    return out

def title(ref):
    """the English title of the index row that bears ref, as the book and hymns.db give it"""
    if ref in SPECIAL: return SPECIAL[ref]
    hid = row(ref)
    master, = _c().execute('SELECT title FROM hymns WHERE id = ?', (hid,)).fetchone()
    titles = _titles(hid)
    order = [s for s in PREF if s in titles]
    order += sorted(s for s in titles if s not in PREF + ['alternate', 'master'])
    order += [s for s in ('alternate',) if s in titles]
    same = [titles[s] for s in order if words(titles[s]) == words(master)]
    punct = lambda x: len(re.findall(r'[,;:!?"]', x))
    t = same[0] if same and not punct(master) else master
    return titlecase(t).replace('’', "'").replace('"', "'").rstrip('!')

def carver(ref):
    """'Walther's Hymnal 442' or the like where the title is Matthew Carver's, else None"""
    t = words(title(ref))
    hid = row(ref)
    titles = _titles(hid)
    srcs = {s for s, x in titles.items() if words(x) == t} - {'master', 'alternate'}
    books = srcs & set(CARVER_BOOKS)
    if not books or srcs - set(CARVER_BOOKS) - {'TL'}:
        return None
    name, code = CARVER_BOOKS[sorted(books)[-1]]
    nums = [n for (n,) in _c().execute('SELECT number FROM hymn_numbers WHERE hymn_id = ? AND '
                                       'hymnal_code = ? ORDER BY position', (hid, code))]
    return f"{name} {nums[0]}" if nums else name

def english(canonical):
    """(title, the hymnal number naming its index row, Carver source or None) for a hymn in the
    index, else None"""
    ref = INDEX.get(canonical)
    return (title(ref), ref, carver(ref)) if ref else None

if __name__ == '__main__':
    for c in sorted(INDEX, key=str.casefold):
        t, ref, cv = english(c)
        print(f'{ref:<10}  {c:<52} {t}{"  [" + cv + "]" if cv else ""}')
