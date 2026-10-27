# -*- coding: utf-8 -*-
"""The English titles of the hymns, from the Lutheran Hymn Index (Hymnal Index/hymnal.db).

A hymn that is in the index takes the index's master title (its HYMN TITLE: the title of
Lutheran Service Book, else of The Lutheran Hymnal, else of the Evangelical Lutheran Hymnary,
else of the hymnal that brought the hymn into the index). The index gives some of those titles
without their commas ("O Lord Look Down from Heaven Behold"); these take the punctuation of the
first hymnal title of the same words (TLH's "O Lord, Look Down from Heaven, Behold"). Titles in
sentence case are put in title case. lexicon.py puts these titles in common_english.

INDEX matches each hymn of the lexicon to its row in the index. The matches were made by the
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

# canonical title of the lexicon -> id of the row in hymnal.db (hymns.id)
INDEX = {
 'A solis ortus cardine': 1036, 'Ach bleib bei uns, Herr Jesu Christ': 2257,
 'Ach Gott und Herr': 82, 'Ach Gott, vom Himmel sieh darein': 2997,
 'Ach, lieben Christen, seid getrost': 793, 'Ad coenam agni providi': 304,
 'All Ehr und Lob soll Gottes sein': 95, 'Allein Gott in der Höh sei Ehr': 96,
 'Allein zu dir, Herr Jesu Christ': 1799, 'Also heilig ist der Tag': 4181,
 'Auf diesen Tag so denken wir': 4393, 'Auf meinen lieben Gott': 1753,
 'Aus tiefer Not schrei ich zu dir': 1034, 'Christ fuhr gen Himmel': 592,
 'Christ ist erstanden': 572, 'Christ lag in Todesbanden': 590,
 'Christ, unser Herr, zum Jordan kam': 4353, 'Christe qui lux es et dies': 2789,
 'Christe, der du bist Tag und Licht': 602, 'Christe, du bist der helle Tag': 2219,
 'Christum wir sollen loben schon': 1036, 'Conditor alme siderum': 765,
 'Corde natus ex parentis': 3197, 'Da Jesus an dem Kreuze stund': 3316,
 'Das alte Jahr vergangen ist': 3989, 'Das neugeborne Kindelein': 3983,
 'Der du bist drei in Einigkeit': 2753, 'Der Tag, der ist so freudenreich': 2673,
 'Der Törichte spricht': 3979, 'Des Königs Panier gehet hervor': 4013,
 'Dies absoluti praetereunt': 3833, 'Dies sind die heilgen zehn Gebot': 4146,
 'Durch Adams Fall ist ganz verderbt': 106, 'Ein feste Burg ist unser Gott': 35,
 'Ein Kind geborn zu Bethlehem': 18, 'Ein Kindelein so löbelich': 4387,
 'Ein Lämmlein geht und trägt die Schuld': 29, 'Erhalt uns, Herr, bei deinem Wort': 2373,
 'Erschienen ist der herrlich Tag': 3848, 'Es ist das Heil uns kommen her': 3542,
 'Es ist gewisslich an der Zeit': 3855, 'Es spricht der Unweisen Mund wohl': 3979,
 'Es wolle Gott uns gnädig sein': 2466, 'Festum nunc celebre': 2724,
 'Fröhlich soll mein Herze springen': 108, 'Fröhlich wolln wir Halleluja singen': 3634,
 'Gelobet seist du, Jesu Christ': 4516, 'Gloria laus et honor': 99,
 'Gott der Vater wohn uns bei': 4408, 'Gott hat das Evangelium': 1134,
 'Gott sei gelobet und gebenedeiet': 3046, 'Gott, heiliger Schöpfer aller Stern': 765,
 'Gottes Sohn ist kommen': 3283, 'Helft mir Gotts Güte preisen': 4339,
 'Herr Christ, der einig Gotts Sohn': 3990, 'Herr Gott, dich loben alle wir': 2228,
 'Herr Jesu Christ, du höchstes Gut': 2254, 'Herr Jesu Christ, wahr Mensch und Gott': 2234,
 'Herzlich lieb hab ich dich, o Herr': 2394, 'Heut triumphieret Gottes Sohn': 4392,
 'Hostis Herodes impie': 4045, 'Ich danke dir, lieber Herre': 1676,
 'Ich hab mein Sach Gott heimgestellt': 2507, 'Ich ruf zu dir, Herr Jesu Christ': 2230,
 'Iesu nostra redemptio': 2777, 'Ihr lieben Christen, freut euch nun': 3487,
 'In dich hab ich gehoffet, Herr': 1680, 'In dulci jubilo': 2715,
 'Jesaja, dem Propheten, das geschah': 1834, 'Jesu, meine Freude': 1988,
 'Jesus Christus, unser Heiland': 1875,
 'Jesus Christus, unser Heiland, der den Tod überwand': 1878,
 'Komm, Gott Schöpfer, Heiliger Geist': 697, 'Komm, Heiliger Geist, Herre Gott': 700,
 'Kommt her zu mir, spricht Gottes Sohn': 650, 'Lasset uns mit Jesu ziehen': 2132,
 'Lob sei dem allmächtigen Gott': 4346, 'Lobt Gott, ihr Christen, allzugleich': 2088,
 'Mein Seel erhebt den Herren': 2600, 'Mensch, willst du leben seliglich': 4794,
 'Menschenkind, merk eben': 2461, 'Mir nach, spricht Christus, unser Held': 5,
 'Mit Fried und Freud ich fahr dahin': 1774, 'Mitten wir im Leben sind': 1798,
 'Nimm von uns, Herr, du treuer Gott': 3496, 'Nun bitten wir den Heiligen Geist': 4343,
 'Nun freut euch, Gottes Kinder, all': 2771, 'Nun freut euch, lieben Christen gmein': 792,
 'Nun komm, der Heiden Heiland': 3549, 'Nun lasst uns den Leib begraben': 4167,
 'Nun lob, mein Seel, den Herren': 2605, 'O filii et filiae': 3114,
 'O Gott, du frommer Gott': 2890, 'O Herre Gott, dein göttlich Wort': 2871,
 'O Lamm Gottes, unschuldig': 2070, 'O lux beata Trinitas': 2753,
 'O Mensch, bewein dein Sünde groß': 3064, 'O Traurigkeit, o Herzeleid': 2813,
 'Puer natus in Bethlehem': 18, 'Rex Christe factor omnium': 2772,
 'Sei Lob und Ehr dem höchsten Gut': 3636, 'Sie ist mir lieb, die werte Magd': 796,
 'So wahr ich leb, spricht Gott der Herr': 3, 'Such, wer da will, ein ander Ziel': 3590,
 'Tröstet, tröstet meine Lieben': 751, 'Valet will ich dir geben': 917,
 'Vater unser im Himmelreich': 3333, 'Veni creator Spiritus': 699,
 'Verleih uns Frieden gnädiglich': 1251, 'Iam maesta quiesce querela': 819,
 'Veni redemptor gentium': 3549, 'Veni sancte Spiritus': 652,
 'Veni Sancte Spiritus, deutsch': 652, 'Vexilla regis prodeunt': 4013,
 'Victimae paschali laudes': 627, 'Vita sanctorum decus angelorum': 2142,
 'Vom Himmel hoch da komm ich her': 1044, 'Vom Himmel kam der Engel Schar': 4361,
 'Von Adam her so lange Zeit': 3624, 'Von Gott will ich nicht lassen': 1041,
 'Wachet auf, ruft uns die Stimme': 4453, 'Was frag ich nach der Welt': 4588,
 'Was fürchtst du, Feind Herodes, sehr': 4786, 'Was mein Gott will, das gscheh allzeit': 4085,
 'Wenn mein Stündlein vorhanden ist': 4662, 'Wenn wir in höchsten Nöten sein': 4644,
 'Wie schön leuchtet der Morgenstern': 3063, 'Wie soll ich dich empfangen': 2995,
 'Wir Christenleut habn jetzund Freud': 4479, 'Wir danken dir, Herr Jesu Christ': 4532,
 'Wir glauben all an einen Gott': 4464, 'Wo Gott der Herr nicht bei uns hält': 1707,
 'Wohl dem, der in Gottes Furcht steht': 1331, 'Wär Gott nicht mit uns diese Zeit': 1705,
}

# titles the rules below would not give: Luther's Creed hymn without the word ("..., Maker")
# that tells it in the index from Clausnitzer's; a title the index gives unpunctuated in every
# form
SPECIAL = {4464: 'We All Believe in One True God', 2772: 'O Christ, Our King, Creator, Lord'}

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

def _titles(hid):
    out = {}
    for src, t in _c().execute('SELECT source, title FROM hymn_titles WHERE hymn_id = ?', (hid,)):
        out.setdefault(src, t)
    return out

def title(hid):
    """the English title of index row hid, as the book and hymns.db give it"""
    if hid in SPECIAL: return SPECIAL[hid]
    master, = _c().execute('SELECT title FROM hymns WHERE id = ?', (hid,)).fetchone()
    titles = _titles(hid)
    order = [s for s in PREF if s in titles]
    order += sorted(s for s in titles if s not in PREF + ['alternate', 'master'])
    order += [s for s in ('alternate',) if s in titles]
    same = [titles[s] for s in order if words(titles[s]) == words(master)]
    punct = lambda x: len(re.findall(r'[,;:!?"]', x))
    t = same[0] if same and not punct(master) else master
    return titlecase(t).replace('’', "'").replace('"', "'").rstrip('!')

def carver(hid):
    """'Walther's Hymnal 442' or the like where the title is Matthew Carver's, else None"""
    t = words(title(hid))
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
    """(title, index id, Carver source or None) for a hymn in the index, else None"""
    hid = INDEX.get(canonical)
    return (title(hid), hid, carver(hid)) if hid else None

if __name__ == '__main__':
    for c in sorted(INDEX, key=str.casefold):
        t, hid, cv = english(c)
        print(f'{hid:>5}  {c:<52} {t}{"  [" + cv + "]" if cv else ""}')
