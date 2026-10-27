#!/usr/bin/env python3
"""Write clean links and Walther's Hymnal titles back into the spreadsheets.

Usage: python3 write_back.py [--add CODE] [--merge-kelg N,N,...]

1. Rebuilds hymnal.db from the spreadsheets.
2. KELG-Hymn-Index.xlsx: fills the empty 'Walther's Hymnal (2012)' cells
   (column S) with each hymn's English first line in WH (wh_index.csv).
3. Lutheran Hymn Index.xlsx (the master index):
   - renames the columns in RENAMED_COLUMNS (KELG German Title is now
     KELG/ELGBS German Title), takes out the columns in REMOVED_COLUMNS
     (ELGBS#: ELGBS numbers its hymns as LPC does, and its German first lines
     are in the database) and adds the hymnal columns in ADDED_COLUMNS it
     lacks yet (TL#, LPC#, WS'69#, WS'00#); with --add CODE, also the column
     of the hymnal taken from Hymnary.org that CODE names (ACS, AH, ... in
     build_db.HYMNARY_CSVS). Add those one at a time, in that order, settling
     each one's links in link_review.csv before adding the next: a hymn new to
     the master index then gets one row, from the first of them to have it,
     and the hymnals after it find it there. An added column goes after the
     nearest column before it in HYMNAL_ORDER that the sheet has; columns are
     otherwise found by their headers in row 1, wherever they are;
   - fills the empty KELG#, TLHy#, ELHB#, TL#, LPC#, Hymnary.org hymnals'
     (WS'69#, WS'00#, ACS#, ...) and
     KELG/ELGBS German Title cells of existing rows from links with status
     'ok' (the German title is KELG's, or for a hymn of ELGBS's house hymnal
     on a row with no KELG hymn, ELGBS's first line). A
     number cell that already holds a value changes only by a decision in
     link_decisions.csv: a 'match' adds its number and a 'no match' takes its
     number out (emptying the cell if nothing is left). Other disagreements
     show up in link_review.csv instead;
   - corrects the hymnal numbers and titles listed in master_corrections.csv:
     a number cell holding the old numbers gets the new ones in their place
     (new left empty: taken out), a title or KELG/ELGBS German Title the old
     one is replaced (an 'alternate' line, an Alternative English Title to
     add, waits for the hymnals' titles below);
   - fills Original Title and Original Language for rows with a TLHy or TL
     hymn that isn't a KELG or ELGBS hymn, from tlhy_originals.csv and
     tl_originals.csv (the language alone when only that is known; ELGBS's
     first lines, which went there before, come out), and Other English Title
     and Other English Source for KELG hymns WH lacks, from kelg_english.csv;
   - retitles rows still titled in German with the hymn's WH English title,
     or for a hymn WH lacks, its English translation in kelg_english.csv
     (which stays in Other English Title, beside its source);
   - adds a row for every KELG, ELHB, TLHy, TL, LPC and Hymnary.org hymnal's
     hymn that has no row yet (a TLHy, TL, LPC or Hymnary.org hymn only when
     nothing matched it, not even a link left for review; TL numbers sharing
     a title share a row: '202, 203', and so do a Hymnary.org hymnal's numbers
     sharing an English first line: WS69's parts of one hymn, '718a, 718b', or
     SBH's text printed with two tunes, '20a, 20b'). A Hymnary.org hymn's row
     is titled with its English first line;
   - with --merge-kelg, merges each listed KELG hymn's own row (titled in
     German or with its English title, and holding nothing but the KELG number)
     into the row(s) the hymn was matched to (a clean link, or a 'WH first
     line' link in link_review.csv): the KELG number and German title move
     there and the hymn's own row is deleted.
   New and retitled rows go in alphabetical position.
   Once those are written:
   - merges the rows same_hymn_decisions.csv calls one hymn: the row titled
     with the decision's master_title keeps its title and gets the others'
     numbers ('297' and '298' make '297, 298'), their texts where its own are
     empty (both, joined, where they differ), and their titles as Alternative
     English Titles; the others are deleted;
   - then adds to each row's Alternative English Titles the ones
     master_corrections.csv gives it ('alternate'), and the English titles the
     hymnals give it through clean links (WH, TLHy, ELHB, TL, LPC, the TLH,
     LW, ELH and LSB titles of tlh_1941.csv and the KELG index, and the
     Hymnary.org hymnals' English first lines: WS69, WS00, ACS, ...) that no other
     row bears and that differ from its title and the alternatives it has in
     Thee/You wording ('I Call to Thee' beside 'I Call to You') or in other
     words altogether, not just in spelling, punctuation or a scanning error,
     and that aren't the start of one of them (new_wording). Alternatives are
     only ever added, so ones typed in by hand stay; only one that repeats
     the row's title (as after a retitle) is taken out. 'Alternative English
     Title N' columns are added at the end of the sheet as rows need them.
   A new cell takes the style most of its column's cells have.
4. Rebuilds hymnal.db again, and repeats step 3 while that turns up more
   (rows that now share a number with another count as the same hymn).

Safe to re-run: once written, links count as 'already in master index' and
nothing is written twice.

The worksheet XML is edited in place (instead of round-tripping through
openpyxl) so that the header/footer image, styles and print settings survive.
"""
import argparse
import bisect
import difflib
import re
import shutil
import sqlite3
import unicodedata
import zipfile
from collections import Counter, defaultdict

from lxml import etree

import build_db
from build_db import (ALT_CORRECTION, ALT_TITLE_HEADER, ALT_TITLE_RE, DB_PATH, ELHB_TITLE_FIXES,
                      GERMAN_CORRECTION, GERMAN_TITLE_HEADER, HYMNALS, HYMNARY_CSVS, KELG_SHEET,
                      KELG_WH_TITLE_COLUMN, KELG_WH_TITLE_HEADER, KELG_XLSX, LCMS_XLSX, LETTERED_HYMNALS,
                      LINKED_HYMNALS, MASTER_CORRECTIONS_CSV, SAME_HYMN_CSV, TEXT_COLUMNS, TITLE_CORRECTION,
                      TRUSTED, hymnary_titles, is_prefix, link_number, match_key, number_order, parse_cell,
                      read_csv, read_same_hymn_decisions, same_hymn_groups, title_rows, titled_rows, tl_titles)

NS = "http://schemas.openxmlformats.org/spreadsheetml/2006/main"
N = f"{{{NS}}}"
SHEET = "xl/worksheets/sheet1.xml"  # the first sheet in both workbooks
STRINGS = "xl/sharedStrings.xml"
WORKBOOK = "xl/workbook.xml"

# Master-index columns are found by their headers (row 1); these must be there.
# A new cell takes the style most of its column's cells have (TEXT_STYLE in a
# column with none yet).
REQUIRED_COLUMNS = ("HYMN TITLE", "Text", "KELG#", "LPC#", "ELHB#", "TLH#", "WS'69#", "LW#", "LSB#", "TLHy#",
                    "ELH#", "WS'00#", "TL#", *TEXT_COLUMNS)
TEXT_STYLE = "6"
TEXT_WIDTHS = dict(zip(TEXT_COLUMNS, (34, 34, 12, 34, 28)))
ALT_WIDTH = 34  # the 'Alternative English Title N' columns
# The master index's hymnal columns in the order write_back.py places them: a
# column it adds goes right after the nearest one before it here that the sheet
# has, and gets that column's width and its cells' styles. The sheet's order,
# with each hymnal from Hymnary.org beside its church's: AH after the Norwegian
# synods' TLHy and ELH; LH after TL, which draws on it; the hymnals of the bodies
# that became the ALC and LCA (and so the ELCA), oldest first, before the ELCA's
# own LBW; ELW and ACS after.
HYMNAL_ORDER = ("KELG#", "LPC#", "ELHB#", "TLH#", "WS'69#", "LW#", "HS'98#", "LSB#", "TLHy#", "TCH#", "ELH#",
                "AH#", "CW'21#", "CWS#", "CW'93#", "WS'00#", "TL#", "LH#", "ELHal#", "ALH#", "THOS#", "HCH#",
                "CHL#", "CHPPPW#", "TBW'67#", "TCSSH#", "TBW'07#", "CSB#", "SBH#", "LBW#", "HS'91#", "WOV#",
                "ELW#", "ACS#")
