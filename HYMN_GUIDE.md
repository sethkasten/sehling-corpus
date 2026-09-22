# Hymn Tables — Reference Guide

`hymns.db` is a SQLite database of the **chief-hymn prescriptions** found
in the corpus: the places where a church order assigns a specific hymn to
a specific Sunday, feast or occasion. See `CORPUS_GUIDE.md` for the
corpus itself and `DB_GUIDE.md` for `eko.db`; this covers the hymn tables
specifically.

## Building or rebuilding it

```
py hymn_tables/build_hymn_db.py
```

The builder reads the pre-extracted `hymn_tables/rows_*.json` files, not
the corpus, so it needs **no `eko.db`** — it runs in about a second and
produces roughly 240 KB. Like `eko.db`, it always rebuilds from scratch.

`build_hymn_db.py` loads only the Sehling orders. The hymnal and
compilation sources are added by a second step, which must follow it:

```
py hymn_tables/build_hymn_db.py
py hymn_tables/merge_sources.py
```

To re-extract from the corpus instead — after an OCR fix, say — re-run
the parsers. The first four *do* need `eko.db` (see `DB_GUIDE.md`), since
they read the document text out of it; the last three read the source
documents committed under `hymn_tables/`:

```
py hymn_tables/parse_weissenfels.py
py hymn_tables/parse_pommern.py
py hymn_tables/parse_latin.py
py hymn_tables/parse_german.py
py hymn_tables/parse_liliencron.py
py hymn_tables/parse_ludecus.py          # needs python-docx
py hymn_tables/parse_hotd_selnecker.py
```

Each prints what it found; each also exposes a `parse()`/`parse_all()`
returning `(occasion, title, source)` tuples, which is how the `rows_*.json`
files are produced.

## Two layers of evidence

The database holds **3,015 prescriptions** from **35 witnesses**, in two
quite different evidentiary layers. Keep them apart when you draw
conclusions:

| Layer | Rows | What it is |
|---|---:|---|
| Sehling church orders | 466 | 16th-c. orders prescribing hymns, read from the corpus itself |
| Hymnals and compilations | 2,549 | later hymnals and modern conflations, read from separate documents |

A row in the first layer is a church *ordering* what shall be sung. A row
in the second is a hymnal or editor *recording* what was sung, sometimes
centuries later. They are not the same claim.

### Witness vs. compilation, and why it matters

Several of these sources are **compilations that cite other sources**.
Liliencron's concordance collates fifteen hymnals; the Hymn of the Day
table collates eight schemes. So each row names two things, folded into
the `source` column as `Witness (via Compilation)`:

- the **witness** — whose appointment this actually is (Keuchenthal 1573, Carpzov, Selnecker…)
- the **compilation** — the document it was read out of

**Deduplication is on the witness, not the document.** Selnecker appears
three times over: in his own prose account, in Liliencron as `Se.`, and in
the Hymn of the Day table as `S`. He is counted **once**, with every
attesting compilation listed:

```sql
SELECT occasion, original_title, source FROM hymn_prescriptions
WHERE source LIKE 'Selnecker%' AND source LIKE '%;%';
```
> `Sunday after Ascension (Exaudi) | Wo Gott der Herr nicht bei uns hält |`
> `Selnecker (via Hymn of the Day table; Liliencron concordance; Selnecker's own account)`

40 such overlapping attestations were folded this way. Counting sources
rather than witnesses would have inflated Selnecker roughly threefold.

### Sigla do not mean the same thing in different compilations

**`K.` in Liliencron is Keuchenthal's *Kirchengesänge* of 1573. `K` in the
Hymn of the Day table is the modern SELK hymnal.** The sigla are
namespaced per compilation in the parsers and must never be pooled. The
same applies to `S`/`Se.` and to `L`/`LL`/`LK`.

## Which orders are covered

Eight Sehling orders carry a hymn table worth extracting. They are **not**
all the same kind of document:

| Source | Rows | Kind |
|---|---:|---|
| Pommern, Agenda 1569 (`Sehling 4`, pp. 425–480) | 166 | Low German, per-Sunday, 2–4 options each |
| Pfalz-Zweibrücken 1565 (`Sehling 18, I/23`, pp. 337–341) | 121 | German, **3-week rotating cycle** by liturgical slot |
| Hof, *Ordo ecclesiasticus* 1592 (`Sehling 11, IV.20`, pp. 407–477) | 58 | Latin office propers, per-Sunday |
| Weissenfels 1578 (`Sehling 1, Nr. 159`, pp. 693–696) | 55 | German, one hymn per Sunday, Advent 1 → Trinity 25 |
| Mansfeld (`Sehling 2`, pp. 210–247) | 27 | German, by season |
| Hohenlohe 1596 (`Sehling 15, Nr. 54`, pp. 641–660) | 21 | German, by feast |
| Nördlingen 1579 (`Sehling 12, VIII.7`, pp. 335–393) | 12 | Latin propers, per-Sunday |
| Heilbronn 1543 (`Sehling 17, II/17`, pp. 320–326) | 6 | Latin Vespers propers |

