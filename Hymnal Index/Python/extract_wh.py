#!/usr/bin/env python3
"""Extract a hymn index from WH.pdf (Walther's Hymnal, tr. Matthew Carver) into wh_index.csv.

Usage: python3 extract_wh.py        (needs pdftotext from poppler-utils)

Only index data is extracted: hymn number, English and German first lines (from
the book's two first-line indexes), and each hymn's tune heading (tune name and
the hymnal settings it points to, e.g. 'TLH 237; LW 215; LSB 947'). WH hymn
numbers are KELG numbers. Two-part hymns (417a/b, 424a/b) are kept under one
number, with their first lines joined by ' / '.

wh_index.csv is plain text so it can be checked and hand-corrected; build_db.py
loads it.
"""
import csv
import re
import subprocess
from collections import defaultdict
from pathlib import Path

HERE = Path(__file__).resolve().parent
PDF = HERE / "WH.pdf"
OUT = HERE / "wh_index.csv"

# PDF page ranges (not printed page numbers)
ENGLISH_INDEX = (446, 450)
GERMAN_INDEX = (451, 455)
HYMNS = (23, 418)

NUMBER = r"(\d{1,3})[a-z]?"
INDEX_ENTRY = re.compile(rf"(\S.*?)(?:(?:\s*\.)+\s*|\s+){NUMBER}\.?(?=\s{{2,}}|\s*$)")
# A tune heading: 'Tune: Name. 58. [TLH 69; ...]', or the same without 'Tune:'
# ('Or Other tune. 2. [...]' continues the heading above it.)
HEADING = re.compile(r"Tune:|^(?!\s*Or\s).*\S\.\s+\d{1,3}\.\s+\[")
PAGE_FURNITURE = re.compile(
    r"PREVIEW SAMPLE|Walther's Hymnal\. English|Published by Concordia|\.indd|^\s*\[\d+\]\s*$"
)


def pdf_text(first, last):
    return subprocess.run(
        ["pdftotext", "-layout", "-f", str(first), "-l", str(last), str(PDF), "-"],
        capture_output=True, text=True, check=True,
    ).stdout


def normalize(text):
    return " ".join(re.sub(r"[^\w\s]", " ", text.lower()).split())


def read_index(pages):
    """{number: [first line, ...]} from a two-column first-line index."""
    out = defaultdict(list)
    for line in pdf_text(*pages).splitlines():
        if PAGE_FURNITURE.search(line) or re.search(r"ndex of [Ff]irst [Ll]ines", line):
            continue
        line = re.sub(r"First Line\s+Hymn", "", line)
        for m in INDEX_ENTRY.finditer(line):
            out[int(m.group(2))].append(m.group(1).strip().rstrip(",;:").strip())
    return out


def heading_number(heading_line, after, before):
    """The hymn number printed beside a tune heading, or None."""
    m = re.search(rf"(?:^|\s{{2,}}){NUMBER}\s{{2,}}\S", heading_line) \
        or re.search(rf"(?:\]|\.)\s{{2,}}{NUMBER}(?=\s{{2,}}|\s*$)", heading_line)
    if m:
        return int(m.group(1))
    for line in after + before[::-1]:
        m = re.search(rf"\s{{2,}}{NUMBER}\s*$", line) or re.fullmatch(rf"\s*{NUMBER}\s*", line)
        if m:
            return int(m.group(1))
    return None


def number_by_first_line(first, english):
    """Fallback: the hymn whose English index entry starts its first stanza line."""
    first = normalize(first or "")
    if not first:
        return None
    hits = {n for n, titles in english.items() for t in titles
            if first == normalize(t) or first.startswith(normalize(t) + " ")}
    return hits.pop() if len(hits) == 1 else None


def read_hymn_headings(english):
    """{number: (tune, settings, first stanza line)} from the hymn pages."""
    lines = [l for l in pdf_text(*HYMNS).splitlines() if not PAGE_FURNITURE.search(l)]
    out = {}
    for i, line in enumerate(lines):
        if not HEADING.search(line):
            continue
        # The heading runs from here to the first stanza ('1. ...').
        j = i + 1
        while j < len(lines) and not re.match(r"\s*1\.\s", lines[j]) and not HEADING.search(lines[j]):
            j += 1
        first = None
        if j < len(lines):
            m = re.match(r"\s*1\.\s+(.+?)(?:\s{3,}|\s+\d+\.\s|$)", lines[j])
            first = m.group(1).strip() if m else None

        number = heading_number(line, lines[i + 1:j], lines[max(0, i - 3):i]) \
            or number_by_first_line(first, english)
        if number is None:
            print(f"no hymn number for: {line.strip()}")
            continue

        text = " ".join(lines[i:j])
        text = text.split("Tune:", 1)[1] if "Tune:" in text else text
        text = text[:text.rindex("]") + 1] if "]" in text else \
            re.sub(rf"\s{{2,}}{NUMBER}(?=\s{{2,}}|\s*$).*", "", text, flags=re.S)
        text = re.sub(rf"^\s*{NUMBER}\s{{2,}}", "", text)
        text = " ".join(text.split())
        tune = re.split(r"[.!?]?\s+\d{1,3}\.(?:\s|$)|\s*\[", text, maxsplit=1)[0].strip().rstrip(".")
        settings = "; ".join(s.strip() for s in re.findall(r"\[([^\]]*)\]", text))
        if number not in out:  # a two-part hymn keeps its first heading
            out[number] = (tune, settings, first)
    return out


def read_cross_references():
    """{number: other number} for hymns printed only as '(See # 85.)'."""
    out = {}
    for line in pdf_text(*HYMNS).splitlines():
        for target, number in re.findall(rf"\(See #\s*(\d+)\.\)\s+{NUMBER}", line):
            out[int(number)] = int(target)
    return out


def main():
    english = read_index(ENGLISH_INDEX)
    german = read_index(GERMAN_INDEX)
    headings = read_hymn_headings(english)
    see = read_cross_references()
    numbers = sorted(set(english) | set(german) | set(headings) | set(see))
    with open(OUT, "w", newline="", encoding="utf-8") as f:
        w = csv.writer(f)
        w.writerow(["number", "english_first_line", "german_first_line", "tune",
                    "tune_settings", "first_stanza_line", "see_number"])
        for n in numbers:
            tune, settings, first = headings.get(n, (None, None, None))
            w.writerow([n, " / ".join(english.get(n, [])), " / ".join(german.get(n, [])),
                        tune, settings, first, see.get(n)])
    missing = [n for n in range(1, max(numbers) + 1) if n not in numbers]
    print(f"wrote {OUT.name}: {len(numbers)} hymns, {len(headings)} with tune headings"
          + (f"; missing numbers: {missing}" if missing else ""))


if __name__ == "__main__":
    main()