# Hymnal columns added whenever the master index lacks them. (A Hymnary.org
# hymnal's column comes with --add CODE.)
ADDED_COLUMNS = ("TL#", "LPC#", "WS'69#", "WS'00#")
# Columns taken out of the master index. ELGBS numbers its house hymnal as LPC
# does (LPC translates it), so ELGBS# only repeated LPC#; the German first lines
# are in elgbs_lpc_hymns.csv (and in the KELG/ELGBS German Title column).
REMOVED_COLUMNS = ("ELGBS#",)
# Columns renamed: old header -> new. ELGBS's house hymnal is a supplement to KELG
# in all but name, so the German title column has its German first lines too.
RENAMED_COLUMNS = {"KELG German Title": GERMAN_TITLE_HEADER}
# Sources of the alternative titles step 3 adds, in this order (hymn_titles), and
# the hymnal whose link brings each: a title comes only with a clean link (none of
# that hymnal's links on the row left for review). TLH's titles come with the
# row's own TLH numbers; LSB's, LW's and ELH's with KELG's (the KELG index); the
# Hymnary.org hymnals' English first lines with their own numbers.
ALT_SOURCES = {"WH": "KELG", "TLHy": "TLHy", "ELHB": "ELHB", "TL": "TL", "LPC": "LPC",
               "LSB": "KELG", "TLH": None, "LW": "KELG", "ELH": "KELG", **{code: code for code in HYMNARY_CSVS}}
HEADER_STYLE = "4"
MAX_ROUNDS = 12  # write_back.py's rounds of writing and rebuilding
ROW_ATTRS = {"ht": "12.5", "{http://schemas.microsoft.com/office/spreadsheetml/2009/9/ac}dyDescent": "0.25"}


def sort_key(title):
    """Approximates Excel's sort: case- and accent-insensitive, ignoring apostrophes and hyphens."""
    text = unicodedata.normalize("NFKD", title)
    text = "".join(c for c in text if not unicodedata.combining(c))
    return re.sub(r"['’\-]", "", text.lower())


def format_numbers(nums):
    """A number cell: 241 (a number), '157a', or '202, 203'."""
    nums = sorted(nums, key=number_order)
    return nums[0] if len(nums) == 1 else ", ".join(str(n) for n in nums)


class Layout:
    """The master index's columns, from its header row ({header: column letter}),
    and the style of a new cell in each ({column letter: style})."""

    def __init__(self, headers, styles):
        missing = [h for h in REQUIRED_COLUMNS if h not in headers]
        if missing:
            raise SystemExit(f"{LCMS_XLSX.name}: no column headed {', '.join(missing)}")
        self.col = {HYMNALS[h][0]: c for h, c in headers.items() if h in HYMNALS}  # 'TL' -> 'F'
        self.text = {h: headers[h] for h in TEXT_COLUMNS}
        self.german, self.original, self.language, self.other_english, self.other_source = self.text.values()
        self.scripture = headers["Text"]
        # 'Alternative English Title 1', '... 2', ... in order
        self.alternates = [c for _, c in sorted((int(ALT_TITLE_RE.match(h).group(1)), c)
                                                 for h, c in headers.items() if ALT_TITLE_RE.match(h))]
        self.styles = {c: styles.get(c, TEXT_STYLE) for c in headers.values()}
        self.last = max(headers.values(), key=col_index)
        self.spans = f"1:{col_index(self.last)}"


def format_ref(raw):
    """A KELG-index number cell in master-index style: '569 + 535' -> '535, 569', 'p223' -> 'p. 223'."""
    parsed = parse_cell(raw)
    nums = sorted(f"{n}{suffix}" for n, suffix, _ in parsed)
    if parsed[0][2]:
        return "p. " + ",".join(nums)
    return int(nums[0]) if len(nums) == 1 and nums[0].isdigit() else ", ".join(nums)


# --- deciding what to write -------------------------------------------------

def plan_wh_titles(con):
    """{kelg_number: WH English first line} for KELG index rows still missing one."""
    wh = {n: (english, see) for n, english, see in con.execute(
        "SELECT number, english_first_line, see_number FROM wh_hymns")}
    out = {}
    for (number,) in con.execute("SELECT number FROM kelg_hymns WHERE wh_title IS NULL"):
        english, see = wh.get(number, (None, None))
        if not english and see:
            english = wh[see][0]  # printed only as 'See # n.'
        if english:
            out[number] = english
    return out


