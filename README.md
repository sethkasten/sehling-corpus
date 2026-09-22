# Emil Sehling's Church Order Corpus

For Corpus guide see `CORPUS_GUIDE.md`

For DB guide see `DB_GUIDE.md`

For Hymn tables guide see `HYMN_GUIDE.md`

## The three layers

| | What it is | Built by |
|---|---|---|
| `sehling/` | The compiled corpus — every segmented church order, OCR'd | (scraped; see `CORPUS_GUIDE.md`) |
| `eko.db` | Full-text search over the corpus + Sehling's own registers | `build_database.py` |
| `hymns.db` | Chief-hymn prescriptions by Sunday and feast, with English titles | `hymn_tables/build_hymn_db.py` |

Both databases are build artifacts and are gitignored — rebuild them
rather than looking for them in the repo.
