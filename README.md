# Emil Sehling's Church Order Corpus

For Corpus guide see `CORPUS_GUIDE.md`

For DB guide see `DB_GUIDE.md`

For Hymn tables guide see `HYMN_GUIDE.md`

For General prayers (Prayers of the Church) guide see `GENERAL_PRAYERS_GUIDE.md`

For the Roman Canon and the priest's prayers in German evangelical Masses (Kantz 1522, Luther's *Formula missae* 1523, Müntzer 1524, Worms 1524, Nürnberg 1524–25, Strasbourg 1524–25, Bremen 1525, Lippe, Kiel, Brandenburg 1540, Calenberg-Göttingen 1542, Pfalz-Neuburg 1543, and Bugenhagen's preparatory prayer), with a corpus-wide concordance and the fraction findings, see `CANON_IN_GERMAN_MASSES.md`

For the liturgical calendar (why feasts were kept; the fate of the medieval grades, octaves and vigils; the Lutheran scales of high feasts, second-rank feasts and apostles' days; whole and half holy days; the *Vierzeiten*; ceremonial marks of rank and the festal ceremonies abolished; the keeping of holy days in common life, from rest and its enforcement to markets, weddings and the *Fastnacht*, *Kirchweih* and Midsummer customs; the seasons, with Lenten preaching and catechism, Holy Week, Rogation, the closed seasons and the Ember days as quarter days; fasting, from the abolished fixed fasts to police abstinence, days of fasting and prayer, and fasting before communion; and rules of occurrence and transfer), with a concordance of the orders quoted, see `LITURGICAL_CALENDAR_GUIDE.md`

For hymn practice in the Mass, the offices and the occasional rites (where hymns were sung, which hymns filled each slot and how fixed each slot was, hymns in place of the introit, gradual, sequence and offertory, troped and paraphrased Kyrie, Gloria, Credo, Sanctus and Agnus Dei, farced sequences, and the reasons the orders give for their choices), with a concordance of the orders quoted, see `HYMN_PRACTICE_GUIDE.md`

For confessional subscription (what each order named as its *corpus doctrinae* or *norma doctrinae*, from the CA and Melanchthon's *Loci* through the territorial corpora to the Formula and Book of Concord, and the refusals and Reformed reorientations; how ministers were bound by book list, visitation question, examination, *Revers*, oath, ordination vow or signature; and how lay people were bound at confirmation, communion, as godparents, as burghers and as officials), with a table by order and a concordance of the orders quoted, see `CONFESSIONAL_SUBSCRIPTION_GUIDE.md`

For minor orders, liturgical roles, deacons and elders (the fate of the porter, lector, exorcist, acolyte and subdeacon; ministrants, levites, thurifer, candle-bearer, cross-bearer and master of ceremonies; the Lutheran *Diaconus*, the liturgical deacon and the lay deacon of the poor; divine or human right; ruling elders and churchwardens; sacristans, altar care and the dissolved confraternities; deaconesses and *Seelfrauen*; monks, nuns, beguines, Lollards and the Brethren of the Common Life; who was ordained, who took a vow and who was simply appointed, and the grounds given for each office), with an installation table, a table by order and a concordance of the orders quoted, see `MINOR_ORDERS_DEACONS_ELDERS_GUIDE.md`

For the propers of the Mass (introit, prophecy and lessons, epistle and gospel, gradual, alleluia and tract, offertory, Proper Preface and communion: where each was kept or dropped, who sang or read it, Latin or German, the old chant kept, cut or reset, polyphony and organ; the seasonal, festal and sanctoral use of the Proper Prefaces), with a table by order, a concordance, and an appendix rendering every Proper Preface in the corpus in Latin and German with formal-equivalence English, see `PROPERS_GUIDE.md`

For the collect, secret and postcommunion (what the Lutheran orders kept, stripped, added and altered of the medieval system of proper and multiplied prayers: one collect or two, the Missal collects in German and Veit Dietrich's gospel collects, the abolition of the secret and what took its place, Luther's *Quod ore sumpsimus* and his 1526 thanksgiving as the new fixed postcommunion, the proper postcommunions kept from Müntzer to Calenberg-Göttingen 1542, and the alternatives such as the Nürnberg thanksgiving and the Corpus Christi collect), with tables, a concordance, and an appendix of the postcommunion texts and their Latin sources, see `COLLECTS_GUIDE.md`

For the daily office (Luther's rulings of 1523 and 1526; where the full canonical hours survived in collegiate churches, cathedrals and convents, and where they were cut to a school Matins and Vespers; who prayed them, from schoolboys, vicars and nuns to village congregations; the obligations laid on beneficed clergy, pastors and students; the shape of the reformed hours; Latin, German or both; and the chant, from the old choir books and the Lossius and Spangenberg antiphoners to German psalm tones, polyphony and organ), with a table by order and a concordance, see `OFFICES_GUIDE.md`

For sermons and preaching (Luther's rule that the congregation never meet without the Word; the occasions, from the Sunday gospel and the afternoon catechism to weekday, early, catechism, Passion, prayer-day, funeral and wedding sermons; the texts, the pericopes kept and books preached in course; the shape of a sermon and its plain speech; the limits of an hour or half an hour; postils, borrowed and written sermons; rebuke without names and the mandates against pulpit polemics; the prayer, greeting, confession, general prayer and notices around the sermon; trial sermons and the censure of sermons; and the duties and fines of hearers), with a table by order and a concordance, see `SERMONS_GUIDE.md`

For the extraordinary and occasional rites (baptism in its four families of forms; exorcism and its abolition; churching; confirmation without chrismation; betrothal, its dissolution, marriage, divorce and annulment; extreme unction and the sick, the dying, the condemned and the possessed; funerals and burial; ordination; the installation of pastors, superintendents, abbots and bishops; the installation of elders, sextons and sacristans, schoolmasters, churchwardens and midwives; sick-women and beguines; the evangelical clothing of a nun at Keppel, the election and oaths of *dominae*, abbesses and prioresses, novices in the evangelical monasteries, and the laying aside of the habit; magistrates; church dedication and the *Kirchweih*; the abolished blessings of water, salt, candles, palms, herbs, fire, the font, chrism and bells; the lesser and greater ban, excommunication, public penance and the restoration of the penitent; private confession and absolution; processions; the tonsure, the return of churches and vessels to common use, and the deposition of ministers), with the full liturgies quoted and translated, a table by order and a concordance of the orders quoted, see `EXTRAORDINARY_RITES_GUIDE.md`

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
