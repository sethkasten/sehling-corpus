# -*- coding: utf-8 -*-
"""Export hymns.db to an Excel workbook for comparing chief-hymn choices by day."""
import sqlite3, re, os, sys, unicodedata, collections
from openpyxl import Workbook
from openpyxl.styles import Font, Alignment, PatternFill, Border, Side
from openpyxl.utils import get_column_letter
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import bridge
import merge_finnish, merge_krusemark, merge_lbw, merge_sbh, merge_slovak, merge_te_laudamus
from resolve import by_occasion
from editorial import EDITORIAL

HERE = os.path.dirname(os.path.abspath(__file__))
DB  = os.path.join(HERE, '..', 'hymns.db')
OUT = os.path.join(HERE, '..', 'hymns.xlsx')

FONT = 'Arial'
HDR_FILL = PatternFill('solid', fgColor='1F3864')
HDR_FONT = Font(name=FONT, size=10, bold=True, color='FFFFFF')
BODY     = Font(name=FONT, size=10)
BOLD     = Font(name=FONT, size=10, bold=True)
TITLE    = Font(name=FONT, size=14, bold=True, color='1F3864')
ALT_FILL = PatternFill('solid', fgColor='F2F5FA')
THIN     = Side(style='thin', color='BFBFBF')

# ---- liturgical ordering ---------------------------------------------------
SEASON = ['Advent','Christmas Eve','Christmas','Sunday after Christmas','New Year',
          'Sunday after New Year','Epiphany','Baptism','Transfiguration','Septuagesima',
          'Sexagesima','Quinquagesima','Ash Wednesday','Lent','Passiontide','Palm Sunday',
          'Holy Week','Maundy Thursday','Good Friday','Holy Saturday','Easter Vigil','Easter',
          'Ascension','Sunday after Ascension','Pentecost','Trinity Sunday','Trinity']
def sort_key(occ):
    for i, s in enumerate(SEASON):
        if occ == s or occ.startswith(s + ' '):
            m = re.search(r'(\d+)', occ[len(s):])
            return (0, i, int(m.group(1)) if m else 0, occ)
    return (1, 0, 0, occ)            # sanctoral and everything else, alphabetical

def norm(s):
    t = unicodedata.normalize('NFKD', (s or '').lower()).replace('’', "'")
    t = ''.join(c for c in t if not unicodedata.combining(c))
    t = re.sub(r'[^a-z0-9 ]', ' ', t)
    return re.sub(r'\s+', ' ', t).strip()

