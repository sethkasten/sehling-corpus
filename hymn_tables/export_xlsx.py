# -*- coding: utf-8 -*-
"""Export hymns.db to an Excel workbook for comparing chief-hymn choices by day."""
import sqlite3, re, os, sys, unicodedata, collections
from openpyxl import Workbook
from openpyxl.styles import Font, Alignment, PatternFill, Border, Side
from openpyxl.utils import get_column_letter
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import bridge

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
        if not ident:
            key = (orig, com)
            if key not in cache:
                c, _l, _c, _how = bridge.identify(orig, com)
                cache[key] = c
            ident = cache[key]
        if not ident:                       # unresolved: group on the normalised title
            ident = (com or orig or '').strip()
            ident = GROUPED.setdefault(norm(ident), ident)
        for cand in (orig, com, ident):     # fold known variant titles together
            a = ALIAS.get(bridge.keyify(cand or ''))
            if a: ident = a; break
        rows.append({'occ': occ, 'orig': orig, 'lit': lit, 'com': com, 'src': src,
                     'wit': wit, 'ident': ident,
                     'eng': english.get(ident) or com or ''})
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
 'Praise the Almighty, my soul, adore Him!': 'Nun lob, mein Seel, den Herren',
 'Our Father, who from heaven above':        'Vater unser im Himmelreich',
 'Our Father, Thou in Heaven Above':         'Vater unser im Himmelreich',
 'Why art thou cast down, my heart?':        'Why Art Thou Thus Cast Down, My Heart',
 'Lord, to You I make confession':           'Lord, to Thee I Make Confession',
 'O Lord Our God, Thy Holy Word':            'O Herre Gott, dein göttlich Wort',
 'O Lord God, Thy Divine Word':              'O Herre Gott, dein göttlich Wort',
 'Menschen kind merck eben':                 'Menschenkind, merk eben',
 'Jr lieben Christen frewdt euch nu':        'Ihr lieben Christen, freut euch nun',
 'O Lord, how shall I meet Thee':            'O Lord, How Shall I Meet You',
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
        ('Krusemark: only his Hymn-of-the-Day entries are here, not his distribution or closing hymns.', BODY),
        ('Thompson\'s column collates Ludecus with twelve other 16th-c. lists and cannot be deduplicated against the Ludecus rows.', BODY),
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
    heads = ['Occasion','Hymn','English title','Witnesses','Who']
    ws.append(heads)
    by = collections.defaultdict(lambda: collections.defaultdict(set))
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
            for col in range(1, 6):
                cell = ws.cell(row=rownum, column=col)
                cell.font = BOLD if (col <= 2 and len(wits) >= 3) else BODY
                cell.alignment = Alignment(vertical='top', wrap_text=(col == 5))
                cell.border = Border(bottom=THIN)
                if band: cell.fill = ALT_FILL
            rownum += 1
    style_header(ws, len(heads))
    ws.freeze_panes = 'C2'          # keep occasion and hymn in view while reading Who
    for w, col in zip([30, 40, 38, 11, 78], 'ABCDE'):
        ws.column_dimensions[col].width = w
    ws.auto_filter.ref = f'A1:E{ws.max_row}'

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
