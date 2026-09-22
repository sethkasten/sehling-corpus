# -*- coding: utf-8 -*-
"""Fold Krusemark's Hymn-of-the-Day rows into hymns.db.

Only the entries Krusemark marks as Hymn of the Day are inserted. His lists
also carry opening, distribution, offering and closing hymns; those are real
data but they are not chief hymns, and mixing them in would wreck the
meaning of the table. The full extraction is kept in rows_krusemark_raw.json.

Note on his Easter numbering: Krusemark counts Easter Day as Easter 1, so
his 'Easter 2, Quasimodo Geniti' is the Sunday this database already calls
'Easter 1 (Quasimodogeniti)'. The mapping below shifts them back.
"""
import re, os, json, sqlite3, collections, sys
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)

COMPILATION = 'Krusemark, Hymns ABC (2018)'

FIXED = {
 'Advent 1, Ad Te Levavi':'Advent 1','Advent 2, Populus Zion':'Advent 2',
 'Advent 3, Gaudete':'Advent 3','Advent 4, Rorate Coeli':'Advent 4',
 'All Saints’':'All Saints (1 Nov)','Annunciation Lord':'Annunciation (25 March)',
 'Ascension Lord':'Ascension','Ash Wednesday':'Ash Wednesday',
 'Baptism Lord':'Baptism of Christ (Octave of Epiphany)',
 'Christmas 1':'Sunday after Christmas','Christmas 2':'Christmas 2',
 'Christmastide':'Christmas','Circumcision Lord Name of Jesus':'New Year (Circumcision)',
 'Day of Thanksgiving':'Thanksgiving','Dormition Mary':'Assumption of Mary (15 Aug)',
 'Easter 2, Quasimodo Geniti':'Easter 1 (Quasimodogeniti)',
 'Easter 3, Misericordias Domini':'Easter 2 (Misericordias Domini)',
 'Easter 4, Jubilate':'Easter 3 (Jubilate)','Easter 5, Cantate':'Easter 4 (Cantate)',
 'Easter 6, Rogate':'Easter 5 (Rogate/Vocem jucunditatis)',
 'Easter 7, Exaudi':'Sunday after Ascension (Exaudi)',
 'Easter Monday':'Easter Monday','Easter Tuesday':'Easter Tuesday','Eastertide':'Easter',
 'Epiphany Lord':'Epiphany','Good Friday':'Good Friday','Holy Trinity':'Trinity Sunday',
 'Lent 1, Invocavit':'Lent 1 (Invocavit)','Lent 2, Reminiscere':'Lent 2 (Reminiscere)',
 'Lent 3, Oculi':'Lent 3 (Oculi)','Lent 4, Laetare':'Lent 4 (Laetare)',
 'Lent 5, Judica Passion Sunday':'Lent 5 (Judica)',
 'Lent 6, Palmarum Palm Sunday':'Palm Sunday','Maundy Thursday':'Maundy Thursday',
 'Michaelmas':'St Michael (29 Sept)','Nativity Lord Dawn':'Christmas (Dawn)',
 'Nativity Lord Day':'Christmas','Nativity Lord Eve Divine Service':'Christmas Eve',
 'Nativity Lord Eve Lessons and Carols':'Christmas Eve (Lessons and Carols)',
 'Nativity Lord Midnight':'Christmas (Midnight)',
 'Nativity St. John Baptist':'St John the Baptist (24 June)',
 'Pentecost Day':'Pentecost','Pentecost Monday':'Pentecost Monday',
 'Pentecost Tuesday':'Pentecost Tuesday','Pentecost Vigil':'Pentecost Vigil',
 'Purification Mary/Presentation Lord':'Purification of Mary (2 Feb)',
 'Quinquagesima':'Quinquagesima (Estomihi)','Reformation Day':'Reformation (31 Oct)',
 'Resurrection Lord, Easter Day':'Easter','Resurrection Lord, Easter Sunrise':'Easter (Sunrise)',
 'Resurrection Lord, Vigil of Easter':'Easter Vigil','Septuagesima':'Septuagesima',
 'Sexagesima':'Sexagesima','St. Peter and St. Paul':'St Peter and St Paul (29 June)',
 'Transfiguration Lord':'Transfiguration','Visitation Mary':'Visitation of Mary (2 July)',
 'St. Joseph':'St Joseph (19 March)',
}

def norm_occ(raw):
    raw = raw.strip()
    if raw in FIXED: return FIXED[raw]
    m = re.match(r'^(Trinity|Epiphany|Advent|Christmas)\s+(\d+)$', raw)
    if m: return f'{m.group(1)} {m.group(2)}'
    return raw

# witnesses Krusemark shares with sources already in the database
SHARED = {
 'Gehrke, Planning the Service':'Gehrke',
 'Carpzov':'Carpzov',
 'Bach’s cantata chorales':'Bach’s Leipzig usage',
 'Zion, Detroit (2013-14)':'Zion',
 'SELK hymnal':'SELK hymnal',
}

def main():
    raw = json.load(open(os.path.join(HERE, 'rows_krusemark_raw.json'), encoding='utf-8'))
    hod = [x for x in raw if x['hod']]
    db = sqlite3.connect(os.path.join(HERE, '..', 'hymns.db'))
    c = db.cursor()

    existing = set()
    for occ, src in c.execute('SELECT occasion, source FROM hymn_prescriptions'):
        existing.add((occ, src.split(' (via')[0]))

    rows, seen, folded = [], set(), 0
    for x in hod:
        occ = norm_occ(x['occasion_raw'])
        wit = SHARED.get(x['witness'], x['witness'])
        title = x['title']
        key = (occ, wit, title.lower())
        if key in seen: continue
        seen.add(key)
        if (occ, wit) in existing: folded += 1
        ref = f"{x['book']} {x['number']}" if x['book'] and x['number'] else None
        rows.append((occ, title, None, title,
                     f"{wit} (via {COMPILATION}{'; ' + ref if ref else ''})"))
    c.executemany('INSERT INTO hymn_prescriptions (occasion,original_title,literal_english,'
                  'common_english,source) VALUES (?,?,?,?,?)', rows)
    db.commit()
    print(f'Krusemark entries      : {len(raw)}')
    print(f'  marked Hymn of the Day: {len(hod)}')
    print(f'  inserted (deduped)    : {len(rows)}')
    print(f'  witnesses             : {len({r[4].split(" (via")[0] for r in rows})}')
    print(f'  occasions             : {len({r[0] for r in rows})}')
    print(f'  total rows now        : {c.execute("SELECT COUNT(*) FROM hymn_prescriptions").fetchone()[0]}')
    db.close()

if __name__ == '__main__':
    main()
