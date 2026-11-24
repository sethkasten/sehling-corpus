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
py hymn_tables/merge_te_laudamus.py
py hymn_tables/merge_lbw.py
py hymn_tables/merge_sbh.py
py hymn_tables/merge_finnish.py
py hymn_tables/merge_slovak.py
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

The database holds **5,631 prescriptions** from **65 witnesses**, in two
quite different evidentiary layers. Keep them apart when you draw
conclusions:

| Layer | Rows | What it is |
|---|---:|---|
| Sehling church orders | 827 | 16th-c. orders prescribing hymns, read from the corpus itself |
| Hymnals and compilations | 4,804 | hymnals, other lists and modern conflations, read from separate documents |

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
| *Te Laudamus* (2024), its table of chief hymns | 85 | 1 | The chief hymn of each Sunday and feast, by its number in the hymnal |
| Hymn of the Week of the *Service Book and Hymnal*, American Lutheran Church (1965) | 62 | 1 | One hymn to each Sunday and festival, from the index of its records *a Time for Singing*, by SBH number |
| *Lutheran Book of Worship* (1978), its Hymns for the Church Year | 82 | 1 | Its de tempore series for the three-year lectionary: the starred hymns of each Sunday and festival, by number |
| Finnish church handbooks of 1614, 1629 and 1694, their gradual hymns | 469 | 3 | The hymn sung between the Epistle and the Gospel, in Finnish, named by the German or Latin hymn it translates where that can be told |
| Ruščin, *Pramene slovenskej hudby* XI (2023), Table 2 | 139 | 2 | Slovak hymns for the Sundays after Trinity, in Czech: the register of the *Cithara Sanctorum* (Levoča, 1674) and the manuscript hymnal B III-107 |

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

