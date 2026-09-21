"""
build_database.py -- builds a searchable SQLite database (with full-text
search) from the compiled Sehling corpus and the register-linking
output. Produces two core tables -- `documents` (every segmented church
order) and `index_entries` (every person/place/subject from Sehling's
own registers) -- plus `index_links`, which connects them.

Run in the same directory as your `sehling/` folder, after both
registers have been linked:

    py link_register.py eko_reg
    py link_register.py eko_reg_6_7
    py build_database.py

Produces `eko.db` by default.

SCHEMA
------
documents(id, volume_id, band_number, citation, heading, part_roman,
          part_title, place, title, year, doc_num, page_start, page_end,
          printed_page_range, digital_page_range, heading_source,
          image_url, text)

  volume_id is ALWAYS the fully-qualified sub-volume id ('eko7_1',
  'eko17_2', ...), never just a Band number -- confirmed necessary
  because several Bande are split into Teilbande that independently
  restart pagination near page 1 (eko7_1/eko7_2_2, eko17_1/eko17_2,
  eko20_1/eko20_2 all fully overlap in absolute page numbers, confirmed
  directly against every split volume's real page range). page_start
  and page_end are unique only within a volume_id, never globally.
  band_number is kept as a separate column for browsing/filtering by
  Band, but is deliberately NOT part of any uniqueness constraint, so a
  "Band 7, page 104" style lookup without a volume_id can never
  silently return the wrong document.

  page_start/page_end are NULL when a document's own printed_page_range
  doesn't parse to a plain (or letter-suffixed) integer at all -- real
  and expected for front/back matter (labelled like "a-f", "Tafel 8").
  The row still exists and is still full-text searchable; it just can't
  be a citation-link target by page number.

index_entries(id, entry_name, register_source)

  One row per unique (entry_name, register_source) pair -- source is
  'eko_reg' (the general index, all 24 Bande) or 'eko_reg_6_7' (the
  regional index, Bande VI-VII only).

index_links(id, entry_id, document_id, volume_id, page, status,
            resolved_via)

  One row per citation the entry's register data pointed to.
  status is 'resolved' (document_id is set, a real match), 'ambiguous'
  (document_id is NULL, volume_id/page identify ONE of several real
  candidates -- one row per candidate, all sharing the same
  entry_id/page/status, so a query surfaces every possibility rather
  than silently picking one or dropping the citation), or 'unresolved'
  (a citation that genuinely couldn't be matched to anything -- kept
  for transparency rather than discarded, matching link_register.py's
  own principle throughout). resolved_via records which of
  link_register.py's four resolution tiers produced a 'resolved' row.

Also builds an FTS5 virtual table `documents_fts` over `documents.text`
(plus citation/heading, unindexed) for full-text search, e.g.:

    SELECT d.citation, d.heading FROM documents_fts f
    JOIN documents d ON d.id = f.rowid
    WHERE documents_fts MATCH 'Kirchenordnung'
"""

import argparse
import json
import re
import sqlite3
from pathlib import Path
from typing import Optional

SCHEMA = """
CREATE TABLE documents (
    id INTEGER PRIMARY KEY,
    volume_id TEXT NOT NULL,
    band_number INTEGER,
    citation TEXT NOT NULL,
    heading TEXT,
    part_roman TEXT,
    part_title TEXT,
    place TEXT,
    title TEXT,
    year TEXT,
    doc_num TEXT,
    page_start INTEGER,
    page_end INTEGER,
    printed_page_range TEXT,
    digital_page_range TEXT,
    heading_source TEXT,
    image_url TEXT,
    text TEXT NOT NULL
);
CREATE INDEX idx_documents_volume_page ON documents(volume_id, page_start);
CREATE INDEX idx_documents_band_page ON documents(band_number, page_start);
CREATE INDEX idx_documents_volume ON documents(volume_id);

CREATE VIRTUAL TABLE documents_fts USING fts5(
    text, citation UNINDEXED, heading UNINDEXED,
    content='documents', content_rowid='id'
);

CREATE TABLE index_entries (
    id INTEGER PRIMARY KEY,
    entry_name TEXT NOT NULL,
    register_source TEXT NOT NULL,
    UNIQUE(entry_name, register_source)
);
CREATE INDEX idx_entries_name ON index_entries(entry_name);

CREATE TABLE index_links (
    id INTEGER PRIMARY KEY,
    entry_id INTEGER NOT NULL REFERENCES index_entries(id),
    document_id INTEGER REFERENCES documents(id),
    volume_id TEXT,
    page INTEGER,
    status TEXT NOT NULL,
    resolved_via TEXT
);
CREATE INDEX idx_links_entry ON index_links(entry_id);
CREATE INDEX idx_links_document ON index_links(document_id);
CREATE INDEX idx_links_status ON index_links(status);
"""


