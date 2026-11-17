#!/usr/bin/env python3
"""Read the WELS12 hymns' own pages on musicanet.org into WELS12/WELS12_texts.csv.

Usage: python3 fetch_wels12_texts.py [CACHE_DIR]

The index (WELS12/1912.html, ...) links 320 of its hymns to a page of their own
(Lieder/<name>.html) with the German text, its author, its melody and, for 178,
a link to an English translation (hymn/<name>.htm: 177 pages, as two hymns share
one). Pages are taken from CACHE_DIR when they are there (Lieder/ and hymn/
subfolders), else downloaded, a second apart. Kept for each hymn with a page: the page, its title, the text's
first two lines, the author and the melody as the page gives them, and the
English page with its title and first line. One link, Lieder/oweltsie.html
(O Welt, sieh hier dein Leben), is dead.
"""
import csv
import html
import re
import sys
import time
import urllib.request
from pathlib import Path

HERE = Path(__file__).resolve().parent
BASE = "https://www.musicanet.org/robokopp/"
PAGES = ("1912.html", "19122.html", "19123.html")
OUT = HERE / "WELS12" / "WELS12_texts.csv"


def fetch(path, cache):
    local = cache / path if cache else None
    if local and local.exists():
        return local.read_bytes().decode("utf-8", "replace")
    time.sleep(1)
    try:
        with urllib.request.urlopen(BASE + path) as r:
            data = r.read()
    except OSError:
        return None
    if local:
        local.parent.mkdir(parents=True, exist_ok=True)
        local.write_bytes(data)
    return data.decode("utf-8", "replace")


def text_of(fragment):
    return " ".join(html.unescape(re.sub(r"<[^>]+>", " ", fragment)).split())


def read(page):
    s = re.sub(r"\s+", " ", page)
    title = re.search(r"<H1>(.*?)</H1>", s, re.I)
    heads = [text_of(h) for h in re.findall(r"<div class='head-size'>(.*?)</div>", s, re.I)]
    body = re.search(r'<TD[^>]*class="colonne"[^>]*>(.*?)(?:</TD>|<TD|</TR>|</TABLE>|\| Liederverzeichnis|\| Hymn Index)', s, re.I)
    lines = [text_of(p) for p in re.split(r"<BR>|<P>", body.group(1), flags=re.I)] if body else []
    lines = [l for l in lines if l]
    melody = next((h for h in heads if re.match(r"Melod", h)), "")
    melody = re.sub(r"^Melod(?:ie|y)\s*-?\s*", "", melody).strip()
    author = next((h.split(";")[0].strip() for h in heads if not re.match(r"Melod|\|", h)), "")
    english = re.search(r'<A HREF="\.\./hymn/([^"]+)"[^>]*>\s*englischer', s, re.I)
    return {"title": text_of(title.group(1)) if title else "", "opening": " / ".join(lines[:2]),
            "author": author, "melody": melody, "english": english.group(1) if english else ""}


def main():
    cache = Path(sys.argv[1]) if len(sys.argv) > 1 else None
    rows = []
    for name in PAGES:
        s = re.sub(r"\s+", " ", (HERE / "WELS12" / name).read_bytes().decode("utf-8"))
        body = s[s.index("<BLOCKQUOTE>"):]
        for m in re.finditer(r"(\d+)\s*([a-z]?)\.\s*(.*?)<BR>", body, re.I):
            link = re.search(r'<A HREF="(Lieder/[^"]+)"', m.group(3), re.I)
            if link:
                rows.append((m.group(1) + m.group(2), link.group(1)))
    out = []
    for number, link in rows:
        page = fetch(link, cache)
        if page is None:
            out.append({"number": number, "page": link, "title": "(dead link)"})
            continue
        r = read(page)
        english_title = english_first = ""
        if r["english"]:
            e = fetch("hymn/" + r["english"], cache)
            if e:
                e = read(e)
                english_title, english_first = e["title"], e["opening"].split(" / ")[0]
        out.append({"number": number, "page": link, "title": r["title"], "opening": r["opening"],
                    "author": r["author"], "melody": r["melody"], "english_page": r["english"] and "hymn/" + r["english"],
                    "english_title": english_title, "english_first_line": english_first})
    fields = ["number", "page", "title", "opening", "author", "melody", "english_page", "english_title",
              "english_first_line"]
    with open(OUT, "w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fields)
        w.writeheader()
        w.writerows(out)
    print(f"{len(out)} hymn pages -> {OUT.relative_to(HERE)}")


if __name__ == "__main__":
    main()
