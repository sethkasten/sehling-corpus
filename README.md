# Emil Sehling's Church Order Corpus

For Corpus guide see `CORPUS_GUIDE.md`

For DB guide see `DB_GUIDE.md`

For Hymn tables guide see `HYMN_GUIDE.md`

For General prayers (Prayers of the Church) guide see `GENERAL_PRAYERS_GUIDE.md`

For the Roman Canon and the priest's prayers in German evangelical Masses (Kantz 1522, Luther's *Formula missae* 1523, Müntzer 1524, Worms 1524, Nürnberg 1524–25, Strasbourg 1524–25, Bremen 1525, Lippe, Kiel, Brandenburg 1540, Calenberg-Göttingen 1542, Pfalz-Neuburg 1543, and Bugenhagen's preparatory prayer), with a corpus-wide concordance and the fraction findings, see `CANON_IN_GERMAN_MASSES.md`

For the ranking of feast days (the fate of the medieval grades, the Lutheran scales of high feasts, second-rank feasts and apostles' days, whole and half holy days, the *Vierzeiten*, ceremonial marks of rank, and rules of occurrence and transfer), with a concordance of the orders quoted, see `FEAST_RANKING_GUIDE.md`

For hymn practice in the Mass, the offices and the occasional rites (where hymns were sung, which hymns filled each slot and how fixed each slot was, hymns in place of the introit, gradual, sequence and offertory, troped and paraphrased Kyrie, Gloria, Credo, Sanctus and Agnus Dei, farced sequences, and the reasons the orders give for their choices), with a concordance of the orders quoted, see `HYMN_PRACTICE_GUIDE.md`

For confessional subscription (what each order named as its *corpus doctrinae* or *norma doctrinae*, from the CA and Melanchthon's *Loci* through the territorial corpora to the Formula and Book of Concord, and the refusals and Reformed reorientations; how ministers were bound by book list, visitation question, examination, *Revers*, oath, ordination vow or signature; and how lay people were bound at confirmation, communion, as godparents, as burghers and as officials), with a table by order and a concordance of the orders quoted, see `CONFESSIONAL_SUBSCRIPTION_GUIDE.md`

For minor orders, liturgical roles, deacons and elders (the fate of the porter, lector, exorcist, acolyte and subdeacon; ministrants, levites, thurifer, candle-bearer, cross-bearer and master of ceremonies; the Lutheran *Diaconus*, the liturgical deacon and the lay deacon of the poor; divine or human right; ruling elders and churchwardens; who was ordained, who took a vow and who was simply appointed, and the grounds given for each office), with an installation table, a table by order and a concordance of the orders quoted, see `MINOR_ORDERS_DEACONS_ELDERS_GUIDE.md`

For the propers of the Mass (introit, prophecy and lessons, epistle and gospel, gradual, alleluia and tract, offertory, Proper Preface and communion: where each was kept or dropped, who sang or read it, Latin or German, the old chant kept, cut or reset, polyphony and organ; the seasonal, festal and sanctoral use of the Proper Prefaces), with a table by order, a concordance, and an appendix rendering every Proper Preface in the corpus in Latin and German with formal-equivalence English, see `PROPERS_GUIDE.md`

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