Weissenfels is the closest thing in the corpus to a modern *Hauptlied* /
*Wochenlied* table. Note that the term `Hauptlied` itself appears
**nowhere** in the corpus — it is later terminology. Searching for it
finds nothing; these tables are what the concept actually looks like in
the 16th century.

### The hymnal and compilation sources

| Source | Rows | Witnesses | What it is |
|---|---:|---:|---|
| Liliencron, *de tempore* concordance (pp. 61–77) | 1,823 | 15 | Collates fifteen hymnals, 1545–1694, Sunday by Sunday |
| Hymn of the Day conflation table | 371 | 12 | Modern table collating Carpzov, Gehrke, SELK, Selnecker, Zion, LW, LSB and others |
| Ludecus, *Ordo cantionum Germanicarum* (1589) | 309 | 1 | A single order, German incipits with English translation |
| Selnecker, own account | 46 | 1 | His prose description of the scheme he kept |

Liliencron's fifteen: Spangenberg 1545, Keuchenthal 1573, Selnecker,
Gesius 1601, Leipzig *Geistliche Lieder* 1605, Stiphelius 1607, Augsburg
1619, Liegnitz 1625–30, Helmstedt 1626, Schein 1627, Erhardi/Frankfurt
1659, Schleswig-Holstein 1665, Darmstadt 1687, Goslar 1687, Leipzig
*Kirchenandachten* 1694.

## Schema

### `hymn_prescriptions` — the main table

One row per (occasion, hymn) pair, in liturgical order.

| Column | Notes |
|---|---|
| `occasion` | Sunday, feast or occasion, normalised to English labels (`Trinity 12`, `Lent 1 (Invocavit)`, `Week 2, Freydag (Introitus)`) |
| `original_title` | The hymn title **as printed in that source** — not normalised. Early-modern spelling and Low German are preserved as-is. |
| `literal_english` | Word-for-word rendering of that incipit |
| `common_english` | The received English hymn title where one exists, otherwise `NULL` — see the caveat below |
| `source` | Sehling volume, order and page range |

### `hymns` — the lexicon

One row per distinct hymn (136: 117 German, 19 Latin). `canonical_title`
is the modern standard spelling; this is what joins the printed variants
together.

### `hymn_prescriptions_by_hymn` — view

Ranks hymns by how often they are prescribed, with the number of orders
using each and the number of distinct printed spellings. Does the
`attestations` join correctly (see below).

### `attestations` — printed spelling → canonical hymn

335 rows. The corpus prints the same hymn many different ways
(`Nu kum der heiden heiland` / `Nun kom der heiden heiland` /
`Nun komm der heyden`), and this table records every one of them against
its canonical identity. Useful if you want to search the corpus text for
a hymn and need all its spellings.

### `translation_candidates` — contested English titles

The one place this database records a judgment rather than a fact. See
below.

## Joining prescriptions to hymns: use both keys

`hymn_prescriptions` deliberately holds the printed title, not the
canonical one, so getting from a prescription to its hymn means going
through `attestations`. That table is keyed on **`(printed_title, source)`**,
because the same spelling can occur in more than one order. Joining on
`printed_title` alone fans out and silently inflates every count:

```sql
-- WRONG: reports 81 prescriptions of O lux beata Trinitas; the real figure is 27
SELECT h.canonical_title, COUNT(*) FROM hymn_prescriptions p
JOIN attestations a ON a.printed_title = p.original_title
JOIN hymns h ON h.canonical_title = a.canonical_title
GROUP BY h.canonical_title;

-- RIGHT: join on the full key
SELECT h.canonical_title, COUNT(*) FROM hymn_prescriptions p
JOIN attestations a ON a.printed_title = p.original_title AND a.source = p.source
JOIN hymns h ON h.canonical_title = a.canonical_title
GROUP BY h.canonical_title;
```

The correct join is 1:1 — it returns exactly 466 rows, the number of
prescriptions. If a `SUM` over your grouping doesn't come to 466, the
join is wrong. The `hymn_prescriptions_by_hymn` view does this correctly
and is the easier path.

## `common_english` is an editorial judgment, not a fact

**47 of 136 hymns have no `common_english` at all.** These are hymns that
never entered the English-language tradition — mostly Low German psalm
paraphrases and local compositions. `NULL` there means "no received
English title exists", not "not yet filled in". Don't backfill it with a
translation; that's what `literal_english` is for.

