# -*- coding: utf-8 -*-
"""The hymn of the lexicon that a hymnal number names: the number's row in the Lutheran Hymn
Index (Hymnal Index/hymnal.db), and the lexicon's hymn on that row. merge_te_laudamus.py reads
Te Laudamus's chief hymns by their TL numbers, merge_krusemark.py Krusemark's by the LSB, TLH,
WH, ELH and LW numbers he gives.

A row's hymn is the one index_titles.INDEX matches to the row. Where a Latin hymn and its German
version share the row, it is the one the row's own original is: the German where the index
records one ("Nun komm, der Heiden Heiland" on the row of "Veni redemptor gentium"), else the
Latin. A row that INDEX does not match takes the hymn its German or Latin original resolves to,
if the original is that hymn's whole incipit or begins with it, word for word: the index's
"Gelobet sei der Herr" (Olearius, TLH 38) is not the German Benedictus, "Gelobet sei der Herr,
der Gott Israel", nor Martin Behm's "O heilige Dreifaltigkeit" (TLH 541) "O Licht, heilige
Dreifaltigkeit" (O lux beata Trinitas), which has a word more. A row whose recorded original is
not its hymn (NOT_ITS_ORIGINAL) takes none. Any other row is a hymn the lexicon lacks.
"""
import collections, difflib, os, re, sys
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import bridge, index_titles
from resolve import resolve, norm

# Walther's Hymnal, Matthew Carver's English edition (2012), keeps the numbers of Walther's
# Kirchengesangbuch, the index's KELG
CODES = {'WH': 'KELG'}

# rows whose original, as the index records it, is not the row's hymn, so that no hymn of the
# lexicon is taken from it, each named by a hymnal number on it (a row's id is its line in the
# sheet, which moves as rows are added): "I Know That My Redeemer Lives" (TLH 200, LBW 352, LSB
# 461) is Samuel Medley's English hymn (1775), which the index records as a translation of "Ich
# weiß, daß mein Erlöser lebt", the opening of the older German hymn of the Magdeburg list of 1632;
# "We All Believe in One True God, Father" (TLH 252, LSB 953) is Tobias Clausnitzer's hymn on the
# Apostles' Creed (1668), "Wir glauben all an einen Gott, Vater", whose German the index records
# only as far as it opens like Luther's creed hymn, "Wir gläuben all' an einen Gott" (TLH 251)
NOT_ITS_ORIGINAL = {
 'TLH 200': "Medley's English hymn, not a translation",
 'TLH 252': "Clausnitzer's hymn on the Apostles' Creed, which opens as Luther's creed hymn does",
}
_not_its_original = None
def not_its_original():
    """NOT_ITS_ORIGINAL by the rows' ids"""
    global _not_its_original
    if _not_its_original is None:
        _not_its_original = {index_titles.row(ref): why for ref, why in NOT_ITS_ORIGINAL.items()}
    return _not_its_original

def rows(code, number, suffix=''):
    """ids in hymnal.db of the rows that bear the hymnal number (a page of the liturgy is not one)"""
    return {h for (h,) in index_titles._c().execute(
        "SELECT hymn_id FROM hymn_numbers WHERE hymnal_code = ? AND number = ? "
        "AND COALESCE(suffix, '') = ? AND is_page = 0", (CODES.get(code, code), int(number), suffix))}

def rows_lettered(code, number):
    """the rows that bear the number with any letter: the Service Book and Hymnal's hymns of two
    tunes are 8a and 8b in the index, but plain 8 in a list that cites them"""
    return {h for (h,) in index_titles._c().execute(
        "SELECT hymn_id FROM hymn_numbers WHERE hymnal_code = ? AND number = ? AND is_page = 0",
        (CODES.get(code, code), int(number)))}

def originals(hid):
    """the German and the other originals the index records for the row, German first"""
    german, original = index_titles._c().execute(
        'SELECT german_title, original_title FROM hymns WHERE id = ?', (hid,)).fetchone()
    return [t.strip() for t in ' / '.join(x for x in (german, original) if x).split(' / ')
            if t.strip()]

def titles(hid):
    """every title the index records for the row: its master title and each hymnal's"""
    out = set(index_titles._titles(hid).values())
    out.update(t for (t,) in index_titles._c().execute('SELECT title FROM hymns WHERE id = ?', (hid,)))
    return {t for t in out if t}

def close(a, b):
    a, b = norm(a), norm(b)
    return a.startswith(b) or b.startswith(a) or difflib.SequenceMatcher(None, a, b).ratio() >= 0.85

def _bare(s):
    """norm without punctuation, which the index's originals print freely ("Pange, lingua, ...")"""
    return re.sub(r'\s+', ' ', re.sub(r'[^\w\s]', ' ', norm(s))).strip()

def _words(s):
    """the words of a title, punctuation aside; an elision ("heil'ge") is one word"""
    return _bare(re.sub(r"['\u2019\u02bc]", '', s)).split()

def whole(canonical, original):
    """the original is the canonical hymn's incipit, or begins with it, word for word: it has at
    least the incipit's words, and its first so many words are the incipit's, spelt alike or
    nearly ("genädig" for "gnädig"), with none wanting or added"""
    a, b = _words(original), _words(canonical)
    if len(a) < len(b):
        return False
    x, y = ' '.join(a[:len(b)]), ' '.join(b)
    return x == y or difflib.SequenceMatcher(None, x, y).ratio() >= 0.85

_matched = None
def _index():
    """row id -> the hymns INDEX matches to it"""
    global _matched
    if _matched is None:
        _matched = collections.defaultdict(list)
        for c, ref in index_titles.INDEX.items():
            _matched[index_titles.row(ref)].append(c)
    return _matched

def hymn(hid):
    """(the lexicon's hymn on index row hid or None, how)"""
    first = originals(hid)[:1]
    matched = list(_index().get(hid, []))
    if len(matched) > 1:   # a Latin hymn and its German version share the row: the row's own
        matched = [c for c in matched if any(close(c, o) or resolve(o)[0] == c for o in first)]
    if len(matched) == 1:
        return matched[0], 'the index row (index_titles.INDEX)'
    if matched:
        raise SystemExit(f'index_rows: row {hid} of the index has {matched}')
    if hid in not_its_original():
        return None, f'not in the lexicon ({not_its_original()[hid]})'
    for o in originals(hid):
        c, _lit, _com, _alt, ok = resolve(o)
        if ok and whole(c, o):
            return c, f'its original, {o}'
    return None, 'not in the lexicon'

def agreement(printed, hid):
    """how near the printed title is to a title the index records for the row: 1.0 where one
    begins the other, else the best ratio of their words"""
    k, best = bridge.keyify(printed), 0.0
    for t in titles(hid):
        kt = bridge.keyify(t)
        if not kt: continue
        if k.startswith(kt) or kt.startswith(k): return 1.0
        best = max(best, difflib.SequenceMatcher(None, k, kt).ratio())
    return best