def load():
    """One identity per hymn, so the same hymn cited in German, Latin or English
    -- or merely under a different capitalisation -- collapses to one row."""
    db = sqlite3.connect(DB)
    canon = {}
    for printed, c, src in db.execute('SELECT printed_title, canonical_title, source FROM attestations'):
        canon[(norm(printed), src)] = c
    english = {}          # canonical -> received English title, for display
    for c, com in db.execute('SELECT canonical_title, common_english FROM hymns'):
        if com: english[c] = com
    rows, cache = [], {}
    for occ, orig, lit, com, src in db.execute(
            'SELECT occasion, original_title, literal_english, common_english, source '
            'FROM hymn_prescriptions'):
        wit = src.split(' (via')[0]
        ident = canon.get((norm(orig), src))
        # Te Laudamus, LBW, the SBH's Hymn of the Week and Krusemark name their hymns by number:
        # by its row in the Lutheran Hymn Index. A row the lexicon lacks (ident None) is named by
        # the index's title for it (the common_english of TL's, LBW's and the SBH's rows), and is
        # not then taken for a lexicon hymn of a like title. The transcriptions of the Finnish
        # handbooks and the Slovak lists name their hymns in the same way: a hymn they leave
        # unnamed keeps its Finnish or Czech title
        by_number, name = False, None
        if not ident and wit in merge_finnish.WITNESSES:
            ident, by_number = merge_finnish.canonical(src), True
        elif not ident and wit in merge_slovak.WITNESSES:
            ident, by_number = merge_slovak.canonical(src), True
        elif not ident and src.startswith(merge_te_laudamus.WITNESS + ' (via'):
            ident, by_number = merge_te_laudamus.canonical(src), True
        elif not ident and src.startswith(merge_lbw.WITNESS + ' (via'):
            ident, by_number = merge_lbw.canonical(src), True
        elif not ident and src.startswith(merge_sbh.WITNESS + ' (via'):
            ident, by_number = merge_sbh.canonical(src), True
        elif not ident and merge_krusemark.COMPILATION in src:
            ident, how = merge_krusemark.canonical(src, orig)
            by_number = how is not None
            if by_number and not ident: name = merge_krusemark.index_title(src)
        if not ident and not by_number:
            key = (orig, com)
            if key not in cache:
                c, _l, _c, _how = bridge.identify(orig, com)
                if not c:                   # an English-only source: its title is English
                    c, _l, _c, _how = bridge.identify(None, orig)
                cache[key] = c
            ident = cache[key]
        if ident:                           # Luther's Easter vs Communion "Jesus Christus, unser Heiland"
            ident = by_occasion(ident, occ, orig)[0]
        if not ident:                       # unresolved: group on the normalised title
            ident = (name or com or orig or '').strip()
            ident = GROUPED.setdefault(norm(ident), ident)
        # fold known variant titles together; a number has named the hymn already
        for cand in ((ident,) if by_number and ident in english else (orig, com, ident)):
            a = ALIAS.get(bridge.keyify(cand or ''))
            if a: ident = a; break
        rows.append({'occ': occ, 'orig': orig, 'lit': lit, 'com': com, 'src': src,
                     'wit': wit, 'ident': ident,
                     'eng': english.get(ident) or (com if com != ident else '') or ''})
    return rows

GROUPED = {}      # normalised title -> first surface form seen, so case/spacing collapse

# Variant English titles for one hymn that the German<->English bridge cannot link,
# because the received titles diverge too far ("Bless" vs "Praise thy Maker").
# Deliberately excluded: 'Veni creator Spiritus' vs 'Komm, Heiliger Geist, Herre Gott'
# and 'O Jesus Christ, Thy manger is' vs 'O Jesus Christ, all praise to Thee' --
# those are genuinely different hymns.
_ALIAS_SRC = {
 'Lord Jesus Christ, I call to Thee':        'Ich ruf zu dir, Herr Jesu Christ',
 'If God Were Not Upon Our Side':            'Wo Gott der Herr nicht bei uns hält',
 'My Soul, Now Bless Thy Maker':             'Nun lob, mein Seel, den Herren',
 'My Soul, Now Praise Thy Maker':            'Nun lob, mein Seel, den Herren',
 # Herrnschmidt's "Lobe den Herren, o meine Seele" (TLH 26, LSB 797), not Gramann's "Nun lob,
 # mein Seel": the Hymn of the Day table's title of it, cut short, and Krusemark's
 'Praise the Almighty, My Soul, Adore':      'Praise the Almighty, My Soul, Adore Him',
 'Praise the Almighty, my soul, adore Him!': 'Praise the Almighty, My Soul, Adore Him',
 # the Hymn of the Day table's titles of two hymns the lexicon lacks, which Krusemark's rows
 # take by the index's titles
 'Soul, Adorn Thyself with Gladness':       'Soul, Adorn Yourself with Gladness',
 'One Thing’s Needful, Lord This Treasure': "One Thing's Needful",
 'Our Father, who from heaven above':        'Vater unser im Himmelreich',
 'Our Father, Thou in Heaven Above':         'Vater unser im Himmelreich',
 'Why art thou cast down, my heart?':        'Warum betrübst du dich, mein Herz',
 'Lord, to You I make confession':           'Lord, to Thee I Make Confession',
 'O Lord Our God, Thy Holy Word':            'O Herre Gott, dein göttlich Wort',
 'O Lord God, Thy Divine Word':              'O Herre Gott, dein göttlich Wort',
 'Menschen kind merck eben':                 'Menschenkind, merk eben',
 'Jr lieben Christen frewdt euch nu':        'Ihr lieben Christen, freut euch nun',
 'O Lord, how shall I meet Thee':            'Wie soll ich dich empfangen',
 'We praise You, Jesus, at Your birth':      'Gelobet seist du, Jesu Christ',
 'We Praise Thee, Jesus, at Thy Birth':      'Gelobet seist du, Jesu Christ',
 'Weltlich ehr vnd zeitlich gut':            'Weltlich Ehr und zeitlich Gut',
 'By Adam\'s Fall Is All Forlorn':            'Durch Adams Fall ist ganz verderbt',
 'By Adam\'s fall man\'s frame entire':       'Durch Adams Fall ist ganz verderbt',
 'Te Deum laudamus':                         'Herr Gott, dich loben wir',
}
# keyed through the same normaliser the lookup uses, or nothing would ever match
ALIAS = {bridge.keyify(k): v for k, v in _ALIAS_SRC.items()}

