# -*- coding: utf-8 -*-
"""Make the table of Appendix 8.A of LITURGICAL_AND_ECCLESIASTICAL_LIFE.md from hymns.db.

The rules are those of §8.A.2. Only the old witnesses are counted; one hymn is one row, with
the identities of the Compare by day sheet of hymns.xlsx; grouped entries are shared out; a
season counts only for the feast at its head; and a hymn is shown when it has at least three
witnesses, three fifths of the leading hymn's and a quarter of the day's. Like export_xlsx.py,
it needs openpyxl.

    py hymn_tables/appendix_8a.py            print the table as Markdown
    py hymn_tables/appendix_8a.py --check    compare it with the table in the book
    py hymn_tables/appendix_8a.py --stats    the figures that §8.A.4 quotes
"""
import collections, os, re, sqlite3, sys
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import export_xlsx as X
from editorial import EDITORIAL

BOOK = os.path.join(HERE, '..', 'LITURGICAL_AND_ECCLESIASTICAL_LIFE.md')

# the witnesses of 1800 onward, which the table leaves out (§8.A.1)
MODERN = {
 'Eckardt, The Lutheran Propers', 'Gehrke', 'Judisch', 'Krusemark, Even Year',
 'Krusemark, Every Year', 'Krusemark, Odd Year', 'Krusemark, Year A', 'Krusemark, Year B',
 'Krusemark, Year C', 'LCMS Synod selections (2016-17)', 'LSB Hymnal Committee',
 'Lutheran Service Book (2006)', 'Lutheran Worship (1982)', 'MC (private scheme)',
 'Mecklenburg hymnal (1855)', 'Redeemer', 'Reuning', 'SD (private scheme)', 'SELK hymnal',
 'Stuckwisch (sword-in-hat list)', 'Zion'}
THOMPSON = 'Thompson, diss. App. 2 (Ludecus + twelve 16th-c. lists)'

LAST = 'Trinity 25–27 (the last Sundays)'
DAYS = (['Advent 1', 'Advent 2', 'Advent 3', 'Advent 4', 'Christmas Day', 'Sunday after Christmas',
         'New Year (Circumcision)', 'Sunday after New Year', 'Epiphany']
        + [f'Epiphany {i}' for i in range(1, 7)]
        + ['Septuagesima', 'Sexagesima', 'Quinquagesima (Estomihi)', 'Lent 1 (Invocavit)',
           'Lent 2 (Reminiscere)', 'Lent 3 (Oculi)', 'Lent 4 (Laetare)', 'Lent 5 (Judica)',
           'Palm Sunday', 'Maundy Thursday', 'Good Friday', 'Easter Day', 'Easter Monday',
           'Easter 1 (Quasimodogeniti)', 'Easter 2 (Misericordias Domini)', 'Easter 3 (Jubilate)',
           'Easter 4 (Cantate)', 'Easter 5 (Rogate)', 'Ascension', 'Sunday after Ascension (Exaudi)',
           'Pentecost', 'Pentecost Monday', 'Trinity Sunday']
        + [f'Trinity {i}' for i in range(1, 25)]
        + [LAST, 'Purification of Mary (2 Feb)', 'Annunciation (25 March)',
           'St John the Baptist (24 June)', 'Visitation of Mary (2 July)', 'St Michael (29 Sept)',
           "Apostles' days"])

# an occasion of hymns.db -> the day(s) of the table it counts for; any other occasion that is
# not itself a day of the table ("Advent", "Lent", "Trinity season", the Zweibrücken cycle) is
# not counted
MAP = {
 'Christmas': ['Christmas Day'], 'Christmas (Midnight)': ['Christmas Day'],
 'Christmas (Dawn)': ['Christmas Day'], 'Christmas / New Year': ['Christmas Day', 'New Year (Circumcision)'],
 'Easter': ['Easter Day'], 'Easter (Sunrise)': ['Easter Day'],
 'Advent 2 & 3': ['Advent 2', 'Advent 3'], 'Advent 3 & 4': ['Advent 3', 'Advent 4'],
 'Septuagesima & Sexagesima': ['Septuagesima', 'Sexagesima'],
 'Quinquagesima': ['Quinquagesima (Estomihi)'], 'Quinquagesima (Esto mihi)': ['Quinquagesima (Estomihi)'],
 'Lent 1-3 (Invocavit, Reminiscere, Oculi)': ['Lent 1 (Invocavit)', 'Lent 2 (Reminiscere)', 'Lent 3 (Oculi)'],
 'Lent 4 (Mid-Lent / Laetare)': ['Lent 4 (Laetare)'],
 'Lent 5 (Judica), Palm Sunday & Good Friday': ['Lent 5 (Judica)', 'Palm Sunday', 'Good Friday'],
 'Lent 5 (Judica) & Palm Sunday': ['Lent 5 (Judica)', 'Palm Sunday'],
 'Easter 5 (Rogate/Vocem jucunditatis)': ['Easter 5 (Rogate)'],
 'Pentecost & Pentecost Monday': ['Pentecost', 'Pentecost Monday'],
 'Trinity 1 & 2': ['Trinity 1', 'Trinity 2'], 'Trinity xxiiii': ['Trinity 24'],
 'Trinity 25': [LAST], 'Trinity 26': [LAST], 'Trinity 27': [LAST], 'Trinity 25 & 26': [LAST],
 'Trinity 25-27': [LAST], 'Trinity 26 & 27': [LAST],
 'St Michael (29 September)': ['St Michael (29 Sept)'], 'Common of Apostles': ["Apostles' days"],
 # a season counts only for the feast at its head
 'Christmas to Purification': ['Christmas Day'], 'Purification to Septuagesima': ['Purification of Mary (2 Feb)'],
 'Easter to Ascension': ['Easter Day'], 'Easter season': ['Easter Day'], 'Pentecost season': ['Pentecost'],
}