def plan(con, layout, merge_kelg=()):
    """Returns (cell updates {hymn_id: {col: value}}, new rows [{col: value}],
    retitles {hymn_id: title}, deleted row ids)."""
    COL = layout.col
    master = defaultdict(set)
    for hymn_id, code in con.execute("SELECT hymn_id, hymnal_code FROM hymn_cells"):
        master[hymn_id].add(code)
    german_done = {h for (h,) in con.execute("SELECT id FROM hymns WHERE german_title IS NOT NULL")}
    german = dict(con.execute("SELECT number, german_title FROM kelg_hymns"))
    elgbs = dict(con.execute("SELECT number, german_first_line FROM elgbs_lpc_hymns"))  # by LPC number
    wh_titles = {n: t for n, t in con.execute("SELECT number, wh_title FROM kelg_hymns") if t}
    # an English translation of a KELG hymn WH lacks (kelg_english.csv)
    english_titles = dict(con.execute("SELECT kelg_number, title FROM kelg_english"))

    # The KELG, TLHy, ELHB, TL and LPC numbers each row should have: the
    # ones it has, less those link_decisions.csv rejected, plus every clean link. A
    # TL number keeps its letter ('157a'); a lettered number anywhere else, or
    # a page number, is left for a person to change.
    have, lettered = defaultdict(set), set()
    for hymn_id, code, n, suffix, is_page in con.execute(
        "SELECT hymn_id, hymnal_code, number, suffix, is_page FROM hymn_numbers WHERE hymnal_code IN ({})".format(
            ", ".join(f"'{c}'" for c in LINKED_HYMNALS))
    ):
        if code in LETTERED_HYMNALS:
            n = link_number(n, suffix)
        elif suffix:
            lettered.add((hymn_id, code))
        have[hymn_id, code].add(n)
        if is_page:
            lettered.add((hymn_id, code))
    want = defaultdict(set, {key: set(nums) for key, nums in have.items()})
    ok = defaultdict(set)
    for hymn_id, code, number, status in con.execute(
        "SELECT hymn_id, hymnal_code, number, status FROM links WHERE status IN ('ok', 'rejected')"
    ):
        if status == "ok":
            ok[hymn_id, code].add(number)
            want[hymn_id, code].add(number)
        else:
            want[hymn_id, code].discard(number)

    # A KELG hymn's own row (titled in German, or with its English title: WH's,
    # else kelg_english.csv's) is retitled with that English title, or with
    # --merge-kelg merged into the row(s) the hymn was matched to.
    deletes, retitles = set(), {}
    german_rows, own_rows = defaultdict(list), defaultdict(list)
    for hymn_id, title, german_title, kelg in con.execute(
        "SELECT id, title, german_title, KELG FROM hymn_index WHERE KELG IS NOT NULL"
    ):
        for n, _, _ in parse_cell(kelg):
            if title == german_title:
                german_rows[n].append(hymn_id)
            if title in (german_title, wh_titles.get(n), english_titles.get(n)):
                own_rows[n].append(hymn_id)
    for n in merge_kelg:
        if not own_rows.get(n):
            raise SystemExit(f"--merge-kelg {n}: no row with KELG {n} is titled with its German or English title")
        targets = {h for (h,) in con.execute(
            "SELECT hymn_id FROM links WHERE hymnal_code = 'KELG' AND number = ? AND status != 'rejected' "
            "AND (status = 'ok' OR method = 'WH first line')", (n,))} - set(own_rows[n])
        if not targets:
            raise SystemExit(f"--merge-kelg {n}: no other row to merge into")
        for hymn_id in own_rows[n]:
            leftovers = set(master[hymn_id]) - {"KELG"}
            if leftovers:
                raise SystemExit(f"--merge-kelg {n}: row {hymn_id} also has {', '.join(sorted(leftovers))}")
            deletes.add(hymn_id)
        for hymn_id in targets:
            want[hymn_id, "KELG"].add(n)
            ok[hymn_id, "KELG"].add(n)
    for n, ids in german_rows.items():
        new_title = wh_titles.get(n) or english_titles.get(n)
        if new_title:
            for hymn_id in set(ids) - deletes:
                retitles[hymn_id] = new_title

    updates = defaultdict(dict)
    for (hymn_id, code), nums in want.items():
        if hymn_id in deletes or nums == have.get((hymn_id, code), set()):
            continue
        if (hymn_id, code) in lettered:
            raise SystemExit(f"row {hymn_id}: its {code} cell has a lettered or page number; change it by hand")
        updates[hymn_id][COL[code]] = format_numbers(nums) if nums else None
    def has(hymn_id, code):
        return bool(want.get((hymn_id, code)) or ok.get((hymn_id, code)))

    # The German title: KELG's, or for a hymn of ELGBS's house hymnal (LPC's
    # numbers; a supplement to KELG in all but name) on a row with no KELG hymn,
    # ELGBS's first line.
    for (hymn_id, code), nums in list(ok.items()):
        if hymn_id in german_done | deletes:
            continue
        if code == "KELG":
            updates[hymn_id][layout.german] = " / ".join(dict.fromkeys(german[n] for n in sorted(nums)))
        elif code == "LPC" and not has(hymn_id, "KELG"):
            updates[hymn_id][layout.german] = " / ".join(dict.fromkeys(elgbs[n] for n in sorted(nums)))
    # The German title of a KELG or ELGBS hymn a decision took off a row goes with it.
    german_titles = set(german.values()) | set(elgbs.values())
    for hymn_id, title in con.execute("SELECT id, german_title FROM hymns WHERE german_title IS NOT NULL"):
        if (hymn_id not in deletes and not has(hymn_id, "KELG") and not has(hymn_id, "LPC")
                and all(t in german_titles for t in title.split(" / "))):
            updates[hymn_id][layout.german] = None
    corrections, corrected_titles = plan_corrections(con, layout)
    for hymn_id, cells in corrections.items():
        updates[hymn_id].update(cells)
    retitles.update({h: t for h, t in corrected_titles.items() if h not in deletes})

    linked = defaultdict(set)
    for code, number in con.execute("SELECT DISTINCT hymnal_code, number FROM links WHERE status != 'rejected'"):
        linked[code].add(number)
    refs = defaultdict(dict)
    for kelg_number, code, raw, title in con.execute(
        "SELECT kelg_number, hymnal_code, COALESCE(fixed, raw), title FROM kelg_refs"
    ):
        refs[kelg_number][code] = (raw, title)
    elhb_titles = dict(con.execute("SELECT number, title FROM elhb_hymns"))

    new_rows, elhb_covered = [], set()
    for kelg_number, german_title in con.execute("SELECT number, german_title FROM kelg_hymns ORDER BY number"):
        if kelg_number in linked["KELG"]:
            continue
        row = {COL["KELG"]: kelg_number, layout.german: german_title}
        title = None
        for code in ("ELHB", "TLH", "LW", "ELH", "LSB"):
            if code not in refs[kelg_number]:
                continue
            raw, ref_title = refs[kelg_number][code]
            row[COL[code]] = format_ref(raw)
            title = title or ref_title
            if code == "ELHB":
                elhb_covered |= {n for n, _, _ in parse_cell(raw)}
        row["A"] = title or wh_titles.get(kelg_number) or english_titles.get(kelg_number) or german_title
        new_rows.append(row)
    for n, title in sorted(elhb_titles.items()):
        if n in linked["ELHB"] or n in elhb_covered:
            continue
        new_rows.append({"A": ELHB_TITLE_FIXES.get(n, title), COL["ELHB"]: n})

    # TLHy and TL hymns: originals (tlhy_originals.csv, tl_originals.csv) for
    # rows that aren't KELG hymns, and a new row for each hymn nothing matched.
    done = {h: (t, l) for h, t, l in con.execute("SELECT id, original_title, original_language FROM hymns")}
    # Rows of a KELG or ELGBS hymn have its German in the KELG/ELGBS German Title column
    # and no original; ELGBS's first lines, which went in Original Title before, come out.
    row_german = {h for (h,) in con.execute(
        "SELECT hymn_id FROM hymn_numbers WHERE hymnal_code IN ('KELG', 'LPC') "
        "UNION SELECT hymn_id FROM links WHERE hymnal_code IN ('KELG', 'LPC') AND status = 'ok'")}
    elgbs_lines = set(elgbs.values())
    for hymn_id, (title, language) in done.items():
        if (hymn_id in row_german and hymn_id not in deletes and title and language in (None, "German")
                and all(t in elgbs_lines for t in title.split(" / "))):
            updates[hymn_id][layout.original] = None
            updates[hymn_id][layout.language] = None
    filled = set()  # rows given an original here, by TLHy before TL

    def originals_of(code, table):
        """{number: (original title or None if not trusted, language)} for translations."""
        out = {}
        for n, title, language, confidence in con.execute(
            f"SELECT number, original_title, language, confidence FROM {table} "
            "WHERE language IS NOT NULL AND language != 'English'"
        ):
            out[n] = (title if confidence in TRUSTED else None, language)
        return out

    def fill_originals(code, originals):
        row_numbers = defaultdict(set)
        for hymn_id, n, suffix in con.execute(
            "SELECT hymn_id, number, suffix FROM hymn_numbers WHERE hymnal_code = ?", (code,)
        ):
            row_numbers[hymn_id].add(link_number(n, suffix) if code in LETTERED_HYMNALS else n)
        for hymn_id, n in con.execute(
            "SELECT hymn_id, number FROM links WHERE hymnal_code = ? AND status = 'ok'", (code,)
        ):
            row_numbers[hymn_id].add(n)
        for hymn_id, numbers in row_numbers.items():
            found = [originals[n] for n in sorted(numbers, key=number_order) if n in originals]
            if hymn_id in row_german | filled or not found:
                continue
            titles = " / ".join(dict.fromkeys(t for t, _ in found if t))
            languages = " / ".join(dict.fromkeys(l for _, l in found))
            title_done, language_done = done[hymn_id]
            if titles and not title_done:
                updates[hymn_id][layout.original] = titles
                filled.add(hymn_id)
            if not language_done:
                updates[hymn_id][layout.language] = languages
                filled.add(hymn_id)

    def new_row(title, code, numbers, originals):
        row = {"A": title, COL[code]: format_numbers(numbers)}
        found = [originals[n] for n in sorted(numbers, key=number_order) if n in originals]
        if found:
            row[layout.language] = " / ".join(dict.fromkeys(l for _, l in found))
            titles = " / ".join(dict.fromkeys(t for t, _ in found if t))
            if titles:
                row[layout.original] = titles
        return row

    tlhy_originals = originals_of("TLHy", "tlhy_originals")
    fill_originals("TLHy", tlhy_originals)
    for n, first_line in con.execute(
        "SELECT number, first_line FROM tlhy_index WHERE alternate = 0 ORDER BY number"
    ).fetchall():
        if n not in linked["TLHy"]:
            new_rows.append(new_row(first_line, "TLHy", [n], tlhy_originals))
    tl_originals = originals_of("TL", "tl_originals")
    fill_originals("TL", tl_originals)
    unplaced = defaultdict(list)  # title -> TL numbers: '202, 203' share a row
    for n, titles in sorted(tl_titles(con).items(), key=lambda kv: number_order(kv[0])):
        if n not in linked["TL"]:
            unplaced[titles[0]].append(n)
    for title, numbers in unplaced.items():
        new_rows.append(new_row(title, "TL", numbers, tl_originals))
    lh_originals = originals_of("LH", "lh_originals")  # Liber Hymnorum's Latin
    fill_originals("LH", lh_originals)
    # LPC's hymns, with ELGBS's German first lines as their German titles
    for n, first_line, row_title in con.execute(
        "SELECT number, english_first_line, row_title FROM elgbs_lpc_hymns ORDER BY number"
    ).fetchall():
        if n not in linked["LPC"]:
            row = new_row(row_title or first_line, "LPC", [n], {})
            row[layout.german] = elgbs[n]
            new_rows.append(row)
    # The hymns of the Hymnary.org hymnals the master index has a column for
    # (WS69, WS00, ACS, ...), titled with their English first lines; a hymnal's
    # numbers sharing one share a row (WS69's parts of a hymn, '718a, 718b').
    for code in HYMNARY_CSVS:
        if code not in COL:
            continue
        unplaced = {}  # match_key -> (title, numbers)
        for n, titles in sorted(hymnary_titles(con, code).items(), key=lambda kv: number_order(kv[0])):
            if n not in linked[code]:
                unplaced.setdefault(match_key(titles[0]), (titles[0], []))[1].append(n)
        for title, numbers in unplaced.values():
            new_rows.append(new_row(title, code, numbers, lh_originals if code == "LH" else {}))

    # English translations of KELG hymns WH lacks, on their rows.
    other_done = {h for (h,) in con.execute("SELECT id FROM hymns WHERE other_english_title IS NOT NULL")}
    english = {}
    for k, title, translator, source in con.execute(
        "SELECT kelg_number, title, translator, source FROM kelg_english"
    ):
        english[k] = (title, f"{translator} ({source})" if translator else source)
    kelg_rows = defaultdict(set)
    for hymn_id, n in con.execute(
        "SELECT hymn_id, number FROM hymn_numbers WHERE hymnal_code = 'KELG' "
        "UNION SELECT hymn_id, number FROM links WHERE hymnal_code = 'KELG' AND status = 'ok'"
    ):
        kelg_rows[n].add(hymn_id)
    for k, (title, source) in english.items():
        for hymn_id in kelg_rows[k] - other_done - deletes:
            updates[hymn_id][layout.other_english] = title
            updates[hymn_id][layout.other_source] = source
    return updates, new_rows, retitles, deletes


