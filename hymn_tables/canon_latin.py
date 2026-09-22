"""Snap OCR'd Latin incipits to canonical forms. The repertoire in these
orders is a small, fixed set of office hymns and sequences."""
import re, unicodedata

CANON = [
 ('Veni redemptor gentium',      [r'veni\s+re[dt]em[pt]?tor']),
 ('Conditor alme siderum',       [r'conditor\s+alme']),
 ('A solis ortus cardine',       [r'a\s+solis\s+ortu']),
 ('Hostis Herodes impie',        [r'hostis\s+herodes', r'herodes\s+hostis']),
 ('Corde natus ex parentis',     [r'corde\s+natus']),
 ('Christe qui lux es et dies',  [r'christe?,?\s+qui\s+lux', r'christus,?\s+qui\s+lux']),
 ('Dies absoluti praetereunt',   [r'dies\s+absoluti']),
 ('Audi benigne conditor',       [r'audi\s+benigne']),
 ('Vexilla regis prodeunt',      [r'vexilla\s+regis']),
 ('Rex Christe factor omnium',   [r'rex\s+christe']),
 ('Crux fidelis',                [r'crux\s+fidelis']),
 ('Ad coenam agni providi',      [r'ad\s+c[oe]+nam\s+agni']),
 ('Vita sanctorum decus angelorum', [r'vita\s+sanctorum']),
 ('Festum nunc celebre',         [r'festum\s+nunc']),
 ('Veni creator Spiritus',       [r'veni,?\s+creator']),
 ('O lux beata Trinitas',        [r'o\s+lux,?\s+beata']),
 ('Veni sancte Spiritus',        [r'veni\s+san[ct]+e\s+spiritus']),
 ('Pange lingua gloriosi',       [r'pange\s+lingua']),
 ('Iam maesta quiesce querela',  [r'[ij]am\s+m[ao]esta']),
 ('Te Deum laudamus',            [r'te\s+deum\s+laudamus']),
 ('Gloria laus et honor',        [r'gloria\s+laus']),
 ('Victimae paschali laudes',    [r'victim[ae]+\s+paschali']),
 ('Grates nunc omnes',           [r'grates\s+nunc']),
 ('Vespertina oratio',           [r'vespertina\s+oratio']),
 ('Iesu nostra redemptio',       [r'[ij]esu\s+nostra\s+redem']),
 ('Aurea luce',                  [r'aurea\s+luce']),
 ('Optatus votis omnium',        [r'optatus\s+votis']),
 ('Summae Trinitati',            [r'summ[ae]+\s+trinitati']),
 ('Beata nobis gaudia',          [r'beata\s+nobis']),
 ('Chorus novae Ierusalem',      [r'chorus\s+nov[ae]+']),
 ('Puer natus in Bethlehem',     [r'puer\s+natus']),
]

def canon(s):
    t = unicodedata.normalize('NFKD', s).lower()
    t = re.sub(r'[^a-z\s]', ' ', t)
    t = re.sub(r'\s+', ' ', t).strip()
    for name, pats in CANON:
        for p in pats:
            if re.search(p, t): return name
    return None
