# Emil Sehling's Church Order Corpus

For Corpus guide see `CORPUS_GUIDE.md`

For DB guide see `DB_GUIDE.md`

For Hymn tables guide see `HYMN_GUIDE.md`

For General prayers (Prayers of the Church) guide see `GENERAL_PRAYERS_GUIDE.md`

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