def plan_corrections(con, layout):
    """From master_corrections.csv: ({hymn_id: {col: value}}, {hymn_id: new title}).

    A number correction takes the old numbers out of the cell and puts the new
    ones in (new left empty: the old ones just go; old left empty: the new ones
    are added). It is done once the cell holds the new numbers and none of the
    old; a cell holding some old numbers but not all is left alone, with a
    warning. A 'title' correction retitles the row still bearing the old title,
    and a 'german' one sets the KELG/ELGBS German Title of the row still
    holding the old one; an 'alternate' one is plan_alternates' to add. Rows
    are found by any title they bear (see title_rows): a correction keeps
    working after its row is merged into another."""
    rows_titled = title_rows(con)
    titles = dict(con.execute("SELECT id, title FROM hymns"))
    germans = dict(con.execute("SELECT id, german_title FROM hymns"))
    cells = {(h, code): raw for h, code, raw in con.execute("SELECT hymn_id, hymnal_code, raw FROM hymn_cells")}

    def numbers(raw, code):
        parsed = parse_cell(raw) if raw else []
        if any(page for _, _, page in parsed):
            raise SystemExit(f"{MASTER_CORRECTIONS_CSV.name}: {code} {raw!r} has page numbers; correct it by hand")
        return {link_number(n, suffix) for n, suffix, _ in parsed}

    out, retitles = defaultdict(dict), {}
    for r in read_csv(MASTER_CORRECTIONS_CSV):
        title, code, old, new = r["master_title"], r["hymnal"], r["old"], r["new"]
        if not rows_titled.get(title):
            raise SystemExit(f"{MASTER_CORRECTIONS_CSV.name}: no master-index row is titled {title!r}")
        if code == ALT_CORRECTION:
            if not new.strip():
                raise SystemExit(f"{MASTER_CORRECTIONS_CSV.name}: an 'alternate' for {title!r} with no title as new")
            continue
        if code not in (TITLE_CORRECTION, GERMAN_CORRECTION) and code not in layout.col:
            raise SystemExit(f"{MASTER_CORRECTIONS_CSV.name}: no column for {code!r} ({title!r})")
        for hymn_id in sorted(rows_titled[title]):
            if code == TITLE_CORRECTION:
                if titles[hymn_id] == old:
                    retitles[hymn_id] = new
                continue
            if code == GERMAN_CORRECTION:
                if (germans[hymn_id] or "") == old:
                    out[hymn_id][layout.german] = new or None
                continue
            raw = cells.get((hymn_id, code))
            have, gone, wanted = numbers(raw, code), numbers(old, code), numbers(new, code)
            want = (have - gone) | wanted
            if want == have:
                continue  # already corrected
            if not gone <= have:
                print(f"{MASTER_CORRECTIONS_CSV.name}: {titles[hymn_id]!r} has {code} {raw!r}, "
                      f"not {old!r}; left alone")
                continue
            out[hymn_id][layout.col[code]] = format_numbers(want) if want else None
    return out, retitles


def merged_numbers(raws, code):
    """One cell for several rows' cells of a hymnal: their numbers together
    ('297' and '298' -> '297, 298'), or their page numbers ('p. 7,11')."""
    parsed = {(n, suffix, page) for raw in raws for n, suffix, page in parse_cell(raw)}
    if all(page for _, _, page in parsed):
        return "p. " + ",".join(sorted({f"{n}{suffix}" for n, suffix, _ in parsed}, key=number_order))
    if any(page for _, _, page in parsed):
        raise SystemExit(f"merging {code} cells {raws}: hymn and page numbers mixed; merge these rows by hand")
    return format_numbers({link_number(n, suffix) for n, suffix, _ in parsed})


