# -*- coding: utf-8 -*-
"""Two further Hauptlied witnesses.

HotD: a modern conflation table. Each line is an English hymn title followed
by sigla for the schemes that appoint it. Its sigla mix historical witnesses
(Carpzov, Selnecker, Mecklenburg 1855, Bach) with modern hymnals and parish
use, so they are namespaced to this compilation -- note that HotD's "K" is
the SELK hymnal whereas Liliencron's "K." is Keuchenthal 1573.

Selnecker: his own prose account of the scheme he kept, supplied in English
translation. Hand-encoded because it is narrative, not tabular.
"""
import re, os, json

HERE = os.path.dirname(os.path.abspath(__file__))
HOTD = 'Hymn of the Day conflation table (modern compilation)'

HOTD_SIGLA = {
 'C':'Carpzov', 'G':'Gehrke', 'K':'SELK hymnal', 'R':'Redeemer', 'S':'Selnecker',
 'Z':'Zion', 'SD':'SD (private scheme)', 'MC':'MC (private scheme)',
 'LW':'Lutheran Worship (1982)', 'LSB':'Lutheran Service Book (2006)',
 'Meckl. 1855':'Mecklenburg hymnal (1855)', 'Bach':'Bach’s Leipzig usage',
}
SIG_RE = re.compile(r'\b(Meckl\. 1855|LSB|LW|SD|MC|Bach|[CGKRSZ])\b')

ROMAN = {'I':1,'II':2,'III':3,'IV':4,'V':5,'VI':6,'VII':7,'VIII':8,'IX':9,'X':10,
 'XI':11,'XII':12,'XIII':13,'XIV':14,'XV':15,'XVI':16,'XVII':17,'XVIII':18,'XIX':19,
 'XX':20,'XXI':21,'XXII':22,'XXIII':23,'XXIV':24,'XXV':25,'XXVI':26,'XXVII':27}

def hotd_occ(s):
    s = s.strip()
    m = re.match(r'^(Advent|Christmas|Epiphany|Trinity)\s+([IVX]+)$', s)
    if m:
        n = ROMAN.get(m.group(2))
        if n: return f'{m.group(1)} {n}'
    m = re.match(r'^(Invocavit|Reminiscere|Oculi|Laetare|Judica)\s*[–-]\s*Lent\s+([IVX]+)$', s)
    if m: return f'Lent {ROMAN[m.group(2)]} ({m.group(1)})'
    m = re.match(r'^(Quasimodogeniti|Misericordias Domini|Jubilate|Cantate|Rogate)\s*[–-]\s*Easter\s+([IVX]+)$', s)
    if m: return f'Easter {ROMAN[m.group(2)]} ({m.group(1)})'
    FIX = {
     'Christmas Eve':'Christmas Eve','Christmas Midnight':'Christmas (Midnight)',
     'Christmas Day':'Christmas','St. Stephen':'St Stephen (26 Dec)','St. John':'St John the Evangelist (27 Dec)',
     'Holy Innocents':'Holy Innocents (28 Dec)','Circumcision and Name of Jesus':'New Year (Circumcision)',
     'Epiphany':'Epiphany','Octave of Epiphany (Baptism)':'Baptism of Christ (Octave of Epiphany)',
     'Transfiguration':'Transfiguration','Septuagesima':'Septuagesima','Sexagesima':'Sexagesima',
     'Estomihi (Quinquagesima)':'Quinquagesima (Estomihi)','Ash Wednesday':'Ash Wednesday',
     'Palmarum':'Palm Sunday','Maundy Thursday':'Maundy Thursday','Good Friday':'Good Friday',
     'Holy Saturday':'Holy Saturday','Easter Vigil':'Easter Vigil','Easter Sunday':'Easter',
     'Easter Monday':'Easter Monday','Easter Tuesday':'Easter Tuesday','Ascension':'Ascension',
     'Exaudi – Sunday after Ascension':'Sunday after Ascension (Exaudi)','Pentecost':'Pentecost',
     'Pentecost Monday':'Pentecost Monday','Pentecost Tuesday':'Pentecost Tuesday',
     'Holy Trinity':'Trinity Sunday','Church Dedication':'Church Dedication',
     'Common of Apostles':'Common of Apostles','Common of Martyrs & Doctors':'Common of Martyrs and Doctors',
     'The Confession of St. Peter (Jan. 15)':'Confession of St Peter (18 Jan)',
     'Conversion of St. Paul (Jan. 25)':'Conversion of St Paul (25 Jan)',
     'Purification of Mary (Feb. 2)':'Purification of Mary (2 Feb)',
     'Annunciation (March 25)':'Annunciation (25 March)',
     'The Nativity of St. John the Baptist (June 24)':'St John the Baptist (24 June)',
     'Presentation of the Augsburg Confession (June 25)':'Presentation of the Augsburg Confession (25 June)',
     'St. Peter and St. Paul (June 29)':'St Peter and St Paul (29 June)',
     'Visitation of Mary (July 2)':'Visitation of Mary (2 July)',
     'St. Mary Magdalene (July 22)':'St Mary Magdalene (22 July)','St. James (July 25)':'St James (25 July)',
     'St. Lawrence (Aug 10)':'St Lawrence (10 Aug)',
     'Dormition of the Blessed Virgin Mary (15 Aug)':'Assumption of Mary (15 Aug)',
     'Beheading of John the Baptist (29 Aug)':'Beheading of St John the Baptist (29 Aug)',
     'Nativity of the Blessed Virgin Mary (8 Sept)':'Nativity of Mary (8 Sept)',
     'Holy Cross (14 Sept)':'Holy Cross (14 Sept)','St. Matthew (21 Sept)':'St Matthew (21 Sept)',
     'St. Michael (29 Sept)':'St Michael (29 Sept)','SS. Simon and Jude (28 Oct)':'Ss Simon and Jude (28 Oct)',
     'Reformation Day (31 Oct)':'Reformation (31 Oct)','All Saints’ Day (1 Nov)':'All Saints (1 Nov)',
     "All Saints' Day (1 Nov)":'All Saints (1 Nov)','Festival of Thanksgiving':'Thanksgiving',
    }
    return FIX.get(s)

