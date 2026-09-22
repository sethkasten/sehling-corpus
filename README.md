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

`hymns.db` is committed (1.2 MB) so it can be queried without building
anything. `eko.db` is not — at 121 MB it is too large for GitHub, and is
gitignored; build it with `build_database.py`.

Both are reproducible from the sources in this repo, so if `hymns.db`
ever disagrees with the parsers, rebuild it and trust the rebuild.