def plan_merges(con, layout):
    """Rows same_hymn_decisions.csv calls one hymn, merged. The row titled with
    the decisions' master_title keeps its title and gets: the others' hymnal
    numbers; their texts where its own are empty, or where they differ, both
    (scripture joined with '; ', the rest with ' / '; Other English Title and
    Source kept in pairs); and their titles and alternative titles as its
    Alternative English Titles (one per wording: match_key). The others are
    deleted. Returns (cell updates, {hymn_id: alternative titles}, deleted ids)."""
    group, apart = same_hymn_groups(con)
    members = defaultdict(set)
    for hymn_id, g in group.items():
        members[g].add(hymn_id)
    titles = dict(con.execute("SELECT id, title FROM hymns"))
    alts = defaultdict(list)
    for hymn_id, title in con.execute(
        "SELECT hymn_id, title FROM hymn_alternative_titles ORDER BY hymn_id, position"
    ):
        alts[hymn_id].append(title)
    named = titled_rows(con)  # as same_hymn_groups reads the titles
    resolved = title_rows(con)
    heads, folded = defaultdict(set), defaultdict(set)  # group -> master_titles, merged titles
    for a, b, decision, _ in read_same_hymn_decisions():
        if decision != "same hymn":
            continue
        if not named.get(b):
            if not resolved.get(b):  # (merged already when the title is spelled like the row's)
                print(f"{SAME_HYMN_CSV.name}: no master-index row is titled {b!r}; skipped")
            continue
        g = group[next(iter(named[b]))]
        heads[g].add(b)
        if a != b:
            folded[g].add(a)
    cells = {(h, code): raw for h, code, raw in con.execute("SELECT hymn_id, hymnal_code, raw FROM hymn_cells")}
    texts = {h: rest for h, *rest in con.execute(
        "SELECT id, scripture, german_title, original_title, original_language, "
        "other_english_title, other_english_source FROM hymns")}
    codes = [HYMNALS[h][0] for h in HYMNALS if HYMNALS[h][0] in layout.col]

    updates, alternates, deletes = defaultdict(dict), {}, set()
    for g, rows in members.items():
        if len(rows) < 2:
            continue
        listed = ", ".join(repr(titles[h]) for h in sorted(rows))
        for x in rows:
            for y in rows:
                if frozenset((x, y)) in apart:
                    raise SystemExit(f"{SAME_HYMN_CSV.name}: {titles[x]!r} and {titles[y]!r} are both "
                                     f"'same hymn' (through {listed}) and kept apart")
        head = heads[g] - folded[g]
        if len(head) != 1:
            raise SystemExit(f"{SAME_HYMN_CSV.name}: {listed} are one hymn, but which title the row keeps "
                             f"is unclear: {sorted(head) or 'every title is merged into another'}")
        head = head.pop()
        keepers = sorted(h for h in rows if titles[h] == head)
        if not keepers:
            raise SystemExit(f"{SAME_HYMN_CSV.name}: none of {listed} is titled {head!r}")
        keep, others = keepers[0], sorted(rows - {keepers[0]})
        order = [keep] + others

        for code in codes:
            raws = [cells[h, code] for h in order if (h, code) in cells]
            mine = cells.get((keep, code))
            if not raws or all(raw == mine for raw in raws):
                continue
            # one cell as it is written ('944-945'; a plain number as a number), several made one
            value = raws[0] if len(set(raws)) == 1 else merged_numbers(raws, code)
            if isinstance(value, str) and value.isdigit():
                value = int(value)
            if str(value) != mine:
                updates[keep][layout.col[code]] = value

        def joined(i, sep):  # each part once: 'Nicene Creed' and 'Nicene Creed; Isaiah 43:1-7'
            parts = (part.strip() for h in order if texts[h][i] for part in texts[h][i].split(sep.strip()))
            return sep.join(dict.fromkeys(part for part in parts if part))

        for i, col, sep in ((0, layout.scripture, "; "), (1, layout.german, " / "), (2, layout.original, " / "),
                            (3, layout.language, " / ")):
            value = joined(i, sep) or None
            if value != texts[keep][i]:
                updates[keep][col] = value
        pairs = list(dict.fromkeys((texts[h][4], texts[h][5]) for h in order if texts[h][4] or texts[h][5]))
        if pairs and pairs != [(texts[keep][4], texts[keep][5])]:
            updates[keep][layout.other_english] = " / ".join(t for t, _ in pairs if t) or None
            updates[keep][layout.other_source] = " / ".join(src for _, src in pairs if src) or None

        have = [titles[keep]] + alts[keep]
        keys = {match_key(t) for t in have}
        new = list(alts[keep])
        for h in others:
            for title in [titles[h]] + alts[h]:
                if match_key(title) not in keys:
                    keys.add(match_key(title))
                    new.append(title)
        if new != alts[keep]:
            alternates[keep] = new
        deletes |= set(others)
    return updates, alternates, deletes


# A hymnal's title this much like one a row has already (match_key with Thee/You
# alike) is a spelling of it or a scanning error ('Now thank we all eur God'),
# not another title.
ALT_LIKENESS = 0.9


def new_wording(title, have):
    """Whether `title` is worth adding to titles `have`: the same words in
    Thee/Thou/Thy where they have You/Your (or the reverse), or other words
    altogether; not the same title in other spelling or punctuation, the start
    of one of them (or the reverse), or one of them with a letter or two off."""
    if any(match_key(title) == match_key(t) for t in have):
        return False
    key = match_key(title, modern=True)
    keys = [match_key(t, modern=True) for t in have]
    if key in keys:
        return True
    return not any(is_prefix(key, k) or difflib.SequenceMatcher(None, key, k).ratio() >= ALT_LIKENESS
                   for k in keys)


def plan_alternates(con):
    """{hymn_id: alternative titles} for rows master_corrections.csv gives an
    alternative title ('alternate'), and for rows the hymnals give an English
    title (hymn_titles, in ALT_SOURCES order, through clean links) that no
    other row bears and that is new in wording (new_wording). The row's own
    alternative titles stay first, as they are, except one that repeats its
    title (match_key), as a retitled row's can; a None at the end empties a
    cell that leaves free."""
    titles = dict(con.execute("SELECT id, title FROM hymns"))
    alts = defaultdict(list)
    for hymn_id, title in con.execute(
        "SELECT hymn_id, title FROM hymn_alternative_titles ORDER BY hymn_id, position"
    ):
        alts[hymn_id].append(title)
    listed = defaultdict(list)  # row -> the alternative titles master_corrections.csv gives it
    rows_titled = title_rows(con)
    for r in read_csv(MASTER_CORRECTIONS_CSV):
        if r["hymnal"] == ALT_CORRECTION:
            for hymn_id in rows_titled.get(r["master_title"], ()):
                listed[hymn_id].append(r["new"])
    unsure = defaultdict(set)  # row -> hymnals with a link on it still to review
    for hymn_id, code in con.execute("SELECT hymn_id, hymnal_code FROM links WHERE status = 'review'"):
        unsure[hymn_id].add(code)
    order = list(ALT_SOURCES)
    found = defaultdict(list)
    for hymn_id, source, title in con.execute(
        "SELECT hymn_id, source, title FROM hymn_titles WHERE source IN ({})".format(
            ", ".join(f"'{src}'" for src in ALT_SOURCES))
    ):
        if ALT_SOURCES[source] not in unsure[hymn_id]:
            found[hymn_id].append((order.index(source), title))
    # A title another row bears is left out: a number two rows share (a whole
    # hymn printed as two centos) can bring the other row's title.
    bearers = defaultdict(set)
    for hymn_id, title in list(titles.items()) + [(h, t) for h, ts in alts.items() for t in ts]:
        bearers[match_key(title)].add(hymn_id)
    out = {}
    for hymn_id in set(alts) | set(listed) | set(found):
        new = [t for t in alts[hymn_id] if match_key(t) != match_key(titles[hymn_id])]
        have = [titles[hymn_id]] + new
        for title in listed[hymn_id]:
            if match_key(title) not in {match_key(t) for t in have}:
                have.append(title)
                new.append(title)
        for _, title in sorted(found[hymn_id]):
            if bearers.get(match_key(title), set()) - {hymn_id} or not new_wording(title, have):
                continue
            have.append(title)
            new.append(title)
        if new != alts[hymn_id]:
            out[hymn_id] = new + [None] * (len(alts[hymn_id]) - len(new))
    return out


# --- worksheet XML ----------------------------------------------------------

def col_index(col):
    i = 0
    for ch in col:
        i = i * 26 + ord(ch) - 64
    return i


