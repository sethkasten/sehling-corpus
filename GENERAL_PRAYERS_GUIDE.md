# General Prayers (Prayers of the Church): Reference Guide

`general_prayers.db` holds the **general prayer of the Sunday service**
(*gemein Gebet*, *Vermahnung zum Gebet*, *Fürbitt für alle Stände*) from each
church order in the Sehling corpus that prints one. Each petition is split
into:

- its rubric (the heading or marginal note);
- its bid (the words addressed to the people, "Let us pray for …");
- its prayer (the words addressed to God).

Each of these is given in the original language and in a formal-equivalence
English translation in the Authorized Version idiom. Every petition also has
a standard **category**, so that orders can be compared intention by
intention.

`general_prayers.xlsx` is the same data as a workbook. Start with its
**Compare** sheet. The **Archetypes** sheet collates each family's witnesses
into one text per category.
Eight comparison sheets lay the family texts out with one row per category
and one column per family, so that one category can be read across all the
families. They come in two sets of four:

- **Critical** sheets show the archetype texts with every variant in square
  brackets (see **Family archetypes**).
- **Representative** sheets show one clean text per family, without brackets
  (see **Representative texts**).

| Critical | Representative |
|---|---|
| **Orig Prayers - Critical** | **Orig Prayers - Representative** |
| **Eng Prayers - Critical** | **Eng Prayers - Representative** |
| **Orig Bids - Critical** | **Orig Bids - Representative** |
| **Eng Bids - Critical** | **Eng Bids - Representative** |

The "Bids" sheets hold the rubric (first line) and the bid, that is, the
Archetypes sheet's bid/rubric columns. Excel does not allow "/" in sheet
names and allows at most 31 characters. That is why the names are shortened
to "Orig", "Eng" and "Bids".

| | |
|---|---|
| Witnesses (orders) | 57, dated 1526–1618 |
| Petitions | 455 |
| Text families | 18 (14 Lutheran/Upper German/early evangelical, 4 Reformed) |
| Standard categories | 28 |
| Languages | High German, Low German, Low Dutch, Latin |

## Building or rebuilding it

```
python3 general_prayers/build_gp_db.py        # needs eko.db (verification); ~1 min
python3 general_prayers/check_archetypes.py   # round-trip check of the collation; representative layout
python3 general_prayers/export_xlsx.py        # general_prayers.xlsx from the db
```

`--no-verify` skips the check against `eko.db`. Use it only while you are
editing. A committed `general_prayers.db` should always come from a verified
build.

The texts are curated by hand in the witness files `general_prayers/w_*.py`:

| File | Contents |
|---|---|
| `w_brenz.py` | Brenz family (A) |
| `w_wtb.py` | Württemberg long and short forms (B1, B2) |
| `w_bugenhagen.py` | Bugenhagen family (H) |
| `w_other.py` | Families C–G and I–M |
| `w_reformed.py` | Reformed families (R1–R4) |

Each petition is a `P(cat, r=, b=, p=, r_en=, b_en=, p_en=, sub=, note=, tr_from=, tr_sub=)`
record. The builder:

1. resolves reused translations (see below);
2. checks that every original has an English and every category is known;
3. checks every original text against the corpus;
4. writes the database.

It refuses to write anything if any of these checks fails.

Curation aids live in the same folder:

| Script | What it does |
|---|---|
| `verify.py` / `check.py` | Coverage of curated text against `eko.db` |
| `rawdump.py` | Prints raw OCR around a pattern |
| `extract.py` | Aligns a known archetype against another witness and shows the differences |
| `audit_reuse.py` | Lists the German words that differ wherever a translation is reused from another witness, so the English can be checked |
| `archetypes.py` | Collates each family's witnesses into the `archetypes` table (run by the builder) |
| `check_archetypes.py` | Reads every witness's text back out of the collation and compares it with the witness |

## How the texts were made

**Original text.** This is the base text of Sehling's edition. The editorial
matter is stripped out:

- sigla glued to words;
- footnote numbers;
- variant readings of later editions;
- `[p. N]` and `|12r|` page and folio markers;
- running heads;
- words interleaved from the second column by the OCR.

The spelling of the print is kept. Obvious OCR slips are corrected silently. Variant editions in the apparatus are not taken
in; the witness `notes` say what was left out.

**Verification.** Every rubric, bid and prayer is re-found in its corpus
document by a fuzzy token alignment (longest common subsequence, tolerant of
spelling drift and glued sigla). It must cover at least 90 % of its tokens.
The score is stored in `petitions.verify_coverage`. A score below 1.0 almost
always means an OCR misreading was corrected.

**English.** The translation is formal-equivalence throughout:

- word order, clause structure and connectives are kept where English allows;
- the language is that of the Authorized Version (thee/thou, -eth, "that …
  may", "vouchsafe", "magistrates");
- Scripture quoted in the prayers is rendered in its KJV wording when the
  German follows the same text.

When one order copies another, its petition names the source (`tr_from`).
The source's English is taken over and then patched (`tr_sub`) wherever the
German differs. The patches fail the build if their target text is missing.
`petitions.translation_reused_from` records the source, for 177 petitions.
`audit_reuse.py` was run over all of them.

## What counts as "the general prayer"

**Included.** The prayer of intercession for all estates and needs in the
chief Sunday service. This is normally after the sermon, from the pulpit.
It is in the Mass itself in family L and in the Prone position in Norden
1528. The following count as part of it:

- an exhortation or preface to it;
- confession and absolution, when the order places them inside the prayer;
- the Our Father, Creed or Decalogue, when printed as its close.

Also included, as orders that *prescribe the contents* in indirect speech:

- Magdeburg 1562;
- Osnabrück 1543.

**Excluded, deliberately:**

- **Collect banks**, even when they supply the texts for the prayer:
  - Wittenberg 1536;
  - Brandenburg-Nürnberg 1533;
  - Mansfeld 1562;
  - Lippe 1566;
  - Grubenhagen;
  - Hoya;
  - the Prussian collects;
  - Hanau-Lichtenberg's "XII Collecten".
- **The Litany.** It is often the alternative form, and it is its own genre.
- **Prayer-day, occasional and emergency prayers.** For example the
  Wild- und Rheingraf "drey Gebett" and the Nassau 1618 Agende variant.
- **Afternoon, weekday and vespers forms.** For example the afternoon forms
  of Henneberg, Strasbourg 1598 and Kurpfalz 1563.
- **Orders that only mention the prayer, or give it by reference:**
  - Strasbourg 1577;
  - Hessen 1574;
  - Mecklenburg 1552;
  - Sponheim 1590;
  - Emden 1594 (free prayer);
  - Saxony 1539 (Luther's paraphrase, by reference only);
  - the references to Veit Dietrich's bank.
- **Orders that Sehling prints only as variants of another order.**
  Kurpfalz 1601 is identical to 1563.

## Dates

`witnesses.year` is the date of the order as Sehling edits it. It is **not**
the `year` of the `eko.db` document, which is wrong for several of these
witnesses:

| Witness | Year used | `eko.db` document |
|---|---|---|
| Henneberg | 1582 (Georg Ernst's KO, per running heads) | printed under 1555 |
| Erbach | 1560 | labelled 1587 |
| Solms-Laubach | 1576–80 manuscript | labelled 1603 |
| Sayn | 1590 | mis-dated 1314 |
| Waldeck | 1556 (the printed KO) | labelled with a 1583 mandate |
| Oldenburg | 1573 | labelled 1551 |
| Nassau-Weilburg | 1618 Agende, the appendix to KO 1617 | — |

## Families

The `families` table groups orders by text descent. Within a family,
petitions line up almost one-for-one, so differences in the **Compare**
sheet are real local changes. Examples:

- the house of Saxony in Kursachsen 1580;
- the fallen-away in Pfalz-Veldenz 1574;
- the communicants in Frankfurt 1589.

| Code | Family | Witnesses |
|---|---|---|
| A | Brenz bidding prayer: Schwäbisch Hall 1526 | 5 |
| B1 | Württemberg 1553, long form (bidding + collect) | 5 |
| B2 | Württemberg 1553, short form (continuous prayer) | 17 |
| C | Strasbourg-type bidding exhortation: Hanau-Lichtenberg 1573 | 1 |
| D | Nürnberg *Vermahnung zum Gebet*: Veit Dietrich 1545 | 5 |
| E | Saxon *Gemein Gebet*: Leipzig 1567 (Pfeffinger) | 1 |
| F | Upper German pulpit intercession: Augsburg 1537 | 1 |
| G | Hessian *Vermanung zum Gebet*: 1566 | 1 |
| H | Bugenhagen pulpit exhortation: Braunschweig 1528 | 3 |
| I | Huberinus *Vorbitt*: Öhringen 1544 | 1 |
| J | Lower Saxon *notel*: Lüneburg 1564 | 3 |
| K | Three collects from the pulpit: Worms 1560 | 1 |
| L | Intercessions under the Sanctus: Brandenburg 1540 | 3 |
| M | Pulpit biddings in the Prone pattern: Norden 1528 | 1 |
| R1 | Heidelberg 1563 Sunday prayer | 5 |
| R2 | Heidelberg Lord's-Prayer paraphrase | 2 |
| R3 | Calvin's *grande prière* (Latin): Frankfurt 1554 | 1 |
| R4 | à Lasco/Micron: London 1554 | 1 |

`witnesses.form` describes the shape of each order's prayer, for example:

- `bidding + collect`;
- `exhortation + continuous prayer`;
- `prescription of contents (indirect speech)`.

`witnesses.position` says where the prayer stands in the service and what
surrounds it.

## Categories

The categories were fixed after the whole corpus had been read, not in
advance. They are the intentions that actually recur across the orders.

Each petition has one **primary** category: what it is chiefly *for*.
Other intentions it names in passing go in `subcategories`, separated by
semicolons. The scheme is defined in `general_prayers/categories.py`, and
the `categories` table carries the descriptions.

In the order in which the prayers usually run:

| Category | Covers |
|---|---|
| Exhortation / preface | Call to prayer, usually citing Mt 18:19, Mt 7:7 or 1 Tim 2 |
| Confession of sins | Confession and/or absolution placed inside the prayer |
| Repentance & forgiveness | Forgiveness of the congregation's sins; turning away of deserved punishment |
| Thanksgiving | Especially for the Word |
| The Word & its fruit | Pure preaching and its fruit in the hearers |
| The Church | The Church universal, with her ministers |
| Ministers of the Word | Preachers specifically; labourers into the harvest |
| Schools & youth | |
| Civil authority | Emperor, princes, council, officials |
| All estates / households | Marriage, parents, children, servants |
| Peace | |
| Enemies | Their conversion |
| Against the Turk | |
| The erring & unbelievers | Heretics, papists, Jews, heathen |
| The persecuted | |
| The afflicted | Sick, poor, captive, widows and orphans, dying |
| Deliverance from calamities | War, pestilence, dearth |
| Women with child | |
| Fruits of the earth | Weather, daily bread |
| The present congregation | |
| Communicants | |
| Special intercessions | Rubric for particular requests |
| All men | |
| Conclusion | "For all things for which God will be prayed", or the doxology |
| Lord's Prayer | |
| Creed | |
| Ten Commandments | |
| Blessing | |

Two conventions matter when you compare:

- **Closing bids.** A bid of the kind "for all that God will be prayed, say
  the Our Father" is classed **Lord's Prayer**, with *Conclusion* as a
  secondary category. The continuous-prayer summary "Auch bitten wir für
  alles …" is classed **Conclusion**.
- **The Word, the Church and ministers are kept apart:**
  - **The Word** is the course and fruit of preaching;
  - **The Church** is the Church and her ministers together;
  - **Ministers** is used where preachers are prayed for on their own.

## Schema

### `petitions`: one row per petition

| Column | |
|---|---|
| `witness_key`, `seq` | Order, and position within its prayer (1-based) |
| `category`, `subcategories` | Standard codes; secondary codes are `; `-separated |
| `rubric_original`, `rubric_english` | Heading or marginal note |
| `bid_original`, `bid_english` | Bid to the people |
| `prayer_original`, `prayer_english` | Prayer to God |
| `note` | Editorial note on this petition |
| `translation_reused_from` | `witness_key#seq` whose English was taken over and patched |
| `verify_coverage` | Lowest token coverage of this row's original texts in `eko.db` |

A row can have any combination of rubric, bid and prayer:

| Shape of the order | Fields filled |
|---|---|
| Bidding + collect (A, B1) | Bid and prayer |
| Exhortation (D, H, J) | Bid only |
| Continuous prayer (B2, R1) | Prayer only, with rubrics where printed |

### `witnesses`: one row per order

The columns are:

- `year`;
- `order_title`;
- `territory`;
- `citation` (Sehling volume and pages);
- `eko_doc_id` (a comma-separated pair when the text runs over two corpus
  documents);
- `family`;
- `family_code`;
- `tradition`;
- `form`;
- `position`;
- `heading_original`;
- `heading_english`;
- `notes`;
- `n_petitions`;
- `categories_sequence` (for example
  `exhortation > church > civil-authority > …`).

### `families` and `categories`

These are lookup tables with descriptions, as above.

### `archetypes`: one row per family × category

There are 18 × 28 = 504 rows. A row is empty where no witness of the family
has a petition of that category. It has these columns:

| Column | |
|---|---|
| `family_code`, `category` | |
| `prayer_original`, `prayer_english` | The collated prayer |
| `bid_original`, `bid_english` | The collated rubric (first line) and bid |
| `rep_prayer_original`, `rep_prayer_english` | The representative prayer |
| `rep_bid_original`, `rep_bid_english` | The representative rubric and bid |
| `witnesses` | The family's witnesses that have a petition of this category |
| `n_texts` | Separately collated petitions in the cell |
| `named_within` | Categories of petitions that mention this intention only in passing |

See **Family archetypes** and **Representative texts** below for how the
texts are made.

### Views

| View | What it gives |
|---|---|
| `prayers_of_the_church` | The flat view in the order requested. Columns: year, order, territory, seq, prayer (original/English), source, bid/rubric (original/English, rubric and bid joined), category label, subcategories, family, form, tradition. |
| `category_pivot` | Witness × category. Each cell lists the petition numbers where the category occurs: `3` means primary, `(3)` means secondary. This is the comparison table. |
| `category_matrix` | Each witness with its `categories_sequence`. |
| `category_usage` | For each category, the number of petitions and of witnesses that use it. |

## Family archetypes

The `archetypes` table, and the **Archetypes** sheet of the workbook, give
each family's text for each category. All of the family's witnesses are
collated into it, so its expansions and local variants can be read at a
glance. Nothing in it is newly written. Every word is taken from a curated
witness text, original or English.

**Base text.** The archetype is the family's earliest witness, verbatim.
This is the witness named in the `families.archetype` column.

**Alignment.** Each other witness is aligned to the base word by word:

- It is a longest-common-subsequence alignment.
- Spelling is ignored, for example *vnd/und*, *ruw/ruhe*, *-dt/-t*, *ai/ei*,
  doubled letters, a final *-e*, and small inflectional drift.
- Variation units separated by two agreeing words or fewer are merged into
  one unit.

**Reading the brackets.** These conventions apply in both the original and
the English:

| Written as | Meaning |
|---|---|
| plain text | The archetype's reading |
| `[a \| W1, W2: b \| W3: om.]` | The archetype reads *a*; W1 and W2 read *b*; W3 lacks it |
| `[+ W1: b]` | W1 adds *b* at this point |
| `[W1 instead: …]` (after a text) | W1 has an unrelated text in its place, with its own variants nested |
| `[om. W1, W2]` (after a text) | These witnesses of the family lack the petition, bid or rubric altogether |
| `[+ W1, W2: …]` (a whole block) | A petition, bid or rubric the archetype lacks. The earliest witness that has it is the base, with the others' variants nested. |

Sehling's own editorial square brackets are shown as `⟨ ⟩` here.

**Several petitions in one category.** Where a family has more than one
petition in a category, they are collated separately and separated by a
blank line. This happens, for example, with Lüneburg's two petitions for the
magistrates, and with the confession and the absolution. A witness's
petition joins the archetype petition it resembles. It counts as related
when the alignment covers at least 30 % of the longer text, or at least
45 % of the shorter text and 20 % of the longer. A petition that resembles
none is shown as an addition.

**English.** The English is collated in the same way, from each witness's
own translation. A witness's English variants are shown only where its
original differs from the base, so two renderings of identical words never
count as a variant.

**Round-trip check.** `check_archetypes.py` reads every witness's text back
out of the brackets and compares it with the witness:

- 675 original texts are checked;
- in English, the base and every witness whose original differs are checked;
- 1,278 texts in all, with no mismatches.

**Limitations.** Some regional word forms still show as variants, such as
Low German *mi/mick* and *di/dick* in Hamburg 1529. Where one print joins
two words (*zuerwerben*), it can read as an omission of one of them.
Variation units that overlap across many witnesses merge into one wide
unit, as in the naming of the ruler in the B2 petition for the magistrates.

## Representative texts

The representative texts give one clean text per family and category, with
no brackets. They are built from the same collation as the critical texts,
following five rules.

1. **Layout.** A representative cell is filled exactly where the critical
   cell is. `check_archetypes.py` checks this.
2. **Majority.** A petition is kept if at least half the family's witnesses
   to that category have it. Within a petition, a rubric, bid or prayer is
   kept if at least half its witnesses have it. Word by word:
   - a variant replaces the parent's reading only if at least half the
     witnesses to that text have it, and more have it than have the parent's
     reading;
   - an addition is kept if at least half the witnesses to that text have it.
3. **Moved words.** A transposition appears in the collation as an omission
   at one place and an addition at another. Both are decided by the votes
   above, so the order that more witnesses have wins. On a tie, the
   parent's order is kept: an addition with exactly half the witnesses is
   dropped when its words already stand in the parent close by.
4. **Consistent openings and endings.** Within each family one pattern is
   applied, taken from the family's own majority:
   - **A (Brenz):** bids end "Bittend also:" (*Pray ye thus:*). Collects end
     bare, as in Schwäbisch Hall 1526. The mediation formula and Amen that
     two collects carry are removed.
   - **B1 (Württemberg long form):** bids end "Bittend also:". Collects end
     "durch unsern Herrn Jesum Christum, Amen." (*through our Lord Jesus
     Christ. Amen.*) wherever they carry a mediation formula or lack a
     closing Amen.
   - **L (Brandenburg):** collects end "durch deinen son Jesum Christum,
     amen." (*through thy Son Jesus Christ. Amen.*). This replaces the
     abbreviation "durch unsern herrn etc.".

   The other families' texts are continuous prayers or exhortations whose
   openings and endings are already consistent.
5. **Divergent texts.** Where no reading has half the witnesses, the
   parent's reading stands. The parent is the earliest witness: the
   archetype, or for an added petition the earliest witness that has it.
   The same applies when no petition, or no group of related texts, has
   half the witnesses.

**English.** The English is not voted on separately. Each English
variation unit takes the reading of the witnesses whose reading the original
chose at the same place. It is matched to the original by relative position
and by which witnesses vary there. Where only the English varies, meaning
two translations of the same words, the parent's English is kept. The two
columns therefore represent the same text.

**Editorial brackets.** Sehling's editorial brackets are removed. His
alternative in Kurpfalz 1563, "(auch einen erbern rath dieser statt)
[einer erbaren gemein dieses orts.]", is rendered "(auch einen erbern rath
dieser statt oder einer erbaren gemein dieses orts)". The English reads
"(and also an honourable council of this city, or an honourable commune of
this place)".

## What the comparison shows

- **Civil authority is the one universal intention.** It appears in all 57
  orders, and in some it is prayed for twice. The Lüneburg family (J) has one
  petition for the Emperor and all magistrates, and another for the princess
  of the land and the young lordship.
- **Church, then magistrates, is the normal Lutheran sequence.** It comes
  from Brenz 1526 through Württemberg 1553, and so reaches roughly half the
  corpus. The typical series is:

  exhortation > Church > magistrates > afflicted > peace > enemies > women
  with child > fruits of the earth > Our Father.

  The Reformed Heidelberg prayer starts elsewhere:

  confession > thanksgiving > Word > magistrates > all men > persecuted >
  afflicted.

  Its petition for **all men** (1 Tim 2) is a Reformed and Upper German
  feature. It occurs only in:
  - R1 (Heidelberg), including the Lutheran Schaumburg 1614, which borrows
    the Heidelberg prayer;
  - R3 (Calvin);
  - Augsburg 1537.
- **The Word and its fruit is named in almost every family except the
  Brenz/Württemberg line.** There it is folded into the petition for the
  Church. Only two witnesses of that line add it:
  - Pfalz-Veldenz 1574 (long form);
  - Magdeburg 1562.

  It opens the prayer in these families:
  - the Nürnberg exhortation (D);
  - Bugenhagen/Osnabrück (H);
  - the Lower Saxon *notel* (J);
  - Heidelberg (R1, R2).
- **Women with child is nearly universal.** It is named in 42 of the 57
  orders:
  - as a petition of its own in the Brenz and Württemberg long forms;
  - within the petition for the afflicted in the short form and most other
    families.

  It is absent from:
  - the Mass intercessions (L);
  - Calvin, à Lasco and the Heidelberg paraphrase;
  - Veit Dietrich's exhortation (Nürnberg 1545 and Waldeck 1556);
  - Osnabrück, Magdeburg, Leipzig, Hessen, Worms and Norden.
- **Brandenburg 1540 and its followers (family L) put the intercessions in
  the Mass under the Sanctus.** These are collects for the ministers, the
  magistrates and peace, standing where the Roman Canon had its prayers of
  intercession (Sehling's note on Pfalz-Neuburg 1543). They are the closest
  evangelical survival of the Canon's intercessions in the corpus.
- **The Württemberg short form is the most copied prayer in the corpus.**
  Its 17 witnesses run from 1553 to 1618 and reach:
  - Electoral Saxony (1580);
  - Magdeburg;
  - Strasbourg;
  - the Wetterau counts.

  Local changes can be seen in the `notes`. Examples: the name of the
  ruling house; heretics among the enemies; the fallen-away; daily bread.

## Example queries

```sql
-- every petition for the magistrates, oldest first
SELECT year, territory, prayer_original, prayer_english, bid_rubric_english
FROM prayers_of_the_church WHERE category = 'Civil authority';

-- how the Württemberg short form was adapted, petition 2 (magistrates) in every witness
SELECT w.year, w.territory, p.prayer_original
FROM petitions p JOIN witnesses w ON w.key = p.witness_key
WHERE w.family_code = 'B2' AND p.category = 'civil-authority' ORDER BY w.year;

-- which orders pray for women with child, and where in the prayer
SELECT year, witness_key, childbirth FROM category_pivot WHERE childbirth IS NOT NULL;

-- orders that pray for the erring (as primary or secondary intention)
SELECT DISTINCT w.year, w.territory FROM petitions p JOIN witnesses w ON w.key = p.witness_key
WHERE p.category = 'errant' OR ('; ' || p.subcategories || '; ') LIKE '%; errant; %'
ORDER BY w.year;
```
