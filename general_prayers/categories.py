"""Standardized categories for petitions of the general prayer.

Every petition gets one primary category (what the bidding/prayer is chiefly
*for*) and optional secondary categories (other intentions it also names).
The codes were fixed after surveying all witnesses, so that the orders can be
compared petition by petition (see the `category_matrix` view).
"""

# code: (English label, description)
CATEGORIES = {
    'exhortation':      ('Exhortation / preface', 'Address to the people calling them to prayer (often citing Mt 18:19, Mt 7:7, 1 Tim 2:1-2), before the first petition.'),
    'confession':       ('Confession of sins', 'Confession of sins and/or absolution placed inside the general prayer.'),
    'repentance':       ('Repentance & forgiveness', 'Petition for forgiveness of the congregation\'s sins, turning away of deserved punishment, amendment of life.'),
    'thanksgiving':     ('Thanksgiving', 'Thanks for God\'s benefits, especially for the Word/Gospel.'),
    'word':             ('The Word & its fruit', 'For the pure preaching of the Word and its fruit in the hearers (the sermon just heard).'),
    'church':           ('The Church', 'For the holy Christian Church in all the world, its preservation, unity and increase.'),
    'ministers':        ('Ministers of the Word', 'For pastors, preachers and teachers; labourers into the harvest (Mt 9:38).'),
    'schools':          ('Schools & youth', 'For schools, universities, the young and their instruction.'),
    'civil-authority':  ('Civil authority', 'For the Emperor, kings, princes, the local lord or city council, their counsellors and officials (1 Tim 2:2).'),
    'estates':          ('All estates / households', 'For all estates and callings, the household estate, parents, spouses, children, servants.'),
    'peace':            ('Peace', 'For common peace and quiet in the land.'),
    'enemies':          ('Enemies', 'For enemies and persecutors, that God would convert them (Mt 5:44).'),
    'turks':            ('Against the Turk', 'Protection of Christendom from the Turk (the "Erbfeind").'),
    'errant':           ('The erring & unbelievers', 'Conversion of heretics, the erring, the papacy, Jews, Turks and heathen; spread of the Gospel.'),
    'persecuted':       ('The persecuted', 'For those suffering persecution or imprisonment for the Gospel\'s sake.'),
    'afflicted':        ('The afflicted', 'For all in trouble and temptation: the sick, poor, captive, widows and orphans, the dying.'),
    'calamities':       ('Deliverance from calamities', 'From war, pestilence, dearth, famine, storm and other plagues.'),
    'childbirth':       ('Women with child', 'For women with child and in travail.'),
    'fruits-of-earth':  ('Fruits of the earth', 'For good weather, the fruits of the earth, daily bread and bodily needs.'),
    'congregation':     ('The present congregation', 'For those gathered here: faith, godly life, perseverance, a blessed end.'),
    'communicants':     ('Communicants', 'For those about to receive the Lord\'s Supper, worthy reception.'),
    'special':          ('Special intercessions', 'Rubric allowing particular persons\' requests or current needs to be named.'),
    'all-men':          ('All men', 'A general intercession for all men (1 Tim 2:1).'),
    'conclusion':       ('Conclusion', 'Closing petition summing up ("for all that for which God will be prayed"), doxology, Amen.'),
    'lords-prayer':     ('Lord\'s Prayer', 'The Our Father (or its paraphrase) said as the close of the general prayer.'),
    'creed':            ('Creed', 'The Apostles\' Creed said with the general prayer.'),
    'decalogue':        ('Ten Commandments', 'The Decalogue said with the general prayer.'),
    'blessing':         ('Blessing', 'Benediction said as part of the prayer block.'),
}

ORDER = list(CATEGORIES)

# aliases used while curating -> standard code
ALIASES = {
    'all-things': 'conclusion',
    'error': 'errant', 'heretics': 'errant', 'papists': 'errant', 'heathen': 'errant', 'jews': 'errant',
    'hearers': 'congregation', 'youth': 'schools',
    'special-supplications': 'special',
    'absolution': 'confession',
    'sick': 'afflicted', 'dying': 'afflicted', 'widows-orphans': 'afflicted',
    'household': 'estates', 'marriage': 'estates',
    'magistrates': 'civil-authority', 'government': 'civil-authority',
    'weather': 'fruits-of-earth',
}


def normalize(code):
    code = ALIASES.get(code, code)
    if code not in CATEGORIES:
        raise KeyError(code)
    return code