def set_cell(row_el, col, value, style):
    """Set (creating if needed, in column order) the cell `col` of a row element;
    None empties it. A cell that already holds a value keeps its own style."""
    rownum = row_el.get("r")
    ref = f"{col}{rownum}"
    cell = None
    for c in row_el.findall(f"{N}c"):
        c_col = re.match(r"[A-Z]+", c.get("r")).group(0)
        if c_col == col:
            cell = c
            break
        if col_index(c_col) > col_index(col):
            cell = etree.Element(f"{N}c", r=ref)
            c.addprevious(cell)
            break
    if cell is None:
        cell = etree.SubElement(row_el, f"{N}c", r=ref)
    if not len(cell):
        cell.set("s", style)
    for child in list(cell):
        cell.remove(child)
    cell.attrib.pop("t", None)
    if value is None:
        return
    if isinstance(value, int):
        etree.SubElement(cell, f"{N}v").text = str(value)
    else:
        cell.set("t", "inlineStr")
        t = etree.SubElement(etree.SubElement(cell, f"{N}is"), f"{N}t")
        t.text = value
        if value != value.strip():
            t.set("{http://www.w3.org/XML/1998/namespace}space", "preserve")


def new_row_element(values, layout):
    row_el = etree.Element(f"{N}row", r="0", spans=layout.spans)
    for k, v in ROW_ATTRS.items():
        row_el.set(k, v)
    for col, style in sorted(layout.styles.items(), key=lambda cs: col_index(cs[0])):
        if col in values:
            set_cell(row_el, col, values[col], style)
        else:
            etree.SubElement(row_el, f"{N}c", r=f"{col}0", s=style)
    return row_el


def cell_text(cell, strings):
    if cell is None:
        return None
    if cell.get("t") == "s":
        return strings[int(cell.find(f"{N}v").text)]
    if cell.get("t") == "inlineStr":
        return "".join(cell.find(f"{N}is").itertext())
    v = cell.find(f"{N}v")
    return v.text if v is not None else None


def read_strings(strings_xml):
    if not strings_xml:
        return []
    return ["".join(si.itertext()) for si in etree.fromstring(strings_xml).findall(f"{N}si")]


def cell_col(cell):
    return re.match(r"[A-Z]+", cell.get("r")).group(0)


def col_letter(i):
    letters = ""
    while i:
        i, rem = divmod(i - 1, 26)
        letters = chr(65 + rem) + letters
    return letters


def header_row(root):
    return next(r for r in root.find(f"{N}sheetData").findall(f"{N}row") if r.get("r") == "1")


def read_headers(root, strings):
    """{header text: column letter} from row 1."""
    out = {}
    for c in header_row(root).findall(f"{N}c"):
        text = cell_text(c, strings)
        if text and text.strip():
            out[text.strip()] = cell_col(c)
    return out


def data_styles(root):
    """{column letter: the style most of its cells below the header have}."""
    counts = defaultdict(Counter)
    for r in root.find(f"{N}sheetData").findall(f"{N}row"):
        if r.get("r") != "1":
            for c in r.findall(f"{N}c"):
                if c.get("s"):
                    counts[cell_col(c)][c.get("s")] += 1
    return {col: styles.most_common(1)[0][0] for col, styles in counts.items()}


def read_layout(path):
    with zipfile.ZipFile(path) as z:
        root = etree.fromstring(z.read(SHEET))
        strings = read_strings(z.read(STRINGS) if STRINGS in z.namelist() else None)
    return Layout(read_headers(root, strings), data_styles(root))


def insert_column(root, strings, header, after):
    """Insert an empty column headed `header` right after the one headed
    `after`, moving everything to its right one column over: cells, column
    widths, the dimension, sort range, row spans and selection. Its cells and
    width are those of the `after` column."""
    for tag in ("mergeCells", "conditionalFormatting", "dataValidations", "hyperlinks", "autoFilter",
                "tableParts", "drawing"):
        if root.find(f"{N}{tag}") is not None:
            raise SystemExit(f"the sheet has <{tag}>, which inserting a column would have to move too")
    if root.find(f".//{N}f") is not None:
        raise SystemExit("the sheet has formulas, which inserting a column would have to move too")
    p = col_index(read_headers(root, strings)[after]) + 1  # the new column
    after_col, new_col = col_letter(p - 1), col_letter(p)

    def shift_ref(ref):  # 'U5' -> 'V5', 'A2:T2441' -> 'A2:U2441'
        return re.sub(r"\b([A-Z]+)(\d*)\b",
                      lambda m: (col_letter(col_index(m.group(1)) + 1) if col_index(m.group(1)) >= p
                                 else m.group(1)) + m.group(2), ref)

    for r in root.find(f"{N}sheetData").findall(f"{N}row"):
        before = None
        for c in r.findall(f"{N}c"):
            col = cell_col(c)
            if col_index(col) >= p:
                c.set("r", col_letter(col_index(col) + 1) + r.get("r"))
            elif col == after_col:
                before = c
        if before is not None:
            cell = etree.Element(f"{N}c", r=new_col + r.get("r"))
            if before.get("s"):
                cell.set("s", before.get("s"))
            before.addnext(cell)
            if r.get("r") == "1":
                set_cell(r, new_col, header, before.get("s", HEADER_STYLE))
        if r.get("spans"):
            lo, hi = map(int, r.get("spans").split(":"))
            r.set("spans", f"{lo + (lo >= p)}:{hi + (hi >= p - 1)}")

    cols = root.find(f"{N}cols")
    template = None
    for c in cols.findall(f"{N}col"):
        lo, hi = int(c.get("min")), int(c.get("max"))
        if lo <= p - 1 <= hi:
            template = c
        if lo < p <= hi:  # a range running past the new column is split around it
            rest = etree.Element(f"{N}col", **dict(c.attrib))
            rest.set("min", str(p + 1))
            rest.set("max", str(min(hi + 1, 16384)))
            c.set("max", str(p - 1))
            c.addnext(rest)
        elif lo >= p:
            c.set("min", str(lo + 1))
            c.set("max", str(min(hi + 1, 16384)))
    own = etree.Element(f"{N}col", **dict(template.attrib if template is not None else
                                          {"width": "7", "customWidth": "1"}))
    own.set("min", str(p))
    own.set("max", str(p))
    own.attrib.pop("bestFit", None)
    earlier = [c for c in cols.findall(f"{N}col") if int(c.get("max")) < p]
    if earlier:
        earlier[-1].addnext(own)
    else:
        cols.insert(0, own)

    dim = root.find(f"{N}dimension")
    dim.set("ref", shift_ref(dim.get("ref")))
    sort_state = root.find(f"{N}sortState")
    if sort_state is not None:
        sort_state.set("ref", shift_ref(sort_state.get("ref")))
        for cond in sort_state.findall(f"{N}sortCondition"):
            cond.set("ref", shift_ref(cond.get("ref")))
    for view in root.iter(f"{N}selection", f"{N}pane"):
        for attr in ("activeCell", "sqref", "topLeftCell"):
            if view.get(attr):
                view.set(attr, shift_ref(view.get(attr)))


