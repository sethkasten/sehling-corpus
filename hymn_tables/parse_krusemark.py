# -*- coding: utf-8 -*-
"""Krusemark, 'Hymns ABC' (2018/2020) -- a three-year hymn-selection series
collating seventeen lists for the LSB one-year lectionary.

Layout: four columns per page. A bold 20pt line names the occasion; bold
11pt lines name each list; the remaining 11pt lines are hymn entries.

The Hymn of the Day is marked ONLY by underlining, which is drawn as a thin
filled rectangle rather than stored as a text attribute -- so it is
recovered geometrically, by matching those rules to the spans above them.
Superscripts (stanza and music-system counts) are set at 7pt and dropped.
"""
import re, os, json, sys
import pymupdf

HERE = os.path.dirname(os.path.abspath(__file__))
PDF = os.path.join(HERE, '..', 'Hymns_ABC_Krusemark.pdf')   # committed at the repo root
COMPILATION = 'Krusemark, Hymns ABC (2018)'

# the lists Krusemark collates, per his explanation on pp. 95-96
LISTS = {
 'Stuckwisch','Gehrke','Reuning','Eckardt','LCMS','ELS','SELK','Zion, Detroit','Dietrich',
 'Judisch','Thompson','Gerhardt','Carpzov','Liliencron','Bach','Stiller','Other',
 'Year A','Year B','Year C','LSB Hymnal Committee',
}
# subdivisions inside a list, not witnesses of their own
SUBHEAD = {'Choir', 'Every Year', 'Odd Year', 'Even Year'}
# lists whose every entry is a Hymn of the Day, so nothing is underlined
ALL_HOD = {'Judisch', 'Liliencron', 'SELK'}
WITNESS = {
 'Stuckwisch':'Stuckwisch (sword-in-hat list)',
 'Gehrke':'Gehrke, Planning the Service',
 'Reuning':'Reuning',
 'Eckardt':'Eckardt, The Lutheran Propers',
 'LCMS':'LCMS Synod selections (2016-17)',
 'ELS':'Evangelical Lutheran Hymnary (ELH)',
 'SELK':'SELK hymnal',
 'Zion, Detroit':'Zion, Detroit (2013-14)',
 'Dietrich':'Dietrich (catechetical)',
 'Judisch':'Judisch',
 'Thompson':'Thompson, diss. App. 2 (Ludecus + twelve 16th-c. lists)',
 'Gerhardt':'Paul Gerhardt (1723 collection)',
 'Carpzov':'Carpzov',
 'Liliencron':'Liliencron de tempore plan (c. 1700, via Graff)',
 'Bach':'Bach’s cantata chorales',
 'Stiller':'Stiller (Leipzig/Weissenfels/Dresden, via Stiller)',
 'Other':'Other (unattributed)',
 'LSB Hymnal Committee':'LSB Hymnal Committee',
 'Year A':'Krusemark, Year A', 'Year B':'Krusemark, Year B', 'Year C':'Krusemark, Year C',
}
COLS = [(0, 250), (250, 460), (460, 670), (670, 1000)]   # page is ~792pt wide, 4 columns

HYMN = re.compile(r'^(?P<mark>(?:pc|[iopcs])\s*)?'
                  r'(?P<book>TLH|LSB|WH|ELH|HG|LW|LBW)?\s*'
                  r'(?P<num>\d{1,3}(?:/\d)?)?\s*'
                  r'(?P<title>.+)$')

def col_of(x):
    for i, (a, b) in enumerate(COLS):
        if a <= x < b: return i
    return len(COLS) - 1

def page_entries(page):
    d = page.get_text('dict')
    lines = []
    for b in d['blocks']:
        if b['type'] != 0: continue
        for l in b['lines']:
            spans = [s for s in l['spans'] if s['text'].strip()]
            if not spans: continue
            # 7pt spans are superscript stanza/system counts
            txt = ''.join(s['text'] for s in spans if s['size'] > 8.5)
            if not txt.strip(): continue
            big = max(spans, key=lambda s: s['size'])
            lines.append({'text': re.sub(r'\s+', ' ', txt).strip(),
                          'bbox': l['bbox'], 'size': round(big['size'], 1),
                          'bold': 'Bold' in big['font']})
    rules = [it['rect'] for it in page.get_drawings()
             if it['type'] == 'f' and (it['rect'][3] - it['rect'][1]) < 2.0
             and (it['rect'][2] - it['rect'][0]) > 12]
    for ln in lines:
        x0, y0, x1, y1 = ln['bbox']
        ln['underlined'] = any(abs(r[1] - y1) < 4.0 and r[0] < x1 - 4 and r[2] > x0 + 4
                               for r in rules)
        ln['col'] = col_of(x0)
    lines.sort(key=lambda l: (l['col'], l['bbox'][1]))
    return lines

def clean_title(t):
    t = re.sub(r'\s*\d+(?:[-–,]\d+)*\s*$', '', t)        # trailing stanza digits
    t = re.sub(r'^\s*(cf\.|sts?\.)\s*', '', t)
    return t.strip(' .,')

def parse():
    doc = pymupdf.open(PDF)
    rows, occ, lst = [], None, None
    prev_head = None          # (col, y1) of the last occasion-heading line
    for pno in range(doc.page_count):
        for ln in page_entries(doc[pno]):
            t = ln['text']
            if not t or t.startswith('cf.') or re.match(r'^sts?\.', t): continue
            if ln['size'] >= 15 and ln['bold']:
                # a heading that wraps continues the one just above it
                if (prev_head and prev_head[0] == ln['col']
                        and 0 < ln['bbox'][1] - prev_head[1] < 34):
                    occ = (occ + ' ' + t).strip()
                else:
                    occ = t; lst = None
                prev_head = (ln['col'], ln['bbox'][3])
                continue
            prev_head = None
            if t in SUBHEAD: continue          # keeps the current list
            if t in LISTS:
                lst = t; continue
            if not occ or not lst: continue
            m = HYMN.match(t)
            if not m: continue
            title = clean_title(m.group('title') or '')
            if len(title) < 5 or title in LISTS: continue
            rows.append({'occasion_raw': occ, 'list': lst, 'witness': WITNESS[lst],
                         'book': m.group('book') or ('LSB' if m.group('num') else None),
                         'number': m.group('num'), 'title': title,
                         'mark': (m.group('mark') or '').strip() or None,
                         'hod': ln['underlined'] or lst in ALL_HOD, 'page': pno + 1})
    return rows

if __name__ == '__main__':
    r = parse()
    hod = [x for x in r if x['hod']]
    print(f'{len(r)} entries | {len(hod)} marked Hymn of the Day | '
          f'{len({x["occasion_raw"] for x in r})} occasions | {len({x["list"] for x in r})} lists')
    json.dump(r, open(os.path.join(HERE, 'rows_krusemark_raw.json'), 'w'),
              ensure_ascii=False, indent=1)
    for x in r[:14]:
        print(f'  {"HOD" if x["hod"] else "   "} {x["occasion_raw"][:22]:<22} | {x["list"][:12]:<12} | '
              f'{(x["book"] or ""):<4} {(x["number"] or ""):<5} {x["title"][:40]}')