def parse_hotd():
    text = open(os.path.join(HERE, 'src_hotd_raw.txt'), encoding='utf-8').read()
    text = text.replace('’', '’')
    rows, occ, seen = [], None, set()
    for raw in text.split('\n'):
        ln = ' '.join(raw.split())
        if not ln or ln.startswith('C = Carpzov') or ln.startswith('S = Selnecker'): continue
        o = hotd_occ(ln)
        if o: occ = o; continue
        if not occ: continue
        m = SIG_RE.search(ln)
        if not m: continue
        title = ln[:m.start()].strip(' .')
        sig_part = ln[m.start():]
        title = re.sub(r'\s*\.\s*\.\s*\.\s*$', '', title).strip(' *')
        title = title.replace('Y e ', 'Ye ').replace('o’ er', 'o’er')
        if len(title) < 6: continue
        for tag in SIG_RE.findall(sig_part):
            wit = HOTD_SIGLA.get(tag)
            if not wit: continue
            key = (occ, title.lower(), wit)
            if key in seen: continue       # the OCR repeats one block of the page
            seen.add(key)
            rows.append({'occasion': occ, 'german': None, 'english': title,
                         'literal_only': False, 'witness': wit,
                         'compilation': HOTD, 'note': None})
    return rows

# ---- Selnecker, from his own prose account -------------------------------
SEL = 'Selnecker'
SEL_SRC = 'Selnecker, own account of his hymn scheme (English translation)'
SELNECKER = [
 ('Advent', ['Savior of the Nations, Come', 'The German Litany']),
 ('Christmas', ['We Praise Thee, Jesus, at Thy Birth', 'Now Praise We Christ, the Holy One',
   'Thanks Let Us Render (Danksagen wir alle)', 'From Heaven Above to Earth I Come',
   'From Heaven the Angel Troop Came Near', 'Why, Herod, Fearest Thou the Foe',
   'Hail the Day So Rich in Cheer']),
 ('Epiphany 2', ['To Jordan Came Our Lord the Christ']),
 ('Purification of Mary (2 Feb)', ['Lord, Now Lettest Thou Thy Servant Depart in Peace',
   'In Peace and Joy I Now Depart']),
 ('Epiphany 5', ['In Peace and Joy I Now Depart', 'O Lord, Look Down from Heaven, Behold']),
 ('Septuagesima', ['Salvation unto Us Has Come']),
 ('Sexagesima', ['Our Father, Thou in Heaven Above']),
 ('Quinquagesima (Estomihi)', ['By Adam’s Fall Is All Forlorn']),
 ('Lent 1 (Invocavit)', ['O Christ, Who Art the Light and Day', 'The German Litany']),
 ('Palm Sunday', ['From Depths of Woe I Cry to Thee']),
 ('Maundy Thursday', ['Jesus Christ, Our Blessed Savior']),
 ('Good Friday', ['Dear Christians, One and All, Rejoice']),
 ('Easter', ['This Is Such a Holy Day', 'Christ Is Arisen from the Grave’s Dark Prison',
   'Jesus Christ, Our Savior True, Who Death Overthrew']),
 ('Easter 5 (Rogate)', ['Our Father, Thou in Heaven Above']),
 ('Ascension', ['Dear Christians, One and All, Rejoice', 'Christ Rose to Heaven']),
 ('Sunday after Ascension (Exaudi)', ['If God Had Not Been on Our Side']),
 ('Pentecost', ['We Now Implore God the Holy Ghost', 'Come, Holy Ghost, God and Lord']),
 ('Trinity Sunday', ['God the Father, Be Our Stay', 'May God Bestow on Us His Grace']),
 ('Trinity 1', ['May God Bestow on Us His Grace', 'The Mouth of Fools Doth God Confess']),
 ('Trinity 2', ['Lord, Hear the Voice of My Complaint']),
 ('Trinity 3', ['Have Mercy on Me, Lord My God', 'The Only Son from Heaven']),
 ('Trinity 4', ['That Man a Godly Life Might Live']),
 ('Trinity 5', ['Were God Not with Us at This Time', 'If God Had Not Been on Our Side']),
 ('Trinity 6', ['Wilt Thou, O Man, Live Happily', 'Salvation unto Us Has Come']),
 ('Trinity 7', ['My Soul, Now Bless Thy Maker', 'My Soul Now Magnifies the Lord']),
 ('Trinity 8', ['O Lord, Look Down from Heaven, Behold']),
 ('Trinity 9', ['The Mouth of Fools Doth God Confess']),
 ('Trinity 10', ['Beside the Streams of Babylon']),
 ('Trinity 11', ['In Thee Alone, O Christ, My Lord', 'From Depths of Woe I Cry to Thee']),
 ('Trinity 12', ['By Adam’s Fall Is All Forlorn']),
 ('Trinity 13', ['Salvation unto Us Has Come', 'That Man a Godly Life Might Live']),
 ('Trinity 14', ['Have Mercy on Me, Lord My God', 'In Thee Alone, O Christ, My Lord']),
 ('Trinity 15', ['A Mighty Fortress Is Our God']),
 ('Trinity 16', ['In the Midst of Earthly Life', 'In Peace and Joy I Now Depart']),
 ('Trinity 17', ['Dear Christians, One and All, Rejoice']),
 ('Trinity 18', ['The Only Son from Heaven']),
 ('Trinity 19', ['Lord, Hear the Voice of My Complaint', 'My Soul, Now Bless Thy Maker']),
 ('Trinity 20', ['O Lord, Look Down from Heaven, Behold']),
 ('Trinity 21', ['Salvation unto Us Has Come', 'May God Bestow on Us His Grace']),
 ('Trinity 22', ['Have Mercy on Me, Lord My God', 'From Depths of Woe I Cry to Thee']),
 ('Trinity 23', ['The Mouth of Fools Doth God Confess']),
 ('Trinity 24', ['In Peace and Joy I Now Depart', 'Lord Jesus Christ, True Man and God']),
 ('Trinity 25', ['God the Father, Be Our Stay']),
 ('Trinity 26', ['Our Father, Thou in Heaven Above']),
 ('Trinity 27', ['Dear Christians, One and All, Rejoice', 'A Mighty Fortress Is Our God']),
 ('Annunciation (25 March)', ['The Only Son from Heaven']),
 ('Conversion of St Paul (25 Jan)', ['Have Mercy on Me, Lord My God']),
 ('Common of Apostles', ['We Praise Thee, O God (Te Deum)']),
 ('St John the Baptist (24 June)', ['To Jordan Came Our Lord the Christ']),
 ('Visitation of Mary (2 July)', ['My Soul Now Magnifies the Lord']),
 ('St Michael (29 Sept)', ['Lord God, We All to Thee Give Praise', 'My Soul, Now Bless Thy Maker']),
]

def parse_selnecker():
    return [{'occasion': occ, 'german': None, 'english': t, 'literal_only': False,
             'witness': SEL, 'compilation': SEL_SRC, 'note': None}
            for occ, titles in SELNECKER for t in titles]

if __name__ == '__main__':
    h, s = parse_hotd(), parse_selnecker()
    json.dump(h, open(os.path.join(HERE,'rows_hotd.json'),'w'), ensure_ascii=False, indent=1)
    json.dump(s, open(os.path.join(HERE,'rows_selnecker.json'),'w'), ensure_ascii=False, indent=1)
    print(f'HotD: {len(h)} rows, {len({x["occasion"] for x in h})} occasions, '
          f'{len({x["witness"] for x in h})} witnesses')
    print(f'Selnecker: {len(s)} rows, {len({x["occasion"] for x in s})} occasions')
