# -*- coding: utf-8 -*-
"""Resolve hymn identity across sources that cite in different languages.

Liliencron prints German incipit and English title side by side for 377
entries, which gives a ready-made bridge for the sources that supply only
an English title (HotD, Selnecker).
"""
import json, os, re, sys, unicodedata, difflib
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
from resolve import resolve, norm

def keyify(s):
    t = unicodedata.normalize('NFKD', (s or '').lower())
    t = t.replace('’', "'").replace('‘', "'").replace('—', ' ')
    t = ''.join(c for c in t if not unicodedata.combining(c))
    t = re.sub(r'\b(the|a|an|o|oh|ye|thou|thy|thee|our|us|we|is|in|of|to|and|now)\b', ' ', t)
    t = re.sub(r'[^a-z ]', ' ', t)
    return re.sub(r'\s+', ' ', t).strip()

def build():
    """english-title key -> German incipit, learned from Liliencron."""
    bridge = {}
    for r in json.load(open(os.path.join(HERE, 'rows_liliencron.json'))):
        k = keyify(r['english'])
        if k and k not in bridge:
            bridge[k] = r['german']
    return bridge

_BRIDGE = build()
_KEYS = list(_BRIDGE)

# English titles that Liliencron's columns do not supply, or supply for a different hymn:
# chiefly the English-only citations of Carpzov, Bach, Selnecker's own account, the plan of
# c. 1700, Thompson and the modern lists.  English title -> German canonical title.
_EN_ALIAS_SRC = {
 'The Day Is Surely Drawing Near': 'Es ist gewisslich an der Zeit',
 'Christ, Who Saves Us by His Cross': 'Christus, der uns selig macht',
 'Why Art Thou Thus Cast Down, My Heart': 'Warum betrübst du dich, mein Herz',
 'Why art thou cast down, my heart?': 'Warum betrübst du dich, mein Herz',
 'How Lovely Shines the Morning Star': 'Wie schön leuchtet der Morgenstern',
 'O Morning Star, How Fair and Bright': 'Wie schön leuchtet der Morgenstern',
 'When in the Hour of Utmost Need': 'Wenn wir in höchsten Nöten sein',
 'Today in Triumph Christ Arose': 'Heut triumphieret Gottes Sohn',
 'All Glory Be to God on High': 'Allein Gott in der Höh sei Ehr',
 'God gave the Gospel that we may': 'Gott hat das Evangelium',
 'Our Father, who from heav’n above': 'Vater unser im Himmelreich',
 'Our Father, Who from Heaven Above': 'Vater unser im Himmelreich',
 'Lord Christ, the Sole-Begotten': 'Herr Christ, der einig Gotts Sohn',
 'Once He Came in Blessing': 'Gottes Sohn ist kommen',
 'The Old Year Now Hath Passed Away': 'Das alte Jahr vergangen ist',
 'In Thee, Lord, Have I Put My Trust': 'In dich hab ich gehoffet, Herr',
 'In Thee, O Lord, I Put My Trust': 'In dich hab ich gehoffet, Herr',
 'The Day Hath Dawned, the Day of Days': 'Erschienen ist der herrlich Tag',
 'From God Can Naught Move Me': 'Von Gott will ich nicht lassen',
 'From God can nothing move me': 'Von Gott will ich nicht lassen',
 'From God Shall Naught Divide Me': 'Von Gott will ich nicht lassen',
 'Now sing we, now rejoice': 'In dulci jubilo',
 'In God, My Faithful God': 'Auf meinen lieben Gott',
 'The Will of God Is Always Best': 'Was mein Gott will, das gscheh allzeit',
 'Triune God, be Thou our stay': 'Gott der Vater wohn uns bei',
 'O Lord, How Shall I Meet You': 'Wie soll ich dich empfangen',
 'O Lord, how shall I meet Thee': 'Wie soll ich dich empfangen',
 'O Lord, we welcome Thee': 'Wie soll ich dich empfangen',
 'We Christians May Rejoice Today': 'Wir Christenleut habn jetzund Freud',
 'Let All Together Praise Our God': 'Lobt Gott, ihr Christen, allzugleich',
 'Lord, Thee I Love with All My Heart': 'Herzlich lieb hab ich dich, o Herr',
 "I Leave All Things to God's Direction": 'Ich hab mein Sach Gott heimgestellt',
 'Christ Rose to Heaven': 'Christ fuhr gen Himmel',
 'Happy the man who feareth God': 'Wohl dem, der in Gottes Furcht steht',
 'Happy the Man That Feareth God': 'Wohl dem, der in Gottes Furcht steht',
 'To God the Holy Spirit let us pray': 'Nun bitten wir den Heiligen Geist',
 'If God will not the building bless': 'Wo Gott zum Haus nicht gibt sein Gunst',
 'In vain is all thy toil and pain': 'Vergebens ist all Müh und Kost',
 'My Soul Now Magnifies the Lord': 'Mein Seel erhebt den Herren',
 'In Babylon by water-streams': 'An Wasserflüssen Babylon',
 'By the Waters of Babylon': 'An Wasserflüssen Babylon',
 'Beside the Streams of Babylon': 'An Wasserflüssen Babylon',
 'In the Very Midst of Life': 'Mitten wir im Leben sind',
 'Alas, My God, My Sins Are Great': 'Ach Gott und Herr',
 'Alas, my God, How great my load!': 'Ach Gott und Herr',
 'To Jordan Came Our Lord the Christ': 'Christ, unser Herr, zum Jordan kam',
 'Wilt Thou, O Man, Live Happily': 'Mensch, willst du leben seliglich',
 'That Man a Godly Life Might Live': 'Dies sind die heilgen zehn Gebot',
 'Lord Jesus Christ, With Us Abide': 'Ach bleib bei uns, Herr Jesu Christ',
 'Lord Jesus Christ, Thou highest Good': 'Herr Jesu Christ, du höchstes Gut',
 'Lord Jesus Chirst, I call to Thee': 'Ich ruf zu dir, Herr Jesu Christ',
 'Lord, Hear the Voice of My Complaint': 'Ich ruf zu dir, Herr Jesu Christ',
 'Lord Jesus Christ, I cry to Thee': 'Herr Jesu Christ, ich schrei zu dir',
 'Lord, keep us in Thy word and work': 'Erhalt uns, Herr, bei deinem Wort',
 'Thanks Let Us Render (Danksagen wir alle)': 'Danksagen wir alle Gott',
 'From Heaven the Angel Troop Came Near': 'Vom Himmel kam der Engel Schar',
 'From Heav’n the Angel Troop Came': 'Vom Himmel kam der Engel Schar',
 'Why, Herod, unrelenting foe!': 'Was fürchtst du, Feind Herodes, sehr',
 'Why, Herod, Fearest Thou the Foe': 'Was fürchtst du, Feind Herodes, sehr',
 'Hail the Day So Rich in Cheer': 'Der Tag, der ist so freudenreich',
 'Lord, Now Lettest Thou Thy Servant Depart in Peace': 'Herr, nun lässest du deinen Diener',
 'Christ Is Arisen from the Grave’s Dark Prison': 'Christ ist erstanden',
 'Jesus Christ, Our Savior True, Who Death Overthrew':
     'Jesus Christus, unser Heiland, der den Tod überwand',
 'Jesus Christ, Our Blessed Savior': 'Jesus Christus, unser Heiland',
 'We Praise Thee, O God (Te Deum)': 'Herr Gott, dich loben wir',
 'Te Deum': 'Herr Gott, dich loben wir',
 'Lord God, we all to Thee give praise': 'Herr Gott, dich loben alle wir',
 'Lord God, we all to Thee give': 'Herr Gott, dich loben alle wir',
 'Lord God, to Thee We Give All Praise': 'Herr Gott, dich loben alle wir',
 'Since Adam’s age, so long have we': 'Von Adam her so lange Zeit',
 'Blessed Is the Man Who Walketh Not': 'Wohl dem Menschen, der wandelt nicht',
 'O Darkest Woe': 'O Traurigkeit, o Herzeleid',
 'My Soul, Now Bless Thy Maker': 'Nun lob, mein Seel, den Herren',
 'Seek Where Ye May to Find a Way': 'Such, wer da will, ein ander Ziel',
 'A Lamb Goes Uncomplaining Forth': 'Ein Lämmlein geht und trägt die Schuld',
 'Wake, Awake, for Night is Flying': 'Wachet auf, ruft uns die Stimme',
 'Jesus, Priceless Treasure': 'Jesu, meine Freude',
 'Come, Follow Me, the Savior Spake': 'Mir nach, spricht Christus, unser Held',
 'All Praise to God Who Reigns Above': 'Sei Lob und Ehr dem höchsten Gut',
 'Let Us Ever Walk with Jesus': 'Lasset uns mit Jesu ziehen',
 'What Is the World to Me': 'Was frag ich nach der Welt',
 'O God, Thou Faithful God': 'O Gott, du frommer Gott',
 'Farewell I Gladly Bid Thee': 'Valet will ich dir geben',
 'Comfort, Comfort, Ye My People': 'Tröstet, tröstet meine Lieben',
 'All My Heart This Night Rejoices': 'Fröhlich soll mein Herze springen',
 'We Praise Y ou, Jesus, at Y our Birth': 'Gelobet seist du, Jesu Christ',
 'The Royal Banners Forward Go': 'Vexilla regis prodeunt',
 'As Surely as I Live, God Said': 'So wahr ich leb, spricht Gott der Herr',
 'Blessed Are They Who Fear the Lord': 'Wohl dem, der in Gottes Furcht steht',
 'Magnificat (Luther)': 'Mein Seel erhebt den Herren',
 'Lord, Now Lettest Thou Thy Servant Depart': 'Herr, nun lässest du deinen Diener',
 'O Jesus Christ, all praise to Thee': 'Gelobet seist du, Jesu Christ',
 'Dear Christians, put away your fears': 'Ach, lieben Christen, seid getrost',
 'Benedictus': 'Gelobet sei der Herr, der Gott Israel',
}
EN_ALIAS = {keyify(k): v for k, v in _EN_ALIAS_SRC.items()}

def english_to_german(title):
    k = keyify(title)
    if k in EN_ALIAS: return EN_ALIAS[k], 1.0
    if k in _BRIDGE: return _BRIDGE[k], 1.0
    m = difflib.get_close_matches(k, _KEYS, n=1, cutoff=0.86)
    if m: return _BRIDGE[m[0]], difflib.SequenceMatcher(None, k, m[0]).ratio()
    return None, 0.0

def identify(german, english):
    """-> (canonical_title, literal_en, common_en, how)"""
    if german:
        c, lit, com, alt, ok = resolve(german)
        if ok: return c, lit, com, 'german'
    if english:
        g, score = english_to_german(english)
        if g:
            c, lit, com, alt, ok = resolve(g)
            if ok: return c, lit, com, f'english->german({score:.2f})'
    return None, None, None, 'unresolved'
