# Sehling Kirchenordnungen Corpus — Reference Guide

This corpus is a compiled, document-segmented extraction of Emil Sehling's
*Die evangelischen Kirchenordnungen des XVI. Jahrhunderts* (church orders
of the 16th-century German Reformation), scraped from Heidelberg's
digi.hadw-bw.de digitization. It covers all 24 Bände (30 physical
volumes/Teilbände, since some Bände were split for printing) plus two
register/index volumes.

## What's in each file

Every volume has a compiled `.md` and `.json`, both with the same
structure: a legend at the top explaining apparatus/OCR conventions,
followed by one entry per document. Each document carries:

- **Citation** — e.g. `Sehling 7, I/Bremen Nr. 3`. The Band number, then
  the Roman-numbered Part and/or place name, then the document number
  Sehling himself assigned. A few volumes cite differently (bare-arabic
  numbering, or no number at all for a short, undivided section) — the
  citation always reflects whatever Sehling's own apparatus used, so
  cite it as given.
- **Heading** — place and year, e.g. "Bremen — Vörder Kirchenordnung,
  1577."
- **Page range** — the printed page numbers in Sehling's own volume, not
  the digital scan numbers.
- **Full text** — the complete OCR'd German/Latin/Low German text for
  that document, including its apparatus (footnotes, source citations,
  editorial brackets) inline with the body text.

## What this corpus does NOT do

**Apparatus and body text are not separated.** Sehling's footnotes,
manuscript variants, and editorial brackets are interleaved with the main
text exactly as printed, distinguished only by typography that OCR
mostly discards. Telling them apart reliably needs the facsimile image,
not just the extracted text — so that separation is left to translation
time, the same way it already is for other facsimile-based work. The
legend at the top of each file explains the conventions Sehling used, as
a guide for that judgment call.

**OCR is not corrected.** This is deliberate, not an oversight — it
matches the existing two-step workflow (below): conservative cleanup
happens as its own pass, not baked into the corpus ahead of time.

**A few named limitations exist and are safe to proceed past:**
- An ordinal-number/heading ambiguity occasionally produces a spurious
  short "document" (e.g. a sentence starting "2. Pfarrstelle...").
  Harmless — the surrounding real documents are unaffected.
- eko12's Kaufbeuren section is genuinely empty of a source text (the
  city's Reformation was suppressed before producing a lasting church
  order) — confirmed by reading the actual pages, not a parsing gap.
- A handful of documents are labeled `heading_source: "toc_only"` in the
  JSON — these are sections where no internal document heading was
  detected, so the whole section (correctly) stayed as one undivided
  unit rather than being split, or mis-split, incorrectly.

None of these lose or corrupt text. Worst case, a document's
auto-generated title or boundary is slightly off; the actual content is
always fully present and readable.

## Translating from this corpus

Apply the existing two-command workflow directly to any document's text
from this corpus:

- **E:** conservative OCR cleanup against the text as given (and against
  the facsimile image, when checking against page scans as usual).
- **T:** complete, literal, source-close English translation. No
  skipping or summarizing. Flag uncertainty explicitly rather than
  silently resolving it.

**One corpus-specific thing worth knowing going in**: a document's own
citation and heading already give the place and year — that context
doesn't need to be re-derived from the text itself, and can be trusted
as Sehling's own attribution.

## Cross-referencing a person, place, or subject across the whole corpus

Two files link Sehling's own register volumes to the actual documents:
`eko_reg_linked.json` (general index, all 24 Bände, ~99.97% resolved) and
`eko_reg_6_7_linked.json` (regional index, Bände VI–VII only, partial —
see below). Each entry looks like:

```json
{
  "entry": "Bugenhagen, Johannes",
  "links": [
    {"volume": "eko6_1", "page": 348, "citation": "Sehling 6, ...",
     "heading": "..."},
    ...
  ],
  "unresolved": [...]
}
```

To find everything the edition says about a person, place, or subject:
look up the `entry` name, then open each linked document by its
`citation`/`volume`+page in the corresponding compiled file. This is
real, index-based coverage — not a text search — so it surfaces
mentions a keyword search would miss (older spellings, Latin forms,
etc.), and it's the fastest way to assemble every passage on one topic
before translating them as a set.

**One structural caveat**: several Bände were split into Teilbände that
were bound as genuinely separate physical books, each restarting its own
page numbering near page 1 — confirmed directly for `eko7_1`/`eko7_2_2`,
`eko17_1`/`eko17_2`, and `eko20_1`/`eko20_2`, which all fully overlap in
absolute page numbers (`eko6_1`/`eko6_2` and `eko19_1`/`eko19_2`, by
contrast, are continuously paginated across their halves and don't have
this problem). `eko_reg_6_7_linked.json`'s `unresolved` entries marked
"ambiguous" (all in Band 7, since that's the only overlapping pair
`eko_reg_6_7` actually covers) are real cases the register genuinely
cannot disambiguate from citation data alone — not a bug, a limit of the
source material. `eko_reg_linked.json` doesn't have this problem
anywhere, since its own citations always specify the exact sub-volume
("XVII/2:", never bare "Band 17:"). See `DB_GUIDE.md` for how the
database schema handles this.

## Multi-Teilband volumes

Eleven volumes are split into Teilbände that were originally one Band:
eko6 (1–2), eko7 (1, 2_1, 2_2), eko17 (1–2), eko19 (1–2), eko20 (1–2). If
working through a whole Band at a time is more natural than
Teilband-by-Teilband, these can be merged into one continuous file with:

```
py sehling_parser.py eko6_1 eko6_2 --merge --out-name eko6 --offline
py sehling_parser.py eko7_1 eko7_2_1 eko7_2_2 --merge --out-name eko7 --offline
py sehling_parser.py eko17_1 eko17_2 --merge --out-name eko17 --offline
py sehling_parser.py eko19_1 eko19_2 --merge --out-name eko19 --offline
py sehling_parser.py eko20_1 eko20_2 --merge --out-name eko20 --offline
```

Cheap to run — it recompiles from the already-cached data, no
re-fetching. Each document's citation stays exactly as it would be if
read individually: the merge does not renumber anything, it just
combines the original Teilbände's data into one file for continuous
reading, which is the only thing it's for.

**Merged output is for reading only — never feed it to `link_register.py`
or `build_database.py`.** A merged file's documents are the exact same
documents already present in the original Teilband directories, just
repackaged; ingesting both would duplicate content, and for the three
overlapping Bände above, a merged volume's page range spans the full
union of its Teilbände, which corrupts the very disambiguation those
scripts depend on. Both scripts detect and skip merged output
automatically, so this is a safety net rather than something to manage
by hand — but the original Teilband directories are what actually
matter for register-linking and the database, and should never be
deleted even once merged versions exist alongside them.
