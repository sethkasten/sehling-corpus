#!/usr/bin/env python3
"""Extract hymn metadata for The Lutheran Hymnal (TLH, 1941) into tlh_1941.csv.

Usage: python3 extract_tlh.py [path/to/tlh.zip]

The source is Project Wittenberg's public-domain text edition of TLH
(https://www.projectwittenberg.org/etext/hymnals/tlh/tlh.zip, downloaded when
no path is given): one tlhNNN.txt per hymn with notes taken from The Handbook
to the Lutheran Hymnal (1942). Only metadata is kept: title, first line,
author, translator, the original-language first line the notes give
('Titled:'), and tune.

The edition is plain ASCII, so the original first lines spell umlauts as
ae/oe/ue (e.g. 'Tut mir auf die schoene Pforte') and Scandinavian letters as
oe/aa/ae; build_db.py folds spellings the same way before comparing.

Known problems in the edition: tlh251.txt repeats hymn 252, so 251 is left
out; about 40 hymns still under copyright in 1941 are missing.
"""
import csv
import io
import re
import sys
import urllib.request
import zipfile
from pathlib import Path

HERE = Path(__file__).resolve().parent
OUT = HERE / "tlh_1941.csv"
URL = "https://www.projectwittenberg.org/etext/hymnals/tlh/tlh.zip"

SKIP = {251: "tlh251.txt repeats hymn 252"}
NOTE = re.compile(r"^([A-Za-z0-9 ]+?)(?:\s*\([^)]*\))?:\s*(.*)$")  # 'Author (Stanzas 2-5 ): ...'
# A few files carry Mac Roman quotes and a dagger ('died'), read here as Latin-1.
MAC_ROMAN = str.maketrans({"\u00d2": '"', "\u00d3": '"', "\u00d5": "'", "\u00dd": "+"})


def clean(text):
    """Drop the edition's _italic_ markers and stray quotes and spaces."""
    text = text.replace("_", "")
    return " ".join(text.split()).strip().strip('"').strip() or None


def parse(name, raw):
    lines = [l.strip() for l in raw.decode("latin-1").translate(MAC_ROMAN).splitlines()]
    title = next((l for l in lines if l.startswith('"')), None)
    # Stanza 1 starts '1.'; when unnumbered, the text starts after the
    # '(St. Louis: Concordia Publishing House, 1941)' line.
    first = next((l for l in lines if re.match(r"^1\.\s*\S", l)), None)
    if first is None and "Text From:" in lines:
        after = lines[lines.index("Text From:"):]
        start = next((i for i, l in enumerate(after) if l.startswith("(")), None)
        first = next((l for l in after[start + 1:] if l), None) if start is not None else None
    first = re.sub(r"^1\.\s*", "", first) if first else None
    notes = {}
    if "Notes:" in lines:
        for l in lines[lines.index("Notes:") + 1:]:
            if l.startswith("___") or l.startswith("This text was"):
                break
            m = NOTE.match(l)
            if m and m.group(1) in ("Author", "Translated by", "Titled", "Tune"):
                notes.setdefault(m.group(1), m.group(2))
    original = notes.get("Titled")
    if original:
        original = re.sub(r'^\W*VV: ed:\s*', "", original)  # an editing note left in tlh168.txt
    if original and '"' in original:
        # 'Titled: "Christus ist erstanden" (Based on ...)': the first quoted part
        quoted = re.findall(r'"([^"]+)"', original)
        original = quoted[0] if quoted else original
    return {
        "number": int(re.search(r"(\d+)", name).group(1)),
        "title": clean(title or ""),
        "first_line": clean((first or "").rstrip(",;:")),
        "author": clean(notes.get("Author", "")),
        "translator": clean(notes.get("Translated by", "")),
        "original_title": clean(original or ""),
        "tune": clean(notes.get("Tune", "")),
    }


def main():
    if len(sys.argv) > 1:
        data = Path(sys.argv[1]).read_bytes()
    else:
        with urllib.request.urlopen(URL) as resp:
            data = resp.read()
    rows = []
    with zipfile.ZipFile(io.BytesIO(data)) as z:
        for name in sorted(z.namelist()):
            if not re.fullmatch(r"(?:.*/)?tlh\d+\.txt", name, re.I):
                continue
            row = parse(name, z.read(name))
            if row["number"] not in SKIP:
                rows.append(row)
    rows.sort(key=lambda r: r["number"])
    with open(OUT, "w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=list(rows[0]))
        w.writeheader()
        w.writerows(rows)
    missing = sorted(set(range(1, 661)) - {r["number"] for r in rows})
    print(f"wrote {OUT.name}: {len(rows)} hymns, "
          f"{sum(1 for r in rows if r['original_title'])} with an original first line; "
          f"missing {len(missing)}: {missing}")


if __name__ == "__main__":
    main()
