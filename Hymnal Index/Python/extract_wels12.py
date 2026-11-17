#!/usr/bin/env python3
"""Extract the index of the Wisconsin Synod's German hymnal of 1912 into WELS12/WELS12_index.csv.

Usage: python3 extract_wels12.py

The book: Evangelisch-Lutherisches Gesangbuch für Kirche, Schule und Haus
(Milwaukee: Verlag der Evang.-Lutherischen Synode von Wisconsin u. a. Staaten,
1912), here WELS12. The source is musicanet.org's index of its hymns
(https://www.musicanet.org/robokopp/1912.html, 19122.html and 19123.html: hymns
1-175, 176-407 and 408-695), saved as WELS12/1912.html, 19122.html, 19123.html.
It gives each hymn's number and German first line under the book's section
headings. Kept, as printed there: number ('292a': 292 is two hymns, 292a and
292b), first line, section heading, and the page it is on.

The index numbers the hymns 1-695 once each, but for 292a/292b; the script
stops if that changes. FIXES and SECTION_FIXES correct its slips, each checked
against the hymn's text (the hymn's own page on musicanet.org, where it has one;
KELG, ELGBS or the hymn's English translation) or plain German; the script
stops if a slip is no longer there. 244's line, garbled in the index ('Gott, das
Verfolstürmt die Kirche sehr'), is corrected from a scan of the book's page
(WELS12/244.png).
"""
import csv
import html
import re
from pathlib import Path

HERE = Path(__file__).resolve().parent
PAGES = ("1912.html", "19122.html", "19123.html")
OUT = HERE / "WELS12" / "WELS12_index.csv"
# number -> (first line as the index gives it, as the book has it)
FIXES = {
    "3": ("Lobe den Herrn", "Lobe den Herren"),  # Neander; its page: 'Lobe den Herren, den mächtigen König'
    "17": ("Laßt uns mit füßen Weisen", "Laßt uns mit süßen Weisen"),  # the long s read as f
    "50": ("Jessia, dem Propheten, das geschah", "Jesaia, dem Propheten, das geschah"),
    "124": ("Schaut, schaut, was ist für Wunder bar?", "Schaut, schaut, was ist für Wunder dar?"),
    "130": ("Nun singet und seit froh", "Nun singet und seid froh"),  # its page: 'seid'
    "199": ("Ihr Christen, seht, daß ihr aussegt", "Ihr Christen, seht, daß ihr ausfegt"),  # f read as s
    # the book (WELS12/244.png): 'Gott! das Verfolgungsmeer bestürmt die Kirche sehr'
    "244": ("Gott, das Verfolstürmt die Kirche sehr", "Gott, das Verfolgungsmeer bestürmt die Kirche sehr"),
    "270": ("Süßes Evengelium", "Süßes Evangelium"),
    "346": ("Nun bircht die finstre Nacht", "Nun bricht die finstre Nacht"),
    "527": ("Warum sollt' ich mich den grämen?", "Warum sollt' ich mich denn grämen?"),
    "559": ("Das walter Gott, der helfen kann!", "Das walte Gott, der helfen kann!"),
    "624": ("Ich ahb mich Gott ergeben", "Ich hab mich Gott ergeben"),
}
SECTION_FIXES = {
    "Butzlieder": "Bußlieder",
    "A. Heilingungslieder": "A. Heiligungslieder",
    "E. Nächtenliebe": "E. Nächstenliebe",
}
ENTRY = re.compile(r"<B>([^<]+)</B>\s*<BR>|(\d+)\s*([a-z]?)\.\s*(.*?)<BR>", re.I)


def read_page(path):
    text = re.sub(r"\s+", " ", path.read_bytes().decode("utf-8"))
    body = text[text.index("<BLOCKQUOTE>"):]
    section, out = None, []
    for m in ENTRY.finditer(body):
        if m.group(1):
            section = html.unescape(m.group(1)).strip()
            section = SECTION_FIXES.get(section, section)
            continue
        first = re.split(r"\s+-\s+(?:<A[^>]*>)?Melodie", m.group(4))[0]
        first = html.unescape(re.sub(r"<[^>]+>", "", first)).strip()
        if not first:
            raise SystemExit(f"{path.name}: hymn {m.group(2)} has no first line")
        out.append((m.group(2) + m.group(3), first, section, path.name))
    return out


def main():
    rows = [r for page in PAGES for r in read_page(HERE / "WELS12" / page)]
    sections = {r[2] for r in rows}
    for number, (old, new) in FIXES.items():
        i = next(i for i, r in enumerate(rows) if r[0] == number)
        if rows[i][1] != old:
            raise SystemExit(f"FIXES: {number} is now {rows[i][1]!r}, not {old!r}")
        rows[i] = (number, new) + rows[i][2:]
    missing = [new for new in SECTION_FIXES.values() if new not in sections]
    if missing:
        raise SystemExit(f"SECTION_FIXES: no section {missing} (the index's headings changed)")
    numbers = [r[0] for r in rows]
    expected = [str(n) for n in range(1, 696) if n != 292]
    expected[291:291] = ["292a", "292b"]
    if numbers != expected:
        raise SystemExit("the index no longer numbers its hymns 1-695 once each (292a, 292b)")
    with open(OUT, "w", newline="", encoding="utf-8") as f:
        w = csv.writer(f)
        w.writerow(["number", "first_line", "section", "page"])
        w.writerows(rows)
    print(f"{len(rows)} WELS12 hymns -> {OUT.relative_to(HERE)}")


if __name__ == "__main__":
    main()
