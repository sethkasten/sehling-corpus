# Hymn Tables — Reference Guide

`hymns.db` is a SQLite database of the **chief-hymn prescriptions** found
in the corpus: the places where a church order assigns a specific hymn to
a specific Sunday, feast or occasion. See `CORPUS_GUIDE.md` for the
corpus itself and `DB_GUIDE.md` for `eko.db`; this covers the hymn tables
specifically. Where and how hymns were sung in the services is treated in
[`LITURGICAL_AND_ECCLESIASTICAL_LIFE.md`](LITURGICAL_AND_ECCLESIASTICAL_LIFE.md#ch8),
Chapter 8, whose Appendix 8.A condenses the Compare by day sheet of
`hymns.xlsx` into a table of the chief hymn of each Sunday and feast.

## Building or rebuilding it

```
py hymn_tables/build_hymn_db.py
```

**`hymns.db` is committed** (1.5 MB), so you can query it straight away
without building anything. Rebuild only if you change a parser or a
source.

The builder reads the pre-extracted `hymn_tables/rows_*.json` files, not
the corpus, so it needs **no `eko.db`** — it runs in about a second. It
also reads the Lutheran Hymn Index, `Hymnal Index/hymnal.db`, for the
English titles (see below). Like `eko.db`, it always rebuilds from scratch,
so a rebuild overwrites the committed copy; commit the result if you meant
to change it.

`build_hymn_db.py` loads only the Sehling orders. The hymnal and
compilation sources are added by a second step, which must follow it:

```
py hymn_tables/build_hymn_db.py
py hymn_tables/merge_sources.py
py hymn_tables/merge_krusemark.py
py hymn_tables/merge_thompson.py
```

The workbook and the book's table follow from the database. Both scripts
need `openpyxl`:

```
py hymn_tables/export_xlsx.py            # writes hymns.xlsx
py hymn_tables/appendix_8a.py --check    # is Appendix 8.A of the book current?
```

`appendix_8a.py` applies the rules of the book's §8.A.2 and prints the
table as Markdown; `--check` compares it with the table in the book, and
`--stats` prints the figures that §8.A.4 quotes. Run it after any change to
the database, and paste its output over the table in §8.A.3 if they differ.

To re-extract from the sources instead — after an OCR fix, say — re-run
the parsers. The first five *do* need `eko.db` (see `DB_GUIDE.md`), since
they read the document text out of it; the rest read the source documents
committed alongside them:

```
py hymn_tables/parse_weissenfels.py      # these five need eko.db
py hymn_tables/parse_pommern.py
py hymn_tables/parse_latin.py
py hymn_tables/parse_german.py
py hymn_tables/parse_sunday.py
py hymn_tables/parse_liliencron.py       # reads the committed OCR text
py hymn_tables/parse_ludecus.py          # needs python-docx
py hymn_tables/parse_hotd_selnecker.py
py hymn_tables/parse_krusemark.py        # needs PyMuPDF; reads the root PDF
py hymn_tables/parse_thompson.py         # reads Thompson's eight list files
```

Each prints what it found; each also exposes a `parse()`/`parse_all()`
returning `(occasion, title, source)` tuples, which is how the `rows_*.json`
files are produced. `parse_thompson.py` writes `rows_thompson.json` itself,
with one dict to a row, and `parse_thompson.py --compare` sets its three
Sehling orders beside `rows_sunday.json` (see *Thompson's lists* below).

## Two layers of evidence

The database holds **4,794 prescriptions** from **57 witnesses**, in two
quite different evidentiary layers. Keep them apart when you draw
conclusions:

| Layer | Rows | What it is |
|---|---:|---|
| Sehling church orders | 827 | 16th-c. orders prescribing hymns, read from the corpus itself |
| Hymnals and compilations | 3,967 | hymnals, other lists and modern conflations, read from separate documents |

A row in the first layer is a church *ordering* what shall be sung. A row
in the second is a hymnal or editor *recording* what was sung, sometimes
centuries later. They are not the same claim. Some lists of the second
layer are orders too, such as Antwerp's of 1567, but they are not in
Sehling and are read from a later transcription (*Thompson's lists*,
below).

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

Twelve Sehling orders carry a hymn table worth extracting. They are **not**
all the same kind of document:

| Source | Rows | Kind |
|---|---:|---|
| Pommern, Agenda 1569 (`Sehling 4`, pp. 425–480) | 166 | Low German, per-Sunday, 2–4 options each |
| Mansfeld, *Kirchen-Agenda* 1580 (`Sehling 2`, pp. 210–247) | 165 | German: by season (Part I), then per Sunday and feast, 2–4 options each (Parts III–IV) |
| Pfalz-Zweibrücken 1565 (`Sehling 18, I/23`, pp. 337–341) | 121 | German, **3-week rotating cycle** by liturgical slot |
| Pirna, Lauterbach's *Kirchenordnung*, 1555–1569 (`Sehling 1, Nr. 128`, pp. 642–643) | 42 | German, two hymns per Sunday, Septuagesima → Advent 4, of which the second (after the epistle) is taken; the high feasts mostly Latin |
| Nördlingen 1579 (`Sehling 12, VIII.7`, pp. 335–393) | 66 | German, the psalm after the epistle, per Sunday (54); Latin office hymns (12) |
| Nördlingen, St George's, 1544/1555 (`Sehling 12, VIII.5`, pp. 321–323) | 61 | German, the psalm after the epistle, per Sunday and feast; taken from Naumburg |
| Hof, *Ordo ecclesiasticus* 1592 (`Sehling 11, IV.20`, pp. 407–477) | 58 | Latin office propers, per-Sunday |
| Weissenfels 1578 (`Sehling 1, Nr. 159`, pp. 693–696) | 55 | German, one hymn per Sunday, Advent 1 → Trinity 25 |
| Naumburg, St Wenzel, 1537/38 (`Sehling 2, Nr. 13`, pp. 76–77) | 48 | German, the psalm after the epistle, one per Sunday and feast |
| Hohenlohe 1596 (`Sehling 15, Nr. 54`, pp. 641–660) | 21 | German, by feast |
| Anhalt, *Ordnung der deutschen Gesänge*, 1551 (`Sehling 2, Nr. 116`, pp. 555–556) | 18 | German, the hymn before the gospel, by feast and season; a rotation after Trinity |
| Heilbronn 1543 (`Sehling 17, II/17`, pp. 320–326) | 6 | Latin Vespers propers |

Naumburg and Weissenfels, with one hymn for each Sunday, are the closest
things in the corpus to a modern *Hauptlied* / *Wochenlied* table; Naumburg's
list of 1537/38 is the earliest of the tables here, and St George's at
Nördlingen took it over (1544/1555). Note
that the term `Hauptlied` itself appears **nowhere** in the corpus — it is
later terminology. Searching for it finds nothing; these tables are what the
concept actually looks like in the 16th century.

**Occasion labels keep the source's own span.** An entry for a season keeps
it (`Christmas to Purification`, `Easter to Ascension`, `Trinity season` for
Anhalt's rotation), and an entry for two days keeps them together
(`Pentecost & Pentecost Monday`, `Lent 5 (Judica) & Palm Sunday`, `Trinity 26
& 27`). The feasts of the Virgin and of the apostles as a class are
`Feasts of the Virgin Mary` and `Common of Apostles`. Pirna's order is
undated, and shares one record in `eko.db` with the visitors' recess of 1555
that Sehling prints before it. Sehling dates it probably after 1555, since
its passage on the poor and the schools uses that recess; Lauterbach, the
first superintendent of Pirna, died in 1569 (Sehling 1, p. 635). The source
string dates it 1555–1569.

All twelve are Lutheran orders, and none is an Interim order (traditions as in
[`LITURGICAL_AND_ECCLESIASTICAL_LIFE.md`](LITURGICAL_AND_ECCLESIASTICAL_LIFE.md#ch1), Chapter 1).
The hymnals and compilations below are Lutheran too.

### The hymnal and compilation sources

| Source | Rows | Witnesses | What it is |
|---|---:|---:|---|
| Liliencron, *de tempore* concordance (pp. 61–77) | 1,823 | 15 | Collates fifteen hymnals, 1545–1694, Sunday by Sunday |
| Krusemark, *Hymns ABC* (2018) | 1,047 | 19 | Three-year series collating seventeen lists for the LSB one-year lectionary |
| Thompson, dissertation, Appendix 2 | 382 | 4 | His transcriptions of the lists of Antwerp 1567, Annaberg 1579, Eler 1588 and Magdeburg 1632 |
| Hymn of the Day conflation table | 371 | 12 | Modern table collating Carpzov, Gehrke, SELK, Selnecker, Zion, LW, LSB and others |
| Ludecus, *Ordo cantionum Germanicarum* (1589) | 311 | 1 | A single order, German incipits with English translation |
| Selnecker, own account | 46 | 1 | His prose description of the scheme he kept |

#### Krusemark, and why only part of it is here

Krusemark collates seventeen lists (Stuckwisch, Gehrke, Reuning, Eckardt,
LCMS, ELS, Zion Detroit, Dietrich, Judisch, Thompson, Gerhardt, Carpzov,
Liliencron, Bach, Stiller, the LSB Hymnal Committee, and his own Years
A/B/C), explained in his own guide on pp. 95–96.

**His own series closes each occasion.** On most days it is Years A, B
and C. Where the three-year series does not run, it is one list headed
*Every Year*, or two headed *Even Year* and *Odd Year*. These are lists
of his own, loaded as the witnesses `Krusemark, Every Year`, `Krusemark,
Even Year` and `Krusemark, Odd Year`; a *Choir* heading inside a list is
only a subdivision of it. (Builds before October 2026 read *Every Year*,
*Even Year* and *Odd Year* as subdivisions, and so gave his picks to the
list printed before them: Stiller, the plan of c. 1700, Judisch, Zion or
the unattributed *Other*.)

**The pages after the occasions are not his lists.** His Explanation
(pp. 95–96) and two pages that only name saints' days (pp. 98 and 100)
are not read. Holy Innocents (p. 99) is, though its heading is set in
the text size and not as an occasion heading; it is loaded as
`Holy Innocents (28 Dec)`.

**Only his Hymn-of-the-Day entries are loaded — 1,047 of 6,749.** His
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

**His *Thompson* column is not loaded.** It comes from Jason Thompson's
dissertation (Appendix 2), which collates **Ludecus with twelve other
lists**, and Krusemark underlines the hymns that three or more of those
lists give (his p. 95). So the column is a tally, not a witness. Ludecus is
in this database in his own right, and Thompson's own transcriptions of
eight of his lists are loaded or checked against the corpus (*Thompson's
lists*, below). Counting the column as well would count those lists twice.
Its rows stay in `rows_krusemark_raw.json`. (Builds before this one loaded
its underlined rows as the witness `Thompson, diss. App. 2 (Ludecus +
twelve 16th-c. lists)`, and warned that Ludecus might be counted twice.)

The nine lists now loaded, Ludecus and Thompson's eight, account for most
of the column. Krusemark underlines 84 pairs of a day and a hymn. Counting
the hymns those lists give for the chief hymn and the sermon, the places
the column covers, 73 of the 84 pairs are given on the same day by at
least two of the nine lists, and 44 by three or more. The rest of the
column's support comes from lists of Thompson's that are not in this
folder.

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

#### Thompson's lists

Jason Thompson, *A Handbook for Reconstructing 16th Century Lutheran
Masses* (doctoral dissertation, Indiana University, 2013), Appendix 2,
sets out the hymns of the Sunday and feast services in a number of orders
and hymnals. Eight of his lists are in `hymn_tables`, one text file to a
list: the list's name and year on the first line, then one line to a hymn,
`Occasion, Hymn`. **A hymn whose place in the service is not given in
parentheses is the chief hymn**; `(introit)`, `(before sermon)`, `(after
sermon)`, `(postlude)` and `(distribution)` name the others.

| File | In `hymns.db` as | Chief hymns | Other places |
|---|---|---:|---|
| `andorff 1567.txt` | `Antwerp (Andorff, 1567)` | 28 | — |
| `annaberg 1579.txt` | `Annaberg (1579)` | 132 | — |
| `eler 1588.txt` | `Eler, Cantica sacra (1588)` | 45 | introit, distribution, postlude |
| `magdeburg 1613.txt` | not loaded | 0 | after the sermon only |
| `magdeburg 1632.txt` | `Magdeburg (1632)` | 177 | — |
| `naumburg 1538.txt` | Sehling order, read from the corpus | (48) | introit, before and after the sermon |
| `anhalt 1551.txt` | Sehling order, read from the corpus | (14) | — |
| `pirna pre-1569.txt` | Sehling order, read from the corpus | (39) | introit |

*Andorff* is Antwerp, whose Lutheran congregation of the Augsburg
Confession had its church order printed in 1567. Franz Eler's *Cantica
sacra* is the Hamburg hymnal of 1588.

`parse_thompson.py` reads the files into `rows_thompson.json`, every place
in the service included, and `merge_thompson.py` loads the chief hymns of
the four lists outside Sehling, with the source `Witness (via Thompson,
diss. App. 2)`. Their `original_title` is Thompson's incipit; their English
titles come from the lexicon. A list that gives one hymn twice on a day is
counted once (one row of Magdeburg 1632). Thompson's "Christmastide",
"Eastertide" and "Trinitytide" are `Christmas season`, `Easter season` and
`Trinity season`; Appendix 8.A counts the first two for Christmas Day and
Easter Day, the feasts at their head.

The files are kept as Thompson gives them, and `parse_thompson.py` mends
their slips: misspelt occasions (`Triniyt 2`, `Quinquagelima`, `Micahel`)
and places (`intorit`, `psotlude`), misspelt titles (`halleuljah`, `Aus
tiefre not`), and a few readings set out in its `FIX`:
- `Allein nach dir Herr Jesu Christ`, which Thompson queries himself, is
  *Allein zu dir*, as Magdeburg 1632 has it on seven other Sundays;
- `Der Herr fährt auf mit grossem Schall` is the second line of Alber's
  Ascension hymn *Nun freut euch, Gottes Kinder, all*;
- `Der Tag der ist so` and `Christ unser Herr` (on St John the Baptist's
  day) are openings cut short.

The Latin introits, sequences and tracts, the litany and the Nicene Creed
are kept in `rows_thompson.json` without a title, as not hymns. A
reference to another day (`"as on Trinity 4"`) is not followed, as in
`parse_sunday.py`.

The lists add six hymns to the lexicon:
- *Kyrie, Gott Vater in Ewigkeit* and *Ich weiß, dass mein Erlöser lebt*,
  from Magdeburg 1632. The second is not Paul Gerhardt's hymn of that
  opening, which is later.
- *O Herr Gott, Schöpfer aller Ding* and *O Gott Vater in Ewigkeit*, from
  Antwerp.
- *O Jesu Christ, dein Nam, der ist*, from Antwerp, which Liliencron's
  hymnals and Ludecus also give and which the lexicon lacked.
- The Pentecost antiphon *Komm, Heiliger Geist, erfüll die Herzen deiner
  Gläubigen*, which Antwerp and Ludecus both give beside Luther's *Komm,
  Heiliger Geist, Herre Gott*. Ludecus's antiphon had been read as Luther's
  hymn.

**What the lists check.** Three of the lists are Sehling orders that
`parse_sunday.py` reads from the corpus. `parse_thompson.py --compare`
sets Thompson's chief hymns beside that reading, day by day:

| Order | Days that agree | Where they differ |
|---|---:|---|
| Naumburg 1537/38 | 45 of 47 | Thompson follows the order's "likewise" from Christmas to the Purification, which this database does not follow; and he gives the apostles' hymn to the apostles only, where the order gives it to St John the Baptist too |
| Anhalt 1551 | 6 of 13 | Thompson spreads the Advent hymn over the four Sundays; takes the Purification hymn, which the order sets before the early sermon and "before the epistle" (corrected from "before the gospel", Sehling notes) and at vespers, where this database takes only the hymn before the gospel; and gives only the first of the nine hymns that the order rotates after Trinity |
| Pirna | 39 of 42 | Thompson gives no second hymn for Advent 1, 2 and 4, which the order has |

So the corpus reading stands, but for Pirna. Its list names two German
hymns for most Sundays, and builds before this one took both. Thompson
marks the first as the introit, and the order's feasts bear him out: for
the Ascension it names the introit *Viri Galilaei*, the Kyrie, the gradual
and the sequence, and then *Christ fuhr gen Himmel*. `parse_sunday.py` now
takes only the last hymn of each Pirna day, and 38 introit hymns have left
the table.

## Schema

### `hymn_prescriptions` — the main table

One row per (occasion, hymn) pair, in liturgical order.

| Column | Notes |
|---|---|
| `occasion` | Sunday, feast or occasion, normalised to English labels (`Trinity 12`, `Lent 1 (Invocavit)`, `Week 2, Freydag (Introitus)`) |
| `original_title` | The hymn title **as printed in that source** — not normalised. Early-modern spelling and Low German are preserved as-is. |
| `literal_english` | Word-for-word rendering of that incipit |
| `common_english` | The hymn's English title: its title in the Lutheran Hymn Index where the hymn is there, otherwise the title of a translation or a canticle's English name; `NULL` where there is none — see below |
| `source` | Sehling volume, order and page range |

### `hymns` — the lexicon

One row per distinct hymn (223: 200 German, 23 Latin), from the Sehling
orders and the hymnal and compilation sources alike. `canonical_title`
is the modern standard spelling; this is what joins the printed variants
together. Hymns that a source names only in a form the lexicon does not
know are not in this table (see *Hymn identity across languages* below).

### `hymn_prescriptions_by_hymn` — view

Ranks hymns by how often they are prescribed, with the number of orders
using each and the number of distinct printed spellings. Does the
`attestations` join correctly (see below).

### `attestations` — printed spelling → canonical hymn

581 rows. The corpus prints the same hymn many different ways
(`Nu kum der heiden heiland` / `Nun kom der heiden heiland` /
`Nun komm der heyden`), and this table records every one of them against
its canonical identity. Useful if you want to search the corpus text for
a hymn and need all its spellings.

### `editorial_assignments` — hymns assigned to days the witnesses leave open

Five rows: the hymn the editor of the corpus assigns to Quinquagesima
(*Durch Adams Fall ist ganz verderbt*), Quasimodogeniti (*O filii et
filiae*), Easter Monday (*Ach bleib bei uns, Herr Jesu Christ* and *Christ
ist erstanden*) and Pentecost Monday (*Komm, Heiliger Geist, Herre Gott*).
On Quasimodogeniti and the two Mondays no hymn has three old witnesses. On
Quinquagesima the old witnesses are divided and no hymn has a quarter of
them, and the hymn assigned is the one with the most (4 of 17). The
assignments come from `hymn_tables/editorial.py`. They are **not
prescriptions**: they are not in `hymn_prescriptions` and are never counted
as witnesses. The workbook's Compare by day sheet flags them "Assigned".
Maundy Thursday had an assignment too, Luther's Communion hymn, until
Thompson's lists of Annaberg 1579 and Magdeburg 1632 gave it the third and
fourth old witnesses for that hymn, after Carpzov and Selnecker.

### `translation_candidates` — where each English title comes from

One row per English title: the row of the Lutheran Hymn Index it was
taken from, or Matthew Carver's translation, and the rival titles of seven
hymns. See below.

## Joining prescriptions to hymns: use both keys

`hymn_prescriptions` deliberately holds the printed title, not the
canonical one, so getting from a prescription to its hymn means going
through `attestations`. That table is keyed on **`(printed_title, source)`**,
because the same spelling can occur in more than one order. Joining on
`printed_title` alone fans out and silently inflates every count:

```sql
-- WRONG: reports 84 prescriptions of O lux beata Trinitas; the real figure is 27
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

The correct join is 1:1 — it returns exactly 827 rows, one for each
prescription from the Sehling orders, which are the rows `attestations`
covers. If a `SUM` over your grouping doesn't come to 827, the join is
wrong. The `hymn_prescriptions_by_hymn` view does this correctly
and is the easier path.

## Hymn identity across languages

The hymnal and compilation sources cite a hymn in four ways: by its German
incipit (Liliencron's hymnals, Ludecus), by a Low German or Latin form, by
an English title only (Selnecker's own account, Carpzov, Bach, the plan of
c. 1700 and the modern lists), or by both. One hymn has one
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
  - *Als Jesus Christus, unser Herr*, which Nördlingen 1579 gives for Palm
    Sunday, is not Luther's Communion hymn, whose opening words it contains.
  - Mansfeld's *Nimm von uns, Herr Gott* is not Martin Moller's *Nimm von
    uns, Herr, du treuer Gott* (1584), which Goslar 1687 and Leipzig 1694
    give for Trinity 10. Moller's hymn is later than Mansfeld's order.
  - *Mag ich dem Tod nicht widerstahn* is not *Mag ich Unglück nicht
    widerstahn*.
  - The Pentecost antiphon *Komm, Heiliger Geist, erfüll die Herzen deiner
    Gläubigen* is not Luther's *Komm, Heiliger Geist, Herre Gott*, which
    grew out of it. Ludecus and Antwerp 1567 give both.

Because the identity of a hymn decides the deduplication key, a witness
that cites the same hymn on the same day in German and in English is
counted once. Selnecker, cited in German by Liliencron and in English in
his own account, is the main case.

## Where `common_english` comes from

**134 of the 223 hymns take the title of the Lutheran Hymn Index.** The
folder `Hymnal Index` holds the index: `hymnal.db` has a row for every
hymn of 34 English Lutheran hymnals and supplements (with Walther's German
hymnal and its English translation, and *Liber Hymnorum*), and its README
explains the tables. Each hymn of this lexicon was matched to its row by
the German or Latin original that the index records, and every match was
checked by hand. The matches are listed in `hymn_tables/index_titles.py`
(`INDEX`), which also makes the title: the row's master title (as a rule
*Lutheran Service Book*'s, else *The Lutheran Hymnal*'s, else the
*Evangelical Lutheran Hymnary*'s), with the commas of the first hymnal
title of the same words where the index leaves them out, in title case.
`lexicon.py` puts these titles in `common_english`, over whatever title it
gave before. A German version of a Latin hymn takes the Latin hymn's row
where the index has no row for the German. One title is shortened: the
index calls Luther's Creed hymn *We All Believe in One True God, Maker*,
to tell it from Clausnitzer's, and `common_english` gives it as the
hymnals do.

**40 hymns carry the title of Matthew Carver's translation.** Of the
index titles, 19 are Carver's, from *Walther's Hymnal* (Concordia, 2012),
which he translated, or *Liber Hymnorum* (2016), for hymns that no older
English book has. For 21 hymns that the index lacks, `common_english`
gives the title of Carver's translation on his blog *Hymnoglypt*
(matthaeusglyptes.blogspot.com), as Krusemark prints it with the reference
"HG" (his pp. 95–96 name Carver as the translator). Each was matched to its
German hymn by Ludecus's entries and those of Krusemark's Thompson column
for the same day. They are listed in `hymn_tables/lexicon.py` (`CARVER`).

**22 other hymns keep the English title their sources give them**, or the
English name of a canticle or creed (*The Litany*, *Athanasian Creed*).

**46 hymns have no `common_english` at all** (three of them are group
rubrics such as "the Christmas hymns"). These are hymns that never entered
the English-language tradition — mostly Low German psalm paraphrases and
local compositions — and that Matthew Carver has not translated either.
`NULL` there means "no English title exists", not "not yet filled in".
Don't backfill it with a translation; that's what `literal_english` is
for.

Every title has a row in `translation_candidates` whose `status` names
its source: `hymnal_index (row N)`, the row of `hymnal.db`, followed by
`; matthew_carver_translation (…)` where the title is Carver's, or
`matthew_carver_translation (Hymnoglypt)`. Seven hymns also keep the rival
titles the lexicon once weighed, with `chosen = 0` and `status =
'alternative'`; the index settles the choice between them.

```sql
SELECT canonical_title, candidate, chosen, status FROM translation_candidates
ORDER BY canonical_title, chosen DESC;
```

Two corrections, as examples of the kind of error this guards against:
`Wo Gott der Herr nicht bei uns hält` (Jonas) and `Wär Gott nicht mit uns
diese Zeit` (Luther) are **two different** Psalm 124 paraphrases, and were
briefly given the same English title. They carry the index's distinct ones,
*If God Were Not upon Our Side* and *If God Had Not Been on Our Side*. And
the English version of Liliencron's concordance gives Johann Hermann's
`Jesu, nun sei gepreiset` the title *Now Greet the Swiftly Changing Year*,
which is Jaroslav Vajda's translation of a Slovak New Year hymn (LSB 896).
`lexicon.py` (`NOT_EN`) keeps that title out, and the hymn has no
`common_english`.

## What this database does NOT do

**It is not the complete contents of those twelve orders.** Three
deliberate scoping decisions, and one gap:

- **From the Latin orders, only the hymn is taken.** Hof and Nördlingen
  1579 give a full set of propers per Sunday — introit, antiphon, responsory,
  versicle, Magnificat antiphon, Benedicamus. Only the hymn field (`H:`)
  is extracted, because the rest are propers but not *hymns*. The other
  fields are still in `eko.db`'s document text if you want them.
- **From Naumburg, Nördlingen 1544/1555 and Anhalt, only the hymn after the
  epistle is taken** (Anhalt: "before the gospel"). Their hymns for the
  introit, before and after the sermon, at vespers and on weekdays are left
  out. Of Pirna's two German hymns a Sunday only the second, after the
  epistle, is taken; the first is sung in the place of the introit (see
  *Thompson's lists*). On its high feasts it gives Latin propers, of which
  only the named sequences (*Grates nunc omnes*, *Victimae paschali*) are
  kept. Where Nördlingen 1544/1555 sets a figural piece or a German hymn,
  only the hymn is taken.
- **References to another day are not followed.** Mansfeld's Part IV sends
  Christmas, Easter, Pentecost and Quasimodogeniti back to its season lists in
  Part I; Naumburg and Nördlingen 1544/1555 keep the Circumcision, Epiphany
  and the Purification "likewise" as Christmas. None of these is repeated as
  a row. The one exception is "Idem" in a Sunday list (Naumburg's Palm
  Sunday, Nördlingen 1579's first and second Sundays after Trinity), which
  repeats the hymn of the entry before it. Where Mansfeld's Part IV repeats a
  hymn of Part I for the same day, it is counted once.
- **Hohenlohe's topical assignments are not in yet.** Its 1596 order also
  assigns hymns by *sermon topic* (12 doctrinal categories) and by
  *catechism part* (6), independent of the calendar. Only its feast
  entries are extracted so far. This is a gap, not a decision.

**Latin incipits are snapped to canonical forms.** The repertoire is a
small fixed set of ~30 office hymns, so OCR'd Latin is matched against
`hymn_tables/canon_latin.py` rather than preserved verbatim; anything not
recognised as a known office hymn is dropped rather than guessed at.

**Three rows were dropped as unresolvable** out of 830 extracted from the
Sehling orders — two were page furniture the parser mistook for a title,
one (`Herre gott`) is too short a fragment to identify. Everything else
resolved.

**`original_title` is not always German.** The Hymn of the Day table and
Selnecker's account cite hymns by English title only; they give no German
incipit, so for those rows `original_title` holds the English title as
printed and `literal_english` is `NULL`. Filter on
`source LIKE '%Liliencron%' OR source LIKE 'Sehling%' OR source LIKE 'Ludecus%'
OR source LIKE '%Thompson%'` if you need German incipits specifically.

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

**Krusemark's non-chief-hymn entries are not loaded, nor his Thompson
column** — see above. And
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