def parse_page_int(token: str) -> Optional[int]:
    """Leading integer from a page label, handling the confirmed
    letter-suffix insertion-page convention (e.g. "725a" -> 725) the
    same way sehling_parser.py's printed_page_from_label does. None for
    labels with no leading digit at all (front/back matter like "a",
    "Tafel 8")."""
    token = token.strip()
    m = re.match(r"(\d+)", token)
    return int(m.group(1)) if m else None


def parse_page_range(printed_page_range: str) -> tuple:
    parts = re.split(r"[\u2013-]", printed_page_range.strip())
    if len(parts) == 1:
        n = parse_page_int(parts[0])
        return n, n
    return parse_page_int(parts[0]), parse_page_int(parts[-1])


def load_documents(root: Path, conn: sqlite3.Connection) -> dict:
    """Inserts every volume's documents; returns volume_id -> sorted
    [(page_start, page_end, document_id)] for resolving index_links."""
    volume_ranges: dict = {}
    cur = conn.cursor()
    volumes = sorted(d.name for d in root.iterdir() if d.is_dir())
    print(f"Loading documents from {len(volumes)} volumes under {root}/ ...")

    total_docs = 0
    for vol in volumes:
        json_path = root / vol / f"{vol}.json"
        if not json_path.exists():
            print(f"  ! {vol}: no {vol}.json, skipping")
            continue
        with json_path.open(encoding="utf-8") as f:
            data = json.load(f)
        sources = data.get("sources", [])
        # A merged (--merge) output's own "sources" array has one entry
        # PER ORIGINAL TEILBAND COMBINED IN, confirmed against
        # sehling_parser.py's own merge code (it appends one SourceResult
        # per volume id passed to --merge, with no renumbering). Skipped
        # here, not ingested: its content duplicates the original,
        # finer-grained Teilband directories that normally still sit
        # alongside it in the same root -- ingesting both would insert
        # every document from whichever Teilband happened to be listed
        # first in the merge a second time (this function used to read
        # only sources[0], which is exactly that bug: it silently
        # dropped every OTHER Teilband's documents from the merged file
        # while still double-inserting the first one via its own,
        # separately-present original directory).
        if len(sources) > 1:
            print(f"  - {vol}: skipped (a --merge output combining multiple Teilbande -- "
                  f"the original Teilband directories already cover this content)")
            continue
        band_number = data.get("band_number")
        docs = sources[0].get("documents", []) if sources else []
        ranges = []
        for d in docs:
            ppr = d.get("printed_page_range") or ""
            page_start, page_end = parse_page_range(ppr) if ppr else (None, None)
            cur.execute(
                "INSERT INTO documents (volume_id, band_number, citation, heading, "
                "part_roman, part_title, place, title, year, doc_num, page_start, "
                "page_end, printed_page_range, digital_page_range, heading_source, "
                "image_url, text) VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)",
                (vol, band_number, d.get("citation"), d.get("heading"),
                 d.get("part_roman"), d.get("part_title"), d.get("place_label"),
                 d.get("doc_title"), d.get("doc_year"), d.get("doc_num"),
                 page_start, page_end, ppr, d.get("digital_page_range"),
                 d.get("heading_source"), d.get("first_page_image_url"),
                 d.get("text") or ""),
            )
            doc_id = cur.lastrowid
            if page_start is not None and page_end is not None:
                ranges.append((page_start, page_end, doc_id))
        ranges.sort()
        volume_ranges[vol] = ranges
        total_docs += len(docs)
        print(f"  {vol}: {len(docs)} documents")

    conn.commit()
    print(f"  TOTAL: {total_docs} documents\n")
    return volume_ranges


def resolve_document_id(volume_id: str, page: int, volume_ranges: dict) -> Optional[int]:
    for start, end, doc_id in volume_ranges.get(volume_id, []):
        if start <= page <= end:
            return doc_id
    return None


