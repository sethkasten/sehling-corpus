# Hymn Tables — Reference Guide

`hymns.db` is a SQLite database of the **chief-hymn prescriptions** found
in the corpus: the places where a church order assigns a specific hymn to
a specific Sunday, feast or occasion. See `CORPUS_GUIDE.md` for the
corpus itself and `DB_GUIDE.md` for `eko.db`; this covers the hymn tables
specifically. Where and how hymns were sung in the services is treated in
[`HYMN_PRACTICE_GUIDE.md`](HYMN_PRACTICE_GUIDE.md), whose Appendix A
condenses the Compare by day sheet of `hymns.xlsx` into a table of the chief
hymn of each Sunday and feast.

## Building or rebuilding it

```
py hymn_tables/build_hymn_db.py
```

**`hymns.db` is committed** (1.2 MB), so you can query it straight away
without building anything. Rebuild only if you change a parser or a
source.

The builder reads the pre-extracted `hymn_tables/rows_*.json` files, not
the corpus, so it needs **no `eko.db`** — it runs in about a second. Like
`eko.db`, it always rebuilds from scratch, so a rebuild overwrites the
committed copy; commit the result if you meant to change it.

`build_hymn_db.py` loads only the Sehling orders. The hymnal and
compilation sources are added by a second step, which must follow it:

```
py hymn_tables/build_hymn_db.py
py hymn_tables/merge_sources.py
py hymn_tables/merge_krusemark.py
```

To re-extract from the sources instead — after an OCR fix, say — re-run
the parsers. The first four *do* need `eko.db` (see `DB_GUIDE.md`), since
they read the document text out of it; the rest read the source documents
committed alongside them:

```
py hymn_tables/parse_weissenfels.py      # these four need eko.db
py hymn_tables/parse_pommern.py
py hymn_tables/parse_latin.py
py hymn_tables/parse_german.py
py hymn_tables/parse_liliencron.py       # reads the committed OCR text
py hymn_tables/parse_ludecus.py          # needs python-docx
py hymn_tables/parse_hotd_selnecker.py
py hymn_tables/parse_krusemark.py        # needs PyMuPDF; reads the root PDF
```

Each prints what it found; each also exposes a `parse()`/`parse_all()`
returning `(occasion, title, source)` tuples, which is how the `rows_*.json`
files are produced.

## Two layers of evidence

The database holds **4,144 prescriptions** from **48 witnesses**, in two
quite different evidentiary layers. Keep them apart when you draw
conclusions:

| Layer | Rows | What it is |
|---|---:|---|
| Sehling church orders | 466 | 16th-c. orders prescribing hymns, read from the corpus itself |
| Hymnals and compilations | 3,678 | later hymnals and modern conflations, read from separate documents |

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

53 such overlapping attestations were folded this way. Counting sources
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

All eight are Lutheran orders, and none is an Interim order (traditions as in
[`CHURCH_ORDERS_GUIDE.md`](CHURCH_ORDERS_GUIDE.md)). The hymnals and compilations below are
Lutheran too.

### The hymnal and compilation sources

| Source | Rows | Witnesses | What it is |
|---|---:|---:|---|
| Liliencron, *de tempore* concordance (pp. 61–77) | 1,823 | 15 | Collates fifteen hymnals, 1545–1694, Sunday by Sunday |
| Krusemark, *Hymns ABC* (2018) | 1,141 | 18 | Three-year series collating seventeen lists for the LSB one-year lectionary |
| Hymn of the Day conflation table | 371 | 12 | Modern table collating Carpzov, Gehrke, SELK, Selnecker, Zion, LW, LSB and others |
| Ludecus, *Ordo cantionum Germanicarum* (1589) | 310 | 1 | A single order, German incipits with English translation |
| Selnecker, own account | 46 | 1 | His prose description of the scheme he kept |

#### Krusemark, and why only part of it is here

Krusemark collates seventeen lists (Stuckwisch, Gehrke, Reuning, Eckardt,
LCMS, ELS, Zion Detroit, Dietrich, Judisch, Thompson, Gerhardt, Carpzov,
Liliencron, Bach, Stiller, the LSB Hymnal Committee, and his own Years
A/B/C), explained in his own guide on pp. 95–96.

**Only his Hymn-of-the-Day entries are loaded — 1,141 of 6,925.** His
lists also carry opening, distribution, offering and closing hymns, which
are real data but are *not* chief hymns; mixing them in would destroy the
meaning of this table. The full extraction, with every entry and its
`hod` flag, hymnal siglum and number, is kept in
`hymn_tables/rows_krusemark_raw.json` if you want the rest.

**The Hymn of the Day is marked only by underlining**, and Word writes
underlines as thin filled rectangles rather than as a text attribute — so
`pdftotext` loses them entirely. `parse_krusemark.py` recovers them
geometrically, matching sub-2pt rules to the spans above them. Three
lists (Judisch, Liliencron, SELK) are wholly Hymns of the Day by
definition and carry no underlining; they are flagged from his guide
rather than from the page.

**His Easter numbering differs from this database's.** Krusemark counts
Easter Day as Easter 1, so his *Easter 2, Quasimodo Geniti* is the Sunday
recorded here as `Easter 1 (Quasimodogeniti)`. The mapping in
`merge_krusemark.py` shifts them back; be careful if you re-derive
occasions from his raw JSON, which preserves his own labels.

**One overlap could not be resolved.** His *Thompson* column is Jason
Thompson's dissertation appendix, which collates **Ludecus together with
twelve other 16th-century lists** — and Ludecus is already in this
database in his own right. Thompson's column does not say which of the
thirteen a given hymn came from, so those rows cannot be deduplicated
against the Ludecus rows. They are kept, labelled
`Thompson, diss. App. 2 (Ludecus + twelve 16th-c. lists)`, and this is the
one place where a witness may be counted twice. Exclude it if that
matters to your count:

```sql
SELECT * FROM hymn_prescriptions WHERE source NOT LIKE 'Thompson%';
```

**His *Liliencron* is not the Liliencron source above.** Krusemark's is a
single de tempore plan of c. 1700 taken from Paul Graff; the other is
Liliencron's concordance of fifteen hymnals, where "Liliencron" is the
compiler rather than a witness. They occupy different rows and do not
collide.

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

One row per distinct hymn (206: 185 German, 21 Latin), from the Sehling
orders and the hymnal and compilation sources alike. `canonical_title`
is the modern standard spelling; this is what joins the printed variants
together. Hymns that a source names only in a form the lexicon does not
know are not in this table (see *Hymn identity across languages* below).

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

### `editorial_assignments` — hymns assigned to days the witnesses leave open

Five rows: the hymn the editor of the corpus assigns to Quasimodogeniti
(*O filii et filiae*), Maundy Thursday (*Jesus Christus, unser Heiland*),
Easter Monday (*Ach bleib bei uns, Herr Jesu Christ* and *Christ ist
erstanden*) and Pentecost Monday (*Komm, Heiliger Geist, Herre Gott*). On
these days no hymn has three old witnesses. The assignments come from
`hymn_tables/editorial.py`. They are **not prescriptions**: they are not in
`hymn_prescriptions` and are never counted as witnesses. The workbook's
Compare by day sheet flags them "Assigned".

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

## Hymn identity across languages

The hymnal and compilation sources cite a hymn in four ways: by its German
incipit (Liliencron's hymnals, Ludecus), by a Low German or Latin form, by
an English title only (Selnecker's own account, Carpzov, Bach, the plan of
c. 1700, Thompson and the modern lists), or by both. One hymn has one
identity in all of them:

- **`lexicon.py`** matches printed German, Low German and Latin incipits to
  a canonical title. It covers the hymns of the Sehling orders and the
  hymns of the hymnal sources. Without the latter, a hymn named only by
  the hymnals either stayed unresolved, so that its German and English
  citations were counted as different hymns, or was fuzzy-matched to the
  nearest Sehling hymn.
- **`bridge.py`** maps an English title to its German hymn: first through
  its own table of English titles (`EN_ALIAS`), then through the English
  column of Liliencron's concordance.
- **Different titles of one hymn are joined.** *O filii et filiae* (Jean
  Tisserand) is cited in English as "O Sons and Daughters of the King" and
  "Ye Sons and Daughters of the King"; both are one hymn.
- **Hymns with the same or a similar opening are kept apart:**
  - Eber's *Herr Gott, dich loben alle wir*, on the angels, is not the German
    Te Deum *Herr Gott, dich loben wir*.
  - Luther's Easter hymn *Jesus Christus, unser Heiland, der den Tod
    überwand* is not his Communion hymn *Jesus Christus, unser Heiland, der
    von uns den Gotteszorn wandt*. A source that prints only the opening
    words for an Easter occasion means the Easter hymn
    (`resolve.by_occasion`). This applies to Pommern, Hohenlohe, Weissenfels
    and Mansfeld.
  - *Als Jesus Christus, Gottes Sohn* is not *Jesus Christus, wahrer
    Gottes Sohn*.
  - *Mag ich dem Tod nicht widerstahn* is not *Mag ich Unglück nicht
    widerstahn*.

Because the identity of a hymn decides the deduplication key, a witness
that cites the same hymn on the same day in German and in English is
counted once. Selnecker, cited in German by Liliencron and in English in
his own account, is the main case.

## `common_english` is an editorial judgment, not a fact

**38 of 206 hymns have no `common_english` at all** (three of them are
group rubrics such as "the Christmas hymns"). These are hymns that never
entered the English-language tradition — mostly Low German psalm
paraphrases and local compositions — and that Matthew Carver has not
translated either (see below). `NULL` there means "no English title
exists", not "not yet filled in". Don't backfill it with a translation;
that's what `literal_english` is for.

**36 hymns carry the title of Matthew Carver's translation.** For hymns
with no received English title, `common_english` gives the English title
of Carver's translation, from *Walther's Hymnal* (Concordia, 2012), which
he translated, or from his blog *Hymnoglypt*
(matthaeusglyptes.blogspot.com). The titles are the ones Krusemark prints
with the references "WH" and "HG" (his pp. 95–96 name Carver as the
translator). Each was matched to its German hymn by the Ludecus and
Thompson entries for the same day. They are listed in
`hymn_tables/lexicon.py` (`CARVER`), and each has a row in
`translation_candidates` whose `status` names the source:

```sql
SELECT canonical_title, candidate, status FROM translation_candidates
WHERE status LIKE 'matthew_carver%';
```

Of the 131 hymns with a received English title, **7 have genuine rivals in current use**, and
the choice between them is a real editorial decision:

```sql
SELECT canonical_title, candidate, chosen
FROM translation_candidates
ORDER BY canonical_title, chosen DESC;
```

`chosen = 1` marks the title currently used in `hymn_prescriptions`;
`status = 'awaiting_adjudication'` marks the whole set as unsettled, and
`status = 'matthew_carver_translation (…)'` marks a Carver title. The
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

**Krusemark's non-chief-hymn entries are not loaded** — see above. And
his PDF lives at the repo root (`Hymns_ABC_Krusemark.pdf`) rather than
under `hymn_tables/`, since it was committed there; `parse_krusemark.py`
reads it from that path.

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
