#!/usr/bin/env python3
"""Extract the hymnals saved from Hymnary.org as page folders into one CSV each.

Usage: python3 extract_hymnary.py [CODE ...]   (default: every folder in HYMNARY_FOLDERS)

Each folder (ACS/, AH/, ... TCH/) holds Hymnary.org's table of a hymnal's hymns,
saved a page at a time as <CODE>1.html, <CODE>2.html, ... The table gives each
hymn's number, first line and tune; the CSV, <CODE>/<CODE>_index.csv, keeps them
as printed there, in the book's order:

  number      as Hymnary gives it: '20', '20a' (a text printed twice, with two
              tunes: 20a and 20b), 'D1' (a doxology in the book's own doxology
              section), 'd1' (Hymnary's placeholder when it lacks the book's
              numbers: The Concordia Hymnal)
  first_line  Hymnary's first line: a hymn in another language followed by its
              English one in parentheses ('Stille Nacht, heilige Nacht! (Silent
              night, holy night)'), or the reverse; variant readings in brackets
              ('From all that [who] dwell below the skies')
  tune        tune name; empty where Hymnary has none, '[...]' where it has only
              the tune's first line

ELW's 'Front matter' (p.1) and 'Psalms' (1, its psalter) aren't hymns and are
left out. build_db.py reads the CSVs (HYMNARY_CSVS) and takes the variants apart.
"""
import csv
import re
import sys
from collections import Counter
from pathlib import Path

from lxml import html

HERE = Path(__file__).resolve().parent
# Hymnary.org's page folders, in the order they were added to the master index.
HYMNARY_FOLDERS = ("ACS", "AH", "ALH", "CSB", "ELHal", "ELW", "HCH", "HS91", "SBH", "THOS",
                   "TBW07", "TBW67", "CHPPPW", "CHL", "TCSSH", "TCH")
NUMBER = re.compile(r"[A-Za-z]?\d+[a-z]?")
SKIP = {("ELW", "p.1"), ("ELW", "1")}  # ELW's 'Front matter' and 'Psalms' (its psalter)


def page_number(path, code):
    return int(path.stem[len(code):])


def read_folder(code):
    """[(number, first line, tune)] from the folder's pages, in page order."""
    folder = HERE / code
    pages = sorted(folder.glob(f"{code}*.html"), key=lambda p: page_number(p, code))
    if not pages:
        raise SystemExit(f"{folder}: no {code}N.html pages")
    numbers = [page_number(p, code) for p in pages]
    if numbers != list(range(1, len(pages) + 1)):
        raise SystemExit(f"{folder}: pages {numbers}, expected 1-{len(pages)}")
    out = []
    for path in pages:
        doc = html.fromstring(path.read_bytes().decode("utf-8"))
        for tr in doc.xpath('//tr[contains(@class, "result-row")]'):
            number, first_line, tune = (" ".join(td.text_content().split()) for td in tr.findall("td")[:3])
            if (code, number) in SKIP:
                continue
            if not NUMBER.fullmatch(number) or not first_line:
                raise SystemExit(f"{path.name}: unexpected row {number!r} {first_line!r}")
            out.append((number, first_line, tune))
    repeated = [n for n, c in Counter(n for n, _, _ in out).items() if c > 1]
    if repeated:
        raise SystemExit(f"{code}: numbers listed twice: {repeated}")
    return out


def main():
    codes = sys.argv[1:] or HYMNARY_FOLDERS
    for code in codes:
        rows = read_folder(code)
        target = HERE / code / f"{code}_index.csv"
        with open(target, "w", newline="", encoding="utf-8") as f:
            w = csv.writer(f)
            w.writerow(["number", "first_line", "tune"])
            w.writerows(rows)
        kinds = Counter("doxology" if n.startswith("D") else "placeholder" if n.startswith("d")
                        else "lettered" if n[-1].isalpha() else "hymn" for n, _, _ in rows)
        print(f"wrote {target.relative_to(HERE)}: {len(rows)} entries ({', '.join(f'{c} {k}' for k, c in kinds.items())})")


if __name__ == "__main__":
    main()