def style_header(ws, ncols, row=1):
    for c in range(1, ncols + 1):
        cell = ws.cell(row=row, column=c)
        cell.fill, cell.font = HDR_FILL, HDR_FONT
        cell.alignment = Alignment(vertical='center', wrap_text=True)
    ws.row_dimensions[row].height = 30
    ws.freeze_panes = ws.cell(row=row + 1, column=2)

def main():
    rows = load()
    occasions = sorted({r['occ'] for r in rows}, key=sort_key)
    witnesses = sorted({r['wit'] for r in rows})
    wb = Workbook()

    # ---------------- Read me ----------------
    ws = wb.active; ws.title = 'Read me'
    notes = [
        ('Sehling Corpus — chief hymn (Hauptlied) prescriptions', TITLE),
        ('', BODY),
        (f'{len(rows):,} prescriptions · {len(occasions)} occasions · {len(witnesses)} witnesses', BOLD),
        ('Generated from hymns.db. Rebuild with hymn_tables/export_xlsx.py.', BODY),
        ('Counts are computed at export time, not by live formulas — re-run the exporter after changing the database.', BODY),
        ('', BODY),
        ('Sheets', BOLD),
        ('Compare by day — every hymn proposed for each day, with how many witnesses back it. Start here.', BODY),
        ('Matrix — one row per day, one column per witness.', BODY),
        ('All prescriptions — the full table, one row per prescription, with autofilter.', BODY),
        ('Witnesses — who each witness is, and which document they were read from.', BODY),
        ('', BODY),
        ('Two layers of evidence — do not flatten them', BOLD),
        ('Sehling rows are 16th-c. churches ORDERING what shall be sung.', BODY),
        ('Hymnal and compilation rows are books RECORDING what was sung, sometimes a century later.', BODY),
        ('', BODY),
        ('Things that will bite you', BOLD),
        ('Counting is by WITNESS, not by document. Selnecker is attested by three compilations and counted once.', BODY),
        ('Grouped days exist: some sources give one entry for "Advent 3 & 4" or "Lent 1-3". These are separate rows from the single days.', BODY),
        ('The same hymn can appear under variant English titles ("Bless" vs "Praise thy Maker") and will not always group.', BODY),
        ('Krusemark: only his Hymn-of-the-Day entries are here, not his distribution or closing hymns. A hymn is '
         'identified by the number he gives it (LSB, TLH, WH) in the Lutheran Hymn Index.', BODY),
        ('Hymn of the Week (SBH, 1965): the Service Book and Hymnal\'s hymn of the week, one to each Sunday and festival, '
         'from the index of hymns on the sleeve of the American Lutheran Church\'s records "a Time for Singing", read in '
         'the order of the records (sides 1-6). A hymn is identified by its SBH number in the Lutheran Hymn Index.', BODY),
        ('Lutheran Book of Worship (1978): the starred hymns of its Hymns for the Church Year, its de tempore series, '
         'one witness. Its days, of the three-year lectionary, are placed on this sheet\'s days by their place in the '
         'church year (2 Easter = Quasimodogeniti, 2 Pentecost = Trinity 1, Christ the King = Trinity 27); the source '
         'gives LBW\'s day and the lectionary years (A, B, C) a hymn is starred for. A hymn is identified by its LBW '
         'number in the Lutheran Hymn Index.', BODY),
        ('Te Laudamus (2024): the chief hymns of its table, one witness. Its rows give TL\'s own titles; a hymn is '
         'identified by its TL number in the Lutheran Hymn Index.', BODY),
        ('Thompson: the chief hymns of four lists he transcribes in his dissertation (Antwerp 1567, Annaberg 1579, Eler 1588, '
         'Magdeburg 1632) are four witnesses. Krusemark\'s Thompson column, which tallies these lists with others, is not '
         'loaded, so they are not counted twice.', BODY),
        ('Finnish handbooks (1614, 1629, 1694): the gradual hymns of three Finnish church handbooks, sung between the '
         'Epistle and the Gospel, three witnesses. Their rows give the Finnish titles as printed, with a literal English '
         'gloss; a hymn is named by the German or Latin hymn it translates where the transcription judges the identity '
         'certain or probable, and otherwise by its Finnish title. The Transfiguration takes the 7th Sunday after '
         'Trinity. They are old witnesses, but Appendix 8.A of the book, a table of the German orders and hymnals, '
         'does not count them.', BODY),
        ('Slovak lists (1674, c. 1674-1720): the hymns for the Sundays after Trinity of the register of the Cithara '
         'Sanctorum (Levoča, 1674) and of the manuscript hymnal B III-107, from Peter Ruščin\'s table of 2023, two '
         'witnesses. Their rows give the Czech titles as printed, with a literal English gloss, and name a hymn as the '
         'Finnish rows do. Appendix 8.A does not count them either.', BODY),
        ('Compare by day, column Editorial: "Assigned" marks the hymn the editor assigns to a day the old witnesses leave open '
         '(Quasimodogeniti, Easter Monday, Pentecost Monday) or divide too widely to choose (Quinquagesima, where it is the '
         'hymn with the most witnesses). It is not a witness and is not counted.', BODY),
        ('', BODY),
        ('See HYMN_GUIDE.md in the repository for the full account.', BODY),
    ]
    for i, (text, font) in enumerate(notes, start=1):
        c = ws.cell(row=i, column=1, value=text); c.font = font
    ws.column_dimensions['A'].width = 118

    # ---------------- All prescriptions ----------------
    ws = wb.create_sheet('All prescriptions')
    heads = ['Occasion','Original title','Literal English','Common English title','Source','Witness','Hymn (comparable)']
    ws.append(heads)
    ordered = sorted(rows, key=lambda r: (sort_key(r['occ']), r['wit'], r['ident']))
    for r in ordered:
        ws.append([r['occ'], r['orig'], r['lit'], r['com'], r['src'], r['wit'], r['ident']])
    style_header(ws, len(heads))
    for w, col in zip([30, 42, 40, 40, 62, 34, 40], 'ABCDEFG'):
        ws.column_dimensions[col].width = w
    for row in ws.iter_rows(min_row=2, max_row=ws.max_row, max_col=len(heads)):
        for c in row: c.font = BODY; c.alignment = Alignment(vertical='top', wrap_text=False)
    ws.auto_filter.ref = f'A1:{get_column_letter(len(heads))}{ws.max_row}'

    # ---------------- Compare by day ----------------
    last_data = len(rows) + 1          # last row of 'All prescriptions'
    ws = wb.create_sheet('Compare by day', 1)
    heads = ['Occasion','Hymn','English title','Witnesses','Who','Editorial']
    ws.append(heads)
    by = collections.defaultdict(lambda: collections.defaultdict(set))
    edit = {(o, h) for o, h, _n in EDITORIAL}
    for o, h, _n in EDITORIAL:      # an assigned hymn is listed even without a witness
        by[o][h]
    eng = {}
    for r in rows:
        by[r['occ']][r['ident']].add(r['wit'])
        if r['eng']: eng.setdefault(r['ident'], r['eng'])
    band, rownum = False, 2
    for occ in occasions:
        items = sorted(by[occ].items(), key=lambda kv: (-len(kv[1]), kv[0]))
        band = not band
        for ident, wits in items:
            ws.cell(row=rownum, column=1, value=occ)
            ws.cell(row=rownum, column=2, value=ident)
            ws.cell(row=rownum, column=3, value=eng.get(ident, ''))
            # computed at export rather than as a formula: this runtime's LibreOffice
            # cannot load xlsx, so formulas could not be recalculated, and openpyxl
            # writes them with no cached value -- they would read as blank everywhere
            # except Excel itself.
            ws.cell(row=rownum, column=4, value=len(wits))
            ws.cell(row=rownum, column=5, value='; '.join(sorted(wits)))
            if (occ, ident) in edit:
                ws.cell(row=rownum, column=6, value='Assigned')
            for col in range(1, 7):
                cell = ws.cell(row=rownum, column=col)
                cell.font = BOLD if (col <= 2 and (len(wits) >= 3 or (occ, ident) in edit)) else BODY
                cell.alignment = Alignment(vertical='top', wrap_text=(col == 5))
                cell.border = Border(bottom=THIN)
                if band: cell.fill = ALT_FILL
            rownum += 1
    style_header(ws, len(heads))
    ws.freeze_panes = 'C2'          # keep occasion and hymn in view while reading Who
    for w, col in zip([30, 40, 38, 11, 78, 12], 'ABCDEF'):
        ws.column_dimensions[col].width = w
    ws.auto_filter.ref = f'A1:F{ws.max_row}'

    # ---------------- Matrix ----------------
    ws = wb.create_sheet('Matrix', 2)
    ws.append(['Occasion', 'Witnesses'] + witnesses)
    cells = collections.defaultdict(list)
    for r in rows:
        if r['ident'] not in cells[(r['occ'], r['wit'])]:
            cells[(r['occ'], r['wit'])].append(r['ident'])
    for i, occ in enumerate(occasions, start=2):
        ws.cell(row=i, column=1, value=occ).font = BOLD
        n_wit = sum(1 for w in witnesses if cells.get((occ, w)))
        ws.cell(row=i, column=2, value=n_wit).font = BODY
        for j, w in enumerate(witnesses, start=3):
            v = cells.get((occ, w))
            if v:
                c = ws.cell(row=i, column=j, value='\n'.join(v))
                c.font = BODY
                c.alignment = Alignment(vertical='top', wrap_text=True)
    style_header(ws, 2 + len(witnesses))
    ws.freeze_panes = 'C2'          # keep the occasion and its count in view
    ws.column_dimensions['A'].width = 30
    ws.column_dimensions['B'].width = 11
    for j in range(3, 3 + len(witnesses)):
        ws.column_dimensions[get_column_letter(j)].width = 34

    # ---------------- Witnesses ----------------
    ws = wb.create_sheet('Witnesses', 4)
    heads = ['Witness','Prescriptions','Read from (compilation)','Layer']
    ws.append(heads)
    meta = {}
    for r in rows:
        via = r['src'].split(' (via ')[1].rstrip(')') if ' (via ' in r['src'] else '(direct)'
        meta.setdefault(r['wit'], set()).add(via)
    for i, w in enumerate(sorted(meta), start=2):
        layer = 'Sehling church order' if w.startswith('Sehling') else 'Hymnal / compilation'
        ws.cell(row=i, column=1, value=w).font = BODY
        ws.cell(row=i, column=2, value=sum(1 for r in rows if r['wit'] == w)).font = BODY
        ws.cell(row=i, column=3, value=' | '.join(sorted(meta[w]))).font = BODY
        ws.cell(row=i, column=4, value=layer).font = BODY
        ws.cell(row=i, column=3).alignment = Alignment(wrap_text=True, vertical='top')
    style_header(ws, len(heads))
    for w_, col in zip([46, 14, 72, 22], 'ABCD'):
        ws.column_dimensions[col].width = w_
    ws.auto_filter.ref = f'A1:D{ws.max_row}'

    wb.save(OUT)
    print('wrote', OUT)
    print(f'  Compare by day: {len(rows)} prescriptions grouped into hymn/day pairs')
    print(f'  Matrix: {len(occasions)} occasions x {len(witnesses)} witnesses')

if __name__ == '__main__':
    main()