def delete_column(root, strings, header):
    """Delete the column headed `header`, moving everything to its right one
    column over to the left: cells, column widths, the dimension, sort range,
    row spans and selection (insert_column undone)."""
    for tag in ("mergeCells", "conditionalFormatting", "dataValidations", "hyperlinks", "autoFilter",
                "tableParts", "drawing"):
        if root.find(f"{N}{tag}") is not None:
            raise SystemExit(f"the sheet has <{tag}>, which deleting a column would have to move too")
    if root.find(f".//{N}f") is not None:
        raise SystemExit("the sheet has formulas, which deleting a column would have to move too")
    p = col_index(read_headers(root, strings)[header])

    def shift_ref(ref):  # 'V5' -> 'U5', 'A2:W2441' -> 'A2:V2441'
        return re.sub(r"\b([A-Z]+)(\d*)\b",
                      lambda m: (col_letter(col_index(m.group(1)) - 1) if col_index(m.group(1)) > p
                                 else m.group(1)) + m.group(2), ref)

    for r in root.find(f"{N}sheetData").findall(f"{N}row"):
        for c in r.findall(f"{N}c"):
            i = col_index(cell_col(c))
            if i == p:
                r.remove(c)
            elif i > p:
                c.set("r", col_letter(i - 1) + r.get("r"))
        if r.get("spans"):
            lo, hi = map(int, r.get("spans").split(":"))
            r.set("spans", f"{lo - (lo > p)}:{max(lo - (lo > p), hi - (hi >= p))}")
    cols = root.find(f"{N}cols")
    for c in cols.findall(f"{N}col"):
        lo, hi = int(c.get("min")), int(c.get("max"))
        if lo <= p <= hi:
            if lo == hi:
                cols.remove(c)
            else:
                c.set("max", str(hi - 1))
        elif lo > p:
            c.set("min", str(lo - 1))
            c.set("max", str(hi - 1))
    dim = root.find(f"{N}dimension")
    dim.set("ref", shift_ref(dim.get("ref")))
    sort_state = root.find(f"{N}sortState")
    if sort_state is not None:
        sort_state.set("ref", shift_ref(sort_state.get("ref")))
        for cond in sort_state.findall(f"{N}sortCondition"):
            cond.set("ref", shift_ref(cond.get("ref")))
    for view in root.iter(f"{N}selection", f"{N}pane"):
        for attr in ("activeCell", "sqref", "topLeftCell"):
            if view.get(attr):
                view.set(attr, shift_ref(view.get(attr)))


def check_defined_names(path, workbook):
    """Defined names (print titles '$1:$1' aside) could point at moved columns."""
    for name in re.findall(r"<definedName[^>]*>([^<]*)</definedName>", workbook):
        if not re.fullmatch(r"'?[^!]*'?!\$\d+:\$\d+", name):
            raise SystemExit(f"{path.name}: the defined name {name!r} would need moving with the columns")


def read_sheet(path):
    with zipfile.ZipFile(path) as z:
        root = etree.fromstring(z.read(SHEET))
        strings = read_strings(z.read(STRINGS) if STRINGS in z.namelist() else None)
        workbook = z.read(WORKBOOK).decode("utf-8")
    return root, strings, workbook


def place_after(header, headers):
    """The header of the column a new column `header` goes after: the nearest one
    before it in HYMNAL_ORDER that the sheet (`headers`) has."""
    i = HYMNAL_ORDER.index(header)
    return next(h for h in reversed(HYMNAL_ORDER[:i]) if h in headers)


def add_missing_columns(path, wanted):
    """Insert the columns among `wanted` (headers) the master index lacks, each
    placed by HYMNAL_ORDER; returns their headers."""
    root, strings, workbook = read_sheet(path)
    missing = [h for h in wanted if h not in read_headers(root, strings)]
    if not missing:
        return []
    check_defined_names(path, workbook)

    def edit(xml, strings_xml):
        root = etree.fromstring(xml)
        strings = read_strings(strings_xml)
        for header in missing:
            insert_column(root, strings, header, place_after(header, read_headers(root, strings)))
        return to_xml(root)

    write_xlsx(path, edit)
    return missing


def rename_columns(path):
    """Give the RENAMED_COLUMNS the master index still has their new headers;
    returns the old headers."""
    root, strings, _ = read_sheet(path)
    headers = read_headers(root, strings)
    present = [h for h in RENAMED_COLUMNS if h in headers]
    if not present:
        return []

    def edit(xml, strings_xml):
        root = etree.fromstring(xml)
        cols = read_headers(root, read_strings(strings_xml))
        for header in present:
            set_cell(header_row(root), cols[header], RENAMED_COLUMNS[header], HEADER_STYLE)
        return to_xml(root)

    write_xlsx(path, edit)
    return present


def remove_columns(path):
    """Delete the REMOVED_COLUMNS the master index still has; returns their headers."""
    root, strings, workbook = read_sheet(path)
    present = [h for h in REMOVED_COLUMNS if h in read_headers(root, strings)]
    if not present:
        return []
    check_defined_names(path, workbook)

    def edit(xml, strings_xml):
        root = etree.fromstring(xml)
        for header in present:
            delete_column(root, read_strings(strings_xml), header)
        return to_xml(root)

    write_xlsx(path, edit)
    return present


def ensure_alt_columns(path, count):
    """Give the master index `count` 'Alternative English Title N' columns, adding
    the missing ones after its last column; returns how many were added."""
    root, strings, workbook = read_sheet(path)
    have = sum(1 for h in read_headers(root, strings) if ALT_TITLE_RE.match(h))
    if have >= count:
        return 0
    check_defined_names(path, workbook)

    def edit(xml, strings_xml):
        root = etree.fromstring(xml)
        strings = read_strings(strings_xml)
        for n in range(have + 1, count + 1):
            headers = read_headers(root, strings)
            last = max(headers, key=lambda h: col_index(headers[h]))
            insert_column(root, strings, f"{ALT_TITLE_HEADER} {n}", last)
            p = str(col_index(headers[last]) + 1)
            for c in root.find(f"{N}cols").findall(f"{N}col"):
                if c.get("min") == p and c.get("max") == p:
                    c.set("width", str(ALT_WIDTH))
                    c.set("customWidth", "1")
        return to_xml(root)

    write_xlsx(path, edit)
    return count - have


def add_column_width(root, col, width):
    """Give column `col` its own <col> width unless it already has one, alone or
    in a range of columns given a width by hand; a default range covering it
    (e.g. Q to the last column) is split around it."""
    cols = root.find(f"{N}cols")
    p = col_index(col)
    covering = next((c for c in cols if int(c.get("min")) <= p <= int(c.get("max"))), None)
    if covering is not None and (covering.get("min") == covering.get("max") or covering.get("customWidth") == "1"):
        return  # already set
    attrs = {"min": str(p), "max": str(p), "width": str(width), "customWidth": "1"}
    if covering is None:
        after = [c for c in cols if int(c.get("max")) < p][-1]
        if after.get("style"):
            attrs["style"] = after.get("style")
        after.addnext(etree.Element(f"{N}col", **attrs))
        return
    if covering.get("style"):
        attrs["style"] = covering.get("style")
    lo, hi = int(covering.get("min")), int(covering.get("max"))
    own = etree.Element(f"{N}col", **attrs)
    if lo < p:
        before = etree.Element(f"{N}col", **dict(covering.attrib))
        before.set("max", str(p - 1))
        covering.addprevious(before)
    covering.addprevious(own)
    if p < hi:
        covering.set("min", str(p + 1))
    else:
        cols.remove(covering)


def to_xml(root):
    return etree.tostring(root, xml_declaration=True, encoding="UTF-8", standalone=True)


def edit_kelg_sheet(sheet_xml, strings_xml, wh_titles):
    """Fill column S of the KELG index with WH titles, keyed by the number in column A."""
    root = etree.fromstring(sheet_xml)
    strings = read_strings(strings_xml)
    col = chr(ord("A") + KELG_WH_TITLE_COLUMN)
    for r in root.find(f"{N}sheetData").findall(f"{N}row"):
        cells = {re.match(r"[A-Z]+", c.get("r")).group(0): c for c in r.findall(f"{N}c")}
        if r.get("r") == "1":
            set_cell(r, col, KELG_WH_TITLE_HEADER, cells["A"].get("s", "0"))
        number = cell_text(cells.get("A"), strings)
        if number and number.isdigit() and int(number) in wh_titles:
            set_cell(r, col, wh_titles[int(number)], cells["B"].get("s", "0"))
    add_column_width(root, col, 45)
    dim = root.find(f"{N}dimension")
    dim.set("ref", re.sub(r"^(A1:)[A-Z]+", rf"\g<1>{col}", dim.get("ref")))
    return to_xml(root)