# a class of hymns, not a hymn: a witness that gives only this gives no hymn for the day
GENERIC = re.compile(r'^(\[.*\]|Passion hymns|Passionslieder und Adventslieder|'
                     r'Christmas hymns preferred over New Year)$')

def days_of(occasion):
    return MAP.get(occasion, [occasion] if occasion in DAYS else [])

def build(exclude=()):
    """-> [(day, [(hymn, witnesses, assigned?)], witnesses of the day)], and the counts by day"""
    day_w = collections.defaultdict(set)
    day_h = collections.defaultdict(lambda: collections.defaultdict(set))
    for r in X.load():
        if r['wit'] in MODERN or r['wit'] in exclude or GENERIC.match(r['ident'] or ''): continue
        for d in days_of(r['occ']):
            day_w[d].add(r['wit'])
            day_h[d][r['ident']].add(r['wit'])
    assigned = collections.defaultdict(list)
    for occasion, hymn, _note in EDITORIAL:
        assigned[occasion].append(hymn)
    table = []
    for d in DAYS:
        total = len(day_w[d])
        items = sorted(((h, len(w)) for h, w in day_h[d].items()), key=lambda kv: (-kv[1], kv[0]))
        lead = items[0][1] if items else 0
        shown = [(h, n, False) for h, n in items if n >= 3 and n >= 0.6 * lead and n >= 0.25 * total]
        if not shown and d in assigned:
            shown = [(h, len(day_h[d].get(h, ())), True) for h in assigned[d]]
        table.append((d, shown, total))
    return table, day_h

def markdown(table):
    db = sqlite3.connect(X.DB)
    lex = {c: (lit, com) for c, lit, com in
           db.execute('SELECT canonical_title, literal_english, common_english FROM hymns')}
    carver = {c for (c,) in db.execute("SELECT canonical_title FROM translation_candidates "
                                       "WHERE status LIKE 'matthew_carver%'")}
    out = []
    for d, shown, total in table:
        for i, (h, n, assigned) in enumerate(shown):
            lit, com = lex.get(h, (None, None))
            com = com + (' †' if h in carver else '') if com else '—'
            out.append(f"| {f'**{d}**' if i == 0 else ''} | *{h}* | {lit} | {com} | "
                       f"{n} of {total}{' ‡' if assigned else ''} |")
    return out

def book_rows():
    text = open(BOOK, encoding='utf-8').read()
    seg = text[text.index('#### <a id="s8-a-3"></a>'):text.index('#### <a id="s8-a-4"></a>')]
    return [l for l in seg.splitlines() if l.startswith('| ') and re.search(r' \d+ of \d+', l)]

def stats(table):
    chosen = [(d, shown, total) for d, shown, total in table if shown and not shown[0][2]]
    two_thirds = [d for d, shown, total in chosen if shown[0][1] >= 2 * total / 3]
    print(f'{len(two_thirds)} of the {len(chosen)} days the witnesses choose have a hymn with '
          f'two thirds of the day\'s witnesses')
    without, _ = build(exclude={THOMPSON})
    first = {d: shown[0][0] for d, shown, _t in table if shown and not shown[0][2]}
    first2 = {d: shown[0][0] if shown else None for d, shown, _t in without}
    print('without Thompson, the leading hymn changes on:', [d for d in first if first[d] != first2[d]])
    a = {d: {h for h, _n, _e in shown} for d, shown, _t in table}
    b = {d: {h for h, _n, _e in shown} for d, shown, _t in without}
    changed = [(d, sorted(a[d] - b[d]), sorted(b[d] - a[d])) for d in a if a[d] != b[d]]
    print(f'and the hymns shown change on {len(changed)} days:')
    for d, lose, gain in changed:
        print(f'   {d}: loses {lose}, gains {gain}')

if __name__ == '__main__':
    table, _ = build()
    rows = markdown(table)
    if '--check' in sys.argv:
        book = book_rows()
        if rows == book:
            print(f'{len(rows)} rows; the table in the book is current')
        else:
            print(f'{len(rows)} rows made, {len(book)} in the book; they differ:')
            for line in [l for l in book if l not in rows]: print('  book:', line)
            for line in [l for l in rows if l not in book]: print('  made:', line)
            sys.exit(1)
    elif '--stats' in sys.argv:
        stats(table)
    else:
        print('\n'.join(rows))