**His hymns are named by their numbers.** He gives each hymn by its title
and its number in a hymnal (LSB, TLH, WH, ELH, LW), which the source keeps
(`Gehrke (via Krusemark, Hymns ABC (2018); TLH 383)`). `export_xlsx.py`
names the hymn by that number, through the Lutheran Hymn Index
(`merge_krusemark.identify`, `index_rows.py`), as it names *Te Laudamus*'s.
991 of his 1,047 rows are named so: 610 as hymns of the lexicon, 381 as
hymns it lacks, which take the index's title for the row
(`merge_krusemark.index_title`), as *Te Laudamus*'s do. So his lists join
where they print different hymnals' wordings of one hymn, and join TL's and
the other modern lists' rows of it; two aliases of `export_xlsx.py` join the
Hymn of the Day table's "Soul, Adorn Thyself with Gladness" and "One Thing's
Needful, Lord This Treasure" to the index's titles. The other 56 are named by
title: his rows without a number (German or Latin titles, "Passion hymns",
the Hymnoglypt translations he cites without one), two pages of the
liturgy (LSB 198, 231), and two misprints, whose numbered rows do not bear
his titles (LSB 566 for 556, Carpzov's "Dear Christians, one and all,
rejoice"; LSB 906 for 942, Eckardt's "Kyrie! God, Father in heav'n
above"). His lists of the old usage (Carpzov, Bach, Stiller, the plan of
c. 1700: `merge_krusemark.HISTORICAL`) give a German hymn by the number of
a modern hymnal; where that number is a translation of the Latin hymn, the
hymn is its German version, which Liliencron's English column gives the same
title. The plan's "Come, Holy Ghost, Creator blest" (LSB 498/9) is Luther's
*Komm, Gott Schöpfer, Heiliger Geist*, and Carpzov's "O Christ, who art the
Light and Day" (LSB 882) is *Christe, der du bist Tag und Licht*, as the
Leipzig hymnals of 1605, 1627 and 1694 give them for Pentecost and
Invocavit. Builds before November 2026 read his titles alone. 55 rows were
then unmatched whose numbers name a lexicon hymn (Bach's *Das neugeborne
Kindelein* and *Nimm von uns, Herr, du treuer Gott*, the plan's *Helft mir
Gotts Güte preisen* and *Kommt her zu mir, spricht Gottes Sohn*, the modern
lists' *Such, wer da will, ein ander Ziel*); 16 were taken for a lexicon
hymn of a like title that their numbers deny; and 14 for another lexicon
hymn than their numbers name (LSB 696, *O Gott, du frommer Gott*, was *Auf
meinen lieben Gott*).

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

#### Te Laudamus

`hymn_tables/TL_Chief_Hymns.md` is the table of chief hymns of *Te Laudamus*
(2024), one line to an occasion, each hymn named by its number in the
hymnal: `Advent 1: 151`. A number can carry the letters of the parts or
settings the hymnal prints (`159a/b`, `204a/b`); a slash joins two numbers
of one hymn (`202/203a/b`: TL prints *O Mensch, bewein dein Sünde groß* as
202 and 203), and `OR` gives a second hymn for the day (`Trinity 4: 274 OR
275`). `merge_te_laudamus.py` loads the 85 chief hymns of its 84 occasions,
with the source `Te Laudamus (2024) (via its chief-hymn table; TL 151)`.

Each number is looked up in TL's index of hymn titles (`Hymnal Index/Hymnary
Tables and PDFs/Te Laudamus/te_laudamus_index.csv`), which gives the row its
`original_title` as TL prints it (*From Heaven High I Come to Earth*), and in
the Lutheran Hymn Index, whose row names the hymn: the hymn of the lexicon
matched to that row (`index_titles.INDEX`; of a Latin hymn and its German
version on one row, the one the row's German or Latin title is, so TL 169,
Luther's *Christum wir sollen loben schon*, is not *A solis ortus cardine*).
56 rows are hymns of the lexicon. The other 29 are later hymns the lexicon
does not hold (Gerhardt's *O Haupt voll Blut und Wunden*, Neumark's *Wer nur
den lieben Gott lässt walten*, Rinkart's *Nun danket alle Gott*, the *Dies
irae*, ...), and keep their English titles, as the other modern lists do.
`common_english` is the title the index gives the row (`index_titles.title`).

The occasions are those of the other modern lists (Krusemark's): `Christmas`,
`Sunday after Christmas`, `Quinquagesima (Estomihi)`, `Easter 5
(Rogate/Vocem jucunditatis)`; TL's *Epiphany 6 (Transfiguration)* is `Epiphany
6`, the Sunday whose old gospel is the Transfiguration, and *Holy Saturday
(Matins)* is `Holy Saturday`. An entry for two services keeps them together:
`Christmas (Midnight & Dawn)`, `Easter Evening & Easter Monday`, `Pentecost
Evening & Pentecost Monday`.

`export_xlsx.py` identifies TL's rows by their numbers
(`merge_te_laudamus.canonical`, through `index_rows.py`, as it does
Krusemark's, LBW's and the SBH list's), since an English title can stand for two
hymns (*If God Had Not Been on Our Side*: see *Hymn identity across
languages*). `bridge.py` has four more index titles that the modern lists
give (*Of the Father's Love Begotten*, *O Mortal, Mourn Thy Grievous Sin*,
*We Thank Thee, Jesus, Dearest Friend*, *O Lord, We Praise Thee*), so their
rows and TL's are one hymn in the workbook. *Te Laudamus* is a modern witness
and is not counted in Appendix 8.A (`MODERN` in `appendix_8a.py`).

#### Lutheran Book of Worship

`Hymnal Index/LBW-hotd/` holds the three pages of *Lutheran Book of
Worship*'s "Hymns for the Church Year" (1978, pp. 929–931), and
`hymn_tables/LBW_Hymns_Church_Year.csv` transcribes them: every hymn of each
Sunday and festival, 240 on 66 days, with its LBW number, its star and the
letters of the lectionary years it suits. Every number agrees with the title
the Lutheran Hymn Index gives its row. A star marks the hymns "which
constitute a contemporary adaptation of the traditional Lutheran de tempore
series", and `merge_lbw.py` loads only these, 82 on 63 days, as the chief
hymns of one witness, `Lutheran Book of Worship (1978)`, as only Krusemark's
Hymns of the Day are loaded. Of the starred hymns, those without letters
serve every year of the three-year lectionary and the others the years they
name, so a day's rows are those of all three years. The source keeps LBW's
day and letters: `Lutheran Book of Worship (1978) (via its Hymns for the
Church Year, 13 Pentecost; LBW 303, A)`.

LBW's days are those of the three-year lectionary, whose Sundays read other
Gospels than the old series'. They take this database's labels by their
place in the church year:

- Easter Day is the first Sunday of Easter, so *2 Easter* is `Easter 1
  (Quasimodogeniti)` and *7 Easter* `Sunday after Ascension (Exaudi)`.
- The Holy Trinity is the first Sunday after Pentecost, so *2 Pentecost* is
  `Trinity 1` and *27 Pentecost* `Trinity 26`. *Christ the King*, the last
  Sunday after Pentecost, is `Trinity 27`, the last Sunday of the year.
- *Baptism of Our Lord* and *Transfiguration* take the labels of the modern
  one-year lists, `Baptism of Christ (Octave of Epiphany)` and
  `Transfiguration`, and the *Sunday of the Passion* is `Palm Sunday`.
- *7 Epiphany* and *8 Epiphany*, which the old series lacks, are `Epiphany 7`
  and `Epiphany 8`.

So a day's LBW hymn need not be the hymn of the same Gospel: LBW's Good
Shepherd Sunday, *4 Easter*, is `Easter 3 (Jubilate)`. On 11 days the old
witnesses give LBW's hymn for the same day, most of them feasts (*Nun komm*
on Advent 1, *Christ lag* at Easter, *Komm, Heiliger Geist* at Pentecost);
after Trinity, where the three-year readings part from the old ones, hardly
ever.

Each hymn is found by its LBW number through `index_rows.py`, as TL's are.
38 rows are hymns of the lexicon; the other 44 are hymns it lacks (Coffin's
*Iordanis oras praevia*, Kingo's and Ingemann's Danish hymns, English hymns
from Wesley to Franzmann), which keep the index's English titles.
`original_title` is LBW's title as printed, `common_english` the index's
title for the row. *Lutheran Book of Worship* is a modern witness and is not
counted in Appendix 8.A.

#### The Service Book and Hymnal's Hymn of the Week

The *Service Book and Hymnal* (SBH, 1958) appointed no chief hymns, but the
American Lutheran Church set out a Hymn of the Week for it in 1965: one hymn
to each Sunday and festival, in *The Hymn-of-the-Week Songbook* (Augsburg,
1965) and on three records, *a Time for Singing: around the year with the
Hymn-of-the-Week*, whose sleeve indexes the 62 hymns by the seasons. A
photograph of the sleeve is in the owner's Google Drive (`Hymnal Project/Large
PDFs/Hymn of the week - a songbook (SBH Companion).jpg`), and
`hymn_tables/SBH_Hymn_of_the_Week.csv` transcribes its index: each hymn's
side, its page in the songbook, the heading it stands under, its title, its
SBH number and the day it falls on. `merge_sbh.py` loads the 62 as one
witness, `Hymn of the Week (SBH, 1965)`, with the source `Hymn of the Week
(SBH, 1965) (via a Time for Singing, side 4; SBH 374, songbook p. 37)`.

The sleeve lists the hymns "in the order of their appropriateness for the
seasons of the church year", and the order of the records is the order of
the year; the songbook's pages are not (below). The records are stacked,
sides 1–3 playing first and 4–6 after, and the sleeve prints sides 4, 5 and
6 from right to left under sides 3, 2 and 1. Read so, its seasons hold one
hymn to a day:

- Advent 1–4; Christmas, the Sunday after Christmas and `Christmas 2`;
- the Epiphany, Epiphany 1–4 and the `Transfiguration`, which the SBH keeps
  on the last Sunday after the Epiphany;
- the three 'Gesima Sundays, Lent 1–5, Palm Sunday and Good Friday;
- Easter, Easter 1–5, the Ascension and Exaudi;
- Pentecost, the Holy Trinity and Trinity 1–27 (the sleeve's four "cycles" of
  the Trinity season), ending with *Wake, Awake* on Trinity 27;
- the Reformation and All Saints' Day.

The Gospels bear the order out: *The King of Love My Shepherd Is* falls on
Misericordias Domini, *O Bread of Life* on Laetare, *Take My Life* on
Trinity 9 (the unjust steward), *Deck Thyself with Joy and Gladness* on
Trinity 20 (the wedding garment) and *Shepherd of Tender Youth* on Trinity
24 (Jairus's daughter). The days of the third Christmas hymn and the sixth
Epiphany hymn are the editor's reading: a hymn of the week goes with a
Sunday, New Year's Day falls in the week of the Sunday after Christmas, and
*God's Word Is Our Great Heritage* suits the Transfiguration's "hear him"
and its Epistle's "more sure word of prophecy" (2 Peter 1:19). On 10 days
its hymn is one the old witnesses give for the same day (*Vom Himmel hoch*
at Christmas, *Komm, Heiliger Geist* at Pentecost, *Wachet auf* on Trinity
27).

The pages are probably not misprinted, though 12 and 46 stand twice and 11,
33, 55 and 63 are wanting. Two short hymns seem to share each of pages 12
and 46 (*Children of the Heavenly Father* and *Come, Thou Bright and Morning
Star*; *My God, How Wonderful Thou Art* and *In Christ There Is No East or
West*), and four long hymns to run from a left-hand page across the opening
(*Of the Father's Love Begotten*, 10–11; *Come, Holy Spirit, God and Lord*,
32–33; *Ye Watchers and Ye Holy Ones*, 54–55; *For All the Saints*, 62–63),
so that the 62 hymns fill pages 1–64 exactly. Three times the songbook
leaves the order of the year so that a long hymn starts on a left-hand page:
*Jesus Shall Reign* (Epiphany 3) stands on 9, before Epiphany 1; *Ye
Watchers* (Trinity 22) before Trinity 21's hymn (56); *For All the Saints*
(1 November) before the Reformation's (64). Where the pages and the records
part, the readings side with the records: *Lord, Keep Us Steadfast in Thy
Word* goes with Trinity 21's "sword of the Spirit, which is the word of God"
(Ephesians 6:17), and *O Lord of Life* (61, after Trinity 26 and 27) with
Trinity 25's dead in Christ (1 Thessalonians 4:13–18). The songbook itself
has not been seen.

Each hymn is found by its SBH number through `index_rows.py`. The index
numbers the SBH's hymns of two tunes 8a and 8b, which the sleeve cites as 8
(`index_rows.rows_lettered`). 17 are hymns of the lexicon; the other 45,
English hymns for the most part, keep the index's English titles.
`original_title` is the sleeve's title, `common_english` the index's title
for the row. The list is a modern witness and is not counted in Appendix 8.A.

#### The Finnish church handbooks

Three Finnish church handbooks (*Käsikirja*) of the seventeenth century give
a hymn for each Sunday and feast, sung between the Epistle and the Gospel:
the gradual hymn (*graduaalivirsi*), "a psalm or hymn of praise drawn out of
Scripture", as the handbook of 1614 puts it. The scans are in `Hymnal
Index/Hymnal PDFs for hotd/`:

| Witness | Scan | PDF pages | Rows | Days |
|---|---|---|---:|---:|
| `Finnish handbook (Sorolainen, 1614)` | `Sorolainen 1614.pdf` | 38–43 | 90 | 67 |
| `Finnish handbook (Elimaeus, 1629)` | `Elimaeus 1629.pdf` | 32–35 | 84 | 68 |
| `Finnish handbook (1694)` | `Karoliininen Käsi-kiria 1694.pdf` | 65–81 | 295 | 80 |

Olavi Rimpiläinen's study of the chief service in the diocese of Viipuri
(*Päiväjumalanpalvelus Viipurin hiippakunnassa puhdasoppisuuden aikana*,
1980) led to them: his appendices give the 1629 list and set the 1614 and
1694 lists side by side. The lists here are read from the prints, which
correct him in places; the transcriptions' notes say where:

- the 1614 handbook's "Vdhen wuoden päiven" is the name of New Year's Day,
  set in the type of the hymns, and not a hymn: the 1629 and 1694 handbooks
  print it as a heading over the same hymn;
- his table leaves out two of the 1694 hymns (*Kylwäjä Siemenens* on
  Sexagesima, *Kehu Kielen* on Palm Sunday) and the last four for the days
  of thanksgiving, fasting and prayer, gives *Mailman menon turhudest* twice
  on Trinity 26, and marks the Nunc dimittis of 1614 at the Purification
  "Sama" (the same) for 1694, which does not have it;
- his reprint of the 1629 list has "synnisie" for "synnisit", "Betlehem",
  the heading "Pyhiltä" for "Pyhinä", and *O laupias HErra Jumala* without
  "Isä".

Each transcription (`hymn_tables/Sorolainen_1614_Gradual_Hymns.csv`,
`Elimaeus_1629_Gradual_Hymns.csv`, `Karoliininen_1694_Gradual_Hymns.csv`)
gives, row by row in the order of the print: the PDF page; the heading and
number the hymn stands under; its title as printed; a literal English gloss;
the day; the German or Latin hymn it translates, where that can be told; the
lexicon's title for it; how sure the identification is; and a note. Hands
later than the print have added hymns in the margins of the 1614 copy; these
are not transcribed.

**Identification.** The Finnish hymns are mostly translations, of German
hymns above all, and many incipits render the German word for word: *Ole
kijtetty JEsu Christ* is *Gelobet seist du, Jesu Christ*, *Linna luja on
Jumala* is *Ein feste Burg ist unser Gott*, *Juur Wirtais wieres Babylon*
is *An Wasserflüssen Babylon*. These are `certain`. A hymn is `probable`
when its incipit agrees with the original's in sense, or is the same
psalm's on a day that suits it (*Autuas se cuin pelkä HErra*, Psalm 128,
for the wedding at Cana on Epiphany 2), and `possible` when it could be one
of two hymns or is guessed from the day's Gospel. Only certain and probable
identifications name the hymn in `hymns.db` (`merge_finnish.canonical`): a
possible one stays in the note, and its row, like a row not identified at
all, is named by its Finnish title. Of the 469 rows, 183 are named by a
hymn of the lexicon. Psalm hymns and canticles the lexicon lacks (Psalms 6,
37, 41, 42, 46, 52, 82, 85, 91 and 139, the Magnificat, the Nunc dimittis)
and the Athanasian Creed in verse are identified in the note and keep their
Finnish titles. Two choices are the editor's:

- *Tule Pyhä Hengi luoja*, the Veni Creator, is counted as Luther's German
  version of it, *Komm, Gott Schöpfer, Heiliger Geist*;
- *Jos eij HErra auta meitä*, a Psalm 124 hymn, is counted as Luther's *Wär
  Gott nicht mit uns diese Zeit*, the commoner of the two German Psalm 124
  hymns on Epiphany 4 (the Conversion of St Paul has neither).

**Days.** The 1614 and 1629 handbooks give one hymn to a day, now and then
two; the 1694 handbook three or four to most days, and twelve at Pentecost.
All of a day's hymns count for it, as the several hymns of one day do for
any witness. The days take this database's labels:

- the handbooks keep the Transfiguration on the 7th Sunday after Trinity
  ("Transfigurationis Christi" between VI and VIII in 1614, no. 7 in 1629,
  "VII. Christuxen kirkastamisest" in 1694), and that Sunday's hymns are the
  `Transfiguration`'s;
- the 1614 and 1629 handbooks give `Septuagesima & Sexagesima` one heading,
  and print the `Baptism of Christ (Octave of Epiphany)` between Christmas
  and New Year; the 1694 handbook prints it between New Year and the
  Epiphany;
- the week before Easter ("Timmintaij wijckon") is `Holy Week`;
- the 1629 handbook adds a 27th Sunday after Trinity: it gives the second of
  the 1614 handbook's two hymns for Trinity 22 a Sunday of its own and moves
  the hymns after it down one (Rimpiläinen, n. 40);
- the 1694 handbook's sixth Sunday after the Epiphany has the three hymns of
  the 27th after Trinity, to which it refers the singer;
- new to the database are `St Matthias (24 Feb)`, from all three, and from
  the 1694 handbook `St Andrew (30 Nov)`, `St Thomas (21 Dec)`, `Ss Philip
  and James (1 May)`, `St Bartholomew (24 Aug)`, the `Rogation days`
  (*Rucous Päiwinä*, which Rimpiläinen equates with the Swedish handbook's
  *gångdagar*) and the `Days of public thanksgiving, fasting and prayer`.

**What they show.** The handbooks sing many of the German *de tempore*
hymns in Finnish on the same days. Of the 60 days of Appendix 8.A for which
it gives a hymn, the 1614 handbook gives on 18 a hymn that the German
witnesses give for the day, and on 8 the table's leading hymn: *Wohl dem,
der in Gottes Furcht steht* on Epiphany 2, *Wär Gott nicht mit uns* on
Epiphany 4, *Ein feste Burg* on Invocavit, *Ich ruf zu dir* on Reminiscere,
*Vater unser* on Rogate, *Komm, Heiliger Geist* at Pentecost, *Ach Gott,
vom Himmel* on Trinity 8 and *Nun lob, mein Seel* on St Michael's Day. The
1629 handbook agrees on 17 days and has the same 8 leading hymns; the 1694
handbook agrees on 37 of 62, and has the leading hymn on 15. Many of the
other Finnish hymns follow the day's Gospel: *Weisatcam nyt rickast
miehest* (Luke 16) on Trinity 1, *Jerusalem pyhä caupungi* (Luke 19) on
Trinity 10.

**Appendix 8.A.** The handbooks are old witnesses, but Appendix 8.A, a
table of the German orders and hymnals, does not count them, nor the Slovak
lists below (`OTHER_LANGUAGES` in `appendix_8a.py`; the book's §8.A.1).
`appendix_8a.py --other-languages` prints the table with both counted, and
`--stats` names the days whose hymns would change, for each group and for
both. The Finnish handbooks would change 14 days: Advent 4 would gain *Christ, unser Herr, zum Jordan kam*, Jubilate
*Ich ruf zu dir*, Pentecost *Komm, Gott Schöpfer* and Trinity 19 *Nun lob,
mein Seel*, but Lent 5 would lose both its hymns, since none would then
have a quarter of the day's witnesses.

`merge_finnish.py` loads the three lists after `merge_sbh.py`, with sources
such as `Finnish handbook (1694) (via its gradual hymns; item 47, PDF p.
68)`.

#### The Slovak lists (Ruščin)

The Slovak Lutherans sang in Czech, from Juraj Tranovský's *Cithara
Sanctorum* (Levoča, 1636) and its later editions. Peter Ruščin's article
on the songs on the Sunday Gospels (*postilové piesne*) and the lists of
songs for the Sundays of the church year in the Slovak Lutheran sources of
the Baroque ("Postilové piesne a rozpisy spevov na nedele cirkevného roka v
slovenských evanjelických prameňoch obdobia baroka", in *Pramene slovenskej
hudby XI: Hudba a liturgia*, Bratislava, 2023, pp. 133–154; the volume is
`Hymnal Index/Hymnal PDFs for hotd/Pramene slovenskej hudby Hudba a
liturgia.pdf`) sets out in its Table 2 (pp. 146–151, PDF pp. 148–153) the
songs that five sources give for the Sundays after Trinity:

| Source | Rows | Loaded as |
|---|---:|---|
| The register of the *Cithara Sanctorum* (Levoča, 1674), "Poznamenání písní některých k obecným nedělím po sv. Trojici případných" | 99 | `Cithara Sanctorum (Levoča, 1674)` |
| The manuscript hymnal B III-107 of the Literary Archive of the Slovak National Library, Martin, from central Slovakia | 40 | `Slovak manuscript B III-107 (c. 1674-1720)` |
| Eliáš Mlynárových, *Písniční knížečka*, 2nd ed. (Kežmarok, 1707), its "Nedělní písničky na evangelia" | 27 | not loaded |
| Matej Bodó, *Zvuk evangelium věčného* (1743) | 27 | not loaded |
| Ján Blasius, *Rozkoše aneb Okrasa domu Božího* (1741, 1745) | 28 | not loaded |

Ruščin's Table 1 gives the order of the seventeenth-century service: after
the Epistle a hymn "de tempore" or a song on the Gospel; after the Gospel
the Creed (*My všickni věříme*); after the sermon a hymn "de tempore" or
one of the register. Tranovský left the cantor to choose the hymns of the
day, and the Levoča editions of the Cithara from the second half of the
century added the register for the Sundays after Trinity, which the seasons
did not guide: four hymns to a Sunday, for 25 Sundays. The editions of the
eighteenth century extend it to the whole year, with up to eight or nine
hymns to a day; Ruščin does not set that register out, and it is not here.
The manuscript B III-107, which Ruščin dates c. 1674–1720 (1674–1710 in the
table, 1655–1720 in his abstract), gives the songs a congregation sang
before and after the sermon ("po kázni") on these Sundays: songs on the
Gospel by Jakub Kunvaldský or of unknown origin, and hymns of the register.

The register and the manuscript are lists of the hymns of the day, and
`merge_slovak.py` loads them as two witnesses, after `merge_finnish.py`,
with sources such as `Cithara Sanctorum (Levoča, 1674) (via Ruščin's table;
item 1, PDF p. 148)`. The three collections are not loaded: each gives its
author's own new text on each Gospel, sung to a known tune, which no other
witness can share, and Ruščin finds that they were little sung in church.

`hymn_tables/Ruscin_Slovak_Trinity_Songs.csv` transcribes all five columns,
221 songs. For each it gives the Sunday and its Gospel; the source; the
title as printed; a literal English gloss; the tune it names ("♪"), with
the German hymn of that tune where it is clear; "after the sermon" for the
manuscript's songs so marked; the day; the German or Latin hymn it
translates; the lexicon's title; how sure the identification is; and a
note. The identifications follow the rules of the Finnish lists. The Czech
Psalm 124 hymn *Jestliť Bůh s námi nebude*, on Trinity 23, is counted as
Jonas's *Wo Gott der Herr nicht bei uns hält*, the commoner of the two
German Psalm 124 hymns on that day, by the editor's rule for the Finnish
Psalm 124 hymn.

**What they show.** 25 of the register's 99 hymns are identified as certain
or probable, 19 of them hymns of the lexicon, and many of them are the
German hymns of the day in Czech. On 12 of its 25 Sundays the register gives
a hymn that the German witnesses give for the same day, and on 5 the
leading hymn of Appendix 8.A: *Es war einmal ein reicher Mann* on Trinity 1,
*Vater unser* on Trinity 7, *Ach Gott, vom Himmel sieh darein* on Trinity 8,
*Es ist das Heil uns kommen her* on Trinity 13 and *Wo Gott der Herr* on
Trinity 23. *Warum betrübst du dich, mein Herz* (Trinity 15), *Dies sind die
heilgen zehn Gebot* (Trinity 18) and *Aus tiefer Not* (Trinity 19) are
among the other hymns the table shows for their days. Of the manuscript's
40 songs, 5 are identified as certain or probable.

**Appendix 8.A.** Like the Finnish handbooks, the Slovak lists are old
witnesses in another language than German, and Appendix 8.A does not count
them. Counted alone, they would change two days: Trinity 1 would have *Es
war einmal ein reicher Mann* alone, and Trinity 20 would gain *Wie schön
leuchtet der Morgenstern*.

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

The hymnal and compilation sources cite a hymn in five ways: by its German
incipit (Liliencron's hymnals, Ludecus), by a Low German or Latin form, by
an English title only (Selnecker's own account and the Hymn of the Day
table, with Carpzov, Bach and the modern lists), by an English title and its
number in a hymnal (Krusemark's lists, *Te Laudamus*, *Lutheran Book of
Worship*, the SBH's Hymn of the Week), or by a German incipit
and an English title (Liliencron's concordance). One hymn has one identity
in all of them:

- **`lexicon.py`** matches printed German, Low German and Latin incipits to
  a canonical title. It covers the hymns of the Sehling orders and the
  hymns of the hymnal sources. Without the latter, a hymn named only by
  the hymnals either stayed unresolved, so that its German and English
  citations were counted as different hymns, or was fuzzy-matched to the
  nearest Sehling hymn.
- **`bridge.py`** maps an English title to its German hymn: first through
  its own table of English titles (`EN_ALIAS`), then through the English
  column of Liliencron's concordance.
- **`index_rows.py`** reads a hymnal number: the number's row in the
  Lutheran Hymn Index, and the lexicon's hymn on that row (the one
  `index_titles.INDEX` matches to it, else the one the row's German or Latin
  original resolves to, if the original is that hymn's whole incipit, word
  for word, punctuation aside).
  `export_xlsx.py` names *Te Laudamus*'s, LBW's, the SBH list's and Krusemark's rows so. A row the
  lexicon lacks is named by the index's title for it, and is not then taken
  for a lexicon hymn of a like title. Krusemark's "Praise the Almighty, my soul,
  adore Him" (LSB 797) showed one such error: a title alias of
  `export_xlsx.py` had made Herrnschmidt's *Lobe den Herren, o meine Seele*
  into Gramann's *Nun lob, mein Seel, den Herren*. The alias now joins only
  the titles of Herrnschmidt's hymn.
- **One English title names two hymns.** *If God Had Not Been on Our Side*
  is Luther's *Wär Gott nicht mit uns diese Zeit* as a hymnal's title (TLH
  267, TL 246), and so in the modern lists and in Krusemark's, who gives the
  number (`EN_ALIAS`). Liliencron's English column gives the title to
  Jonas's *Wo Gott der Herr nicht bei uns hält*, and the Hymn of the Day
  table and Selnecker's account use it in that sense for their old
  witnesses. Liliencron's German shows this for Selnecker on Exaudi,
  Krusemark's Walther's Hymnal 438 for Carpzov on Exaudi, and Selnecker
  offers both on Trinity 5 ("Were God Not with Us at This Time" or "If God
  Had Not Been on Our Side"). An English-only row of a historical witness
  (`parse_hotd_selnecker.HISTORICAL`) therefore takes the title in
  Liliencron's sense (`bridge.RENDERED`). Earlier builds read it as Jonas's
  hymn everywhere but in TL, Krusemark's TLH 267 included, and so gave
  Jonas's hymn to Bach, Stiller and the plan of c. 1700 on Epiphany 4.
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
(`INDEX`), each by a hymnal number on the row (`LSB 656`), since a row's id
in `hymnal.db` is its row number in the spreadsheet and changes as rows are
added. `index_titles.py` also makes the title: the row's master title (as a rule
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
its source: `hymnal_index (LSB 656)`, a hymnal number on the hymn's row of
`hymnal.db`, followed by
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

**`original_title` is not always German.** The Hymn of the Day table,
Selnecker's account, Krusemark's lists, *Te Laudamus*, *Lutheran Book of
Worship* and the SBH's Hymn of the Week cite hymns by
English title only; they give no German
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