def load_index_links(linked_json_path: Path, register_source: str,
                      volume_ranges: dict, conn: sqlite3.Connection) -> None:
    if not linked_json_path.exists():
        print(f"  ! {linked_json_path} not found -- run link_register.py first. "
              f"Skipping {register_source} (index_entries/index_links will have no rows for it).")
        return
    with linked_json_path.open(encoding="utf-8") as f:
        results = json.load(f)

    cur = conn.cursor()
    entry_count = link_count = 0
    for r in results:
        entry_name = r["entry"]
        cur.execute(
            "INSERT INTO index_entries (entry_name, register_source) VALUES (?,?) "
            "ON CONFLICT(entry_name, register_source) DO NOTHING",
            (entry_name, register_source),
        )
        cur.execute(
            "SELECT id FROM index_entries WHERE entry_name=? AND register_source=?",
            (entry_name, register_source),
        )
        entry_id = cur.fetchone()[0]
        entry_count += 1

        for link in r.get("links", []):
            vid, page = link["volume"], link["page"]
            doc_id = resolve_document_id(vid, page, volume_ranges)
            cur.execute(
                "INSERT INTO index_links (entry_id, document_id, volume_id, page, "
                "status, resolved_via) VALUES (?,?,?,?,?,?)",
                (entry_id, doc_id, vid, page,
                 "resolved" if doc_id else "unresolved", link.get("resolved_via")),
            )
            link_count += 1

        for u in r.get("unresolved", []):
            page = u.get("page")
            reason = u.get("reason", "")
            if reason.startswith("ambiguous") and u.get("candidates"):
                for cand in u["candidates"]:
                    cur.execute(
                        "INSERT INTO index_links (entry_id, document_id, volume_id, "
                        "page, status, resolved_via) VALUES (?,?,?,?,?,?)",
                        (entry_id, None, cand, page, "ambiguous", None),
                    )
                    link_count += 1
            else:
                cur.execute(
                    "INSERT INTO index_links (entry_id, document_id, volume_id, page, "
                    "status, resolved_via) VALUES (?,?,?,?,?,?)",
                    (entry_id, None, u.get("volume"), page, "unresolved", None),
                )
                link_count += 1

    conn.commit()
    print(f"  {register_source}: {entry_count} entries, {link_count} links")


def build(root: Path, db_path: Path, eko_reg_linked: Path, eko_reg_6_7_linked: Path) -> None:
    if db_path.exists():
        db_path.unlink()
    conn = sqlite3.connect(db_path)
    conn.executescript(SCHEMA)

    volume_ranges = load_documents(root, conn)

    print("Loading register links...")
    load_index_links(eko_reg_linked, "eko_reg", volume_ranges, conn)
    load_index_links(eko_reg_6_7_linked, "eko_reg_6_7", volume_ranges, conn)

    print("\nBuilding full-text search index...")
    conn.execute("INSERT INTO documents_fts(rowid, text, citation, heading) "
                 "SELECT id, text, citation, heading FROM documents")
    conn.commit()

    cur = conn.cursor()
    cur.execute("SELECT COUNT(*) FROM documents")
    doc_count = cur.fetchone()[0]
    cur.execute("SELECT COUNT(*) FROM index_entries")
    entry_count = cur.fetchone()[0]
    cur.execute("SELECT COUNT(*) FROM index_links")
    link_count = cur.fetchone()[0]
    cur.execute("SELECT status, COUNT(*) FROM index_links GROUP BY status")
    status_counts = cur.fetchall()

    conn.close()

    print(f"\n{'=' * 60}\nDONE\n{'=' * 60}")
    print(f"  documents:      {doc_count}")
    print(f"  index_entries:  {entry_count}")
    print(f"  index_links:    {link_count}")
    for status, count in status_counts:
        print(f"    {status:<12} {count}")
    print(f"\nDatabase: {db_path}  ({db_path.stat().st_size / (1024 * 1024):.1f} MB)")


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("--root", default="sehling", help="Path to the sehling/ output directory (default: sehling)")
    parser.add_argument("--db", default="eko.db", help="Output SQLite database path (default: eko.db)")
    parser.add_argument("--eko-reg-linked", default="eko_reg_linked.json")
    parser.add_argument("--eko-reg-6-7-linked", default="eko_reg_6_7_linked.json")
    args = parser.parse_args()
    build(Path(args.root), Path(args.db), Path(args.eko_reg_linked), Path(args.eko_reg_6_7_linked))


if __name__ == "__main__":
    main()
