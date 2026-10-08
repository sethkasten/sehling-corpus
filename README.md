# Emil Sehling's Church Order Corpus

## The book

*Liturgical and Ecclesiastical Life in Reformation Germany: An Examination of the German Church
Orders from 1521–1620* is in one file,
[`LITURGICAL_AND_ECCLESIASTICAL_LIFE.md`](LITURGICAL_AND_ECCLESIASTICAL_LIFE.md). It has a table
of contents, an Introduction (which also describes this repository and how the book was made),
Conventions, seventeen chapters, a Scripture index, an Index of persons and a Glossary of the
rarer terms. Every reference to a section, and every entry in the contents and the indexes, is a
link.

| Chapter | |
|---|---|
| 1 | [The Church Orders: An Inventory by Tradition](LITURGICAL_AND_ECCLESIASTICAL_LIFE.md#ch1) |
| 2 | [The Order of the Mass](LITURGICAL_AND_ECCLESIASTICAL_LIFE.md#ch2) |
| 3 | [Mass Preliminaries](LITURGICAL_AND_ECCLESIASTICAL_LIFE.md#ch3) |
| 4 | [The Propers of the Mass](LITURGICAL_AND_ECCLESIASTICAL_LIFE.md#ch4) |
| 5 | [Collect, Secret and Postcommunion](LITURGICAL_AND_ECCLESIASTICAL_LIFE.md#ch5) |
| 6 | [The General Prayer of the Church: Texts by Family](LITURGICAL_AND_ECCLESIASTICAL_LIFE.md#ch6) |
| 7 | [The Roman Canon in German Evangelical Masses (1522–1544)](LITURGICAL_AND_ECCLESIASTICAL_LIFE.md#ch7) |
| 8 | [Hymn Practice](LITURGICAL_AND_ECCLESIASTICAL_LIFE.md#ch8) |
| 9 | [Organ, Instruments and Bells](LITURGICAL_AND_ECCLESIASTICAL_LIFE.md#ch9) |
| 10 | [The Daily Office](LITURGICAL_AND_ECCLESIASTICAL_LIFE.md#ch10) |
| 11 | [Sermons and Preaching](LITURGICAL_AND_ECCLESIASTICAL_LIFE.md#ch11) |
| 12 | [The Liturgical Calendar](LITURGICAL_AND_ECCLESIASTICAL_LIFE.md#ch12) |
| 13 | [Extraordinary Rites](LITURGICAL_AND_ECCLESIASTICAL_LIFE.md#ch13) |
| 14 | [Art, Architecture, Paraments and Vestments](LITURGICAL_AND_ECCLESIASTICAL_LIFE.md#ch14) |
| 15 | [Ecclesiastical Duties](LITURGICAL_AND_ECCLESIASTICAL_LIFE.md#ch15) |
| 16 | [Minor Orders, Deacons and Elders](LITURGICAL_AND_ECCLESIASTICAL_LIFE.md#ch16) |
| 17 | [Confessional Subscription](LITURGICAL_AND_ECCLESIASTICAL_LIFE.md#ch17) |

The chapters were first written as separate guides. They are kept in [`archive/`](archive/), as
they stood when the book was assembled.

### Tools

The contents and the two indexes are generated from the text of the book. After editing it,
run these from the top of the repository:

| Command | What it does |
|---|---|
| `python3 tools/master_toc.py` | Rebuilds the contents from the headings. |
| `python3 tools/master_scripture.py` | Rebuilds the Scripture index. |
| `python3 tools/master_persons.py` | Rebuilds the Index of persons. The persons, and the forms of their names that it looks for, are listed in the script. |
| `python3 tools/master_links.py` | Checks every link: its target must exist, and a link labelled with a section number must point to that section. |

With `--check`, the first three only report whether the generated part is current. With
`--list`, the two index tools print every reference or name they find, for review.

## The data guides

For the corpus see [`CORPUS_GUIDE.md`](CORPUS_GUIDE.md).

For the database `eko.db` see [`DB_GUIDE.md`](DB_GUIDE.md).

For the hymn tables (`hymns.db`) see [`HYMN_GUIDE.md`](HYMN_GUIDE.md).

For the general prayers (Prayers of the Church) and `general_prayers.db` see
[`GENERAL_PRAYERS_GUIDE.md`](GENERAL_PRAYERS_GUIDE.md).

## The layers

| | What it is | Built by |
|---|---|---|
| `sehling/` | The compiled corpus — every segmented church order, OCR'd | (scraped; see `CORPUS_GUIDE.md`) |
| `eko.db` | Full-text search over the corpus + Sehling's own registers | `build_database.py` |
| `hymns.db` | Chief-hymn prescriptions by Sunday and feast, with English titles | `hymn_tables/build_hymn_db.py` |
| `general_prayers.db` | The general prayer of the Sunday service in 57 orders, petition by petition: original + Jacobean English, bid/rubric, standard category | `general_prayers/build_gp_db.py` |

`hymns.db` and `general_prayers.db` are committed (with `.xlsx` exports) so they can be queried without building
anything. `eko.db` is not — at 121 MB it is too large for GitHub, and is
gitignored; build it with `build_database.py`.

All are reproducible from the sources in this repo, so if a committed
database ever disagrees with its sources, rebuild it and trust the rebuild.