def edit_sheet(sheet_xml, strings_xml, layout, updates, new_rows, retitles, deletes):
    root = etree.fromstring(sheet_xml)
    strings = read_strings(strings_xml)
    sheet_data = root.find(f"{N}sheetData")
    rows = sheet_data.findall(f"{N}row")
    by_num = {int(r.get("r")): r for r in rows}

    # Widths of the text columns after the numbers.
    for header, col in layout.text.items():
        add_column_width(root, col, TEXT_WIDTHS[header])

    # Fill cells of existing rows, and retitle.
    for hymn_id, cells in updates.items():
        for col, value in cells.items():
            set_cell(by_num[hymn_id], col, value, layout.styles[col])
    for hymn_id, title in retitles.items():
        set_cell(by_num[hymn_id], "A", title, layout.styles["A"])
    moved = [by_num[h] for h in retitles]
    gone = {id(by_num[h]) for h in deletes} | {id(r) for r in moved}

    # Data rows are the ones with a title; anything after them (empty, styled
    # leftovers) stays at the bottom.
    def title_of(r):
        a = next((c for c in r.findall(f"{N}c") if c.get("r").startswith("A")
                  and re.fullmatch(r"A\d+", c.get("r"))), None)
        return cell_text(a, strings)

    data = [r for r in rows[1:] if title_of(r)]
    trailing = [r for r in rows[1:] if not title_of(r)]
    if trailing and data and int(trailing[0].get("r")) < int(data[-1].get("r")):
        raise SystemExit("found an untitled row in the middle of the data; fix it before writing back")
    for r in rows[1:]:
        sheet_data.remove(r)
    data = [r for r in data if id(r) not in gone]

    keys = [sort_key(title_of(r)) for r in data]
    placing = [(sort_key(str(v["A"])), new_row_element(v, layout)) for v in new_rows] \
        + [(sort_key(title_of(r)), r) for r in moved]
    for k, row_el in sorted(placing, key=lambda p: p[0]):
        i = bisect.bisect_right(keys, k)
        keys.insert(i, k)
        data.insert(i, row_el)

    for i, r in enumerate(data + trailing, start=2):
        r.set("r", str(i))
        for c in r.findall(f"{N}c"):
            c.set("r", re.match(r"[A-Z]+", c.get("r")).group(0) + str(i))
        sheet_data.append(r)

    last_row = len(data) + len(trailing) + 1
    last_data = len(data) + 1
    dim = root.find(f"{N}dimension")
    dim.set("ref", re.sub(r"\d+$", str(last_row), dim.get("ref")))
    sort_state = root.find(f"{N}sortState")
    if sort_state is not None:
        sort_state.set("ref", f"A2:{layout.last}{last_data}")
        for cond in sort_state.findall(f"{N}sortCondition"):
            cond.set("ref", f"A1:A{last_data}")

    return to_xml(root)


def write_xlsx(path, edit):
    """Rewrite the first worksheet of `path` with edit(sheet_xml, shared_strings_xml)."""
    tmp = path.with_suffix(".xlsx.tmp")
    with zipfile.ZipFile(path) as zin, zipfile.ZipFile(tmp, "w", zipfile.ZIP_DEFLATED) as zout:
        strings_xml = zin.read(STRINGS) if STRINGS in zin.namelist() else None
        for item in zin.infolist():
            data = zin.read(item.filename)
            if item.filename == SHEET:
                data = edit(data, strings_xml)
            zout.writestr(item, data)
    shutil.move(tmp, path)


def main():
    ap = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    ap.add_argument("--add", metavar="CODE",
                    help="add the column of this hymnal taken from Hymnary.org (" + ", ".join(HYMNARY_CSVS) + ")")
    ap.add_argument("--merge-kelg", default="",
                    help="comma-separated KELG numbers whose own row to merge into their WH match")
    args = ap.parse_args()
    merge_kelg = [int(n) for n in args.merge_kelg.split(",") if n.strip()]
    wanted = ADDED_COLUMNS
    if args.add:
        if args.add not in HYMNARY_CSVS:
            raise SystemExit(f"--add {args.add}: not a hymnal taken from Hymnary.org ({', '.join(HYMNARY_CSVS)})")
        header = next(h for h, (code, _, _) in HYMNALS.items() if code == args.add)
        if header in read_headers(*read_sheet(LCMS_XLSX)[:2]):
            print(f"{LCMS_XLSX.name} has its {header} column already\n")
        con = sqlite3.connect(DB_PATH)
        unsettled = con.execute(
            "SELECT hymnal_code, COUNT(*) FROM links WHERE status = 'review' AND hymnal_code IN ({}) "
            "GROUP BY hymnal_code".format(", ".join(f"'{c}'" for c in HYMNARY_CSVS if c != args.add))).fetchall()
        con.close()
        if unsettled:  # a hymn left there could get a row from each hymnal that has it
            print(f"warning: links of hymnals added before {args.add} are still to review in link_review.csv: "
                  + ", ".join(f"{n} {code}" for code, n in unsettled) + "\n")
        wanted += (header,)

    renamed = rename_columns(LCMS_XLSX)
    if renamed:
        print(f"{LCMS_XLSX.name}: renamed the column(s) "
              f"{', '.join(f'{h} -> {RENAMED_COLUMNS[h]}' for h in renamed)}\n")
    removed = remove_columns(LCMS_XLSX)
    if removed:
        print(f"{LCMS_XLSX.name}: took out the column(s) {', '.join(removed)}\n")
    added = add_missing_columns(LCMS_XLSX, wanted)
    if added:
        print(f"{LCMS_XLSX.name}: added the column(s) {', '.join(added)}\n")
    build_db.build()
    con = sqlite3.connect(DB_PATH)
    wh_titles = plan_wh_titles(con)
    con.close()
    if wh_titles:
        print(f"\n{KELG_XLSX.name}: writing {len(wh_titles)} WH titles\n")
        write_xlsx(KELG_XLSX, lambda xml, strings: edit_kelg_sheet(xml, strings, wh_titles))
        build_db.build()

    # Some links only show once earlier ones are written (rows that come to
    # share a number count as the same hymn), so repeat until nothing changes:
    # links and corrections first, then merges, then alternative titles.
    for round_ in range(MAX_ROUNDS):
        layout = read_layout(LCMS_XLSX)
        con = sqlite3.connect(DB_PATH)
        updates, new_rows, retitles, deletes = plan(con, layout, merge_kelg if round_ == 0 else ())
        alternates, step = {}, "links and corrections"
        if not (updates or new_rows or retitles or deletes):
            (updates, alternates, deletes), step = plan_merges(con, layout), "merging rows"
        if not (updates or alternates or deletes):
            alternates, step = plan_alternates(con), "alternative titles"
        con.close()
        if not (updates or new_rows or retitles or deletes or alternates):
            print(f"\n{LCMS_XLSX.name}: nothing (more) to write\n")
            break
        needed = max((len(titles) for titles in alternates.values()), default=0)
        if ensure_alt_columns(LCMS_XLSX, needed):
            layout = read_layout(LCMS_XLSX)
        for hymn_id, titles in alternates.items():
            for col, title in zip(layout.alternates, titles):
                updates[hymn_id][col] = title
        filled = sum(len(c) for c in updates.values())
        emptied = sum(v is None for c in updates.values() for v in c.values())
        print(f"\n{LCMS_XLSX.name} ({step}): writing {filled} cells ({emptied} emptied) in {len(updates)} "
              f"existing rows, retitling {len(retitles)} rows, adding {len(new_rows)} and deleting "
              f"{len(deletes)}\n")
        write_xlsx(LCMS_XLSX, lambda xml, strings: edit_sheet(
            xml, strings, layout, updates, new_rows, retitles, deletes))
        build_db.build()
    else:
        print(f"{LCMS_XLSX.name}: still changing after {MAX_ROUNDS} rounds; run write_back.py again")


if __name__ == "__main__":
    main()
