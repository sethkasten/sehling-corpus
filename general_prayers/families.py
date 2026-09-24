"""Text families of the general prayer.  A witness's `family` string begins
with one of these codes ("B2. Württemberg short form"); the builder writes
this table so that orders can be compared within and across families."""

# code: (archetype / earliest witness, description)
FAMILIES = {
    'A':  ('Schwäbisch Hall 1526 (Brenz)',
           'Deacon or pastor bids the people for one intention ("Lasst uns bitten für …"), '
           'then says a collect for it; the series runs Church, magistrates, peace, afflicted, '
           'all needs, and closes with the Lord\'s Prayer. Frankfurt adds collects from '
           'Brandenburg-Nürnberg 1533 and Veit Dietrich.'),
    'B1': ('Württemberg 1553, long form',
           'Brenz\'s bidding-plus-collect scheme in its ducal form: a preface on prayer '
           '(Mt 18:19, 1 Tim 2), then biddings each followed by a collect; used chiefly on high '
           'feasts. Spread through Pfalz-Neuburg 1554 to the Palatinate, Zweibrücken, Veldenz '
           'and Leiningen.'),
    'B2': ('Württemberg 1553, short form',
           'The same intentions compressed into a single continuous prayer ("Allmächtiger, '
           'ewiger Gott, himmlischer Vater …") after a brief exhortation; the ordinary Sunday '
           'form. The most widely copied general prayer in the corpus, reaching Saxony (1580), '
           'Magdeburg, Strasbourg, Sayn, Nassau and the Ysenburg counties.'),
    'C':  ('Hanau-Lichtenberg 1573',
           'A bidding exhortation in the Strasbourg manner: the minister tells the people what '
           'to pray for, item by item, without addressing God, and ends with the Our Father.'),
    'D':  ('Nürnberg 1545 (Veit Dietrich)',
           '"Vermahnung zum Gebet": an exhortation in the second person ("Lieben Freund, '
           'bittet …") listing the intentions, closed by the Our Father. Copied in Waldeck, '
           'Erbach, Solms-Laubach and Henneberg.'),
    'E':  ('Leipzig 1567',
           'The Albertine Saxon "Gemein Gebet" in the Melanchthon/Pfeffinger tradition, a '
           'continuous prayer with pronounced petitions against war and for the Elector.'),
    'F':  ('Augsburg 1537',
           'Upper German (Bucerian/Zwinglian) intercession after the sermon, a continuous '
           'prayer with rubrics, related to Zürich 1535 and the Strasbourg forms.'),
    'G':  ('Hessen 1566',
           'Hessian "Vermanung zum Gebet": a numbered bidding exhortation which the order '
           'allows to be shortened or lengthened locally.'),
    'H':  ('Braunschweig 1528 (Bugenhagen)',
           'Bugenhagen\'s pulpit exhortation after the sermon in Low German: the people are led '
           'through Creed, confession, biddings for all estates and needs, and the Our Father. '
           'Hamburg copies it verbatim; Osnabrück prescribes the same contents in indirect speech.'),
    'I':  ('Öhringen 1544 (Huberinus)',
           'Caspar Huberinus\' "Vorbitt", whose first part is arranged by the '
           'petitions of the Lord\'s Prayer.'),
    'J':  ('Lüneburg 1564',
           'Lower Saxon exhortation to prayer read "from the notel" after the sermon; passed '
           'verbatim to Braunschweig-Wolfenbüttel 1569 and Oldenburg 1573.'),
    'K':  ('Worms 1560',
           'After an exhortation the minister reads three collects from the pulpit: thanksgiving '
           'or the Church, the magistrates, and a special need, chosen from a bank.'),
    'L':  ('Brandenburg 1540',
           'Not a pulpit prayer but collects said by the priest in the Mass under the Sanctus, '
           'for ministers, magistrates and peace, in the place the Roman Canon had its '
           'intercessions. Followed by Calenberg-Göttingen 1542 and Pfalz-Neuburg 1543.'),
    'M':  ('Norden 1528',
           'Early East Frisian pulpit biddings after the medieval Prone: three biddings, then '
           'Decalogue, confession, Creed and Our Father.'),
    'R1': ('Kurpfalz 1563 (Heidelberg)',
           'The Reformed Sunday prayer after the sermon: confession and absolution, a long '
           'continuous prayer (fruit of the Word, ministers, magistrates, all men, the '
           'persecuted, the afflicted, the congregation), then the Our Father. Copied in Moers, '
           'Bentheim-Tecklenburg, Ysenburg-Birstein 1598 and, abridged, Lutheran Schaumburg 1614.'),
    'R2': ('Kurpfalz 1563, alternative',
           'The Heidelberg alternative prayer paraphrasing the Lord\'s Prayer clause by clause '
           '(after Geneva and the Heidelberg Catechism qq. 122-127).'),
    'R3': ('Frankfurt 1554 (Poullain)',
           'Calvin\'s Strasbourg/Geneva "grande prière" in Latin, for the French refugee church, '
           'ending in a paraphrase of the Lord\'s Prayer.'),
    'R4': ('London 1554 (à Lasco/Micron)',
           'The London Dutch stranger church\'s prayer after the sermon (German version for '
           'East Frisia), still praying for the King of England and the city of London.'),
}


def code(family):
    return family.split('.')[0].strip()
