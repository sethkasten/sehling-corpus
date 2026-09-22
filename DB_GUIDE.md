# Sehling Corpus Database — Reference Guide

`eko.db` is a SQLite database built from the compiled corpus
(`sehling/`) and the register-linking output (`eko_reg_linked.json`,
`eko_reg_6_7_linked.json`). See `CORPUS_GUIDE.md` for what the corpus
itself is; this covers the database specifically.

A second, much smaller database — `hymns.db` — is derived from this one
and covers the corpus's chief-hymn prescriptions by Sunday and feast.
See `HYMN_GUIDE.md`.

## Building or rebuilding it

```
py link_register.py eko_reg
py link_register.py eko_reg_6_7
py build_database.py
```

`build_database.py` always rebuilds `eko.db` from scratch (deletes any
existing file at that path first) — there's no incremental update, so
re-run all three whenever the underlying corpus or register linking
changes. Building from the full 32-volume corpus takes well under a
minute and produces roughly 120 MB.

**Never feed merged (`--merge`) volume output into any of this.**
`build_database.py` detects and skips it automatically, so nothing
breaks if it's present — but the original Teilband directories
(`eko6_1`, `eko7_2_1`, etc.) are what this whole pipeline actually runs
on. See `CORPUS_GUIDE.md`'s "Multi-Teilband volumes" section for why.

## Schema

### `documents` — every segmented church order

| Column | Notes |
|---|---|
| `volume_id` | Always the fully-qualified sub-volume id (`eko7_1`, `eko17_2`, ...) — see "The Band-overlap issue" below. Never just a Band number. |
| `band_number` | For browsing/filtering by Band. Not part of any uniqueness constraint. |
| `citation` | e.g. `Sehling 7, I/Bremen Nr. 3` |
| `heading`, `place`, `title`, `year`, `doc_num` | Parsed fields from the same heading a compiled `.md`/`.json` file shows |
| `page_start`, `page_end` | Integers, unique only within a `volume_id`. `NULL` for documents whose page range doesn't parse to a number at all (front/back matter labelled "a–f", "Tafel 8") — the row and its text still exist, it just can't be a citation-link target. |
| `heading_source` | `running_head` (a real detected document heading), `toc_only` (a TOC-level section kept as one undivided unit), or `front_matter`/`back_matter` |
| `image_url` | Direct link to the facsimile page image on Heidelberg's site |
| `text` | Full OCR'd text, uncorrected — see `CORPUS_GUIDE.md` |

### `index_entries` — every person/place/subject from Sehling's own registers

One row per unique `(entry_name, register_source)` pair.
`register_source` is `eko_reg` (general index, all 24 Bände) or
`eko_reg_6_7` (regional index, Bände VI–VII only).

**One thing worth knowing about `eko_reg_6_7` specifically**:
it has separate Personen-/Orts-/Sachregister sections per Band (one set
for Band 6, another for Band 7), so a person discussed in both — e.g.
"Bugenhagen, Johannes" — is consolidated into a single `index_entries`
row (same name, same `register_source`), but can end up with two
`index_links` rows pointing at the exact same document if both Band
sections happened to cite the same page. Not a bug or duplicate
insertion — confirmed directly against the source citations — just a
real feature of how the regional index itself is organized.

### `index_links` — connects the two

One row per citation an entry's register data pointed to.

| `status` | Meaning |
|---|---|
| `resolved` | `document_id` is set — a real, confirmed match. `resolved_via` records which of `link_register.py`'s four resolution tiers found it (`eko_reg_cross_reference`, `page_range`, `eko_reg_interpolation`, `content_match` — `NULL` means it came from `eko_reg`'s own explicit citation, which needs no further disambiguation). |
| `ambiguous` | `document_id` is `NULL`. One row per real candidate volume, same `entry_id`/`page` — a genuine case the source citation data cannot disambiguate (see below), not something silently guessed or dropped. |
| `unresolved` | Couldn't be matched to anything at all (a footnote-fusion artifact, an out-of-range page, etc.) — kept for transparency rather than discarded. |

## The Band-overlap issue, and why it matters here specifically

Three Bände (7, 17, 20) were bound as separate physical Teilbände that
each independently restart page numbering near page 1 — confirmed
directly for every split volume in the corpus (see `CORPUS_GUIDE.md`).
That means **"Band 7, page 104" alone is genuinely ambiguous**; only
`volume_id` + page disambiguates it. This is enforced in the schema, not
just documented:

```sql
-- SAFE: exact volume specified
SELECT * FROM documents WHERE volume_id = 'eko7_1' AND page_start <= 104 AND page_end >= 104;

-- NOT SAFE on its own: can return more than one real document for
-- Bands 7, 17, or 20
SELECT * FROM documents WHERE band_number = 7 AND page_start <= 104 AND page_end >= 104;
```

Confirmed directly: that second query against the real corpus returns
two different genuine documents (one in `eko7_1`, one in `eko7_2_2`).
`band_number` exists for browsing ("show me everything in Band 7"), not
for pinpointing a specific page.

## Example queries

**Full-text search:**
```sql
SELECT d.citation, d.heading
FROM documents_fts f JOIN documents d ON d.id = f.rowid
WHERE documents_fts MATCH 'Katechismus';
```

**Everything the edition says about a person or place** (the main
reason `index_entries`/`index_links` exist — surfaces older spellings
and Latin forms a text search would miss):
```sql
SELECT d.citation, d.heading, d.volume_id, d.page_start
FROM index_entries e
JOIN index_links l ON l.entry_id = e.id
JOIN documents d ON d.id = l.document_id
WHERE e.entry_name = 'Bugenhagen' AND e.register_source = 'eko_reg'
  AND l.status = 'resolved';
```

**Include the honestly-ambiguous cases too**, rather than only the
clean matches — useful when doing thorough research on a topic rather
than a quick lookup:
```sql
SELECT e.entry_name, l.volume_id, l.page, l.status
FROM index_entries e
JOIN index_links l ON l.entry_id = e.id
WHERE e.entry_name = 'Some Entry' AND l.status IN ('resolved', 'ambiguous');
```

**Browse a whole Band, ordered correctly across its Teilbände:**
```sql
SELECT volume_id, citation, heading, page_start
FROM documents
WHERE band_number = 7 AND heading_source = 'running_head'
ORDER BY volume_id, page_start;
```

**How complete is the register linking, by status:**
```sql
SELECT register_source, status, COUNT(*)
FROM index_links l
JOIN index_entries e ON e.id = l.entry_id
GROUP BY register_source, status;
```
