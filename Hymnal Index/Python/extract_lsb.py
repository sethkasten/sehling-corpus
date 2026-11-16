#!/usr/bin/env python3
"""Extract Lutheran Service Book's hymn titles into LSB/LSB_index.csv.

Usage: python3 extract_lsb.py [path/to/LSB.html]

The source is singpraises.net's list of the book
(https://singpraises.net/collections/en/lutheran-service-book), saved as
LSB/LSB.html. It gives every hymn, 331-966, with LSB's number and title; LSB
numbers its hymns from 331 and prints no hymn under 1-330. The master index's
LSB 967-986 are hymns of the accompaniment edition that no pew edition prints,
so they are not in it. Only the number and title are kept, as printed there:
'Agnus Dei - I (Lamb of God)'. LSB_FIXES corrects four typing errors.
"""
import csv
import html
import re
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
SRC = HERE / "LSB" / "LSB.html"
OUT = HERE / "LSB" / "LSB_index.csv"
# singpraises.net's typing errors, each against its own first line and LSB's other
# titles for the hymn: number -> (title there, title in LSB)
LSB_FIXES = {
    550: ("Lamb O God", "Lamb of God"),  # 'Your only Son, no sin to hide'; its other title 'Lamb of God'
    552: ("O Christ, Who Shared Our Mortal Live", "O Christ, Who Shared Our Mortal Life"),
    653: ("In Christ There Is No East of West", "In Christ There Is No East or West"),
    822: ("Alleluia! Let Praise Ring", "Alleluia! Let Praises Ring"),  # 'Alleluia! Let praises ring!'
}
ROW = re.compile(r'<td class="number"[^>]*>\s*(\d+)\.\s*</td>.*?<div class="title info-group"[^>]*>(.*?)</div>', re.S)


def main():
    src = Path(sys.argv[1]) if len(sys.argv) > 1 else SRC
    rows = [(int(n), " ".join(html.unescape(re.sub(r"<[^>]+>", " ", t)).split()))
            for n, t in ROW.findall(src.read_text(encoding="utf-8"))]
    for i, (n, title) in enumerate(rows):
        if n in LSB_FIXES:
            if title != LSB_FIXES[n][0]:
                raise SystemExit(f"LSB_FIXES: LSB {n} is now {title!r}, not {LSB_FIXES[n][0]!r}")
            rows[i] = (n, LSB_FIXES[n][1])
    numbers = [n for n, _ in rows]
    assert numbers == sorted(set(numbers)) == list(range(331, 967)), "LSB.html is not LSB 331-966 once each"
    with open(OUT if len(sys.argv) < 3 else sys.argv[2], "w", newline="", encoding="utf-8") as f:
        w = csv.writer(f)
        w.writerow(["number", "title"])
        w.writerows(rows)
    print(f"{len(rows)} LSB hymns -> {OUT.name}")


if __name__ == "__main__":
    main()
