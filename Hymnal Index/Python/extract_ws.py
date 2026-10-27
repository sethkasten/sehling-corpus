#!/usr/bin/env python3
"""Extract the indexes of the two TLH supplements into ws69_index.csv and ws2000_index.csv.

Usage: python3 extract_ws.py

The sources are Hymnary.org's tables of the hymns in each book, saved as
WS69.html (Worship Supplement, 1969) and WS2000.html (Worship Supplement
2000): number, first line and tune. Both books number their hymns from 701
on, after TLH's. Hymnary letters the parts of a hymn that a book prints with
several tunes (WS69 718a-c, 741a-b); the numbers keep those letters.

WS69's own index of first lines and titles (WS69 hymn index.pdf, printed
pp. 251-253) agrees with Hymnary's table on every number. It also lists a
few first lines that Hymnary's table gives only under the hymn's first part:
those are written as `alternate` entries (WS69_INDEX_ENTRIES), and what else
the index says is kept in the `note` column (WS69_NOTES).
"""
import csv
import re
from pathlib import Path

from lxml import html

HERE = Path(__file__).resolve().parent
SOURCES = {HERE / "WS69.html": HERE / "ws69_index.csv", HERE / "WS2000.html": HERE / "ws2000_index.csv"}

# WS69's index entries for a part of a hymn that Hymnary's table titles with the
# hymn's first line: number -> first line. 718 is the Quempas Celebration (Quem
# pastores, Nunc angelorum, Resonet in laudibus; the index gives 718 for each)
# and 741 the Victimae Paschali Celebration; the part is the one sung to the
# carol's own tune.
WS69_INDEX_ENTRIES = {
    "718b": "The glorious angels came today",  # NUNC ANGELORUM
    "718c": "God's own Son is born a child",  # RESONET IN LAUDIBUS
    "741b": "Christ is arisen",  # CHRIST IST ERSTANDEN
    "770": "Now the silence",
}
WS69_NOTES = {
    "718a": "the Quempas Celebration (WS69's index: 'Quempas Celebration', 718)",
    "718b": "the Quempas Celebration (WS69's index: 'Quempas Celebration', 718)",
    "718c": "the Quempas Celebration (WS69's index: 'Quempas Celebration', 718)",
    "729": "WS69's index: 'Vexilla Regis Celebration', 729, 730",
    "730": "WS69's index: 'Vexilla Regis Celebration', 729, 730",
    "741a": "the Victimae Paschali Celebration (WS69's index: 'Victimae Paschali Celebration', 741)",
    "741b": "the Victimae Paschali Celebration (WS69's index: 'Victimae Paschali Celebration', 741)",
    "745": "Luther's Te Deum (WS69's index: 'Te Deum, Luther's')",
    "747": "WS69's index prints 'Thy strong arm did cleave the darkness'",
}


def read_table(path):
    """[(number, first line, tune)] from a saved Hymnary table of a book's hymns."""
    doc = html.fromstring(path.read_bytes().decode("utf-8"))
    out = []
    for tr in doc.xpath('//tr[contains(@class, "result-row")]'):
        number, first_line, tune = (" ".join(td.text_content().split()) for td in tr.findall("td")[:3])
        if not re.fullmatch(r"\d+[a-z]?", number) or not first_line:
            raise SystemExit(f"{path.name}: unexpected row {number!r} {first_line!r}")
        out.append((number, first_line, tune))
    return out


def main():
    for source, target in SOURCES.items():
        rows = read_table(source)
        ws69 = source.name == "WS69.html"
        with open(target, "w", newline="", encoding="utf-8") as f:
            w = csv.writer(f)
            w.writerow(["number", "first_line", "tune", "alternate", "note"])
            for number, first_line, tune in rows:
                note = WS69_NOTES.get(number, "") if ws69 else ""
                w.writerow([number, first_line, tune, 0, note])
                if ws69 and number in WS69_INDEX_ENTRIES:
                    w.writerow([number, WS69_INDEX_ENTRIES[number], tune, 1, "WS69's index of first lines"])
        print(f"wrote {target.name}: {len(rows)} hymns")


if __name__ == "__main__":
    main()