Of the 89 that do have one, **7 have genuine rivals in current use**, and
the choice between them is a real editorial decision:

```sql
SELECT canonical_title, candidate, chosen
FROM translation_candidates
ORDER BY canonical_title, chosen DESC;
```

`chosen = 1` marks the title currently used in `hymn_prescriptions`;
`status = 'awaiting_adjudication'` marks the whole set as unsettled. The
rejected alternatives are kept rather than discarded so the decision can
be revisited — the same way `eko.db` keeps its `ambiguous` index links.

One correction already applied, as an example of the kind of error this
guards against: `Wo Gott der Herr nicht bei uns hält` (Jonas) and
`Wär Gott nicht mit uns diese Zeit` (Luther) are **two different**
Psalm 124 paraphrases, and were briefly given the same English title.
They now carry distinct ones.

## What this database does NOT do

**It is not the complete contents of those eight orders.** Two
deliberate scoping decisions:

- **From the Latin orders, only the hymn is taken.** Hof and Nördlingen
  give a full set of propers per Sunday — introit, antiphon, responsory,
  versicle, Magnificat antiphon, Benedicamus. Only the hymn field (`H:`)
  is extracted, because the rest are propers but not *hymns*. The other
  fields are still in `eko.db`'s document text if you want them.
- **Hohenlohe's topical assignments are not in yet.** Its 1596 order also
  assigns hymns by *sermon topic* (12 doctrinal categories) and by
  *catechism part* (6), independent of the calendar. Only its feast
  entries are extracted so far. This is a gap, not a decision.

**Latin incipits are snapped to canonical forms.** The repertoire is a
small fixed set of ~30 office hymns, so OCR'd Latin is matched against
`hymn_tables/canon_latin.py` rather than preserved verbatim; anything not
recognised as a known office hymn is dropped rather than guessed at.

**Three rows were dropped as unresolvable** out of 469 extracted from the
Sehling orders — two were page furniture the parser mistook for a title,
one (`Herre gott`) is too short a fragment to identify. Everything else
resolved.

**`original_title` is not always German.** The Hymn of the Day table and
Selnecker's account cite hymns by English title only; they give no German
incipit, so for those rows `original_title` holds the English title as
printed and `literal_english` is `NULL`. Filter on
`source LIKE '%Liliencron%' OR source LIKE 'Sehling%' OR source LIKE 'Ludecus%'`
if you need German incipits specifically.

**Liliencron was OCR'd.** That PDF carries its text as vector outlines
with no text layer, so no parser can extract it — it is rendered at 300
dpi and read with tesseract. `hymn_tables/src_liliencron_ocr.txt` is the
OCR output, kept in the repo so the parse is reproducible without
re-running OCR. Umlauts are the weak point (`fiir` for `für`, `héchsten`
for `höchsten`); the known substitutions are repaired in
`parse_liliencron.py`'s `OCR_FIX`, but assume some remain.

**Liliencron's own editorial notes are applied, not ignored.** His
translator flags two printer's slips of an undefined siglum `G.` (it is
`Go.` at *Vom Himmel hoch*, `Ge.` at Cantate); both are resolved in the
parser. His Quasimodogeniti entry is prose rather than a table — the one
coincidence it records is carried in as `PROSE_ENTRIES`. Three hymn-identity
distinctions he insists on are honoured: the two Psalm 124 settings
(Jonas vs. Luther), the two hymns called *Jesus Christus unser Heiland*
(Easter vs. Communion), and *Herr Gott, dich loben alle wir* (Eber, on the
angels) against *Herr Gott, dich loben wir* (the German Te Deum).

**`Hymns ABC Krusemark.pdf` is not in here.** It was referenced but failed
to upload twice, so its guide (said to be at pp. 95–96) has not been seen
and none of its content is represented.

## Example queries

**The full year for one order:**
```sql
SELECT occasion, original_title, common_english
FROM hymn_prescriptions
WHERE source LIKE 'Sehling 1, Nr. 159%'
ORDER BY id;
```

**Which hymn is prescribed most often** — already done for you as a view:
```sql
SELECT * FROM hymn_prescriptions_by_hymn LIMIT 10;
```

**Compare what different orders assign to the same Sunday:**
```sql
SELECT source, original_title, common_english
FROM hymn_prescriptions
WHERE occasion = 'Trinity 12';
```

**Every printed spelling of one hymn** — for searching the corpus text:
```sql
SELECT DISTINCT printed_title FROM attestations
WHERE canonical_title = 'Nun komm, der Heiden Heiland';
```

**Hymns with no English title** (the Low German psalm paraphrases,
mostly):
```sql
SELECT canonical_title, literal_english FROM hymns
WHERE common_english IS NULL ORDER BY canonical_title;
```
