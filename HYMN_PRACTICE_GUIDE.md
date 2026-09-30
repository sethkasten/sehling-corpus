# Hymn Practice in the Sehling Church Orders

This guide covers where hymns were sung in the evangelical church orders of the sixteenth
century, as printed in Emil Sehling's *Die evangelischen Kirchenordnungen des XVI. Jahrhunderts*.
It asks four questions:

- In which parts of the Mass, the offices and the occasional rites (baptism, weddings, the sick,
  burial, ordination) did the orders put hymns?
- Which hymns did they assign to each of these places?
- Was a given place filled by one fixed hymn, by a choice among a handful, or by a hymn that
  changed with the season, the feast, the Sunday gospel or the sermon?
- What reasons did the orders give for their choices?

It deals with the slots of the service, not with the propers as such. Where a hymn took the place
of a proper (introit, gradual, alleluia, sequence, offertory, communion), the replacement is
recorded. Troped, farced and paraphrased ordinaries (Kyrie, Gloria, Credo, Sanctus, Agnus Dei)
are treated in full.

This guide is separate from `HYMN_GUIDE.md`. That guide documents `hymns.db`, the database of
per-Sunday and per-feast hymn tables. The tables it holds (Pomerania 1569, Pfalz-Zweibrücken
1565, Hof 1592, Weissenfels 1578, Mansfeld 1580, Hohenlohe 1596, Nördlingen 1579 and Heilbronn
1543) are referred to here but not repeated.

The findings are summarised in §1, and the method is described in §2. §3 sets out the slots in
outline. §§4–15 follow the slots of the Mass in order. §16 covers the offices, the catechism and
the weekday services, and §17 the occasional rites. §18 gathers the reasons the orders give. §19
is a concordance of every order quoted.

**Conventions**

- **Quotations.** Every quotation is Sehling's text as it stands in the `eko.db` database built
  from the digitized edition.
  - Footnote numbers, sigla, folio markers and interleaved apparatus are left out.
  - Sehling's own supplied words in square brackets are kept, as are "[!]" and his other signs.
    Words supplied in this guide to complete a sentence cut by a page break or footnote are also
    in square brackets.
  - Spelling and punctuation are as printed, including plain OCR errors (such as "heilaut" for
    "heiland" or "hemehck" for "hemelick").
  - "[…]" marks an omission.
  - Every quotation has been checked against the database text, allowing for OCR noise: at
    least 90 per cent of its words must be found there in order. Its page has been checked
    against the edition's page markers.
  - Each quotation is preceded by an HTML comment, invisible when rendered, that names the
    `eko.db` document it was checked against.
- **Translations.** The English is formal-equivalence, in the idiom of the Authorized Version:
  - Word order and clause structure are kept where English allows.
  - Hymn incipits are translated literally and put in quotation marks, so that the reader can
    see what the words say. They are not given under the titles of the English hymnals. Thus
    "Nun bitten wir den heiligen Geist" is "Now pray we the Holy Ghost", and "Erhalt uns, Herr,
    bei deinem Wort" is "Keep us, Lord, by thy word". In the body of the guide the German
    incipit is used.
  - Stock terms are rendered the same way throughout. *Psalm*, *deutscher Psalm* is "psalm",
    "German psalm"; in these orders it means any metrical hymn, not only a psalm paraphrase.
    *Lied*, *Gesang*, *Lobgesang* are "song", "song of praise". *Gesetz*, *Vers*, *Versch* are
    "stanza" or "verse". *figurieren*, *in mensuris* are "figured music" or "measured music".
    *Amt* is "the office" (the communion service). *Küster*, *Custos*, *Opfermann*, *Köster* are
    "sexton". *Schulmeister* is "schoolmaster". *Leise* is kept.
  - Words the translation supplies are in square brackets.
- **Citations.** Citations are in the form "Sehling volume, page".
  - The half-volumes of the edition are written 6/1, 6/2, 7/1, 7/2.1, 7/2.2, 17/1, 17/2, 19/1,
    19/2, 20/1 and 20/2, following the digitized volumes.
  - Each order is named by place, title and date as they appear in Sehling's running heads.
    These sometimes differ from the database's record headings (see §2.3).

---

## Contents

- [1. Summary of findings](#1-summary-of-findings)
- [2. Scope, sources and method](#2-scope-sources-and-method)
- [3. The hymn slots in outline](#3-the-hymn-slots-in-outline)
- [4. The opening of the service](#4-the-opening-of-the-service)
- [5. Hymns in place of the introit](#5-hymns-in-place-of-the-introit)
- [6. The Kyrie: plain, in three tongues, troped and German](#6-the-kyrie-plain-in-three-tongues-troped-and-german)
- [7. The Gloria: "Allein Gott in der Höh" and "All Ehr und Lob"](#7-the-gloria-allein-gott-in-der-höh-and-all-ehr-und-lob)
- [8. Between the epistle and the gospel](#8-between-the-epistle-and-the-gospel)
- [9. The creed: "Wir glauben all"](#9-the-creed-wir-glauben-all)
- [10. Before the sermon: "Nun bitten wir" and the old *Leisen*](#10-before-the-sermon-nun-bitten-wir-and-the-old-leisen)
- [11. After the sermon: "Erhalt uns", the offertory, and the hymn that answers the sermon](#11-after-the-sermon-erhalt-uns-the-offertory-and-the-hymn-that-answers-the-sermon)
- [12. The Sanctus: "Jesaia dem Propheten" and "Heilig ist Gott der Vater"](#12-the-sanctus-jesaia-dem-propheten-and-heilig-ist-gott-der-vater)
- [13. The Lord's Prayer and the Words of Institution](#13-the-lords-prayer-and-the-words-of-institution)
- [14. Under the communion (*sub communione*)](#14-under-the-communion-sub-communione)
- [15. The Agnus Dei, the thanksgiving, and the close](#15-the-agnus-dei-the-thanksgiving-and-the-close)
- [16. Vespers, matins, the catechism and the weekday services](#16-vespers-matins-the-catechism-and-the-weekday-services)
- [17. Hymns at the occasional rites](#17-hymns-at-the-occasional-rites)
- [18. How hymns were chosen: the reasons given](#18-how-hymns-were-chosen-the-reasons-given)
- [19. Concordance of the orders quoted](#19-concordance-of-the-orders-quoted)

---
## 1. Summary of findings

### 1.1 The main findings

**1. Most hymn slots were fixed.** In nearly every order a given place in the service was
filled by one hymn, or by a choice among two to five. The choice was often exchanged at the high
feasts for a hymn of the feast. Only one slot regularly changed from Sunday to Sunday: the hymn
between the epistle and the gospel. From about 1560 a second slot joined it in some regions: the
hymn after the sermon. The table in §1.2 sets out the pattern slot by slot.

**2. The opening of the service was a prayer for the Holy Ghost.** *Veni sancte Spiritus*, in
Latin or in German ("Komm heiliger Geist, Herre Gott", or the prose "Komm, heiliger Geist,
erfülle"), or "Nun bitten wir", was often sung kneeling. The Hessian *Agende* gives the reason:
"that the help and assistance of the Holy Ghost may be prayed for, for the performing of the
whole service" (§4.1). Many orders also say plainly that the opening songs were sung "until the
congregation cometh together" (§4.2). Some northern orders opened with the German Benedictus or
the German Te Deum instead (§§4.3–4.4).

**3. Hymns took the place of the introit, the gradual, the sequence and the offertory.**
- **Introit.** A Scriptural Latin introit could be kept where a school sang it. Otherwise, and
  in the villages always, "a German psalm" was sung "an stat des introitus". The usual psalms
  were Ps 67, 51, 130, 12, 124 and 14, or "Komm heiliger Geist", usually rotated (§5).
- **Gradual, alleluia and sequence.** These gave way to a German psalm or hymn, often chosen by
  season or gospel (§8).
- **Offertory.** This became a German psalm sung while bread and wine were prepared and the
  communicants came forward (§11.3). In Bugenhagen's orders the creed hymn "Wir glauben all"
  served here, sung after the sermon (§9.2).
- **Communion chant.** This was replaced by the communion hymns (§14).
- **Particular days.** A hymn replaced the gradual at the Purification ("Mit Fried und Freud"),
  the sequence in Passiontide (Ps 51), and the offertory at Christmas ("Ein Kindelein so
  löbelich") (§§8.5, 11.3).

**4. The ordinaries were troped and paraphrased in German.**
- **Kyrie.** Troped German Kyries survive in the Low German Mass of Schleswig-Holstein (after
  1526), Naumburg (1537/38), Mecklenburg (1545), Ritzebüttel (1556), Pfalz-Zweibrücken (1557) and
  Hof (1592). They were sung to the melodies of the Latin *Kyrie summum*, *paschale*, *magne Deus*
  and *fons bonitatis*, and graded by season. The Kyrie was also sung in three tongues, Greek,
  Latin and German (Prussia 1525, Riga 1530) (§6).
- **Gloria.** "Allein Gott in der Höh" was sung for, alternately with, or inside the Latin
  Gloria. In the last case the whole German hymn was inserted between *Et in terra pax* and
  *Laudamus te* (Wolfenbüttel 1543, Hildesheim 1544, Osnabrück 1543). "All Ehr und Lob" was the
  alternative (§7).
- **Creed.** "Wir glauben all" (§9).
- **Sanctus.** Luther's "Jesaia dem Propheten" was usual, and a Trinitarian troped Sanctus,
  "Heilig ist Gott der Vater", was also sung (§12).
- **Agnus Dei.** "Christe, du Lamm Gottes" and "O Lamm Gottes unschuldig" (§15).
- **Lord's Prayer and Verba.** No troped or farced Lord's Prayer or Words of Institution was
  found. The congregation sometimes sang Luther's "Vater unser im Himmelreich" (§13).

**5. At the three high feasts the Latin sequences were farced with German stanzas.** The
pairs were *Grates nunc omnes* with "Gelobet seist du", *Victimae paschali* with "Christ lag in
Todesbanden" (or "Christ ist erstanden"), and *Veni sancte Spiritus* with "Nun bitten wir".
Choir and people, or organ and cantor, sang by turns (§8.3). Most other sequences were dropped as
impure (§8.2).

**6. Before the sermon the congregation prayed in song.** The hymn was "Nun bitten wir", often
begun by the preacher from the pulpit, and sung "an Gebets statt". At the high feasts the old
pre-Reformation *Leisen* took its place: "Ein Kindelein so löbelich", "Christ ist erstanden",
"Christ fuhr gen Himmel", "Gott der Vater wohn uns bei". Some orders sang the Lord's Prayer hymn
in Lent or Advent. Several orders give the whole year as a seasonal table (§10).

**7. After the sermon the core hymn was "Erhalt uns, Herr, bei deinem Wort".** It was sung as a
prayer for the word against the Pope and the Turk (Prussia 1568: "as after every sermon
always"). Other choices were "Es woll uns Gott genädig sein" and "Gott der Vater wohn uns bei".
From the 1570s the Hanau-Lichtenberg, Hohenlohe, Öhringen, Reutlingen, Rostock and Marienhafe
orders wanted a hymn that "agreeth with the sermon". Hohenlohe (1596) gave a menu under twelve
doctrinal articles (§11.5).

**8. The communion hymns hardly changed through the century.** The core was Hus's "Jesus
Christus unser Heiland", "Gott sei gelobet", "Jesaia dem Propheten" and Ps 111, followed by the
German Agnus Dei. What changed was the number of hymns, measured almost everywhere by the number
of communicants. Bugenhagen's orders stopped the song as soon as the distribution ended, "though
a song begun be not sung out" (§14.3). Festal hymns, the Passion, *Discubuit*, *Pange lingua* and
the Te Deum were added at the margin (§14).

**9. Hymns covered movements and actions.** Many orders say that the hymn is sung "while" or
"meanwhile":
- the people gather (§4.2);
- the priest prays at the altar step (§4.6);
- the preacher goes up into or comes down from the pulpit (§§9.3, 10.5, 11.2);
- the priest "takes a little breath" (§11.2) or puts on his vestments (§11.2);
- the bread and wine are prepared (§11.3);
- the communicants come into the choir (§§11.4, 12.1);
- the celebrant takes off his vestments (§15.4).

Hof sang at baptism "that two actions may not follow one upon the other without a song" (§17.1).

**10. The rules for choosing a hymn grew stricter over the century.** In broad order, the
reasons given were these:
- The text must be from Scripture and "pure" (§18.1).
- The hymn must "rhyme with the feast" and the season (§18.2).
- On ordinary Sundays it should "rhyme with the gospel". The rule of Pomerania 1542 and
  Mecklenburg 1545 lists hymns for gospels of faith and grace, of Christ's enemies, of good
  works, and of the use of earthly goods (§8.6).
- It should agree with the sermon (§§11.5, 18.3).
- In the catechism service it should be the hymn of the chief part being taught (§16.6).

Alongside these ran the practical reasons:
- The people should learn a few hymns well, repeated and rotated (§18.4).
- Luther's hymns should come first. Prussia 1568 says no new poet "can hold a candle to Luther"
  (§18.5).
- Private choice by schoolmasters and organists was to be curbed.
- Authorized cantionals were enforced: Spangenberg, Lossius, and an "unfalsified" Luther
  songbook (§18.6).
- There were limits of language, length and organ use (§§18.7–18.9).

### 1.2 The slots compared

"Fixed" means one hymn, or one per grade or feast. "A handful" means a named choice of two to
five, often rotated. "Variable" means the hymn changed with the Sunday, gospel or sermon.

| Slot | Where it falls | Hymns usually named | How fixed |
|---|---|---|---|
| Opening (§4) | before the introit, or before the sermon in the Württemberg type | *Veni sancte* / "Komm heiliger Geist"; "Nun bitten"; German Benedictus; German Te Deum; Ps 51 | **fixed** or a handful; graded by feast in some orders |
| For the introit (§5) | first chant of the Mass | "Es woll uns Gott" (Ps 67), "Erbarm dich mein" (Ps 51), "Aus tiefer Not" (Ps 130), "Ach Gott vom Himmel" (Ps 12), "Wär Gott nicht mit uns" (Ps 124), "Komm heiliger Geist"; festal *Leisen* | **a handful**, rotated; festal exchange |
| Kyrie (§6) | after the introit or confession | Latin by grade; German plain or troped ("Kyrie, Gott Vater in Ewigkeit", "Ach Vater, allerhöchster Gott", "O Herre Gott", "O Vater allmächtiger Gott") | **fixed by grade and season** |
| Gloria (§7) | after the Kyrie | "Allein Gott in der Höh"; "All Ehr und Lob" | **fixed**; Latin and German alternate or combine |
| Between epistle and gospel (§8) | the gradual, alleluia and sequence | farced sequences at the high feasts; German psalm matched to season or gospel; litany-hymn "Nim von uns" | **variable**: Sunday or seasonal tables, gospel rule |
| Creed (§9) | after the gospel, or after the sermon | "Wir glauben all"; sung Apostles' or Nicene Creed | **fixed**; place varies |
| Before the sermon (§10) | after the creed or prayers; from the pulpit | "Nun bitten"; *Leisen* at feasts; Lord's Prayer hymn | **fixed with seasonal exchange** |
| After the sermon (§11) | after the sermon and prayers; the offertory place | "Erhalt uns"; "Es woll uns Gott"; "Gott der Vater wohn uns bei"; any German psalm; sermon-matched hymn | **a handful**, becoming **variable** in later orders |
| Sanctus (§12) | after the preface or exhortation | "Jesaia dem Propheten"; "Heilig ist Gott der Vater"; Latin Sanctus by grade | **fixed** |
| Lord's Prayer and Verba (§13) | before the distribution | "Vater unser im Himmelreich" (rare) | **fixed** or none |
| Under the communion (§14) | during the distribution | "Jesus Christus unser Heiland"; "Gott sei gelobet"; "Jesaia"; Ps 111; Agnus; extras by number of communicants | **fixed core**; quantity varies |
| Post-communion (§15) | after the distribution | "Christe, du Lamm Gottes"; "O Lamm Gottes"; "Gott sei gelobet" | **fixed** |
| Close (§15) | after the blessing | "Verleih uns Frieden" / *Da pacem*; "Erhalt uns"; "Es woll uns Gott"; "Sei Lob und Ehr"; "Dank sagen wir alle"; festal hymn | **a handful**; festal exchange |
| Office hymn (§16) | vespers, matins | Latin hymn *de tempore*, purged; German office hymns | **fixed by season** |
| Catechism service (§16.6) | before or after the catechism sermon | the hymn of the chief part | **fixed by the part taught** |
| Occasional rites (§17) | baptism, wedding, burial, ordination | "Christ unser Herr zum Jordan kam"; Ps 127/128; "Mitten wir im Leben", "Mit Fried und Freud", "Nun lasst uns den Leib begraben"; "Nun bitten", Te Deum | **a handful** per rite |

### 1.3 How the practice changed over the century

- **1523–1535: Luther and Bugenhagen.** Luther's *Formula missae* (1523) wanted German songs
  near the gradual, Sanctus and Agnus. The *Deutsche Messe* (1526) filled these slots.
  Bugenhagen's orders (Braunschweig 1528, Hamburg 1529, Pomerania 1535) fixed the
  northern pattern:
  - German psalm or Benedictus at the start;
  - farced sequences at three feasts;
  - creed as offertory;
  - Hus's hymn and "Gott sei gelobet" at communion, stopped when the distribution ends;
  - "Christe du Lamm Gottes" after all have communicated.
- **1540s: the gospel rule and the *Leisen*.** Pomerania (1542) and Mecklenburg (1545) chose the
  post-epistle hymn by the matter of the gospel. The *Leisen* before the sermon became standard.
  Mecklenburg 1552 had the preachers sing them from the pulpit, and Lüneburg (1564),
  Wolfenbüttel (1569) and Oldenburg (1573) copied the rule.
- **1550s–1590s: tables, sermons, catechism and books.**
  - Sunday tables appeared (Pirna 1555, Pfalz-Zweibrücken 1565, Pomerania 1569, Weissenfels 1578,
    Mansfeld 1580, Hof 1592, Hohenlohe 1596).
  - Orders asked for hymns matched to the sermon (Hanau-Lichtenberg 1573, Öhringen 1582, Brieg
    1592, Marienhafe 1593, Hohenlohe 1596).
  - Catechism hymns spread (Lippe 1571, Hoya 1581, Grubenhagen 1581).
  - Luther's hymns were defended as a canon (Prussia 1568, Harlingerland 1573/74, Hoya 1581).
  - Cantionals were imposed (Lossius, Spangenberg).
- **1607: Hessen-Kassel.** As Hesse turned Reformed, Lobwasser's psalms entered the communion.
  Hymn numbers were posted on boards at the church doors, and the synod asked for a table of
  hymns "accommodated to the texts which should be preached" (§18.3).

---

## 2. Scope, sources and method

### 2.1 The corpus

The source is `eko.db`, the full-text database of Sehling's edition described in `DB_GUIDE.md`.
It holds 2,368 records in 32 digitized volumes and half-volumes, with Sehling's own subject
registers. The orders run from Luther's *Formula missae* (1523) to the early seventeenth century.
They cover Saxony, Thuringia, the Harz counties, Brandenburg, Silesia, Prussia, Pomerania,
Mecklenburg, the Baltic, Schleswig-Holstein, Lower Saxony, Westphalia, Hesse, the Rhineland,
Franconia, Bavaria, Württemberg, Swabia, Alsace and Transylvania.

The guide quotes 161 orders, held in 142 records. Some records hold several orders:
for example, the Henneberg village reports, the Nördlingen and Schwäbisch Hall volumes, and
Prussia 1544/1568.

### 2.2 How the corpus was searched

The search was done in three passes.

1. **Slot vocabulary.** The whole text was searched for the terms by which the orders name the
   places of hymns:
   - Latin: *introitus*, *pro introitu*, *loco introitus*, *post confessionem*, *post
     epistolam*, *graduale*, *sequentia*, *prosa*, *tractus*, *post evangelium*, *ante
     concionem*, *post concionem*, *offertorium*, *sub communione*, *post communionem*,
     *conclusio*, *pro ingressu*, *hymnus*, *cantilena*, *cantio*.
   - German and Low German: *an stat des introitus*, *für den introitum*, *für das Halleluja*,
     *anstat des offertorii*, *an stat des sequenz*, *vor der predigt*, *nach der predigt*,
     *auf die epistel*, *nach der epistel*, *unter der communion*, *under der berichtinge*, *zum
     beschluss*, *tom beslute*, *deutscher Psalm*, *düdesch psalm*, *Lied*, *Leise*, *Gesang*,
     *Lobgesang*, *figurieren*, *orgel*.
   - The incipits of the common hymns and of the ordinaries in German ("Kyrie, Gott Vater",
     "Allein Gott", "All Ehr und Lob", "Wir glauben", "Jesaia dem Propheten", "Heilig ist Gott",
     "Christe du Lamm", "O Lamm Gottes").
2. **Registers.** Sehling's per-volume registers of *Lieder und Gesänge* were read, and every
   page they cite was checked.
3. **Reading the orders.** About three hundred orders with hymn material were then read in the
   passages around each hit. Notes were taken slot by slot, and the rites were read in full.

The guide gives the passages that state a rule, give a reason, or show a practice clearly. Where
many orders say the same thing, the earliest or clearest is quoted and the others are named.

### 2.3 Cautions

- **Prescription, not observation.** Church orders say what should be sung. Only a few sources
  report what was actually sung. The Henneberg village pastors' reports of 1562–1566 are the
  richest of these (Sehling 2, pp. 329–357), with the Langenburg dispute of 1592. Even these may describe what the pastor wished the visitors to
  read.
- **"Psalm".** In these orders *ein deutscher Psalm* means any German metrical hymn, not only a
  psalm paraphrase. "Aus tiefer Not" is a psalm; so is "Nun freut euch".
- **Database headings.** The database's record headings, years and numbering do not always
  match the orders inside them. This guide names each order from Sehling's running heads. In
  particular:
  - Doc 373 (headed 1544) is the Nördlingen St George's order of 1555.
  - Doc 1955 (headed 1590) is the Hadeln order of 1526.
  - Doc 2065 (headed 1571) is the Hoya order of 1581.
  - Doc 1809 holds both the Liegnitz order of 1542 and the Brieg order of 1592.
  - Doc 1248 holds the Henneberg village orders of Belrieth, Goldlauter, Herpf and Meiningen.
    The running head spells Goldlauter "Groldlauter".
  - Doc 1249 holds Obermassfeld and Queienfeld. A passage on p. 344–345 belongs to Queienfeld,
    though the running head of p. 345 names Ritschenhausen.
  - Doc 1250 holds Suhl, Sulzfeld and Wasungen (p. 356 is Wasungen, not Vachdorf).
  - Doc 84 is the Eisfeld visitation order of 1554, and doc 78 the Dresden Kreuzkirche order of
    1574.
  - Doc 1262 holds the Anhalt order of 3 August 1548 and the *Ordnung der deutschen Gesänge* of
    before 8 February 1551.
  - Doc 2204 holds two Goslar chapter orders, of 1560 (p. 319–321) and August 1566 (p. 322–323).
  - Doc 2003, 2009 and 2017 (Lüneburg) are in half-volume 6/1.
- **Sehling's summaries.** For Danzig (1557) Sehling prints a summary with quotations, and the
  guide quotes it as such.
- **Apparatus.** Footnotes, variant readings and editorial notes are interleaved in the database
  text. They have been removed from quotations. Where a quotation crosses a page break or a
  footnote, the break is marked "[…]".
- **Later additions.** A few passages are later additions printed with an earlier order. The
  Brandenburg-Nürnberg rule on the burial of the unrepentant (§17.4) is one; the 1577 variants
  of Kurpfalz 1556 (§12.1) are another. They are marked as such.
- **Not repeated here.** The per-Sunday hymn tables already extracted into `hymns.db` are
  described in `HYMN_GUIDE.md` and are not repeated.

---

## 3. The hymn slots in outline

### 3.1 What the orders called the slots

Most orders name a slot by where it falls: before or after something, or in the place of
something. The Latin orders use *introitus*, *post confessionem*, *post epistolam*, *post
evangelium*, *ante concionem*, *post concionem*, *sub communione* and *conclusio*. The German
and Low German orders say *vor der predigt*, *nach der predigt*, *unter der communion* and *zum
beschluss*. The replacement of a chant is always marked: *an stat des introitus*, *für das
Halleluja*, *anstat des offertorii*, *an stat des sequenz*, *pro introitu*, *loco Et in terra*.

The fullest set of slot labels is the three-week hymn plan of **Pfalz-Zweibrücken, *Ordnung
der Kirchengesänge*, 17 August 1565** (Sehling 18, p. 337). Its first Sunday after Trinity
reads:

<!-- doc 985 -->
> Introitus: Nun freudt euch, lieben [Christen gemein], die erst melodi. Kom, heilliger Geist.
> Post Confessionem: Das zweyt Kyrie. Post Epistolam: Ich glaub an gott etc. Ante Contionem:
> Nun bitten wir etc. Post Contionem: Herr, wie lanng wilt vergessen etc. Conclussio: Christum,
> unnsern Heylanndt.

*Introitus*: "Now rejoice, dear Christians all," the first melody; "Come, Holy Ghost." *After
the confession*: the second Kyrie. *After the epistle*: "I believe in God," etc. *Before the
sermon*: "Now pray we," etc. *After the sermon*: "Lord, how long wilt thou forget," etc.
*Conclusion*: "Christ, our Saviour."

The Mass order of **Hof, *Ordo ecclesiasticus*, 1592** (Sehling 11, p. 425) numbers the same
slots. The eighth is the German hymn to the Holy Ghost before the sermon,
sung kneeling:

<!-- doc 294 -->
> VIII. Organicen cantilenam germanicam ad Spiritum Sanctum directam: Nun bitten wir den
> Heiligen Geist etc. incipit (vel etiam in cantu figurali mutetam aliquam). Illa cantilena
> germanica genibus flexis a tribus choris continuatur.

Eighthly, the organist beginneth the German song directed to the Holy Ghost, "Now pray we the
Holy Ghost," etc. (or else some motet in figured song). That German song is continued by the
three choirs upon bended knees.

### 3.2 Luther's two orders

Luther's *Formula missae* wished for German songs "near the gradual, the Sanctus and the
Agnus Dei", and said that the poets to write them were lacking. **Wittenberg, Luther,
*Formula missae*, 1523** (Sehling 1, pp. 8–9):

<!-- doc 2 -->
> Cantica velim etiam nobis esse vernacula quam plurima, quae populus sub missa cantaret, vel
> iuxta gradualia, item iuxta Sanctus et Agnus dei. Quis enim dubitat, eas olim fuisse voces
> totius populi, quae nunc solus chorus cantat vel respondet episcopo benedicenti? […] Sed
> poetae nobis desunt, aut nondum cogniti sunt, qui pias et spirituales cantilenas (ut Paulus
> vocat) nobis concinnent, quae dignae sint in ecclesia dei frequentari.

I would also that we had as many songs as may be in the vulgar tongue, which the people
might sing during the Mass, either next to the graduals, and likewise next to the Sanctus and
Agnus Dei. For who doubteth that these were once the voices of the whole people, which now the
choir alone singeth, or answereth to the bishop when he blesseth? […] But poets are wanting
to us, or are not yet known, which might make us godly and spiritual songs (as Paul calleth
them), such as be worthy to be used often in the church of God.

Three years later the *Deutsche Messe* had its slots filled. It opens with a German psalm to
the first tone, puts a German hymn after the epistle and the German creed after the gospel.
**Wittenberg, Luther, *Deutsche Messe*, 1526** (Sehling 1, p. 14):

<!-- doc 3 -->
> Zum anfang aber singen wir ein geistlich lied oder einen deudschen psalmen in primo tono auf
> die weise wie folget. „Ich will den Herrn loben alle zeit.“

But at the beginning we sing a spiritual song or a German psalm in the first tone, after the
manner following: "I will bless the Lord at all times."

<!-- doc 3 -->
> Auf die epistel singet man ein deudsch lied: 'Nu bitten wir den heiligen geist’. oder sonst
> eins, und das mit dem ganzen chor. Darnach lieset er das evangelion in quinto tono […] Nach
> dem evangelio singt die ganze kirche den glauben zu deudsch: Wir gleuben all an einen gott.

After the epistle a German song is sung, "Now pray we the Holy Ghost," or some other, and that
with the whole choir. Then he readeth the gospel in the fifth tone […] After the gospel the
whole church singeth the creed in German: "We all believe in one God."

At the communion the *Deutsche Messe* allows the German Sanctus, "Gott sei gelobet" or Hus's
hymn. These three were for the whole century the core of the communion slot (§14)
(Sehling 1, p. 15):

<!-- doc 3 -->
> Und die weil singe das deudsche sanctus oder das lied: Gott sey globet oder Johans Hussen
> lied: Jhesus Christus unser heiland. Darnach segene man den kilch und gebe den selbigen auch
> und singe, was ubrig ist von obgenanten liedern oder das deudsch Agnus dei.

And the while let the German Sanctus be sung, or the song "God be praised," or John Hus's
song, "Jesus Christ our Saviour." Thereafter let the cup be blessed and given likewise, and
let that be sung which remaineth of the aforenamed songs, or the German Agnus Dei.

### 3.3 A whole service in hymns

Where there was no school to sing Latin, nearly every part of the service became a German
hymn. The village order of the city of Braunschweig lists them in order. **Braunschweig,
*Ordnung der ceremonien auf den dorfern*, undated** (Sehling 6/1, p. 473):

<!-- doc 1988 -->
> Sal erstlick der pfarher mit dem opfermann und ganzem volk singen: Kum heiliger Geist, Here
> Godt etc. 2. Damach das Kirieleison und et in terra deutsch, wie es Doctor Martinus
> vordeutschet hat. 3. Darauf sal der pfarher die collecten und epistel lesen. 4. ALßdann sol
> der opfermann mit dem volk das Vaterunser singen, auch wie es Doctor Martinus gemacht hat.
> 5. Nach diesem sal der pfarher dem volk die funf haubtstucke des catechismi […] vorlesen.
> 6. Darauf sal der opfermann mit dem volk singen erstlick den glauben, darnach: Nhun piten wir
> den heiligen Geist. 7. Dan sal der pfarher das evangelium von der kanzel lesen und die
> predigt darauf thim. 8. Nach der predig sal der opfermann mit dem volk dat Sanctus Esaie
> deutsch singen. 9. Darnach sal der pfarher die vormanung an die communicanten lesen und das
> Vaterunser und die verba coene so pald darauf singen deutsch. 10. Unter der communion sal
> der opfermann mit dem volk singen: Jesus Christus ader Godt sei gelobt ein Sontag umb den
> andern, wen man des Hern abentmal helt.

First the pastor shall sing with the sexton and all the people "Come, Holy Ghost, Lord God,"
etc. 2. Thereafter the Kyrie and *Et in terra* in German, as Doctor Martin hath put them into
German. 3. Thereupon the pastor shall read the collects and the epistle. 4. Then shall the
sexton with the people sing the Our Father, also as Doctor Martin hath made it. 5. After this
the pastor shall read to the people the five chief parts of the catechism […]. 6. Thereupon
the sexton shall sing with the people first the creed, thereafter "Now pray we the Holy
Ghost." 7. Then shall the pastor read the gospel from the pulpit and preach the sermon
thereon. 8. After the sermon the sexton shall sing with the people the Sanctus of Isaiah in
German. 9. Thereafter the pastor shall read the exhortation to the communicants, and
straightway thereafter sing the Our Father and the words of the Supper in German. 10. During
the communion the sexton shall sing with the people "Jesus Christ" or "God be praised," one
Sunday after the other, when the Lord's Supper is held.

The same order closes with "Es wolt uns Gott genedig sein" and "Erhalt uns, Herr" on
alternate Sundays (§15.4).

### 3.4 Three shapes of service

The slots fall differently in three kinds of service. The hymns in each kind are much alike.

| | Mass-shaped (Saxony, Bugenhagen's northern orders, Brandenburg, Prussia, Pomerania, Mecklenburg, Hesse) | Preaching service with communion (Württemberg and its derivatives, Kurpfalz 1556, Pfalz-Zweibrücken, Baden, Strasbourg) | Village Mass without a school |
|---|---|---|---|
| Opening | Latin introit, or German psalm in its place; often *Veni sancte* or "Komm heiliger Geist" first | "Komm heiliger Geist", "Nun bitten" or a German psalm "der zeit gemeß" | "Komm heiliger Geist" or a German psalm |
| Kyrie, Gloria | Latin, German, or troped German Kyrie; "Allein Gott" for or with *Et in terra* | none | German Kyrie; "Allein Gott" |
| After the epistle | sequence, alleluia or German psalm; farced sequence at the three high feasts | none | German psalm or hymn "de tempore" |
| Creed | "Wir glauben all" after the gospel, or after the sermon | sometimes after the sermon | "Wir glauben all" |
| Before the sermon | "Nun bitten"; the old *Leisen* at the high feasts | the opening hymn serves | "Nun bitten" |
| After the sermon | a psalm-hymn, "Erhalt uns", or a hymn in the place of the offertory | a German psalm or the creed while the pastor goes to the altar | "Es woll uns Gott" or "Erhalt uns" |
| Communion | German Sanctus, "Jesus Christus unser Heiland", "Gott sei gelobet", Ps 111, O Lamm Gottes | "Gott sei gelobet", "Jesus Christus", German Sanctus | the same |
| Close | "Christe du Lamm Gottes", "Verleih uns Frieden", "Erhalt uns", festal hymn | "Erhalt uns", "Verleih uns Frieden" | "Erhalt uns" |

The Württemberg shape begins with a hymn, then the sermon, then the communion. There is no
introit, Kyrie, Gloria or sequence to replace. In its orders the whole weight of hymn choice
falls on the hymns before and after the sermon and during the distribution. The
*Kirchenordnung* of 1553 (Sehling 16, p. 252):

<!-- doc 671 -->
> So dann das Nachtmal Christi auff ein Sontag oder andern Feyrtag in der kirchen zuhalten
> fürgenommn würdt, soll anfenglich das gsang: Komm heiliger geist, etc., Nun bitten wir den
> heiligen geist, etc. oder sonst ein teutscher Psalm oder geistlich lied, sonderlich der zeit
> gemeß, gesungen werden. Nach disem gsang soll die gemein predig geschehen.

When, then, the Supper of Christ is purposed to be held in the church upon a Sunday or other
holy day, the song "Come, Holy Ghost," etc., "Now pray we the Holy Ghost," etc., or else a
German psalm or spiritual song, especially one agreeable to the season, shall be sung at the
beginning. After this song the common sermon shall be held.

The Bugenhagen orders give the plainest reason for all these German songs. **Hamburg,
*Kirchenordnung*, 1529** (Sehling 5, p. 491), after listing the parts of the Mass:

<!-- doc 1958 -->
> Solck alle geschüt dat meiste to düden umme des volkes willen, de wile Christus gebaden
> hefft. Solck dot to miner gedechtenisse.

All this is done for the most part in German for the people's sake, since Christ hath
commanded: "This do in remembrance of me."

---

## 4. The opening of the service

Before the introit, or instead of it, stood a hymn or chant that asked for the Holy Ghost, or
a German canticle. These opening pieces are the most fixed of all the slots. The choice is
nearly always between the Latin antiphon *Veni sancte Spiritus*, its German form "Komm heiliger
Geist, Herre Gott", and "Nun bitten wir den heiligen Geist". A second group opens with a German
canticle: the Benedictus, the Te Deum, or Psalm 51.

### 4.1 *Veni sancte Spiritus* and "Komm heiliger Geist"

The Hessian *Agende* gives the reason. The whole service is asked of the Holy Ghost at its
beginning, on bended knees. **Hessen, *Agende*, 1574** (Sehling 8, p. 411):

<!-- doc 2272 -->
> Erstlich singen die schuler mit gebogenen knien: Komm heiliger Geist etc., damit die hülfe
> und beistand des heiligen Geistes zu verrichtung des ganzen kirchendienstes gebeten wird.
> 2. Darnach wird gesungen der introitus de trinitate oder de tempore auf Nativitatis,
> Resurrectionis und Pentecostes. 3. Hierauf folget das Kyrie und Et in terra.

First the scholars sing upon bended knees "Come, Holy Ghost," etc., that the help and
assistance of the Holy Ghost may be prayed for, for the performing of the whole service of the
church. 2. Thereafter is sung the introit of the Trinity, or of the season at the Nativity,
the Resurrection and Pentecost. 3. Hereupon followeth the Kyrie and *Et in terra*.

The order of the village of Bruchhausen in the abbey lands of Corvey (1603) copies this
sentence word for word (Sehling 21, p. 244).

At Hof the German forms were sung kneeling by the whole choir whenever the organ was silent.
There were two of them: "Komm, du herzlich Tröster" (the German *Veni sancte Spiritus*
sequence) and Luther's "Komm, heiliger Geist, Herre Gott". **Hof, *Ordo ecclesiasticus*,
1592** (Sehling 11, p. 424):

<!-- doc 294 -->
> Quotiescunque organi pneumatici usus est nullus; totus chorus introitui praemittit: Veni,
> sancte etc. Kom, du herzlich tröster etc. germanice genibus flexis. Hoc absoluto incipit
> introitus. Potest introitui quoque praemitti cantilena d. Lutheri: Kom, Heiliger Geist,
> Herre Gott etc.

As oft as there is no use of the organ, the whole choir setteth before the introit *Veni,
sancte*, etc., "Come, thou heartfelt Comforter," etc., in German, with bended knees. This
being ended, the introit beginneth. Doctor Luther's song, "Come, Holy Ghost, Lord God," etc.,
may also be set before the introit.

Soest, whose order follows Bugenhagen's Braunschweig order, had three boys sing it kneeling at
the altar. **Soest,
*Kirchenordnung*, 1532** (Sehling 22, p. 450):

<!-- doc 1527 -->
> Up etlike tide mach men dree kleyne Jungen, gekneyt vor dem Altar, dat Veni sancte spiritus
> Dütsch edder latyn singen lathen vor der Mysse, darup eyne Dütssche Collecta.

At certain times three little boys may be made to sing, kneeling before the altar, the *Veni
sancte Spiritus* in German or Latin before the Mass, thereupon a German collect.

In the late Verden order the antiphon is the priest's preparation at the altar, with versicle
and collect. **Verden, *Kirchenordnung*, 1606** (Sehling 7/1, p. 155):

<!-- doc 2090 -->
> Erstlich, wann der priester oder pfarrer vor den altar getretten, so soll der chor die
> antiphen Veni, sancte Spiritus anfahen. Darnach soll der priester singen: Emitte Spiritum et
> creabuntur. Der chor soll antworten: Et renovabis faciem terrae.

First, when the priest or pastor is come before the altar, the choir shall begin the antiphon
*Veni, sancte Spiritus*. Thereafter the priest shall sing: *Emitte Spiritum et creabuntur*.
The choir shall answer: *Et renovabis faciem terrae*.

Some orders grade the opening hymn by feast. At Nördlingen the three stanzas of "Komm heiliger
Geist" belonged to the high feasts. On other feasts and on Sundays all the stanzas of "Nun
bitten" were sung, by two choirs, the school and the people, while the celebrant made his
confession. **Nördlingen, *Kirchenordnung* of Kaspar Löner, 1544** (Sehling 12, p. 311):

<!-- doc 372 -->
> Indes sollen zwen chore - einer der schulen, der ander des volks - an hohen festen singen umb
> einander Kum, hailiger Geist, alle drei gesetze aus. An andern festen aber und suntagen Nun
> bitten wir den Heiligen Gaist mit allen seinen gesetzen.

Meanwhile two choirs, one of the school, the other of the people, shall sing by turns on high
feasts "Come, Holy Ghost," all three stanzas through. But on other feasts and on Sundays, "Now
pray we the Holy Ghost," with all its stanzas.

At Reutlingen the same pair of hymns ran from the last bell until the preacher was in the
pulpit. **Reutlingen, *Ordnung der Schule und des Kirchengesangs*, 1565/1566**
(Sehling 17/2, p. 49):

<!-- doc 828 -->
> An dem sontag zur hauptpredig sollen schulmaister und provisor sampt den knaben, nach dem
> das ander zaichen gelitten worden, in die kirchen ghon und daselbst an statt des introitus
> ainen, zwen oder mehr gewonliche psalmen singen und zu letst gleich under oder nach dem
> zusamen leuthen den gesang: Kom, hailiger gaist, oder: Nun pithen wir den hailigen gaist
> etc., biß der prediger auff die cantzel gät.

On the Sunday, at the chief sermon, the schoolmaster and the usher with the boys shall go
into the church after the second bell hath been rung, and there, in the stead of the introit,
sing one, two or more customary psalms, and at the last, either during or after the ringing
together, the song "Come, Holy Ghost," or "Now pray we the Holy Ghost," etc., until the
preacher goeth up into the pulpit.

The prose German form of the antiphon, "Komm, heiliger Geist, erfülle die Herzen", was sung
to the Latin melody. On the Henneberg prayer days it followed the litany and covered the
preacher's going up into the pulpit. **Henneberg, *Kirchenordnung*, 1582** (Sehling 2, p. 311):

<!-- doc 1247 -->
> und wenn dieselbige geendet, als denn darauf das deutsche Kom heiliger geist, erfülle die
> herzen, etc. nach den noten des lateinischen Veni sancte spiritus gesungen werden, unter
> diesem gesang sol der prediger auf den predigstuel sich verfügen.

and when the same is ended, then thereupon the German "Come, Holy Ghost, fill the hearts,"
etc. shall be sung after the notes of the Latin *Veni sancte Spiritus*; during this song the
preacher shall betake himself up into the pulpit.

### 4.2 Singing while the people gather

A reason given again and again for the opening songs is plain: the people were still coming
in. The Dortmund order even defines the introit this way. **Dortmund, *Gottesdienstordnung*,
1554** (Sehling 21, p. 208):

<!-- doc 1446 -->
> Introitus ys unde schal syn ein Psalm edder ein ander Geistlick lavesanck, den men singet,
> dewile dat volck yngheit unde sick ynn de Kercke vorsamelt, dar he ock den namen van hefft.

The introit is, and shall be, a psalm or another spiritual song of praise, which is sung while
the people go in and gather themselves into the church, from which also it hath its name.

**Northeim, *Kirchenordnung*, 1539** (Sehling 6/2, p. 925), defending the Latin chants
against those who would have no ceremonies:

<!-- doc 2047 -->
> warümb solte man einen reinen introitum, Kyrieeleyson, Gloria in excelsis und das Et in
> terra, bis die gemeine zusamenkeme, nicht singen und bleiben lassen? Solchs kan ich zwar fur
> meine person nicht finden.

Why should one not sing, and let remain, a pure introit, Kyrie eleison, *Gloria in excelsis*
and the *Et in terra*, until the congregation were come together? For my own person I can
indeed find no reason for it.

**Hessen, *Kirchenordnung*, 1566** (Sehling 8, p. 248):

<!-- doc 2257 -->
> Erstlich, bis die gemein zusamenkompt, singt man ein psalm oder 2 nach gelegenheit eines
> iglichen orts.

First, until the congregation cometh together, a psalm or two are sung, according to the
occasion of every place.

**Bremen, *Kirchenordnung*, 1561** (Sehling 7/2.2, p. 513), for the weekday sermons:

<!-- doc 2221 -->
> praemittantur etiam singulis concionibus aliquot Germanicae cantilenae, donec populus
> confluat.

Let there also be set before every sermon some German songs, until the people flock together.

**Lippe, *Kirchenordnung*, 1571** (Sehling 21, p. 396). In the villages, where the people
lived far apart, the Kyrie itself served while they gathered. On the high feasts a hymn of the
feast took the place of the introit:

<!-- doc 1462 -->
> nachdem die Leute hin und wider fern von einander zerstrewet wohnen, mit dem Teutschen oder
> Lateinischen Kyrie, bis die Gemein zusammen kömpt, anfahen. Aber auff den Hohen Festagen sol
> für den Introitum ein Geistlich Lied nach gelegenheit des Festes gesungen werden. Demnach
> sol volgen: Allein Gott in der höhe sey Ehre.

Forasmuch as the folk dwell here and there scattered far from one another, [he shall] begin
with the German or Latin Kyrie until the congregation come together. But upon the high feast
days a spiritual song according to the occasion of the feast shall be sung for the introit.
Thereafter shall follow "To God alone on high be glory."

A Henneberg pastor wrote in his report that without communicants a psalm took the place of
the Kyrie and *Et in terra*, "that the people might meanwhile come together".
**Belrieth and Einhausen (Henneberg), *Gottesdienst-Ordnung*, 1566** (Sehling 2, p. 330):

<!-- doc 1248 -->
> So aber keine communicanten furhanden sind, las ich erstlich an stat des kyrie und Et in
> terra ein psalm singen, das sich das volk in des zusamen bringe.

But when no communicants are present, I cause first, in the stead of the Kyrie and *Et in
terra*, a psalm to be sung, that the people may meanwhile gather themselves together.

Bremen had the sexton see that German hymns were sung while the last bell rang. **Bremen,
*Kirchenordnung*, 1534** (Sehling 7/2.2, p. 464):

<!-- doc 2217 -->
> schal als denn de Köster bestüren, dat yn der Kercken gesungen werde ein ledt, Alse: Nu ys
> dat heil uns kamen her, Nu frouwet juw leven Christen gemene, Unde Veni Sancte spiritus
> Düdesch edder Latin, alse me wil dat laste teken lüden.

Then shall the sexton see to it that a song be sung in the church, as "Now is salvation come
to us," "Now rejoice, dear Christians all," and *Veni Sancte Spiritus* in German or Latin,
when the last sign is to be rung.

**Goslar, *Neugestaltung des Gottesdienstes* in the chapter church of SS. Simon and Jude, 1560**
(Sehling 7/2.2, p. 320), at the Sunday vespers:

<!-- doc 2204 -->
> oder sollen die leuthe, so sich in der predigtt samlen, christliche loebgesinge singen, biß
> das der seyer zwey slechtt.

or the people that gather for the sermon shall sing Christian songs of praise until the clock
strike two.

The cost of this practice was noticed. The Mansfeld *Agenda* complained that Luther's hymns
were being forgotten because they were sung only at the start, before the people were there,
while the towns sang Latin and figured music. **Mansfeld, *Kirchen-Agenda*, 1580**, article
XVIII (Sehling 2, p. 234):

<!-- doc 1241 -->
> Wir befinden, das leider d. Luthers, des teuren mans gottes und letzten propheten deutsches
> landes schöne psalmen und anderer fürtrefflicher leute geistreiche deutsche lieder an vielen
> orten also in abfall und vergessen komen, das die jungen hernach wachsende leute wenig von
> denselbigen wissen. Und kömpt solches daher, das dieselben gar wenig und seiden oder etwa im
> anfange des ampts, ehe die leute zusamen komen, in der kirchen gesungen werden, oder auch
> das in den stedten am meisten die lateinischen gesenge und musica figuralis gehalten werden.

We find that, alas, the fair psalms of Doctor Luther, the dear man of God and last prophet of
the German land, and the spiritual German songs of other excellent men, are in many places
so fallen into disuse and forgetting that the young folk growing up after know little of
them. And this cometh thereof, that they are sung in the church very little and seldom, or
perchance at the beginning of the office, before the people come together; or also that in the
towns the Latin songs and figured music are for the most part kept.

### 4.3 The German Benedictus

Bugenhagen's orders often begin the Mass with the German Benedictus ("Gelobet sei der Herr,
der Gott Israel"), sung by the schoolmaster, the children and all the people. It is sung
without the organ, so that the people might learn the words of Scripture. **Wolfenbüttel,
*Kirchenordnung*, 1543** (Sehling 6/1, p. 54):

<!-- doc 1972 -->
> Int erste hefft an de scholemeister und singet dat düdesche Benedictus mit synen kindern und
> mit dem ganzen volke. […] Sülck Benedictus schal men nicht spelen up den orgelen, dat sick
> dat volk gewenne tho den worden der hilgen schrift. Darup singet men einen düdeschen psalm
> edder led uth der hilgen schrift gemaket, als im sankbökeschen doctoris Lutheri is.

First the schoolmaster beginneth, and singeth the German Benedictus with his children and
with all the people. […] Such Benedictus shall not be played upon the organs, that the people
may accustom themselves to the words of Holy Scripture. Thereupon a German psalm is sung, or a
song made out of Holy Scripture, as is in Doctor Luther's little songbook.

**Pomerania, *Kirchenordnung*, 1535** (Sehling 4, pp. 340–341):

<!-- doc 1856 -->
> De scholmeister eder cantor hevet balde an dat düdesch benedictus, den sank Sacharie, mit der
> differentia septimi toni, mit der antiph. alleine in fine, Gelavet si de herr de godt Israel
> […] Dar up singet me einen düdeschen psalm Erbarm di miner etc. eder einen anderen.

The schoolmaster or cantor straightway beginneth the German Benedictus, the song of
Zacharias, with the *differentia* of the seventh tone, with the antiphon only at the end,
"Blessed be the Lord, the God of Israel" […]. Thereupon is sung a German psalm, "Have mercy on
me," etc., or another. (Where there were good schools, a Latin introit might be sung at times.)

In Transylvania the German Benedictus replaced the Sunday procession that had been abolished;
at Easter *Salve festa dies* was kept. **Transylvanian Saxons, *Kirchenordnung*, 1547**, Latin
text (Sehling 24, p. 223):

<!-- doc 1669 -->
> Dominicis diebus pro abrogato circuitu, ante Introitum, canitur Germanicum canticum
> Zachariae: Benedictus Dominus […] tempore Paschali: Salve festa dies.

On the Lord's days, for the procession that is abolished, before the introit is sung the
German canticle of Zacharias, *Benedictus Dominus* […]; in Eastertide, *Salve festa dies*.

The German text of the same order (Sehling 24, p. 244):

<!-- doc 1669 -->
> Am sontag an stat des abgelegten umbgangs singt man den lobgesang Zacharie: Gelobet sey der
> Herr. Zu Ostern: das Salve festa dies.

On the Sunday, in the stead of the procession laid aside, the song of praise of Zacharias is
sung, "Blessed be the Lord." At Easter, the *Salve festa dies*.

The Wittenberg order of 1533 puts the Benedictus before everything, then an introit, Latin
or a German psalm. **Wittenberg, *Kirchenordnung*, 1533** (Sehling 1, p. 704):

<!-- doc 148 -->
> Vor allem in der messen soll man erstlich singen das deutsch benedictus Sacharie mit seiner
> kurzen antiphon, darnach einen introitum, zu zeiten lateinisch, zu zeiten deutsch, welches
> soll sein ein deutscher psalm.

Before all things in the Mass there shall be sung first the German Benedictus of Zacharias
with its short antiphon, thereafter an introit, at times in Latin, at times in German, which
shall be a German psalm.

In the Henneberg village of Sulzfeld the Benedictus was sung "an stat des introitus".
**Sulzfeld (Henneberg), 1566** (Sehling 2, p. 352):

<!-- doc 1250 -->
> an stat des introitus hebt der schulmeister mit den knaben zu singen das benedictus
> Zachariae deutsch und darauf die antiphon: Gelobet sei der herre der gott Israel, wie es die
> noten ausweisen.

In the stead of the introit the schoolmaster with the boys beginneth to sing the Benedictus
of Zacharias in German, and thereupon the antiphon "Blessed be the Lord, the God of Israel,"
as the notes show.

### 4.4 The German Te Deum at the opening

In some later northern orders the German Te Deum ("Herr Gott, dich loben wir") opens the
morning service. It was played on the organ, or sung verse by verse. **Hoya, *Kirchenordnung*,
1581** (Sehling 6/2, p. 1148):

<!-- doc 2065 -->
> und da orgeln sein, sol der organist anfahen zu schlagen Herr Gott, wir loben dich etc. Da
> aber keine orgel ist, sol man es singen. Und wenn das geendet, sol der pastor in seinem
> gewönlichen langen rock für den altar treten, das meßkleid anziehen und den introitum de
> tempore singen. Darauf schlegt der organist das Kyrie, und der chor singet: Christe
> el[eison].

And where there are organs, the organist shall begin to play "Lord God, we praise thee," etc.
But where there is no organ, it shall be sung. And when that is ended, the pastor in his
accustomed long gown shall step before the altar, put on the Mass vestment, and sing the
introit of the season. Thereupon the organist playeth the Kyrie, and the choir singeth
*Christe eleison*.

The East Frisian order of Marienhafe, which follows Hoya, begins with a German Kyrie sung
kneeling, "Ach Vatter", and then the Te Deum. **Marienhafe, *Kirchenordnung*, 1593**
(Sehling 7/1, p. 695):

<!-- doc 2120 -->
> Zur hoichpredigt soll der schulmeister mit den knaben balt umme acht uhr dasein und kniend
> myt den Kyrie, Ach Vatter, ahnfangen etc. […] Darauf soll der organist das Te Deum laudamus
> anheben und das chor sampt der gemeinten dasselbe deutsch versch umb versch nach dem orgel
> andechtich singen etc. […] Darnach noch ein psalm oder geistlich leid, von prediger
> angesagt, spielen und singen.

For the high sermon the schoolmaster with the boys shall be there at eight o'clock, and begin
kneeling with the Kyrie "Ah Father," etc. […] Thereupon the organist shall begin the *Te Deum
laudamus*, and the choir together with the congregation shall sing the same in German
devoutly, verse by verse, after the organ, etc. […] Thereafter yet a psalm or spiritual song,
given out by the preacher, [shall be] played and sung.

The Hildesheim chapter lands opened with a choice of three: the German Te Deum, "Gott der
Vater wohn uns bei" or "Nun freut euch", followed by "Allein Gott". **Hildesheim (Stift),
*Kirchenordnung für Steuerwald und Peine*, 1561** (Sehling 7/2.1, p. 781):

<!-- doc 2129 -->
> erstlich das deutsche Te Deum laudamus oder: Gott der Vater wahn uns bey und lasse uns etc
> oder: Nun freuwet euch lieben Christen gemain singen, darauf: Allein Gott in der höge sey
> ehr.

[He shall] first sing the German *Te Deum laudamus*, or "God the Father be with us, and let
us," etc., or "Now rejoice, dear Christians all"; thereupon "To God alone on high be glory."

Where a village pastor could not sing matins with his sexton, Pomerania had the German Te
Deum sung "pro introitu". **Pomerania, *Agenda*, 1569** (Sehling 4, p. 440):

<!-- doc 1865 -->
> Wo de pastor mit dem cöstere nicht kan metten singen, alse vörhen gesecht is, schal he doch
> pro introitu singen dat düdische te deum laudamus, mit einer collecte.

Where the pastor cannot sing matins with the sexton, as is before said, he shall yet sing
for the introit the German *Te Deum laudamus*, with a collect.

### 4.5 A penitential psalm-hymn for the confession

In Hesse the congregation could sing Psalm 51 in Erhart Hegenwalt's metrical version ("Erbarm
dich mein, o Herre Gott") in place of the spoken confession and absolution. **Hessen,
*Kirchenordnung*, 1566** (Sehling 8, p. 248):

<!-- doc 2257 -->
> Darnach tut man entweder die bekantnis der sünden mit aufnemung der absolution, oder singt
> die ganze kirch den 51. psalm: Erbarm dich mein, o Herre Gott, etc.

Thereafter either the confession of sins is made, with the receiving of the absolution, or
the whole church singeth the fifty-first psalm, "Have mercy on me, O Lord God," etc.

Wittgenstein used "Aus tiefer Not" in the same way. **Wittgenstein, *Kirchenordnung* [1565]**
(Sehling 22, p. 116):

<!-- doc 1493 -->
> unnd nach dem Auß tieffer nott schrey ich zu dir etc. als ein confessionem singen unnd nach
> diesem das 6. capitel Johannis oder das 53. capitel Jesaiae vorlesen und alßdann den glauben
> singen, und folgend auff die cantzel tretten.

and thereafter sing "Out of the depths I cry to thee," etc., as a confession, and after this
read the sixth chapter of John or the fifty-third chapter of Isaiah, and then sing the creed,
and following that step up into the pulpit.

### 4.6 A hymn to cover the priest's prayers at the altar step

In the Bugenhagen city order of Hildesheim the opening German psalm is sung while the priest
kneels at the altar with the sexton and prays the preparatory prayers. **Hildesheim (city),
*Kirchenordnung*, 1544** (Sehling 7/2.1, p. 852):

<!-- doc 2136 -->
> Int erste mach me singen vor dem introitum einen düdeschen psalm edder ledt, ut der
> hilligen schrift gemaket. Under dem gesange geit de prester vor dat altar unde kneet sick
> mit dem oppermanne, bedet vor sick unde vor dat volk unde vor alle nodt der christenheit.

First one may sing before the introit a German psalm or song made out of Holy Scripture.
During the song the priest goeth before the altar and kneeleth with the sexton, and prayeth
for himself and for the people and for all the need of Christendom.

### 4.7 How fixed the opening was

The opening slot was the most stable in the corpus. Where a choice is named it is nearly
always among these few:

- *Veni sancte Spiritus* (Latin antiphon), or its German forms "Komm heiliger Geist, Herre
  Gott" (Luther's hymn) and "Komm, heiliger Geist, erfülle" (prose, sung to the Latin melody).
- "Nun bitten wir den heiligen Geist".
- The German Benedictus.
- The German Te Deum.
- Psalm 51 ("Erbarm dich mein" or "O Herre Gott, begnade mich").

Only the grading by feast varies (§4.1). A few orders instead fill the slot with a seasonal
song "pro ingressu" at vespers (§16.2).

---

## 5. Hymns in place of the introit

The introit is a proper, and this guide does not treat the Latin introits as such. But it is
the proper most often replaced by a hymn. The rule is nearly everywhere the same. A Latin
introit taken from Scripture might be kept where a school could sing it. Otherwise, and in
the villages always, "a German psalm" was sung instead. In the 16th century a "German psalm"
(*ein deutscher Psalm*) is any metrical hymn, above all Luther's psalm-hymns, and not only a
paraphrase of a psalm.

### 5.1 The rule: a Scriptural introit, or a German psalm

**Schleswig-Holstein, *Kirchenordnung*, 1542** (Sehling 23, p. 89):

<!-- doc 1576 -->
> Thom Ersten mach men singen effte lesen den Introitum, de nicht wedder de Gödtlike schrifft
> sy, men de gelick syn den yennen, de up den Sondagen, ock yn den Festen Christi, uth dem
> Psalter genamen, gesungen werden. Up den dörpen mach men einen düdeschen Psalmen vor den
> Introitum singen.

First one may sing or read the introit, such as is not against the divine Scripture, but like
unto those which are sung on the Sundays, and also on the feasts of Christ, taken out of the
Psalter. In the villages one may sing a German psalm for the introit.

**Buxtehude, *Kirchenordnung*, 1552** (Sehling 7/1, p. 74):

<!-- doc 2082 -->
> So der introitus in der misse hilliger schrift enlich, schall he ahn den festen edder
> fyrdagen beholden werden. So averst der introitus in der schrift ungegrundet edder sunst tor
> beteringe undenstlick were, schall ahnstede des introitus ein dudesch psalm gesungen werden,
> alse Kum, hilliger Geist, edder sunst ein ander na bevehl des pastoris. Des werkeldages
> averst schall stedewech vor den introitum ein dudesch psalm gesungen werden.

If the introit in the Mass be like unto Holy Scripture, it shall be kept on the feasts or holy
days. But if the introit be not grounded in Scripture, or otherwise unserviceable to
edification, then in the stead of the introit a German psalm shall be sung, as "Come, Holy
Ghost," or else another at the bidding of the pastor. But on the working day a German psalm
shall always be sung for the introit.

**Prussia, *Artikel der Ceremonien*, 1525** (Sehling 4, p. 32). The German psalms already
sung in place of the introit may stay until the new Latin schools can sing the Latin again:

<!-- doc 1832 -->
> wo aber die introit abgethan sein, und deütsch psalmen dafur gesungen werden, lass man es
> auch dabei bleiben, bis das man der aufgerichten lateinischen schulen halben den
> lateinischen introit oder ganzen lateinischen psalm an die stadt ordnen wirt.

but where the introits are done away and German psalms sung for them, let it also abide so,
until, for the sake of the Latin schools set up, the Latin introit or the whole Latin psalm
shall be ordained in their stead.

**Riga, *Kirchenordnung*, 1530** (Sehling 5, p. 15). The reason for keeping some Latin is
that "the tongues should not be put so wholly out of the church's use":

<!-- doc 1897 -->
> möchte man die sonteglichen introit um ubung willen der jugent (so sie nu in der schulen
> wird zugenommen haben) lateinisch singen, oder an stadt des introitus einen psalmen deudsch
> oder lateinisch, als nemlich diesen, es wolt uns gott gnedig sein etc. oder einen andern denn
> ie die sprachen nicht sollen so ganz aus der kirchen übung gethan werden.

one might sing the Sunday introits in Latin for the exercise of the youth (when it shall now
have increased in the school), or in the stead of the introit a psalm in German or Latin,
namely this, "May God be gracious unto us," etc., or another; for the tongues should not be so
wholly put out of the church's use.

**Tecklenburg, *Kirchenordnung*, 1543** (Sehling 22, p. 243):

<!-- doc 1505 -->
> In stede des introitus sall man singen einen duischen psalm Davids of dergelichen, mit Gades
> worde beweirt, darneist dat Kyrie eleison und Gloria in excelsis duisch.

In the stead of the introit shall be sung a German psalm of David, or the like, proved by God's
word; next thereto the Kyrie eleison and *Gloria in excelsis* in German.

The Calenberg order replaces all four chants of the village Mass with a single psalm.
**Calenberg-Göttingen, *Kirchenordnung*, 1542** (Sehling 6/2, p. 795):

<!-- doc 2036 -->
> Demnach sollen die pfarherrn anstat des introitus, des Et in terra, des haleluja und des
> sequenz als einen psalmen singen.

Accordingly the pastors shall sing, in the stead of the introit, the *Et in terra*, the
alleluia and the sequence, a psalm for each.

The same rule reached the Bohemian villages of Teschen. **Teschen, *Kirchenordnung*, 1584**
(Sehling 3, p. 462):

<!-- doc 1815 -->
> Auf den dörfern aber mag man sonst einen gesang oder psalmen siengen anstadt des introits,
> deutsch oder böhemisch.

But in the villages one may otherwise sing a song or psalm in the stead of the introit, in
German or Bohemian.

In the Albertine order the whole communion service of the villages begins with a hymn "pro
introitu". **Saxony (Albertine), *Kirchenordnung*, 1539** (Sehling 1, p. 272):

<!-- doc 30 -->
> Wenn man communicanten hat, sol man das volk ein feinen psalm oder sonst ein geistlichen
> gesang lassen singen, pro introitu.

When there are communicants, the people shall be made to sing a fine psalm or else a
spiritual song, for the introit.

### 5.2 Which hymns: a short rotating list

Where the orders name the hymns for this slot, they give a short list, and several say
plainly that the list is to be rotated. The favourites are Luther's and his circle's
penitential and psalm-hymns: "Es wolt uns Gott genädig sein" (Ps 67), "Erbarm dich mein, o
Herre Gott" (Ps 51), "Aus tiefer Not" (Ps 130), "Ach Gott vom Himmel sieh darein" (Ps 12),
"Wär Gott nicht mit uns" (Ps 124), "Es spricht der Unweisen Mund" (Ps 14), and "Komm heiliger
Geist, Herre Gott".

**Prussia, *Kirchenordnung*, 1544** (Sehling 4, p. 64):

<!-- doc 1833 -->
> Zum anfang, an stadt des introits, singt man der deüdschen psalmen einen, wie auch bishere
> alhie im fürstenthumb geschehen ist, nemlich: Es wolt uns got gnedig sein. Erbarm dich mein,
> o herre got. Aus tiefer noth. Ach gott vom himel sich darein. Wer got nicht mit uns diese
> zeit. Es spricht der unweisen mund wol etc. und dergleichen psalmen, umb einander
> abzuwechseln. In festen aber als Ostern, Pfingsten, Weinachten singe man die eigene introit
> deütsch oder lateinisch nach gelegenheit des orts, umb ubung willen, der jugend.

At the beginning, in the stead of the introit, one of the German psalms is sung, as hath
been done hitherto here in the duchy, namely: "May God be gracious unto us"; "Have mercy on
me, O Lord God"; "Out of the depths"; "Ah God, from heaven look down"; "Were God not with us
at this time"; "The mouth of the unwise saith indeed," etc., and the like psalms, to be
changed about one after another. But on feasts, as Easter, Pentecost, Christmas, let the proper
introits be sung, in German or Latin according to the occasion of the place, for the exercise
of the youth.

**Naumburg, *Kirchen-Ordnung* for St Wenzel, 1537/1538** (Sehling 2, p. 71) alternates three
hymns Sunday by Sunday, and keeps sung Latin introits in part-music for the feasts:

<!-- doc 1219 -->
> Für den introitum singet man einen sontag umb den andern: Kom heiliger geist etc. Erbarm
> dich mein etc. Aus tiefer noth etc. An den hohen festen aber singt man in mensuris als zu
> Weinachten. Den introitum puer natus oder dies est laetitiae etc. Palmarum. Gloria, laus et
> honor. Ostern. Salve festa dies etc. Pfingsten. Introitum de sancto spiritu. Trinitatis.
> Introitum de trinitate. Annunciationis Mariae. Haec est dies etc.

For the introit is sung, one Sunday after another: "Come, Holy Ghost," etc.; "Have mercy on
me," etc.; "Out of the depths," etc. But on the high feasts one singeth in measured music, as
at Christmas the introit *Puer natus*, or *Dies est laetitiae*, etc.; Palm Sunday, *Gloria,
laus et honor*; Easter, *Salve festa dies*, etc.; Pentecost, the introit of the Holy Ghost;
Trinity, the introit of the Trinity; the Annunciation of Mary, *Haec est dies*, etc.

The St George's order of Nördlingen (1555) copies this rotation, putting it after the Latin
introit and before the confession (Sehling 12, p. 319). The *Auctuarium* of
Brandenburg-Ansbach gives the fullest village list. **Brandenburg-Ansbach, *Auctuarium*,
1548** (Sehling 11, pp. 329–330):

<!-- doc 278 -->
> Wo nit schulen oder leut vorhanden, die lateinisch singen konten, sollen die pfarhern anstad
> des introitus mit dem volk singen: Nun freud euch, lieben Christen gemain etc. Dis sind die
> heiligen zehen gebot etc. Erbarm, dich mein, o Herr Gott etc, […] Ich ruef zu dir, Herr
> Jesu Christ etc.

Where there are no schools, or folk that could sing Latin, the pastors shall sing with the
people in the stead of the introit: "Now rejoice, dear Christians all," etc.; "These are the
holy ten commandments," etc.; "Have mercy on me, O Lord God," etc.; […] "I call to thee, Lord
Jesu Christ," etc.

In the Pomeranian orders of 1542 and 1569 the choice is Latin introit or Psalm 51, in one of
its two German versions. **Pomerania, *Kirchenordnung*, 1542** (Sehling 4, p. 356):

<!-- doc 1859 -->
> heven den introitum an to latin, efft singen einen düdeschen psalm darvor, erbarm di miner,
> in der melodie als idt in den druckeden sankbokern steit, efft den psalm, o here godt
> begnade mi etc.

[they] begin the introit in Latin, or sing a German psalm for it, "Have mercy on me," in the
melody as it standeth in the printed songbooks, or the psalm "O Lord God, be gracious unto
me," etc.

**Pomerania, *Agenda*, 1569** (Sehling 4, p. 437):

<!-- doc 1865 -->
> Tom anfange singet dat chor den introitum de festo vel tempore, edder up de dominica, edder:
> Kum hilige geist, herre godt. Erbarme di miner. O herre godt begnade mi etc. edder einen
> andern düdeschen psalm.

At the beginning the choir singeth the introit of the feast or of the season, or of the
Sunday; or "Come, Holy Ghost, Lord God"; "Have mercy on me"; "O Lord God, be gracious unto
me," etc.; or another German psalm.

### 5.3 Early German Masses: a hymn as the introit itself

In some of the earliest German Masses a hymn stands where the introit stood, under the
heading *Introitus*. The Nürnberg hospital Mass of Andreas Döber prints "Nun bitten wir"
with the heading "Introitus oder eingang der meß". **Nürnberg, Döber's German Mass in the New
Hospital, 1525** (Sehling 11, p. 56):

<!-- doc 250 -->
> Introitus oder eingang der meß. [Noten] Nun bitten wir den Heiligen Geist [4 Verse. Hier
> nicht abgedruckt; dann Schluß der Noten].

Introit, or entrance of the Mass. [Notes] "Now pray we the Holy Ghost" [four verses].

Strasbourg's Mass of 1525 had Psalm 51 or Psalm 130 "an stat des Introits". **Strasbourg,
*Ordnung des Herren Nachtmal*, 1525** (Sehling 20/1, p. 156):

<!-- doc 1279 -->
> Auff das fahet an die kirch zu singen ein psalmen als das Miserere oder ein anderen psalmen
> an stat des Introits und etwan das Kyrieleyson und Gloria in excelsis. Der CXXX. Psalm: De
> profundis, an stat des Introits etwan in der Meß: Uß tieffer not schrey ich zu dir.

Thereupon the church beginneth to sing a psalm, as the Miserere or another psalm, in the stead
of the introit, and sometimes the Kyrie eleison and *Gloria in excelsis*. The hundred and
thirtieth psalm, *De profundis*, sometimes in the stead of the introit in the Mass: "Out of
the depths I cry to thee."

A Low German Mass from Lippe gives "Uth deper nodt" as the introit, with the choice of any
other psalm. **Lippe, *Deutsche Messe* [c. 1525–1538]** (Sehling 22, p. 565):

<!-- doc 1549 -->
> Dewyle averst de prester den confiteor lest, synget dat choer den introitum der misse.
> Introitus misse Uth deper nodt schrye ik tho dy etc. Offte eynen anderen psalmen, wat me vor
> eynen wyl. Item, nu thor tydt synget dat choer offte volck ghemeylick vor dem introitu de
> antiffen Veni sancte spiritus, Kum, hillige geist.

But while the priest readeth the *Confiteor*, the choir singeth the introit of the Mass.
Introit of the Mass: "Out of the depths I cry to thee," etc., or another psalm, whichever one
will. Item, now at this time the choir or people commonly sing before the introit the antiphon
*Veni sancte Spiritus*, "Come, Holy Ghost."

### 5.4 A hymn of the feast for the introit

On feasts, some orders let a hymn of the feast replace the Latin festal introit. Mecklenburg
sang Luther's Christmas *Leise* "Ein Kindelein so löbelich" (the four stanzas of "Der Tag, der
ist so freudenreich") at Candlemas and on the Sundays between Christmas and Candlemas.
**Mecklenburg, *Ordeninge der misse*, 1545** (Sehling 5, p. 151):

<!-- doc 1922 -->
> In die Purificationis singe me vor enen introitum de veer schonen versche. Ein kindelin
> etc. Welck ock de sondage twischen winachten und lechtmissen up den dörpern schal vor enen
> introitum gesungen werden. Up welckere sondage in den steden, under tiden dat Offitium, Puer
> natus, mach gesungen werden.

On the day of the Purification let the four fair verses, "A little Child," etc., be sung for
an introit. The same shall also be sung for an introit in the villages on the Sundays between
Christmas and Candlemas; on which Sundays in the towns the office *Puer natus* may be sung
at times.

Wittgenstein kept the Latin introits of the high feasts but allowed three hymns in their
place: "Der Tag, der ist so freudenreich" for *Puer natus*, "Christ lag in Todesbanden" for
*Resurrexi*, and "Es ist das Heil" for *Spiritus Domini*. **Wittgenstein, *Kirchenordnung*,
1563** (Sehling 22, p. 102):

<!-- doc 1493 -->
> nach dem Veni sancte den gewönlichen introitum singen, als da sind: Puer natus est nobis
> etc., Resurrexi et adhuc tecum sum etc., Spiritus Domini replevit orbem terrarum etc.,
> welche man auch auff den dörffern deutsch lernen und singen kan oder an stadt derselbigen
> brauchen: Der tag, der ist so freudenreich etc., Christ lag in todes banden etc., Es ist das
> heyl uns kommen her etc.

[they shall] after the *Veni sancte* sing the customary introit, as these are: *Puer natus est
nobis*, etc., *Resurrexi et adhuc tecum sum*, etc., *Spiritus Domini replevit orbem
terrarum*, etc.; which may also be learned and sung in German in the villages, or, in the
stead of the same, may be used: "The day that is so full of joy," etc., "Christ lay in the
bands of death," etc., "Salvation now is come to us," etc.

In the Henneberg village of Sulzfeld the chorus sang the Christmas song "Ein Kind geboren zu
Bethlehem" (*Puer natus in Bethlehem*) instead of the introit, and "Also heilig ist der Tag"
three times at Easter and Ascension. **Sulzfeld and Klein-Bardorf, *Kirchen-Ordnung*, 1566**
(Sehling 2, p. 353):

<!-- doc 1250 -->
> zu weinachten an stat des introitus singt der chor: Ein kind geboren zu Bethlehem, auf
> ostern und himmelfart aber: Also heilig ist der tag etc. dreimal und an stat des psalmen
> zwischen den capiteln werden die gewönlich lieder von festen gesungen.

At Christmas, in the stead of the introit, the choir singeth "A Child is born in Bethlehem";
but at Easter and the Ascension, "So holy is the day," etc., three times; and in the stead of
the psalm between the chapters the customary songs of the feasts are sung.

The Hamburg order of 1529 lists the Latin introits for the feasts it keeps. For other feasts,
where there is no chant from Scripture, it allows "joyful psalms and songs". **Hamburg,
*Kirchenordnung*, 1529** (Sehling 5, p. 528):

<!-- doc 1960 -->
> Int erste singet me einen dudeschen psalm, edder up etlike feste latinisch. Van winachten
> bet up purificationis puer natus. Twischen paschen und der hemmelfart salus populi ego sum.
> Darna bet up pinxten viri galilei. Van pinxten spiritus domini. Van sunte Johanse ne timeas
> Sacharia […] Van sunte Michael Benedicite domino. Up feste, dar men sundergen sank ut der
> schrift nicht van hefft, kan me wol frolike psalme und lede singen.

First is sung a German psalm, or on certain feasts [an introit] in Latin: from Christmas unto
the Purification, *Puer natus*; between Easter and the Ascension, *Salus populi ego sum*;
thereafter unto Pentecost, *Viri Galilaei*; from Pentecost, *Spiritus Domini*; of St John, *Ne
timeas, Zacharia* […]; of St Michael, *Benedicite Domino*. On feasts whereof one hath no proper
chant out of Scripture, one may well sing joyful psalms and songs.

### 5.5 A German prose antiphon as introit

Ritzebüttel, in Hamburg's territory, sang the prose German "Komm, heiliger Geist, erfülle"
with its Alleluia "in stede des introitus". **Ritzebüttel, *Kirchenordnung*, 1556**
(Sehling 5, p. 557):

<!-- doc 1963 -->
> Des sondages anfenglick hevet men an, in stede des introitus to singen den dudeschen
> gesanck: Kum hilliger geist, erfülle die herten diener gelovigen, und entfenge in en dat fuer
> diner godtlicken leer […] Alleluia.

On the Sunday one beginneth first to sing, in the stead of the introit, the German song "Come,
Holy Ghost, fill the hearts of thy faithful, and kindle in them the fire of thy divine love"
[…] Alleluia.

### 5.6 Why a short list: that the people might learn them

The Halle order explains the aim of the rotation. The German psalms sung "pro introitu" were
to be chosen so that the whole church might become sure of some good psalms, and in time of
the whole Psalter, as at Jena. **Halle, *Kirchen-Ordnung der christlichen Gemein*, 1543** (Sehling 2, p. 436):

<!-- doc 1257 -->
> Wan man Aus tiefer noth, oder andere deutsche psalmen pro introitu singet, sollen dieselbigen
> dahin gericht werden, das die ganze kirche etlicher gueter trostlicher nüzlicher psalmen
> gewiss gewone, und man kente mit der zeit anrichten, das aller psalmen im ganzen psalter das
> volk durch solche fleissige übung, wan man der psalmen nacheinander brauchet, gewenete, wie
> in etlichen kirchen, als zu Jena und andern orten nüzlich angericht.

When "Out of the depths" or other German psalms are sung for the introit, the same shall be
so ordered that the whole church may become surely accustomed to some good, comfortable,
profitable psalms; and in time it might be brought about that the people, by such diligent
exercise, using the psalms one after another, should grow accustomed to all the psalms in the
whole Psalter, as hath been profitably set up in some churches, as at Jena and other places.

Nördlingen dropped the introit altogether when the psalm after the epistle was a long one,
and in winter "for the cold and for beloved brevity's sake". **Nördlingen, *Kirchenordnung*,
1579** (Sehling 12, p. 375):

<!-- doc 375 -->
> Wo aber ein langer psalm fürfelle als Vater unser, Nun freuet euch, lieben christen gemein,
> Es ist das heil uns kommen her, Durch Adams fall, Wo Gott der Herr nicht bei uns helt und
> dergleichen, so würd der introitus zu singen ausgelassen und schlegt allein der organist.
> Sonderlich aber zue winterszeiten solle der introitus umb der kelte und geliebter kurze
> wülen ausgelassen werden.

But where a long psalm falleth, as "Our Father," "Now rejoice, dear Christians all,"
"Salvation now is come to us," "Through Adam's fall," "Where God the Lord standeth not by
us," and the like, then the singing of the introit is left out, and the organist alone
playeth. But especially in the winter season the introit shall be left out, for the cold's
sake and for beloved brevity's sake.

### 5.7 How fixed the slot was

Where a German hymn replaced the introit, the choice was among **a handful**, usually
rotated. The core was "Komm heiliger Geist", Psalm 51, Psalm 130 and Psalm 67, with a few other
psalm-hymns. At the high feasts the Latin introit returned, or a hymn of the feast took its
place. No order found assigns a different introit-hymn to each Sunday of the year, as the
Latin propers had done.

---

## 6. The Kyrie: plain, in three tongues, troped and German

The Kyrie is an ordinary, not a proper, so it was not replaced by a hymn in the way the
introit was. But it was sung in German, it was troped in German, and it was graded by season,
like the medieval Kyrie melodies. Most orders cut it back to three petitions, one to each
Person of the Trinity. The Kyrie melodies of the chant books (*summum*, *paschale*,
*dominicale*, *angelicum*, *apostolicum*, *in adventu*, *de beata Virgine*) survived as seasonal
grades in the Lutheran cantionals of Spangenberg and Lossius. The grades themselves are
treated in `FEAST_RANKING_GUIDE.md` §3.2. This section deals with the texts sung to them.

### 6.1 Three times, not nine

Luther's *Deutsche Messe* already prescribed the Kyrie "drei mal und nicht neun mal"
(Sehling 1, p. 14). The Wolfenbüttel order gives the reason: once for each Person of the
Trinity. **Wolfenbüttel, *Kirchenordnung*, 1543** (Sehling 6/1, p. 54):

<!-- doc 1972 -->
> Id is nicht van nöden, negen mal dat eleison edder Kyrie tho repetirende, yd is genoch
> dremal im namen des Vaders und des Sons und des hilgen Geistes tho singende ane orgelen.

It is not needful to repeat the *eleison* or Kyrie nine times; it is enough to sing it three
times, in the name of the Father and of the Son and of the Holy Ghost, without organs.

Wittenberg kept a nine-fold Kyrie for the feasts. After the plain three-fold Kyrie there was
no Gloria. **Wittenberg, *Kirchenordnung*, 1533** (Sehling 1, p. 704):

<!-- doc 148 -->
> Darnach das rechte kyrie dreimal, oder zu zeiten, besondern uf die feste, ein anders
> neunmal, wie gewonlich. Auf das schlechte kyrie singet man nicht gloria in excelsis deo,
> sondern auf andere, wenn man will, und sonderlich uf die feste.

Thereafter the right Kyrie three times; or at times, especially on the feasts, another nine
times, as is customary. After the plain Kyrie one singeth not *Gloria in excelsis Deo*, but
after the others, when one will, and especially on the feasts.

### 6.2 In three tongues

Two Baltic orders have the three petitions sung in three languages: Greek, Latin and German.
**Prussia, *Artikel der Ceremonien*, 1525** (Sehling 4, p. 32):

<!-- doc 1832 -->
> Von dem kyrieleyson ist fur gut angesehen, dieweil es dreimal gesungen wirt, das es in
> dreien zungen, wie man auch alhier pfleget, krichisch, lateinisch und deütsch gefangen
> werde.

Of the Kyrie eleison it is thought good, since it is sung three times, that it be sung in
three tongues, as is also the custom here: Greek, Latin and German.

**Riga, *Kirchenordnung*, 1530** (Sehling 5, p. 15):

<!-- doc 1897 -->
> Auf den introit, singt man das kyrie eleison, mit wenig noten (ausgenommen auf die hohen
> fest, da man notam paschalem nemen mag) und were nicht unformlich, das es in dreien zungen,
> kriechisch, lateinisch und deudsch, wie man auch an etlichen orten pfleget, gesungen würde,
> die weil es doch dreimal gesungen wird.

After the introit the Kyrie eleison is sung with few notes (save on the high feasts, when the
Easter note may be taken). And it were not unseemly that it be sung in three tongues, Greek,
Latin and German, as is the custom in some places, since it is sung three times.

### 6.3 Bugenhagen's defence of the Greek Kyrie

Bugenhagen defended keeping the Greek words, even in German. The people already sang
*Kyrieleis* at the end of their best-loved hymns. **Braunschweig, *Kirchenordnung*, 1528**
(Sehling 6/1, p. 438):

<!-- doc 1983 -->
> Eynen düdeschen text uth latinischer edder anderer hilger scrift to maken mit schicklikeme
> sange, is nicht eynes jederen mannes, unlustich singen anrichten is neyne kunst. Worumme
> scholde me dat Kyrie elsen in der misse nicht singen? Singet me id doch in anderen leden,
> alse synt: Got sy gelavet, Midden in deme levend, Dit synt de hilgen teyn gebot, Mynsche
> wiltu leven salichlick, Christ is upgestanden, Nu bidde wy den hilgen Geyst, Gelavet sistu
> Jesu Christ etc.

To make a German text out of Latin or other holy Scripture, with a seemly tune, is not every
man's work; to set up an unlovely singing is no art. Why should one not sing the Kyrie eleison
in the Mass? For it is sung in other songs, as are: "God be praised," "In the midst of life,"
"These are the holy ten commandments," "Man, wilt thou live blessedly," "Christ is arisen,"
"Now pray we the Holy Ghost," "Praised be thou, Jesu Christ," etc.

### 6.4 Troped German Kyries

Several orders print German Kyries that expand each petition, as the medieval tropes did. They
were sung to the melodies of the Latin troped Kyries of the same names.

The oldest is in a Low German manuscript Mass from Schleswig-Holstein, written after 1526. Its
first Kyrie is troped; the *Kyrie dominicale* follows plain. **Schleswig-Holstein, *Deutsche
Messe* [after 1526]** (Sehling 23, p. 56):

<!-- doc 1576 -->
> Here, o Godt vader yn ewicheit, de du levest unde aver alle regerst, vorbarme dy unser.
> Criste, de du heffst upgeloßet den bant des dodes, vorbarme dy unßer. Here, o hilge geist,
> de du van vader unde sone utgeist unde gelyck Godt gepryset werst, vorbarme dy unser. […]
> Kyrie Dominicale Here, Got vader, vorbarme dy unser. Criste, vorbar me dy unser. Here,
> hylige geist, vorbarme dy unser.

Lord, O God the Father in eternity, who livest and reignest over all, have mercy upon us.
Christ, who hast loosed the band of death, have mercy upon us. Lord, O Holy Ghost, who
proceedest from the Father and the Son and art praised as God alike, have mercy upon us.
[…] *Kyrie dominicale*: Lord God the Father, have mercy upon us. Christ, have mercy upon us.
Lord, Holy Ghost, have mercy upon us.

The Naumburg order prints three German Kyries for the high Mass on feast days: the *summum*
("Kyrie, Gott Vater in Ewigkeit"), the *paschale* ("O Herre Gott, Vater in Ewigkeit") and
the *magne Deus* ("O Vater, allmächtiger Gott"). **Naumburg, *Kirchen-Ordnung* for St Wenzel,
1537/1538** (Sehling 2, p. 78):

<!-- doc 1219 -->
> Hierauf singt der ganze chor das kyrie eleison wie volget. Kyrie sumum. Kyrie got vater in
> ewigkeit, gross ist dein barmherzigkeit, aller ding ein schopfer und regirer eleison.
> Christe aller welt trost und sunder allein due hast erlost, o Jesu gottes sohn unser mitler
> bist in dem hochstem thron, zu dir schreien wir aus herzen begier eleison, kyrie got
> heiliger geist trost sterk uns im glauben alle zeit, das wir am letzten end frolich uns
> scheiden aus diesem elend, eleison. Kyrie paschale. O herre gott, vater in ewigkeit bis uns
> sundern gnedig, Christe der werlet heilant und ihr trost mach uns allen von sunden los. O
> gott heiliger geist, theil uns mit weisheit lieb und glauben allermeist, bring gotlich
> gerechtigkeit. Kyrie magne deus. O vater almechtiger gott zu dir schreien wir in der noth,
> durch dein gross barmherzigkeit erbarme dich uber uns. Christe wolst uns horen, fur uns
> bistue geboren von Maria, erbarm dich uber uns. Herr vorgib uns unser sunde, hilf uns in der
> letzten stunde, der due für uns bist gestorben, erbarme dich uber uns.

Hereupon the whole choir singeth the Kyrie eleison as followeth. *Kyrie summum*: "Kyrie, God
the Father in eternity, great is thy mercy, Creator and Ruler of all things, *eleison*.
Christ, comfort of all the world, thou alone hast redeemed sinners; O Jesu, Son of God, our
mediator thou art in the highest throne; to thee we cry with the desire of our heart,
*eleison*. Kyrie, God the Holy Ghost, comfort, strengthen us in faith at all times, that at
the last end we may depart joyfully out of this misery, *eleison*." *Kyrie paschale*: "O Lord
God, Father in eternity, be gracious unto us sinners. Christ, Saviour of the world and its
comfort, make us all free from sins. O God the Holy Ghost, impart unto us wisdom, love, and
faith most of all; bring divine righteousness." *Kyrie magne Deus*: "O Father, almighty God,
to thee we cry in our need; by thy great mercy have mercy upon us. Christ, be pleased to hear
us, who for us wast born of Mary; have mercy upon us. Lord, forgive us our sins, help us in
the last hour, thou who for us hast died; have mercy upon us."

The St George's order of Nördlingen (1555) takes over these three German Kyries by season:
the *paschale* from Easter to Pentecost, the *Fons bonitatis* from Pentecost to Christmas, and
the *Magne Deus* from Christmas to Easter (Sehling 12, p. 318).

The *summum* text, "Kyrie, Gott Vater in Ewigkeit", became the common German festal Kyrie. A
Henneberg pastor calls it "das schöne christliche gesang". **Obermassfeld (Henneberg),
*Kirchen-Ordnung*, 1566** (Sehling 2, p. 343):

<!-- doc 1249 -->
> singt der schulmeister mit den knaben und der kirchen, wan communicanten vorhanden sind,
> erstlich das schöne christliche gesang: Kyrie got vater in ewigkeit, gros ist deine
> barmherzigkeit etc. Folgend darauf das Gloria in excelsis deo wie dasselbige auch
> gesangsweis deutsch gestellet: Allein got in der höhe sei ehr und dank für seine gnade etc.
> Wo aber nicht communicanten vorhanden singen wir: Kom heiliger geist, herre got.

When communicants are present, the schoolmaster with the boys and the church singeth first
the fair Christian song "Kyrie, God the Father in eternity, great is thy mercy," etc.
Following thereupon, the *Gloria in excelsis Deo*, as the same is also set in German as a
song: "To God alone on high be glory and thanks for his grace," etc. But where no
communicants are present we sing "Come, Holy Ghost, Lord God."

Hof names the German Kyries by the Latin melodies they were sung to. At Christmas
(Sehling 11, p. 433):

<!-- doc 294 -->
> Kyrie magnae Deus potentiae: O Vater allmechtiger Gott.

*Kyrie magnae Deus potentiae*: "O Father, almighty God."

At Pentecost (Sehling 11, p. 441):

<!-- doc 294 -->
> Kyrie fons bonitatis: [Noten] Kyrie, Gott Vater in ewigkeit [Ende der Noten]. Loco Et in
> terra: All ehr und lob soll Gottes sein.

*Kyrie fons bonitatis*: [notes] "Kyrie, God the Father in eternity" [end of notes]. In the
place of *Et in terra*: "All honour and praise shall be God's."

The Mecklenburg order of 1545 has the German *Kyrie summum* "Ach Vater, allerhöchster Gott"
sung in the villages, where the sexton was to teach it to the people. **Mecklenburg,
*Ordeninge der misse*, 1545** (Sehling 5, p. 151):

<!-- doc 1922 -->
> Das düdesche kyrie summum: Ach vader, alder högeste godt, schölen de kerckheren up den
> dörpern singen, unde dem volke idt leren, dat de ganze kercke idt singe. De koster kan groth
> gut darinne don, wenn he sick nicht ut dem wege stickt, ock nicht (wo etlike don) up dat
> altar liggen gaen, sonder im chör sick to tiden na der kercken wende, und dem volke wol
> vorsinge. Dat kyrie paschale, kyrie angelicum, dominicale, de anderen to tiden ock mach men
> in den steden singen.

The German *Kyrie summum*, "Ah Father, God most high," the parsons shall sing in the villages,
and teach it to the people, that the whole church may sing it. The sexton can do great good
herein, if he keep not out of the way, nor (as some do) go and lie upon the altar, but turn
himself at times in the choir toward the church and sing it well before the people. The
*Kyrie paschale*, *Kyrie angelicum*, *dominicale* and the others may also at times be sung in
the towns.

"Ach Vater" was still the opening Kyrie at Marienhafe in 1593, sung kneeling (§4.4). The
Ritzebüttel order gives three German Kyries, one plain and two troped, "each with its own
melody". **Ritzebüttel, *Kirchenordnung*, 1556** (Sehling 5, p. 557):

<!-- doc 1963 -->
> Darna wert gesungen dat kyrieleison mit noten in dudescher sprake also: Herr godt vader,
> erbarme di unser. Christe, godt sohn, erbarme di unser. Herr godt, heiliger geist, erbarme
> di unser. Ein andrer kyrieleison. Also: Herr godt vader, alder hogste godt, wie klein achtet
> man din gebot. Verschone unser blindheit, die vele sunde deit. Erbarme di unser Christe, der
> du bist die weg und dat ware licht. Die porte der warheit, und dat levent, des vaters radt
> und wort, den he uns hefft tom troste gegeven, erbarm die unser. Herr, hillige geist in
> ewicheit, stah uns bi dorch dine barmhertigkeit; unse sunde sind uns leid, wil nicht
> vorlaten di in di hapen, erbarm di unser. Ein ander kyrie. Also: Kyrie, milde vader, wie
> bidden di alle, vader, erbarme di unser. Christe, unse konink und herr, erbarm di unser.
> Kyrie, heiliger geist, die du ein troster der bloden bist, erbarme di unser. Ein ieder mit
> siner melodie.

Thereafter the Kyrie eleison is sung with notes in the German tongue thus: "Lord God the
Father, have mercy upon us. Christ, God the Son, have mercy upon us. Lord God, Holy Ghost,
have mercy upon us." Another Kyrie eleison, thus: "Lord God the Father, God most high, how
little is thy commandment regarded! Spare our blindness, which doeth many sins; have mercy
upon us. Christ, who art the way and the true light, the gate of truth and the life, the
Father's counsel and word, whom he hath given us for our comfort, have mercy upon us. Lord,
Holy Ghost in eternity, stand by us through thy mercy; our sins are grievous unto us; we will
not forsake thee, in thee we hope; have mercy upon us." Another Kyrie, thus: "Kyrie, gentle
Father, we all pray thee, Father, have mercy upon us. Christ, our King and Lord, have mercy
upon us. Kyrie, Holy Ghost, who art the comforter of the fainthearted, have mercy upon us."
Each with its own melody.

The Ritzebüttel order also speaks of a *missa dominicalis*, *paschalis*, *pentecostes* and
*nativitatis*: seasonal sets of Kyrie and Gloria. The songbook appended to the Pfalz-Zweibrücken
*Kirchenordnung* of 1557 prints three German Kyries, each paired with a German Gloria.
**Pfalz-Zweibrücken, *Kirchenordnung*, 1557**, songbook (Sehling 18, p. 248):

<!-- doc 968 -->
> Folget das Kyrieleison mit dem Gloria in Excelsis: Kyrie Eleyson, Herr erbarme dich. Gloria
> in Excelsis: Glori sey Gott in der höhe Und auff erden Frid. Ein ander Kyrie und Et in
> terra: Herr, erbarm dich unser. Ehre sei Gott in der höhe. Kyrie Paschale: Kyrie, Gott aller
> welt sehöpffer und Vatter, Eleyson. Gloria in Exelsis Deo: All ehr und lob sol Gottes sein.

Here followeth the Kyrie eleison with the *Gloria in excelsis*: "Kyrie eleison, Lord have
mercy." *Gloria in excelsis*: "Glory be to God on high, and on earth peace." Another Kyrie and
*Et in terra*: "Lord, have mercy upon us." "Glory be to God on high." *Kyrie paschale*:
"Kyrie, God, Creator of all the world, and Father, *eleison*." *Gloria in excelsis Deo*: "All
honour and praise shall be God's."

The Henneberg village orders also name the German *Kyrie summum*, sung after the German
Benedictus "or [the Kyrie] of the present feast". **Herpf (Henneberg), 1566** (Sehling 2, p. 334):

<!-- doc 1248 -->
> So man communicanten hat, singt man das benedictus deutsch, darauf auch das deutsch kyrie
> eleison summum oder vom gegenwertigen fest.

When there are communicants, the Benedictus is sung in German, thereupon also the German
*Kyrie eleison summum*, or that of the present feast.

At Wasungen the school, when there were no communicants, sang a long psalm-hymn with
"three short Kyries in German" added at the end. **Wasungen (Henneberg), pastor's report, 1566** (Sehling 2, p. 356):

<!-- doc 1250 -->
> Anfenglich singet die schul die deutsche letanei oder sonsten einen zimlichen langen psalmen
> als das vater unser oder: Durch Adams fall oder mit den drei kurzen kyrie daran gehenget
> deutsch: O herre gott vater allen barmherzigkeit bist uns sündern gnedig etc.

At the beginning the school singeth the German litany, or else a fairly long psalm, as the
Our Father or "Through Adam's fall," or, with the three short Kyries hung thereto in German,
"O Lord God, Father of all mercy, be gracious unto us sinners," etc.

### 6.5 The Kyrie and Gloria in one hymn: "Allein Gott"

In East Frisia the German Kyrie and Gloria together were sung "as it is sung in the song
*Allein Gott in der Höh sei Ehr*". **Ostfriesland, *Kirchenordnung*, 1535** (Sehling 7/1, p. 376):

<!-- doc 2107 -->
> Tom ersten schal gesungen werden eyn edder twee duedsche psalmen. Darna synge man dat
> Kyrieleyson sampt den Gloria in excelsis to duedsche, alze dat gesungen wort in dem gesenge
> Alleyn Godt in der hoge sy eer.

First shall be sung one or two German psalms. Thereafter let the Kyrie eleison together with
the *Gloria in excelsis* be sung in German, as it is sung in the song "To God alone on high be
glory."

### 6.6 How fixed the Kyrie was

The Kyrie was **fixed by grade**. Its text hardly changed. Its melody changed with the season
and the rank of the day, where a school could sing the grades. In the villages there was one
German Kyrie, or three at most, rotated by season. No order found fits the Kyrie to the gospel
of the day. It is the most calendar-bound and least topical of the sung ordinaries.

---

## 7. The Gloria: "Allein Gott in der Höh" and "All Ehr und Lob"

Two German Gloria hymns run through the orders:

- Nikolaus Decius's "Allein Gott in der Höh sei Ehr", which reached the north first in Low
  German ("Allene Gade in der hoge sy ere").
- Luther's rhymed *Et in terra*, "All Ehr und Lob soll Gottes sein".

The priest's Latin or German intonation ("Gloria in excelsis Deo", "Ehre sei Gott in der Höhe")
usually stayed. The hymn was sung for, or together with, the choir's *Et in terra*.

### 7.1 The German hymn inside the Latin Gloria

The Bugenhagen orders of Wolfenbüttel (1543) and Hildesheim (1544) interpolate the whole of
"Allein Gott" into the Latin Gloria. The priest intones. The school choir sings the first line
of the Latin. The whole church sings "Allein Gott" through. Then the scholars and the organ go
on with *Laudamus te* to the end. **Wolfenbüttel, *Kirchenordnung*, 1543** (Sehling 6/1, p. 55):

<!-- doc 1972 -->
> Na dem Kyrie singet de prester: Gloria in excelsis Deo. Dat scholerchor antwerdet und
> singet: Et in terra pax, hominibus bona voluntas, nicht mehr. Balde singet de ganze kercke:
> Alleine Got in der höged sy ehr etc. vul uth. Darna singen de scholer und orgeln vordan:
> Laudamus te, benedicimus te etc. vul uth.

After the Kyrie the priest singeth: *Gloria in excelsis Deo*. The scholars' choir answereth
and singeth: *Et in terra pax, hominibus bona voluntas*, no more. Straightway the whole church
singeth "To God alone on high be glory," etc., fully through. Thereafter the scholars and the
organs sing on: *Laudamus te, benedicimus te*, etc., fully through.

The Hildesheim city order of 1544 has the same rubric almost word for word (Sehling 7/2.1, p. 852). The Osnabrück city order puts "Allein Gott" straight after the intonation, and then
the Latin Gloria "to the end". **Osnabrück (city), *Kirchenordnung*, 1543** (Sehling 7/1, p. 258):

<!-- doc 2099 -->
> Gloria in excelsis, darup gesungen Allene Gott in der höhe sy ehr, darna dat latineschen
> Gloria in excelsis, verfolget bet tom ende.

*Gloria in excelsis*; thereupon is sung "To God alone on high be glory"; thereafter the Latin
*Gloria in excelsis*, followed through to the end.

### 7.2 Latin one Sunday, German the next

Where a school sang the Latin, many orders alternated it with the German hymn so that the
people would not lose their part. The Prussian order says so outright. **Prussia,
*Kirchenordnung und Ceremonien*, 1568** (Sehling 4, p. 81):

<!-- doc 1833 -->
> Darauf singet der priester mit gebürlicher reverenz: Gloria in excelsis deo, der chor einen
> sonntag um den andern: Et in terra pax, oder: Allein gott in der höhe sei ehre, denn man muss
> die deutschen psalmen auch in ubung behalten und dem gemeinen haufen auch raum geben, das
> sie ihre andacht mit solchen geistlichen liedern uben.

Thereupon the priest singeth with due reverence *Gloria in excelsis Deo*; the choir, one
Sunday after the other, *Et in terra pax*, or "To God alone on high be glory." For the German
psalms must also be kept in use, and room be given to the common multitude also, that they
may exercise their devotion with such spiritual songs.

**Lüneburg, *Reformatio coenobiorum*, 1555**, for the convents (Sehling 6/1, p. 614):

<!-- doc 2009 -->
> In der messe soll gesungen werden introitus, Kyrieleison, Gloria in excelsis et in terra
> pax oder Allein Gott in der hohe einen Sontag umb den anderen.

In the Mass shall be sung the introit, Kyrie eleison, *Gloria in excelsis et in terra pax*, or
"To God alone on high," one Sunday after the other.

At Harzgerode in Anhalt the Latin *Gloria* and *Et in terra dominicale* alternated with the
German on ordinary Sundays. At Christmas the old verses *Dies est laetitiae* were sung into it
in Latin and German. **Harzgerode, *Kirchenordnunge*, 1534 (?)** (Sehling 2, p. 586):

<!-- doc 1263 -->
> Volgende das Kyrie eleison auf die grosse feste mit dem Gloria in excelsis und Et in terra
> auf der orgel und chor, und zu weinachten mag man nach alten gebrauchen die vers dies est
> laeticie cum sequentibus latine und deutsch mit dreinsingen. Aber an die gemein sontag sol
> man umb einander einen sontag das latinsche gloria und Et in terra dominicale, den a[ndern]
> […].

Following, the Kyrie eleison on the great feasts, with the *Gloria in excelsis* and *Et in
terra*, upon the organ and by the choir; and at Christmas one may, after old custom, sing in
among them the verses *Dies est laetitiae* with those following, in Latin and German. But on
the common Sundays one shall sing by turns, one Sunday the Latin *Gloria* and the *Et in terra
dominicale*, the other [the German] […].

Pomerania allowed the laity "Allein Gott" after the choir's *Et in terra*. When that grew too
long, one or other was dropped by turns, and in Lent the Gloria might be left out altogether.
**Pomerania, *Kirchenordnung*, 1542** (Sehling 4, p. 356):

<!-- doc 1859 -->
> die chor singe darup dat et in terra, wenn dat ut is, lat me die leien singen, allein godt
> in der hoge si ehr; wenn idt will to lange werden, so lat me under tiden dat latinische,
> unter tiden dat düdesche na, in der vasten mach me dat gloria wol gar ute laten.

The choir singeth thereupon the *Et in terra*; when that is out, let the laity sing "To God
alone on high be glory." When it will grow too long, let the Latin be left off at times, and
the German at times; in Lent the Gloria may well be left out altogether.

The Pomeranian *Agenda* of 1569 offers both German Glorias. **Pomerania, *Agenda*, 1569**
(Sehling 4, p. 437):

<!-- doc 1865 -->
> Et in terra pax, latin edder düdisch: Allene godt in der högede si ehre etc., Alle ehre unde
> pris schal gades sin, etc.

*Et in terra pax*, in Latin or German: "To God alone on high be glory," etc., "All honour and
praise shall be God's," etc.

### 7.3 Teaching the people to sing it

Oldenburg placed the sexton and some scholars among the congregation, below the choir. There
they sang the German *Et in terra* and other German hymns in alternation with the upper choir,
so that the people might learn tune and words. **Oldenburg, *Kirchenordnung*, 1573**
(Sehling 7/2.1, p. 1089):

<!-- doc 2149 -->
> lateinisch für sich selbst, zu zeiten deudsch mit dem volk oder auch umbgewechselt singen.
> Darzu denn vonnöten, das der opperman oder küster sampt etlichen schülern an einem gewissen
> ort bey der gemein unter dem chor stehet und das deudsche Et in terra, wie auch andere
> deudsche geistliche heder mit umbwechselung der vers und gesetz des öbern chors singen,
> damit das volk des gesangs der melodey und der wörter je lenger je mehr gewohne und lust und
> liebe darzu gewinne.

[the scholars shall sing the *Et in terra pax*, at times] in Latin by themselves, at times in
German with the people, or else by turns. For which it is needful that the sexton or clerk,
with some scholars, stand at a set place by the congregation beneath the choir, and sing the
German *Et in terra*, as also other German spiritual songs, changing verses and stanzas with
the upper choir, that the people may more and more grow used to the song, the melody and the
words, and win pleasure and love thereto.

The Brenz order for Schwäbisch Hall had hoped for this from the start. **Schwäbisch Hall,
*Kirchenordnung*, 1527** (Sehling 17/1, p. 49):

<!-- doc 755 -->
> Nach dem Kirieleyson dient wol das lobgesang Gottes, Gloria in excelsis, nach gelegenhait
> der zeyt und alter gewonhait, were auch gut zubesserung der kirchen, wie alle ding geschehen
> sollen in der gemein versamlung, das mit der Zeyt das volck uff teutsch das lobgesang, von
> engeln gesungen, et in terra pax hominibus und psalmen singen lernt.

After the Kyrie eleison the song of praise to God, *Gloria in excelsis*, serveth well,
according to the occasion of the season and the old custom. It were also good for the
edifying of the church, as all things should be done in the common assembly, that the people
should in time learn to sing in German the song of praise sung by the angels, *et in terra pax
hominibus*, and psalms.

Bugenhagen asked for "fine short German notes" for a German Gloria, so that children, maids
and women could sing it together. **Braunschweig, *Kirchenordnung*, 1528** (Sehling 6/1, pp. 438–439):

<!-- doc 1983 -->
> Wil me övers Gloria in excelsis düdesch underwilen singen, besundergen dar neyne schölere
> synt, so schicke me ock fine korte düdesche noten darto, dat kyndere, megede unde wyve […]
> konen schicklick unde eyntrechtichlick mitsingen unde nicht alleyne de, de des latinischen
> sanges gewanet synt.

But if one will at times sing the *Gloria in excelsis* in German, especially where there are
no scholars, let fine short German notes also be provided for it, that children, maids and
wives […] may sing along seemly and with one accord, and not only those that are used to the
Latin singing.

An early Low German Mass from Lippe prints "Allene Gade in der hoge" as the Gloria then
"commonly" sung. **Lippe, *Deutsche Messe* [c. 1525–1538]** (Sehling 22, p. 566):

<!-- doc 1549 -->
> ghemeynlick synget me nu düt nabescreven Gloria in excelsis […] Gloria in excelsis Deo
> Allene Gade in der hoge sy ere unde danck vor syne gnade.

Commonly this Gloria in excelsis written hereafter is now sung […]. *Gloria in excelsis Deo*:
"To God alone on high be glory and thanks for his grace."

### 7.4 Intonation and answer

In Wittgenstein the priest intoned in German and the people answered with Decius's hymn.
**Wittgenstein, *Kirchenordnung*, 1563** (Sehling 22, p. 102):

<!-- doc 1493 -->
> Preiß sey Gott in der höhe. Antwortet der chor oder das volck: Allein Gott in der hohe sey
> ehr und danck vor seine gnade etc.

"Praise be to God on high." The choir or the people answereth: "To God alone on high be glory
and thanks for his grace," etc.

Luther's "All Ehr und Lob" was the other answer. In Nördlingen two choirs sang it stanza by
stanza until the organ was ready. **Nördlingen, *Kirchenordnung* of Kaspar Löner, 1544**
(Sehling 12, p. 312):

<!-- doc 372 -->
> und die zwen chore solange, bis die orgel mecht angericht werden, das Et in terra auch
> teusch, wie doctor Martin Luther in die noten gebracht hat, ein gesetze umb das ander singen.

and the two choirs, until the organ might be made ready, [shall] sing the *Et in terra* also in
German, as Doctor Martin Luther hath set it to the notes, one stanza after the other.

**Naumburg, *Kirchen-Ordnung* for St Wenzel, 1537/1538** (Sehling 2, p. 78), for feast days:

<!-- doc 1219 -->
> Darauf singet der priester das Gloria in excelsis deutsch, wie volget. Ehr sei got, in der
> hohe. Antiphona angelorum. All ehr und lob sol gottes sein, er ist und heist der höchst
> allein.

Thereupon the priest singeth the *Gloria in excelsis* in German, as followeth: "Glory be to
God on high." The antiphon of the angels: "All honour and praise shall be God's; he is, and is
called, the Highest alone."

Hof also marks "All Ehr und Lob" as sung "loco Et in terra" at Pentecost (§6.4) and at
Christmas, Epiphany and the Purification.

### 7.5 Left out: Advent, Lent, winter

The Gloria was the ordinary most easily dropped. Nördlingen left it out in Advent because the
hymns after the epistle were long. **Nördlingen, *Ordnung der ceremonien* at St George's,
1555** (Sehling 12, p. 319):

<!-- doc 373 -->
> Aber den Advent uber wird das Gloria in excelsis sampt dem Et in terra ausgelassen, von
> wegen der langen geseng nach der epistel.

But through Advent the *Gloria in excelsis* together with the *Et in terra* is left out, by
reason of the long songs after the epistle.

At Meiningen it was left out in winter, "when it will grow too long". **Meiningen,
*Gottesdienst-Ordnungen*, 1562/1566** (Sehling 2, p. 340):

<!-- doc 1248 -->
> hebt das ambt an mit dem Veni sancte spiritus deutsch, darauf singt man einen psalm, das
> kyrie eleison deutsch, darauf das gloria (welchs man im winter da es zu lang werden will,
> auslesst) und das deutsch: Et in terra: Allein gott in der höhe sei ehr etc.

[he] beginneth the office with the *Veni sancte Spiritus* in German; thereupon is sung a
psalm, the Kyrie eleison in German, thereupon the Gloria (which is left out in winter, when it
will grow too long), and the German *Et in terra*, "To God alone on high be glory," etc.

### 7.6 How fixed the Gloria was

The Gloria slot was **fixed**. When a hymn was sung, it was nearly always "Allein Gott in der
Höh", with "All Ehr und Lob" as the alternative. The variation was not in which hymn was sung.
It was in whether the German hymn replaced the Latin, alternated with it Sunday by Sunday,
was inserted into it, or was left out for length or season.

---

## 8. Between the epistle and the gospel

This is the slot of the gradual, alleluia, tract and sequence. It is the one where German
hymns were first put into the Mass (Luther, *Formula missae*: "iuxta gradualia"), and it is by
far the most variable. Here the orders let the hymn change with the season, the feast and
sometimes the gospel of the Sunday. Most per-Sunday hymn tables in the corpus are tables for
this slot. This is the slot that later came to be called the *Hauptlied* or *Graduallied*,
though neither word occurs in the corpus (see `HYMN_GUIDE.md`).

### 8.1 The rule: a pure sequence, or a German psalm

The standard formula names the sequence first and "a German psalm" as the alternative. The
choice depends on the school, the season, the length of the service, and whether the sequence
is "pure". **Saxony (Albertine), *Kirchenordnung*, 1539** (Sehling 1, p. 271):

<!-- doc 30 -->
> darauf die epistel gegen dem volk deudsch, darnach ein sequenz, oder deudschen psalm, oder
> andern geistlichen gesang, wie solches ein jede zeit erfordert.

thereupon the epistle in German toward the people; thereafter a sequence, or a German psalm,
or another spiritual song, as every season requireth.

**Kurpfalz, provisional *Kirchenordnung*, 1546** (Sehling 14, p. 96):

<!-- doc 472 -->
> so sing alsdann der chor das alleluia mit ainem sequentz, der do reyne und der heyligen
> geschrift nit entgegen ist. Wo solcher nit verhanden, werdt der sequentz underlassen oder mag
> gesungen werden ein tractus als dieser: Domine, non secundum peccata nostra facias nobis etc.

then let the choir sing the alleluia with a sequence that is pure and not contrary to holy
Scripture. Where such is not at hand, let the sequence be left off; or a tract may be sung,
as this: *Domine, non secundum peccata nostra facias nobis*, etc.

The later northern orders name the reason for having both. The Latin trains the scholars and
the German lets the congregation sing. **Wolfenbüttel, *Kirchenordnung*, 1569** (Sehling 6/1, p. 143):

<!-- doc 1974 -->
> Nach der epistel singet man einen sequenz oder alleluja oder tractum, so rein sein, damit die
> schüler auch im lateinischen gesang geübet, oder auß D. Luthers gesangbuch ein deutscher
> psalm, auf das die christliche gemein mitsingen, auch ihr gottselige ubung haben möchte.

After the epistle a sequence or alleluia or tract is sung, such as are pure, that the scholars
also may be exercised in the Latin song; or out of Doctor Luther's songbook a German psalm,
that the Christian congregation may sing along and also have its godly exercise.

This sentence comes from the Lüneburg order of 1564 and passed into Oldenburg (1573). The
Northeim order insists the choice is free. **Northeim, *Kirchenordnung*, 1539** (Sehling 6/2, p. 925):

<!-- doc 2047 -->
> Nach der epistelen mag auch der chor das haleluja und sequenz, wenn der text rein und die
> zeit nicht zu kurz ist, singen odder aber anstat des haleluja und sequenz einen psalm mit der
> ganzen gemeine. Denn es müssen solche dinge frey und keinem gesetz unterworfen sein.

After the epistle the choir may also sing the alleluia and sequence, when the text is pure and
the time not too short; or else, in the stead of the alleluia and sequence, a psalm with the
whole congregation. For such things must be free and subject to no law.

Honterus's reformation of Kronstadt in Transylvania uses the same test: German songs, or the
customary chants, "if they be not repugnant to Scripture". **Kronstadt, Honterus,
*Reformationsbüchlein*, 1543**, Latin text (Sehling 24, p. 183):

<!-- doc 1666 -->
> consuetis cantionibus de tempore utimur neque in iis, quae primitiva servavit ecclesia,
> quicquam mutuamus, nisi quod post epistolam interdum adhibemus cantiones Germanicas, interdum
> vero alias consuetas, si non repugnent scripturae.

We use the customary songs of the season, and in those things which the primitive church
kept we change nothing; save that after the epistle we sometimes use German songs, and
sometimes other customary ones, if they be not repugnant to the Scriptures.

### 8.2 The sequences cut back to the chief feasts

Most of the medieval sequences were dropped. The northern orders keep only three, for the
three high feasts of Christ, and always "with its German song". **Schleswig-Holstein,
*Kirchenordnung*, 1542** (Sehling 23, p. 90):

<!-- doc 1576 -->
> darna vor dat Gradual einen düdesschen Psalm, uth der Schrifft genamen, edder ock ein
> Gradual, dat men twe verse hefft. De Sequentien unde prosen scholen alle underlaten unde
> nicht gesungen werden, uthgenamen yn dren groten Festen Christi, alse van Wynachten wente
> tho Lichtmissen: Grates nunc omnes, mit synem düdeschen gesange.

thereafter, for the gradual, a German psalm taken out of Scripture, or else a gradual that
hath two verses. The sequences and prosae shall all be left off and not sung, save on the
three great feasts of Christ: as from Christmas unto Candlemas, *Grates nunc omnes*, with its
German song.

The Wolfenbüttel order of 1543 and the Hildesheim city order of 1544 carry the same rule,
naming the three German songs: "Gelobet seist du" with *Grates nunc omnes*, "Christ lag in
Todesbanden" with *Victimae paschali*, and "Nun bitten wir" with *Veni sancte Spiritus*.

Herford gives the reason: the old sequences were godless, and God will be honoured only
according to his word. **Herford, *Kirchenordnung*, 1532** (Sehling 21, pp. 176–177):

<!-- doc 1442 -->
> Me hefft in vor tyden in der misse gesungen Gotlose Sequentie sunder jenige beschedenheit.
> Solkes wille wy nicht mer holden, so wy nu uth Gades gnaden weten, dat God na sinem worde wil
> geeret sin, und is alle Gadesdenst nichtes werth, de nicht na sinem worde geschüd, Math. 15.
> So wil wy van Winachten an wente tho Paschen singen de Sequentie Grates nunc etc. und
> dartüsschen Gelovet sistu, Jhesu Christ und Danck segge wy alle etc., alle mael 2 versch,
> thom lesten Huic oportet etc.

In former times godless sequences were sung in the Mass without any discretion. Such we will
no more keep, since we now know by God's grace that God will be honoured according to his
word, and all service of God is worth nothing that is not done according to his word
(Matthew 15). So from Christmas unto Easter we will sing the sequence *Grates nunc*, etc., and
between, "Praised be thou, Jesu Christ," and "Thanks say we all," etc., two verses each time,
and at the last *Huic oportet*, etc.

<!-- doc 1442 -->
> Paschen wente tho Pinxsten schal me singen de Sequentie Victime Paschali etc., darup Christ
> lach in dodes banden Offt Christ ys erstanden etc. In dem Pinxsten overst schal me singen de
> sequentie Veni sancte spiritus etc. und darup na twen verschen Nu bidde wy den Hilgen gest,
> up der hilgen drevoldicheit dach den Introitum Benedicta und Sequentia Benedicta sit sancta,
> darup Nu bidde wy den Hilgen geist, so me wil. Doch me schal wenich singen van langen
> Sequentien.

From Easter unto Pentecost shall be sung the sequence *Victimae paschali*, etc., thereupon
"Christ lay in the bands of death," or "Christ is arisen," etc. But at Pentecost shall be sung
the sequence *Veni sancte Spiritus*, etc., and thereupon, after every two verses, "Now pray we
the Holy Ghost." On the day of the Holy Trinity, the introit *Benedicta* and the sequence
*Benedicta sit sancta*, thereupon "Now pray we the Holy Ghost," if one will. Yet little shall
be sung of long sequences.

Wittenberg (1533) is more generous, but it names one sequence it will not have: the "lousy
and monkish" sequence of St John the Baptist. **Wittenberg, *Kirchenordnung*, 1533** (Sehling 1, p. 704):

<!-- doc 148 -->
> Auf nativitatis Johannis den sequenz psallite regi nostro etc. Denn den lausigen und
> monichischen sequenz Sancti Johannis Christi präconis etc. und dergleichen wollen wir nicht
> haben. Den sequenz de Maria Magdalena laus tibi Christe mag man wol ein mal oder zwei im jar
> singen auf einen sontag, wen man will. Aber den sequenz de sancta trinitate so oft man will.

On the Nativity of John, the sequence *Psallite regi nostro*, etc. For the lousy and monkish
sequence *Sancti Johannis Christi praeconis*, etc., and the like, we will not have. The
sequence of Mary Magdalene, *Laus tibi Christe*, may be sung once or twice in the year upon a
Sunday, when one will. But the sequence of the Holy Trinity as oft as one will.

The Brandenburg-Ansbach *Auctuarium* lists the "pure and good" sequences of the chief feasts.
On other days it puts a German psalm-hymn in the place of an impure gradual or alleluia. For
the Purification its "sequence" is already Luther's German "Mit Fried und Freud".
**Brandenburg-Ansbach, *Auctuarium*, 1548** (Sehling 11, p. 329):

<!-- doc 278 -->
> Die fürnembsten fest, haben ir raine und gute sequenz. Bei den soll man bleiben, als
> nemblich: Nativitatis Domini: Grates nunc omnes reddamus Domino. Purificationis: Mit frid und
> freud ich far dahin. Pascha: Victime paschali laudes. De Trinitate: Benedicta semper sancta
> sit Trinitas. De Spiritu Sancto: Veni, Sancte Spiritus, oder Sancti Spiritus adsit nobis
> gratia. An den andern feirtagen und festen, die nit raine oder keine sequenz haben, sol man
> das gradual oder Alleluia singen. Wo aber die nit rain weren, als gemainlich de sanctis, an
> dero stat sing man dieser psalm einen: Ein feste burg ist unser Gott etc. Wer Gott nit mit
> uns diese zeit etc. Wol dem, der in Gottes forcht steht etc. Aus tiefer not etc. Mensch,
> wilt du leben seliglich etc. Dan mag auch die gradualia und alleluia abwechseln an sontagen
> und gemelter psalmen ainen an dero stat singen von des volks wegen.

The chiefest feasts have their pure and good sequences. By these one shall abide, namely: the
Nativity of the Lord, *Grates nunc omnes reddamus Domino*; the Purification, "In peace and joy
I now depart"; Easter, *Victimae paschali laudes*; of the Trinity, *Benedicta semper sancta sit
Trinitas*; of the Holy Ghost, *Veni, Sancte Spiritus*, or *Sancti Spiritus adsit nobis
gratia*. On the other holy days and feasts, that have no pure sequences or none, the gradual
or alleluia shall be sung. But where these were not pure, as commonly of the saints, let one
of these psalms be sung in their stead: "A mighty fortress is our God," etc.; "Were God not
with us at this time," etc.; "Blessed is he that standeth in God's fear," etc.; "Out of the
depths," etc.; "Man, wilt thou live blessedly," etc. Then also on Sundays the graduals and
alleluias may be changed about, and one of the said psalms sung in their stead, for the
people's sake.

### 8.3 Farced sequences: Latin verses and German stanzas by turns

At the three high feasts the northern and Saxon orders sang the Latin sequence with the
stanzas of a German *Leise* sung between its verses, by the people or the whole church.
The pairs are always the same:

| Season | Latin sequence | German hymn sung between |
|---|---|---|
| Christmas to Candlemas | *Grates nunc omnes* | "Gelobet seist du, Jesu Christ" (at Herford also "Dank sagen wir alle") |
| Easter to Ascension or Pentecost | *Victimae paschali* | "Christ lag in Todesbanden" or "Christ ist erstanden" |
| Pentecost | *Veni sancte Spiritus* | "Nun bitten wir den heiligen Geist" |
| Trinity (some orders) | *Benedicta semper sit Trinitas* | "Nun bitten wir" (Herford) or "Gott der Vater wohn uns bei" (Anhalt) |

The Hamburg order of 1529 gives the scheme exactly. *Grates* is sung three times, each time
followed by two German stanzas. *Huic oportet* is followed by the last stanza. At Easter a
stanza of "Christ lag" comes after every verse of *Victimae*. At Pentecost a German stanza of
"Nun bitten" comes after every two Latin verses of *Veni sancte*. **Hamburg, *Kirchenordnung*,
1529** (Sehling 5, p. 530):

<!-- doc 1960 -->
> Van winachten bet up purificationis schalme singen de sequentie grates nunc omnes etc. und mit
> sulker wise dar twischen dat leed: Gelavet sistu Jesu Christ etc. Ersten schalme singen
> Grates, dar up twe dudesche versche, noch eins Grates und twe ander dudesche versche, ock tom
> drudden mal Grates und twe ander dudesche versche. Tom lesten Huic oportet mit dem lesten
> dudeschen versche. Van paschen bet up pinxsten schallme singen de snquentie Victime pascali,
> also dat me na allen verschen singe ock ein versch van dem dudeschen lede Christ lach in
> dodes banden, dat leed averst Christ is uperstanden, schal me singen na wontliker wise, wen me
> de predike anhevet. In pinxsten schalme singen de sequentie Veni sancte spiritus und na twen
> latinschen verschen ein dudesch versch van dem lede: Nu bidde wi den hilligen geest etc.

From Christmas unto the Purification shall be sung the sequence *Grates nunc omnes*, etc., and
after this manner, between, the song "Praised be thou, Jesu Christ," etc. First *Grates* shall
be sung, thereupon two German verses; once more *Grates* and two other German verses; also the
third time *Grates* and two other German verses. At the last *Huic oportet*, with the last
German verse. From Easter unto Pentecost shall be sung the sequence *Victimae paschali*, so
that after every verse one also sing a verse of the German song "Christ lay in the bands of
death." But the song "Christ is arisen" shall be sung after the accustomed manner when the
sermon is begun. At Pentecost shall be sung the sequence *Veni sancte Spiritus*, and after
every two Latin verses a German verse of the song "Now pray we the Holy Ghost," etc.

The Prussian order of 1568 has the same scheme and adds Trinity. The Trinity sequence is
to alternate Sunday by Sunday with a German psalm, "that the German songs may remain in the
church". **Prussia, *Kirchenordnung und Ceremonien*, 1568** (Sehling 4, p. 81):

<!-- doc 1833 -->
> Nach der epistel singet man die festtage die sequenzen, wo die rein sind, als weihnachten:
> Grates nunc omnes, und wenn das einmal gesungen, darauf mit der gemeine die zwei ersten verse
> im: Gelobet seist du, Jesu Christ etc., wenn es zum andern mal gesungen, abermals zwe versen
> im selbigen psalmen. Wenn nu darauf gesungen ist: Huic oportet, ut canamus cum angelis sollen
> darauf folgen die drei letzten vers und soll das von weihnachten gehalten werden bis auf
> Purificationis. Ostern singet man den sequenz: Victimae paschali laudes, und darunter: Christ
> lag in todesbanden, vers um vers. In pfingsten singet man: Veni sancte spiritus et emitte
> coelitus, etc. und auf zwen lateinische vers allezeit einen deutschen aus dem schönen gesang:
> Nu bitten wir den heilgen geist etc. Trinitatis singet man den sequenz: Benedicta semper sit
> trinitas, und mag man denselbigen den folgenden sonntag, einen um den andern, mit einem
> deutschen psalm abwechseln, dass man einen sonntag gemelten sequenz, den andern einen
> deutschen psalm singet, damit die deutschen geseng in der kirchen bleiben.

After the epistle, on the feast days, the sequences are sung where they are pure: as at
Christmas, *Grates nunc omnes*; and when that hath been sung once, thereupon with the
congregation the two first verses of "Praised be thou, Jesu Christ," etc.; when it is sung
the second time, again two verses of the same psalm. When *Huic oportet, ut canamus cum
angelis* hath then been sung, the three last verses shall follow; and this shall be kept
from Christmas unto the Purification. At Easter the sequence *Victimae paschali laudes* is
sung, and among it "Christ lay in the bands of death," verse by verse. At Pentecost is sung
*Veni sancte Spiritus et emitte coelitus*, etc., and after two Latin verses always one German
verse out of the fair song "Now pray we the Holy Ghost," etc. On Trinity the sequence
*Benedicta semper sit Trinitas* is sung; and the same may be changed on the following Sundays,
one after the other, with a German psalm, so that one Sunday the said sequence is sung, the
other a German psalm, that the German songs may remain in the church.

In Mecklenburg the organ played the Latin verses and the cantor sang the German stanzas in
between. The Latin text was not sung at all; the organ stood for it. **Mecklenburg,
*Ordeninge der misse*, 1545** (Sehling 5, p. 152):

<!-- doc 1922 -->
> In den winachten unde vort bet to Purificationis schal me singen de sequentie: Grates nunc
> omnes, mit düsser wise. Wor ein orgel is, dar sla de organiste Grates. Dar na holde he stille
> unde de cantor vange an: Gelavet sistu. Dar na dat ander versch, des ewigen vaders, unde
> singe denn: Grates nunc omnes. Dar na sleit wedder de organiste Grates. […] In den ostern ock
> also, de organiste sla: Victime. De cantor höve an twe de ersten versche: Christ lach in
> dodes banden.

At Christmas and onward unto the Purification the sequence *Grates nunc omnes* shall be sung
after this manner. Where there is an organ, let the organist play *Grates*. Thereafter let
him hold still, and the cantor begin "Praised be thou." Thereafter the other verse, "Of the
eternal Father," and then sing *Grates nunc omnes*. Thereafter the organist playeth *Grates*
again. […] At Easter likewise: let the organist play *Victimae*; let the cantor begin the two
first verses of "Christ lay in the bands of death."

The same Mecklenburg order sang Luther's Advent hymn "Nun komm der Heiden Heiland" (the German
*Veni redemptor*) after the Advent alleluia.

The Calenberg order sets the German stanzas "between every verse". **Calenberg-Göttingen,
*Kirchenordnung*, 1542** (Sehling 6/2, p. 793):

<!-- doc 2036 -->
> Den sequenz belangen, sol man auf das haleluja denselbigen auch singen, doch also, das man von
> Ostern bis auf die Pfingsten singe: Victime paschali, von Pfingsten bis auf Trinitatis:
> Veni, sancte Spiritus, von Trinitatis, solange es den pfarherrn gut dünkt, den sequenz de
> sancta Trinitate, von den Weinachten bis purificationis Marie Grates nunc omnes. Man sol aber
> hie zwischen einem iden fers die gewönliche deutsche gesenge singen, als auf Ostern Christ
> ist erstanden, auf die Pfingsten Nu bitten wir den heiligen Geist, auf die Weinachten
> Gelobet seiestu, Jhesu Christ etc.

Touching the sequence, one shall sing the same also after the alleluia; yet so that from
Easter unto Pentecost one sing *Victimae paschali*; from Pentecost unto Trinity, *Veni, sancte
Spiritus*; from Trinity, as long as it seemeth good to the pastor, the sequence of the Holy
Trinity; from Christmas unto the Purification of Mary, *Grates nunc omnes*. But here, between
every verse, one shall sing the customary German songs: at Easter, "Christ is arisen"; at
Pentecost, "Now pray we the Holy Ghost"; at Christmas, "Praised be thou, Jesu Christ," etc.

At Harzgerode the people "sang in" the German stanzas, and on ordinary Sundays a German song
took the place of the sequence. On the feasts of Our Lady the hymn was "Herr Christ, der einig
Gotts Sohn". **Harzgerode, *Kirchenordnunge*, 1534 (?)** (Sehling 2, p. 586):

<!-- doc 1263 -->
> zu weinachten werden in der sequenz Grates nunc omnes, die deutschen gesetz Gelobet seistu mit
> dem volgenden, vom volk mit drein gesungen, auf Oestern die sequenz Victime paschali sampt dem
> Christ ist erstanden, pfingsten die sequenz Veni sancte spiritus et Emitte celitus und darzu
> die gesetz Nu bitten wir den heiligen geist mit den andern, auf die gemeine sontag an stat des
> sequenz ein deutsch lied ader psalm, auf unser frauen fest das lied Her Christ der einig gots
> son.

At Christmas, in the sequence *Grates nunc omnes*, the German stanzas "Praised be thou" with
those following are sung in among it by the people; at Easter the sequence *Victimae paschali*
together with "Christ is arisen"; at Pentecost the sequence *Veni sancte Spiritus et emitte
coelitus*, and thereto the stanzas "Now pray we the Holy Ghost" with the others; on the common
Sundays, in the stead of the sequence, a German song or psalm; on the feasts of Our Lady the
song "Lord Christ, the only Son of God."

The Anhalt *Ordnung der deutschen Gesänge* calls this "weaving in". **Anhalt, *Ordnung der
deutschen Gesänge*, before 8 February 1551** (Sehling 2, p. 555):

<!-- doc 1262 -->
> An die hohe festage als christag, ostern, pfingsten und trinitatis mag man die mess und vesper
> in latin und discant singen. Doch das under die sequentien vor dem evangelio die deudsche
> […] gesenge, zu den festagen gehorig, mit angeflochten, und da und sunst allenthalben vor der
> predig des evangelii der glaube zu deudsch gesungen werde.

On the high feast days, as Christmas, Easter, Pentecost and Trinity, one may sing the Mass
and vespers in Latin and in descant. Yet so that the German songs belonging to the feast days
be woven in among the sequences before the gospel, and that there and everywhere else, before
the sermon on the gospel, the creed be sung in German.

In the Hadersleben articles of 1528 the Latin sequences of the great feasts are allowed "and
the *Leisen* in them". **Hadersleben, *Artikel*, 1528** (Sehling 23, p. 64):

<!-- doc 1576 -->
> Eth schal ock friig sin, dat sie in den groten festen mögen Gloria in excelsis up latin
> singen, des gelicken Alleluya und eine sequentien, alse Grates nunc omnes, Victime Paschali,
> Veni Sancte Spiritus, und de leyssen darinn, item dat latinische Patrem, prefatien, Sanctus
> unnd Agnus Dei, doch dat aleine up di groten feste.

It shall also be free for them on the great feasts to sing the *Gloria in excelsis* in Latin,
likewise the alleluia and a sequence, as *Grates nunc omnes*, *Victimae paschali*, *Veni Sancte
Spiritus*, and the *Leisen* therein; item the Latin *Patrem*, prefaces, *Sanctus* and *Agnus
Dei*; yet only on the great feasts.

### 8.4 German sequences

Some orders sang the sequence itself in German prose, to the Latin melody. The Calenberg
printed Masses of 1542 give "Danksagen wir alle Gott" as the Christmas sequence (the German
*Grates*), followed by "Gelobet seist du". **Calenberg-Göttingen, *Kirchenordnung*, 1542**,
the German Christmas Mass (Sehling 6/2, p. 820):

<!-- doc 2037 -->
> Sequenz. [Noten:] Danksagen wir alle Got, unserm Herrn Christo, der uns mit seinem wort hat
> erleuchtet, hat uns erlöset mit seim blut von des teufels gewalte. Den sollen wir alle mit
> seinen engeln loben mit schalle singend: Preis sey Gott in der höhe [Ende der Noten]. Ein
> lobgesang von der geburt Christi.

Sequence. [Notes:] "Thanks say we all to God, our Lord Christ, who hath enlightened us with
his word, hath redeemed us with his blood from the power of the devil. Him shall we all praise
with his angels, with sound, singing: Praise be to God on high" [end of notes]. A song of praise
of the birth of Christ.

The same Calenberg Masses have the Easter sequence "Laßt uns Christen alle singen" with "Christ
ist erstanden" sung between its verses. The Pentecost sequence is "Komm, du Tröster, heiliger
Geist" with "Nun bitten wir" "between every verse". The Hessian *Agende* of 1574 printed the
same German sequences in its songbook appendix (Sehling 8, pp. 464–469). At Hof the Easter
sequence was sung in German as "Wir Christen opfern allesamt". **Hof, *Ordo ecclesiasticus*,
1592** (Sehling 11, p. 440):

<!-- doc 294 -->
> Post epistolam: Christ lag in todesbanden, oder der sequenz Victimae paschali, deudsch: Wir
> christen opfern allesambt.

After the epistle: "Christ lay in the bands of death," or the sequence *Victimae paschali* in
German, "We Christians offer all together."

### 8.5 A hymn in the place of the gradual

Calenberg's German Masses replace the gradual and alleluia outright on two days. At the
Purification the hymn is Simeon's song in Luther's version (Sehling 6/2, p. 823):

<!-- doc 2037 -->
> Vor das gradual und alleluja sing man den gesang Simeonis wie volgt. [Noten:] Mit fried und
> freud ich far dahin in Gottes wille.

For the gradual and alleluia let the song of Simeon be sung, as followeth. [Notes:] "In peace
and joy I now depart, according to God's will."

In the Passion Mass Psalm 51 replaces the sequence (Sehling 6/2, p. 825):

<!-- doc 2037 -->
> Anstat des sequenz singe man den volgenden psalm. Erbarm dich mein, o Herre Gott, nach deiner
> grossen barmherzigkeit!

In the stead of the sequence let the following psalm be sung: "Have mercy on me, O Lord God,
after thy great mercy!"

### 8.6 A German psalm that "rhymes with the gospel"

The fullest rule for choosing the hymn is in Pomerania (1542) and Mecklenburg (1545). On
ordinary Sundays the German psalm-hymn is to be chosen by the matter of the Sunday gospel.
Faith and grace, Christ's enemies, good works and the right use of earthly goods each have
their hymns. **Pomerania, *Kirchenordnung*, 1542** (Sehling 4, p. 356):

<!-- doc 1859 -->
> effte up die andern sondage einen psalm, de sick upt evangelium rimet so vele mogelick, alse
> wenn dat evangelium ludet vam loven und der gnade, so singe me, idt is dat heil uns kamen her,
> item dorch Adams val oder dergeliken, wenn averst dat evangelion ludet van den godtlosen
> joden und huchelern, wo se wedder Christum handlen, so singe me, idt sprecket der unwise munt
> wol, item ach godt van hemmel; wenn idt van guden werken ludet, de uns godt gebut, so singe
> me, herr wol werd wohnen etc. und andere psalme, de man wet upt bequemest to gebruken.

or on the other Sundays a psalm that rhymeth with the gospel as much as may be: as, when the
gospel speaketh of faith and of grace, let "Salvation now is come to us" be sung, item "Through
Adam's fall," or the like; but when the gospel speaketh of the godless Jews and hypocrites,
how they deal against Christ, let "The mouth of the unwise saith indeed" be sung, item "Ah God,
from heaven"; when it speaketh of good works which God commandeth us, let "Lord, who shall
dwell," etc. be sung; and other psalms which one knoweth to use most fitly.

**Mecklenburg, *Ordeninge der misse*, 1545** (Sehling 5, p. 153):

<!-- doc 1922 -->
> Up den dörpern schal me stedes einen düdeschen psalm singen, wo me in den steden to tiden ock
> don mach. Unde sundergen de psalm, de sick up dat hillige evangelion rimen. Als wen dat
> evangelion ludet van dem geloven und der gnade, so singe me: Idt is dat heil uns kamen her
> etc., Dorch Adams vall. So idt is ein lere unses heilandes, so singe me: Gades rechte und
> wunderdat. Ludet dat evangelion van den jöden, wo se wedder Christum handelen, so singe me:
> Idt sprickt der unwise mundt wol, Ach godt, van hemmel sü darin, Wo godt de here nicht bi uns
> hölt, und den II. psalm: Help godt, wo geit dat jümmer to. Wen idt van guden werken ludet, so
> singe men: Dit sint de hilligen tein gebot, Wol dem, de in gades fruchten steit, Here, wol
> wert wanen in diner hütten […]. Wenn dat evangelion eine lere is, van dem rechten gebruke
> düsser vorgenklicken dinge, so singe me: Wo godt nicht sülvest dat hus uprichtet.

In the villages a German psalm shall always be sung, as may also at times be done in the
towns; and especially the psalms that rhyme with the holy gospel. As, when the gospel speaketh
of faith and of grace, let "Salvation now is come to us," etc., "Through Adam's fall," be sung.
If it be a teaching of our Saviour, let "God's justice and wondrous deed" be sung. If the gospel
speak of the Jews, how they deal against Christ, let "The mouth of the unwise saith indeed,"
"Ah God, from heaven look down," "Where God the Lord standeth not by us," and the second psalm,
"Help, God, how goeth it ever so," be sung. When it speaketh of good works, let "These are the
holy ten commandments," "Blessed is he that standeth in God's fear," "Lord, who shall dwell in
thy tabernacle" […] be sung. When the gospel is a teaching of the right use of these
transitory things, let "Except God himself build the house" be sung.

Later orders keep the rule in shorter form. **Pomerania, *Agenda*, 1569** (Sehling 4, p. 438):

<!-- doc 1865 -->
> Hirup singet de chor de sequentiam de tempore vel feste, edder tractum, edder to tiden ein
> alleluia mit dem gradual, edder up de sondage einen düdischen psalm, de sick mit dem
> evangelio rimet. Up de sondage na Trinitatis schal men alle maente de sequentiam de trinitate
> singen. Wenn apostel dage, decollationis Iohannis, Mariae Magdalenae, conversionis Pauli, der
> hiligen marterer vallen, schal men des sondages to vörne, edder dar na, alse idt gelegen,
> desülvige sequentiam singen, alse se Lossius gesettet hefft, up dat de olden herliken gesenge
> de apostolis, evangelistis etc. nicht genzlick vorla[ren werden].

Hereupon the choir singeth the sequence of the season or of the feast, or the tract, or at
times an alleluia with the gradual, or on the Sundays a German psalm that rhymeth with the
gospel. On the Sundays after Trinity the sequence of the Trinity shall be sung every month.
When apostles' days, the Beheading of John, Mary Magdalene, the Conversion of Paul, the holy
martyrs fall, the same sequence shall be sung on the Sunday before or after, as it falleth, as
Lossius hath set them; that the old glorious songs of the apostles, evangelists, etc. be not
wholly lost.

**Naumburg, *Kirchen-Ordnung* for St Wenzel, 1537/1538** (Sehling 2, p. 71):

<!-- doc 1219 -->
> Ein deuzscher psalm nach der zeitgelegenheit oder der sich mit dem evangelio reimet.

A German psalm according to the occasion of the season, or one that rhymeth with the gospel.

**Weissenfels, *Ordnung der geseng*, 1578** (Sehling 1, p. 693). This is the order whose
one-hymn-per-Sunday table is printed in `hymns.db`:

<!-- doc 145 -->
> Singet die gemein ein deutsch lied, das sich uf die zeit und evangelium schicket, 5. Als
> dominica 1. adventus: Nun kom der heiden heiland.

The congregation singeth a German song that fitteth the season and the gospel; as on the first
Sunday of Advent, "Now come, the Saviour of the heathen."

At Weissenfels even the festal Mass sung in figured music kept this German hymn. **Weissenfels,
*Ordnung der geseng*, 1578** (Sehling 1, p. 694):

<!-- doc 145 -->
> Uf die fest werden vorgenannte gesenge alle figuraliter gesungen, ohne die deutschen lieder
> nach der epistel in der messen, und nach dem hymno in der vespern.

On the feasts the aforenamed songs are all sung in figured music, save the German songs after
the epistle in the Mass and after the hymn in the vespers.

**Verden, *Kirchenordnung*, 1606** (Sehling 7/1, p. 156):

<!-- doc 2090 -->
> Nach der epistel soll man einen sequenz oder halleluja de tempore oder einen deutschen
> psalmen, der mit dem text oder inhalt des evangelii ubereinkomet, singen.

After the epistle one shall sing a sequence or alleluia of the season, or a German psalm that
agreeth with the text or content of the gospel.

### 8.7 Sunday and season tables for this slot

Many orders fix the hymn for this slot by season, and some by Sunday. The tables of Pomerania
(1569), Pfalz-Zweibrücken (1565), Weissenfels (1578), Mansfeld (1580) and Hohenlohe (1596) are
extracted in `hymns.db` and described in `HYMN_GUIDE.md`. They are not repeated here. The
following orders have tables that are not in `hymns.db`.

**Neuenrade, *Kirchenordnung*, 1564**, Low German (Sehling 22, pp. 530–531). The table runs
by season. Holy Week has no hymn in this slot; instead, a Passion hymn is split around the
sermon. The order closes with an open clause for the rest of the year:

<!-- doc 1544 -->
> Na der Episteln singet man Alleluia und de Sequentie oder sunst ein Ledt, wie de hir
> naeinander verordent sint. Im Advent: Alleluia. Darup: Herr Christ, de einige Godes Son,
> etc. Up Winachten bet up Purificat[ionis]: Alleluia. Grates nunc omnes […] Darup: Gelovet
> s[e]istu Jhesu Christ […] Up Purificationis oder Lichtmesse Na dem Alleluia: Mit fred und
> freud ick far dahen, etc. In der Fasten: Midden wy im leven sint mit dem dod umfangen, etc.
> Up Annunciationis und Visitationis: Her Christ, de einige Godes Son, Vader in ewicheit, etc.

After the epistle the alleluia is sung, and the sequence, or else a song, as they are here
ordained one after another. In Advent: alleluia; thereupon "Lord Christ, the only Son of God,"
etc. From Christmas unto the Purification: alleluia, *Grates nunc omnes* […]; thereupon
"Praised be thou, Jesu Christ" […]. On the Purification or Candlemas, after the alleluia, "In
peace and joy I now depart," etc. In Lent: "In the midst of life we are compassed with death,"
etc. On the Annunciation and the Visitation: "Lord Christ, the only Son of God, Father in
eternity," etc.

<!-- doc 1544 -->
> Up Ostern beth up Hemelfarth: Alleluia. Darup volget Victimae Paschali laudes etc., Und
> singet dat volck dartwischen: Christ is upgestanden, oder man singe: Christ lag in
> dodesbanden […] Hemelfart: Alleluia. Nu freuwet iw, leven Christen gemein, etc. […]
> Pingsten: Alleluia. Nu bidde wy den hilligen Geist, etc. Trinitatis: God, de Vader, wone uns
> by, etc. Michaelis: Nu lave mine seele den Heren, etc. Up andere thijde nemet man, wat man
> will und sick am be[sten schicket].

From Easter unto the Ascension: alleluia; thereupon followeth *Victimae paschali laudes*, etc.,
and the people sing between: "Christ is arisen"; or one singeth "Christ lay in the bands of
death" […]. The Ascension: alleluia, "Now rejoice, dear Christians all," etc. […] Pentecost:
alleluia, "Now pray we the Holy Ghost," etc. Trinity: "God the Father be with us," etc.
Michaelmas: "Now praise, my soul, the Lord," etc. At other times one taketh what one will and
what fitteth best.

**Anhalt, *Ordnung der deutschen Gesänge*, before 8 February 1551** (Sehling 2, p. 556). This
order gives hymns by season for three slots: before the early sermon, in the Mass before the
gospel, and before the vesper sermon. For the Trinity season it tells the Mass to keep one
hymn for about four Sundays running, so that the congregation may learn it:

<!-- doc 1262 -->
> Nach Trinitatis. Bis auf die advent singe man allezeit vor der frupredig: Nu bitten wir den
> heiligen, in der messen aber sol man diese nachfolgende gesenge vor dem evangelio, etwan vier
> sontag nach einander bis auf den advent singen, damit die gemein des zu leichtlicher lerne
> und behalde: Erbarm dich mein o herre gott, Vater unser im himelreich, Es ist das heil uns
> komen her, etvan halb und die ander helft darnach, Ach got von himel sich drein, Es spricht
> der unweiser mund wol, Ein feste burg, Es wolt uns got gnedig sein, Aus tiefer not, Ich rufe
> zu dir her Jesu Christ und dergleichen.

After Trinity. Until Advent let "Now pray we the Holy [Ghost]" be sung always before the early
sermon; but in the Mass these following songs shall be sung before the gospel, some four
Sundays one after another, until Advent, that the congregation may the more easily learn and
keep them: "Have mercy on me, O Lord God"; "Our Father in the kingdom of heaven"; "Salvation now
is come to us" (about half, and the other half afterward); "Ah God, from heaven look down";
"The mouth of the unwise saith indeed"; "A mighty fortress"; "May God be gracious unto us"; "Out
of the depths"; "I call to thee, Lord Jesu Christ"; and the like.

**Prussia, *Kirchenordnung*, 1544** (Sehling 4, p. 65). Here the alleluia is sung "with the
melody rhymed to" the German psalm that follows. The list is to be rotated, "as is the use at
Königsberg":

<!-- doc 1833 -->
> Volgt Halleluja mit der melodei gereimet auf den deudschen psalmen, so man singen wil, als:
> Frölich wöllen wir halleluja singen. Eine feste burg ist unser got. Von der taufe Christi,
> doctoris Martini lied, item desselbigen Vater unser im himelreich. Item, Ach vater unser,
> der du bist etc. Abzuwechseln wie dann zu Königsberg in ubung ist etc. In den festen hats
> eigenes, als uf Ostern: Christ lag in todes banden. Item, Jesus Christ unser heiland. Auf
> Pfingsten: Kom, got schöpfer, heiliger geist. Nun bitten wir den heiligen geist. In
> Weihnachten: Gelobet seistu Jesu Christ. Item, Grates nunc omnes. Dank sagen wir nu alle etc.

There followeth the alleluia, with the melody rhymed to the German psalm that one will sing,
as: "Joyfully will we sing alleluia"; "A mighty fortress is our God"; Doctor Martin's song of
the baptism of Christ; item his "Our Father in the kingdom of heaven"; item "Ah Father of ours,
who art," etc. To be changed about, as is the use at Königsberg, etc. On the feasts there is
proper matter, as at Easter "Christ lay in the bands of death," item "Jesus Christ our
Saviour"; at Pentecost, "Come, God Creator, Holy Ghost," "Now pray we the Holy Ghost"; at
Christmas, "Praised be thou, Jesu Christ," item *Grates nunc omnes*, "Thanks say we now all,"
etc.

**Nördlingen, *Ordnung der ceremonien* at St George's, 1555** (Sehling 12, p. 323). The
order prints a Sunday list for the psalm after the epistle, taken from Naumburg. It then
leaves the choice open:

<!-- doc 373 -->
> Nach gelegenhait der zeit, nachdem es in der christenhait zustehet, mag man wol andere, die
> bequemer sich zu jeder zeit schicken, an diser stad bisweilen nemen, desgleichen auch, wenn
> man mensur singet.

According to the occasion of the time, as it standeth in Christendom, one may well take at
times others in this place, that fit themselves more fitly to every season; likewise also
when one singeth measured music.

The Nördlingen order of 1579 prints its own list and fits it to the sermon as well. **Nördlingen,
*Kirchenordnung*, 1579** (Sehling 12, p. 386):

<!-- doc 375 -->
> Wo aber den sechsten Januarii oder den sonntag vor dem Obersttag von der taufe Christi
> geprediget, solle der psalm Christ unser Herr zum Jordan kam etc. gesungen werden. Von
> Purificationis bis uf den sonntag Septuagesima: Mit frid und freud ich fahr dahin etc.

But where on the sixth of January, or the Sunday before Epiphany, it is preached of the baptism
of Christ, the psalm "Christ our Lord to Jordan came," etc. shall be sung. From the
Purification unto the Sunday Septuagesima, "In peace and joy I now depart," etc.

**Pirna, *Kirchenordnung* of Anton Lauterbach, 1555** (Sehling 1, pp. 642–643). This order
lists two German hymns for each Sunday. It says they are arranged by the sense of the Sunday
epistles and gospels, and may give way to Latin on the high feasts:

<!-- doc 119 -->
> Haec cantica germanica iuxta epistolarum et evangeliorum dominicalium sensum ordinata sunt,
> quae aliquando latinis canticis mutari possunt ad exercitium scholasticorum ad musicam
> pracipue solennibus festis ubi responsoria, hymni, introitus, gradualia pura assueto ordine
> cani possunt.

These German songs are ordered according to the sense of the Sunday epistles and gospels, and
may sometimes be changed for Latin songs for the exercise of the scholars in music, chiefly
on the solemn feasts, when pure responsories, hymns, introits and graduals may be sung in the
accustomed order.

The Mansfeld table of 1580 goes furthest toward gospel narrative hymns. For the first Sunday
after Trinity, whose gospel is Dives and Lazarus, it adds a ballad of the rich man, marked `*`
as not by Luther. **Mansfeld, *Kirchen-Agenda*, 1580** (Sehling 2, p. 238):

<!-- doc 1241 -->
> Domin. I. post trinitatis. Gott der vater wohne uns bei, etc. Ach gott von himel sich darein
> etc. *Es war einmal ein reicher man.

The first Sunday after Trinity: "God the Father be with us," etc.; "Ah God, from heaven look
down," etc.; *"There was once a rich man."

On Oculi, Mansfeld puts the litany in the place of the sequence (Sehling 2, p. 238):

<!-- doc 1241 -->
> Hie sol auch die litanei gesungen werden, an stat des sequenz, wenn das volk zusammen komen
> ist.

Here also the litany shall be sung, in the stead of the sequence, when the people are come
together.

### 8.8 Why the hymn might not change: an unknown tune

Hof's Sunday table shows why a new hymn could not always be sung. For Septuagesima it offers a
familiar alternative, because the congregation did not know the new hymn and "heareth only the
tune". **Hof, *Ordo ecclesiasticus*, 1592** (Sehling 11, p. 436):

<!-- doc 294 -->
> Post epistolam: Herr Got, dein namen rufn wir, oder dafür Ach Gott vom himel sih darein, weil
> das vorgehend sowol des künftigen sontagsgesang dem gemeinen man unbekant. und er allein den
> ton höret.

After the epistle: "Lord God, we call upon thy name," or instead "Ah God, from heaven look
down," because the foregoing, as also the song of the coming Sunday, is unknown to the common
man, and he heareth only the tune.

For Advent the same table offers a shorter hymn "when it is very cold", and keeps the longer one
for the communion (Sehling 11, p. 432):

<!-- doc 294 -->
> Post epistolam: Durch Adams fall ist ganz verderbt oder wanns sehr kalt: Ich ruf zu dir, Herr
> Jesu. Ita ut praecedens sub communionem reservetur. vel etiam sequentia: Als der gutige Got
> vollenden wolt.

After the epistle: "Through Adam's fall is all corrupt," or, when it is very cold, "I call to
thee, Lord Jesu"; so that the foregoing be kept back for the communion; or else the sequence
"When the good God would fulfil."

Wittgenstein rotated its psalm-hymns for the opposite reason: so that the congregation would
not stay "on one side" and leave the other fine psalms unlearned. **Wittgenstein,
*Kirchenordnung*, 1563** (Sehling 22, p. 103):

<!-- doc 1493 -->
> Solche ordnung behelt man etliche sontage nach den hohen festen. Wenn aber solche zeit auß
> ist, soll man an stadt der vorigen gesenge andere geistliche deutsche psalmen singen also,
> das gleichwoll diese ordnung unnd gantze action fur und fur in ihrem wesen bleibe und erhalten
> werde. Unnd sollen die pastores auff den dörffern ihr völcklin vermanen und underweisen, das
> sie solche psalmen mit singen lernen, als da seind: Durch Adams fall etc. Diß sind die
> heiligen zehen gebot etc. Ich ruff dich an, herr Jesu Christ etc. Nun frewt euch, lieben
> christen gemein etc. Auß tieffer nott schrey ich zu dir etc. Erbarm dich mein, o herre Gott
> etc. Ein feste burg ist unser Gott etc. Wo Gott, der herr, nicht bey uns helt etc. Ach Gott,
> vonn himel sih darein etc. Es spricht der unweisen mund woll etc., welcher psalmen man
> jehands einen umb den andern singen soll, damit man nicht allezeit auff einer seiten bleibe
> und die schönen psalmen ungelernet bleiben.

This order is kept some Sundays after the high feasts. But when that time is out, in the
stead of the foregoing songs other spiritual German psalms shall be sung, so that
nevertheless this order and the whole action remain and be kept in its being continually. And
the pastors in the villages shall exhort and instruct their little folk to learn to sing
along such psalms, as these are: "Through Adam's fall," etc.; "These are the holy ten
commandments," etc.; "I call upon thee, Lord Jesu Christ," etc.; "Now rejoice, dear Christians
all," etc.; "Out of the depths I cry to thee," etc.; "Have mercy on me, O Lord God," etc.; "A
mighty fortress is our God," etc.; "Where God the Lord standeth not by us," etc.; "Ah God, from
heaven look down," etc.; "The mouth of the unwise saith indeed," etc.; of which psalms one shall
sing one after the other in turn, that one abide not always on one side and the fair psalms
remain unlearned.

### 8.9 The litany in this slot

Several orders put a litany between the epistle and the gospel. Lüneburg used a
Kyrie-litany hymn, "Nim von uns, Herr Gott". It gave way when there were children to baptize,
and baptism was then held between the epistle and the gospel. **Lüneburg, *Kirchenordnung*,
1564** (Sehling 6/1, pp. 543–544):

<!-- doc 2003 -->
> Nach der epistel singet man einen sequenz oder alleluja, Lobet den Herrn, oder Nim, Herre Gott,
> von uns all unser sünde und missethat, und der priester das gebet, darin die litania
> begrieffen.

After the epistle a sequence or alleluia is sung, "Praise ye the Lord," or "Take from us, Lord
God, all our sin and misdeed," and the priest [prayeth] the prayer wherein the litany is
comprised.

<!-- doc 2003 -->
> Wenn aber die zeit zu kurz fellet oder kinder zu teufen verhanden, so kan entweder der
> sequenz oder der gesang: Nim von uns, Herr Gott etc. oder der tractus ein oder alle
> ausgelassen werden. So denn kinder zu teufen verhanden, die sollen für der lection des
> evangelii getauft werden. So aber keine kinder zu teufen verhanden oder sonst so viel zeit
> ist, sol die litania stets gesungen werden.

But when the time falleth too short, or there be children to baptize, then either the sequence
or the song "Take from us, Lord God," etc., or the tract, one or all, may be left out. When,
then, there be children to baptize, they shall be baptized before the lesson of the gospel.
But when there be no children to baptize, or there is otherwise time enough, the litany shall
always be sung.

**Kurland, *Kirchenordnung*, 1570** (Sehling 5, p. 88), which prints the same hymn:

<!-- doc 1907 -->
> Folgends die sequentia pro tempore, mit dem alleluia, oder auf den gemeinen sontagen ein
> christlicher psalm, unterzeiten die letania. Oder um der kurze willen diese letania. Nim von
> uns, lieber herr, Unser sünd und missethat.

Following, the sequence of the season with the alleluia; or on the common Sundays a Christian
psalm; at times the litany; or, for brevity's sake, this litany: "Take from us, dear Lord, our
sin and misdeed."

Regensburg used the Prussian litany with "Erhalt uns, Herr" as its appendix, and the sequence
only when there was figured music. **Regensburg, *Kirchenordnung* of Justus Jonas, 1553**
(Sehling 13, p. 420):

<!-- doc 440 -->
> Darnach singt der chor die zu Preußen gesetzten letanei mit dem anhang: Erhalt uns, Herr, bei
> deinem wort etc. […] An sunderlichen festen aber pflegt man je zu weilen von kurz wegen, so
> oft man figurirt, für die letanei die alleluia und sequenz de tempore zu nemen.

Thereafter the choir singeth the litany set forth in Prussia, with the appendix "Keep us, Lord,
by thy word," etc. […] But on special feasts it is the custom now and then, for brevity's
sake, as oft as figured music is sung, to take the alleluia and sequence of the season in the
stead of the litany.

The later Regensburg order even calls "Erhalt uns" the "sequence of the season". **Regensburg,
*Kirchenordnung*, 1567** (Sehling 13, p. 462):

<!-- doc 450 -->
> darauf singt der chor sequentiam de tempore: Erhalt uns, Herr, bei deinem wort, oder sonst
> etwas deudsches.

thereupon the choir singeth the sequence of the season: "Keep us, Lord, by thy word," or else
something German.

### 8.10 How fixed the slot was

This slot was **variable**. At the three high feasts it was fixed by the farced sequence and
its *Leise*. Through the rest of the year practice ran along a scale:

1. A short list rotated to teach the people (Anhalt 1551, Prussia 1544, Wittgenstein 1563).
2. Seasonal assignment (Neuenrade 1564, Mansfeld, Nördlingen 1579).
3. A Sunday-by-Sunday table matched to the gospel (Pirna 1555, Weissenfels 1578, Hof 1592,
   Pomerania 1569).
4. The rule of Pomerania 1542 and Mecklenburg 1545, which chooses by the matter of the gospel
   without a fixed table.

The Latin alternatives (sequence, alleluia, tract) and the litany came in at the edges.

---

## 9. The creed: "Wir glauben all"

The creed slot is among the most fixed in the corpus. Luther's "Wir glauben all an einen Gott"
was sung by the people, either instead of the Latin *Patrem* or after it. It is named in more
orders than any other hymn except "Nun bitten" and the communion hymns. The alternatives are
few:

- the Apostles' Creed sung "von Wort zu Wort" ("Ich glaub an Gott Vater"), a sung prose form;
- a German Nicene Creed;
- rarely, the Athanasian Creed in German;
- in Advent at Schweinfurt, "Wir glauben" in the place of "Nun bitten" (§9.4).

What varies is where the creed stands and what it is used for.

### 9.1 After the gospel, with or instead of the Latin *Patrem*

The *Deutsche Messe* set the pattern: "Nach dem evangelio singt die ganze kirche den glauben
zu deudsch: Wir gleuben all an einen gott" (§3.2). Where the Latin was kept, the people sang
the German creed after it, or even at the same time as it. **Pfalz-Neuburg,
*Kirchenordnung*, 1543** (Sehling 13, p. 72):

<!-- doc 386 -->
> Nach dem evangelio sol der priester das Credo und der chor das Patrem lateinisch singen oder,
> wo kein chor ist, mag es der priester selbs singen oder sprechen und das volk dieweil das
> teutsch gesang: Wir glauben all in einen Gott lassen singen.

After the gospel the priest shall sing the *Credo* and the choir the *Patrem* in Latin; or,
where there is no choir, the priest may sing or say it himself, and meanwhile let the people
sing the German song "We all believe in one God."

At Aschersleben the credal slot rotated over four Sundays: German, Latin with the *Patrem*,
figured music, and the litany. **Aschersleben, *Kirchen-Agenda*, 1575** (Sehling 2, p. 478):

<!-- doc 1260 -->
> Es soll aber auch der cantor einen sontag teutsch, den andern lateinisch singen, darzu dan das
> patrem auch gehört, den dritten sontag figuriren, und den vierten die litaniam singen.

The cantor shall also sing one Sunday in German, the other in Latin (whereto the *Patrem* also
belongeth), the third Sunday figured music, and the fourth sing the litany.

The Hessian *Agende* allows three German creeds, and on occasion the German *Grates nunc
omnes* in their place. **Hessen, *Agende*, 1574** (Sehling 8, p. 411):

<!-- doc 2272 -->
> Auf verlesung des evangelii wird gesungen das symbolum apostolicum teutsch, von wort zu wort,
> oder wie es Doctor Luther paraphrastice in gesangsweise gestelt hat, oder das symbolum
> Nicenum teutsch. Man mag auch je bisweilen nach dem evangelio das teutsch Grates nunc omnes,
> oder einen andern kurzen gesang singen und darauf das symbolum Nicenum oder Athanasianum mit
> klarer stimm dem volk für dem altar fürlesen.

Upon the reading of the gospel the Apostles' Creed is sung in German, word for word; or as
Doctor Luther hath set it in paraphrase after the manner of a song; or the Nicene Creed in
German. One may also now and then, after the gospel, sing the German *Grates nunc omnes*, or
another short song, and thereupon read the Nicene or the Athanasian Creed to the people before
the altar with a clear voice.

At Brieg (1592) the Latin Nicene Creed alternated Sunday by Sunday with the Athanasian Creed in
German, taken from Triller's songbook. **Brieg, *Kirchenordnung*, 1592** (Sehling 3, p. 446):

<!-- doc 1809 -->
> nach der epistel einen deutschen gesang aus dem gesangbüchlein des herrn doctoris Lutheri,
> nach dem evangelio das Symbolum Nicaenum oder Athanasii, einen sontag latine, den andern
> sontag das Symbolum Athanasii deutsch, aus des Trilleri gesangbüchlein.

after the epistle a German song out of the songbook of Doctor Luther; after the gospel the
Nicene or Athanasian Creed, one Sunday in Latin, the other Sunday the Athanasian Creed in
German, out of Triller's songbook.

In the Prussian villages the creed-hymn is followed at once by "Nun bitten", so the two
together lead into the sermon. **Prussia, *Kirchenordnung und Ceremonien*, 1568** (Sehling 4, p. 83):

<!-- doc 1833 -->
> auf das evangelium singet man: Wir glauben all an einen gott etc. und nach denselbigen: Nu
> bitten wir den heiligen geist etc.

after the gospel is sung "We all believe in one God," etc., and after the same, "Now pray we
the Holy Ghost," etc.

### 9.2 After the sermon: the creed as the offertory

In Bugenhagen's orders the sermon comes between the gospel and the creed. After it the
people sing the creed while the communicants go into the choir and the priest prepares the
bread and wine. The creed-hymn thus fills the slot of the old offertory. **Hamburg,
*Kirchenordnung*, 1529** (Sehling 5, p. 528):

<!-- doc 1960 -->
> Wen de predicante afsticht, so singet de prester vor dem altar na dem altar gewendt: Ick love
> an einen godt. So singet dat volk edder chor versch umme versch dat ganze Simbolum Nicenum
> ut, unde dar to Wi loven all in einen godt etc. De wile gan de communicanten in dat chor, de
> frouwen und junckfrouwen an der luchter siden, besundergen, und de mans und knechte an der
> rechten siden besundergen und de prester bereidet brodt und win, und wes dar to nodt is.

When the preacher cometh down, the priest before the altar, turned toward the altar, singeth:
"I believe in one God." Then the people or the choir sing the whole Nicene Creed through,
verse by verse, and thereto "We all believe in one God," etc. Meanwhile the communicants go
into the choir, the women and maidens on the left side apart, and the men and servants on the
right side apart; and the priest prepareth bread and wine, and what is needful thereto.

In the Braunschweig order of 1528 the creed stood before the sermon, and a German psalm or
song after the sermon did this work. **Braunschweig, *Kirchenordnung*, 1528** (Sehling 6/1, p. 441):

<!-- doc 1983 -->
> Wen de predicante affstiget, so singet me eynen düdeschen psalm edder led, dewile gan de
> communicanten int chor, de frauen unde de junkfrauen an de luchter side besundergen, unde de
> mans unde knechte an de rechter side besundergen, unde de prester bereydet bröt unde wyn,
> unde wes darto nöt is.

When the preacher cometh down, a German psalm or song is sung; meanwhile the communicants go
into the choir, the women and maidens on the left side apart, and the men and servants on the
right side apart; and the priest prepareth bread and wine, and what is needful thereto.

Buxtehude sings all three stanzas of "Wir glauben" without the organ, because in it the church
confesses its faith. **Buxtehude, *Kirchenordnung*, 1552** (Sehling 7/1, p. 75):

<!-- doc 2082 -->
> Wen de predige geendiget, so schall der prediger upp dem predigstole dem chor und volke
> ahnheven Wy geloven. Unde dewile dat in dem Wy geloven de kercke ehren geloven bekennet,
> schollen alle dre versche ahne orgel van der gemeine ganz utgesungen werden. Dewile Wy
> geloven gesungen wert, schollen de communicanten in den chorr gahn, schicklick, ordentlick,
> mit reverentie dat hochwerdige sacramente aldar to entfangende.

When the sermon is ended, the preacher in the pulpit shall begin "We believe" for the choir
and people. And because in "We believe" the church confesseth her faith, all three verses
shall be sung wholly through by the congregation without organ. While "We believe" is being
sung, the communicants shall go into the choir, seemly, orderly, with reverence, there to
receive the most worthy sacrament.

**Bremen, *Kirchenordnung*, 1534** (Sehling 7/2.2, p. 460):

<!-- doc 2217 -->
> Darna singet de Köster edder Scholemester mit synen Jüngern unde allem volcke, manne unde
> frouwen, de thom singende vormanet werden, den geloven. Unde darunder ghan de Communicanten
> ynt Chor.

Thereafter the sexton or schoolmaster, with his disciples and all the people, men and women,
who are exhorted to sing, singeth the creed. And during it the communicants go into the choir.

**Osnabrück (Stift), *Kirchenordnung*, 1543** (Sehling 7/1, p. 224):

<!-- doc 2096 -->
> Na dem sermone hevet de prester vor dem altare an: Credo in unum Deum. Darup gesungen: Wii
> geloven alle an einen Godt etc.

After the sermon the priest before the altar beginneth *Credo in unum Deum*. Thereupon is sung
"We all believe in one God," etc.

The Lüneburg city order of 1575 keeps the organ silent during the creed. The creed also covers
the minister's return to the altar. **Lüneburg, *Kirchenordnung*, 1575** (Sehling 6/1, p. 659):

<!-- doc 2017 -->
> Es werden auch zu zeiten die leute vormhanet, das sie in der kirchen bey der communion
> pleiben, und wird darauf das: Wir gleuben gesungen und unter deme nicht uff der orgel
> geschlagen und darnegst nach gelegenheit derzeit das: Credo in unum Deum etc. Unter dem
> gehet der diener widderumb vor den altar.

The people are also at times exhorted to abide in the church for the communion; and thereupon
"We believe" is sung, and during it the organ is not played; and next, according to the
occasion of the time, the *Credo in unum Deum*, etc. During it the minister goeth again before
the altar.

The Liegnitz order of 1542 also has the creed after the sermon, after the Lord's Prayer and
the reading of 1 Corinthians 11. **Liegnitz, *Kirchenordnung*, 1542** (Sehling 3, p. 439):

<!-- doc 1809 -->
> Darnach das evangelium teutsch und den gesang: Komm heiliger geist, und predigen drauf. Nach
> der predigt mag man singen das vater unser, nachdem mag man lesen den text Pauli 1. Cor. 11.
> Von dem abendmahl, oder das 6 te capitel Johannis. Darauf werde gesungen der glaube.

Thereafter the gospel in German, and the song "Come, Holy Ghost," and preach thereon. After the
sermon one may sing the Our Father; after that one may read the text of Paul, 1 Corinthians 11,
of the Supper, or the sixth chapter of John. Thereupon let the creed be sung.

### 9.3 The creed-hymn to cover the preacher's movement

The creed often covered the preacher's going up into the pulpit or coming down to the altar.
**Hadeln, *Kirchenordnung*, 1526** (Sehling 5, p. 468):

<!-- doc 1955 -->
> Finito evangelio singe de magister mit dem chore: Wi geloven etc., underdes sticht de
> predicante up den predigstole.

When the gospel is finished, let the schoolmaster sing with the choir "We believe," etc.;
meanwhile the preacher goeth up into the pulpit.

In Württemberg the creed or a German psalm covered his coming down. **Württemberg,
*Kirchenordnung*, 1536** (Sehling 16, p. 107):

<!-- doc 651 -->
> In dem aber, so er herab steygt und die predig volendet hat, soll man den teutschen glauben
> oder ein teutschen Psalmen singen, bis der pfarrherr mit statten zu dem altar kompt, da man
> das nachtmal begeen will.

But while he cometh down, having ended the sermon, the German creed or a German psalm shall be
sung, until the pastor is fully come to the altar where the Supper is to be kept.

### 9.4 "Wir glauben" in the place of "Nun bitten"

At Schweinfurt "Nun bitten" followed the Latin *Patrem* on most Sundays. In Advent "Wir
glauben all" was sung instead. **Schweinfurt, *Gottesdienstordnung*, 1576** (Sehling 11, p. 646):

<!-- doc 304 -->
> Chorus incipit Patrem, quo finito immediate sequitur cantio Nun bitten wir den Heiligen
> Geist. NB. Im Advent aber mus und sol anstatt des gesanges Nun bitten wir etc. das Wir glauben
> all an einen Gott etc. gesungen werden. NB. Per tres dominicas Adventus soll der glaub
> gesungen werden.

The choir beginneth the *Patrem*, which being ended there followeth straightway the song "Now
pray we the Holy Ghost." N.B.: But in Advent, in the stead of the song "Now pray we," etc.,
"We all believe in one God," etc. must and shall be sung. N.B.: Through three Sundays of Advent
the creed shall be sung.

### 9.5 How fixed the slot was

**Fixed.** The text was "Wir glauben all", with a sung Apostles' or Nicene Creed as the only
alternative. It did not change with the season (Schweinfurt's Advent rule is an exchange
between two fixed slots). Its place moved: after the gospel in the Saxon and southern orders,
after the sermon in Bugenhagen's northern orders. After the sermon it served as the offertory
while the communicants gathered.

---

## 10. Before the sermon: "Nun bitten wir" and the old *Leisen*

The hymn before the sermon (*ante concionem*) is the second most fixed slot, after the creed.
Its hymn is "Nun bitten wir den heiligen Geist". Its function is prayer. Many orders say the
people shall "pray an Our Father, or sing" it, or sing it "an Gebets statt", "in the stead of
prayer". The whole congregation asks for the Holy Ghost before the word is preached, and the
preacher often intones it from the pulpit.

On the high feasts the orders put the old pre-Reformation *Leisen* in its place. These are
single-stanza vernacular songs ending "Kyrieleis", in use before the Reformation and kept
because the people knew them:

| Feast | *Leise* |
|---|---|
| Christmas | "Ein Kindelein so löbelich" (or "Gelobet seist du, Jesu Christ") |
| Easter | "Christ ist erstanden" (or "Also heilig ist der Tag") |
| Ascension | "Christ fuhr gen Himmel" |
| Pentecost | "Nun bitten wir" itself, or "Komm heiliger Geist" |
| Trinity | "Gott der Vater wohn uns bei" |

The pattern is **fixed, with seasonal exchange**. One hymn stands for most of the year and a
*Leise* for each high feast and its season. Some orders use the Lord's Prayer hymn in Advent
and Lent.

### 10.1 "Nun bitten" as the prayer before the sermon

**Buxtehude, *Agende*, 1526** (Sehling 7/1, p. 70). This is the earliest seasonal table for
the slot. The Ascension hymn is "Zu Himmel zu dem Vater mein", the ninth stanza of Luther's
"Nun freut euch":

<!-- doc 2082 -->
> und vor alle sinen predigen dat gebett Nun bidde wy denn hilligen Geist gesangeswyse bidden,
> utgenahmen, dat sick de gesang vor der predige na gelegenheit der tydt mut voranderen, alse
> in Winacht bet to lichtmissen: Gelavet sistu, Jesu Christ, van Pasten bet up de himmelfart
> Christi: Christ ist uperstanden, van der himmelfart bet to Pinxsten: To himmel to dem Vader
> myn, van Pinxsten wedder bet to Wynachten: Nun bidden wy den hilligen Geist.

and before all his sermons [the pastor shall] pray in the manner of a song the prayer "Now
pray we the Holy Ghost"; save that the song before the sermon must change according to the
occasion of the season: as from Christmas unto Candlemas, "Praised be thou, Jesu Christ"; from
Easter unto the Ascension of Christ, "Christ is arisen"; from the Ascension unto Pentecost, "To
heaven, to my Father"; from Pentecost again unto Christmas, "Now pray we the Holy Ghost."

The Naumburg order of 1527 sang the first stanza of "Nun bitten" with an added stanza of its
own, "Herre Christ, Gottes Sohn". **Naumburg, *Kirchen-Ordnung* for St Wenzel, 1527**
(Sehling 2, p. 60):

<!-- doc 1218 -->
> so ruft man den heiligen geist an mit disem gesange also: Nuhe bitten wir den heiligen
> geist, u.s.w. […] Herre Christ, gottes son, durch deiner marter willen, so bedenk aller
> christenheit not, denn du uns lieber herr an dem creuze hast erlost. Kirieleis. Hirnach so
> geht der prediger auf die canzel.

then the Holy Ghost is called upon with this song, thus: "Now pray we the Holy Ghost," etc.
[…] "Lord Christ, Son of God, for thy passion's sake, remember the need of all Christendom; for
thou, dear Lord, hast redeemed us on the cross. Kyrieleis." Hereafter the preacher goeth up
into the pulpit.

**Prussia, *Kirchenordnung und Ceremonien*, 1568** (Sehling 4, p. 79), at the early sermon in
Königsberg:

<!-- doc 1833 -->
> und wird auf das gebet gesungen: Nun bitten wir den heiligen geist etc., damit gehet der
> pfarrherr auf die kanzel und predigt das evangelium de tempore.

and after the prayer is sung "Now pray we the Holy Ghost," etc.; therewith the pastor goeth up
into the pulpit and preacheth the gospel of the season.

In Nördlingen only the first stanza was sung, and the preacher began at once. **Nördlingen,
*Kirchenordnung* of Kaspar Löner, 1544** (Sehling 12, p. 312):

<!-- doc 372 -->
> Nach dem glauben sol aber die ganze kirche singen Nun bitten wir den Hailigen Gaist, nur das
> erste gesetze, und der predicant sol darauf predigen.

But after the creed the whole church shall sing "Now pray we the Holy Ghost," only the first
stanza, and the preacher shall preach thereupon.

In Herford the preacher, from the pulpit, bade the people pray an Our Father or sing "Nun
bitten", "according as the feasts are". **Herford, *Kirchenordnung*, 1532** (Sehling 21, p. 176):

<!-- doc 1442 -->
> Den geit de Prediker up den predikestoel und vormanth, en Pater noster tho sprecken offt
> singen Nu bidde wy den Hilgen geist etc., nadem dat de feste sinth Paschen, Pinxsten,
> Winachten etc.

Then the preacher goeth up into the pulpit and exhorteth to say a *Pater noster*, or to sing
"Now pray we the Holy Ghost," etc., according as the feasts are, Easter, Pentecost, Christmas,
etc.

The Pfalz-Zweibrücken plan of 1565 has "Nun bitten" before the sermon every Sunday of the
Trinity season, "one day as the other", and says so twice (Sehling 18, p. 340):

<!-- doc 985 -->
> Ante Concionem: Nun bitten wir etc. ain tag wie den andern. […] Nota: Unnd hernach allen
> Sontag vor der Predig bis Weinachten gesungen werden: Nun bitten wir etc.

Before the sermon: "Now pray we," etc., one day as the other. […] Note: and thereafter on
every Sunday before the sermon, until Christmas, "Now pray we," etc. shall be sung.

For Christmas the same plan gives the *Leise* instead, until Candlemas, and then "Nun bitten"
again until Easter (Sehling 18, p. 340):

<!-- doc 985 -->
> Also Mutatis Mutandis soll es an den nachvolgenden tagen gehalten, auch: Das kindelin,
> allemal vor der Predig gesungen werden bis Purificationis Marie, unnd hernach bis Ostern:
> Nun bitten wir etc.

So, *mutatis mutandis*, shall it be kept on the days following; also "The little Child" shall
be sung always before the sermon until the Purification of Mary, and thereafter until Easter,
"Now pray we," etc.

At Hof, on Good Friday, "Nun bitten" was dropped and the last stanza of the Passion hymn "Gott
dem Vater sei Lob" was sung kneeling in its place. **Hof, *Ordo ecclesiasticus*, 1592**
(Sehling 11, p. 439):

<!-- doc 294 -->
> Loco Patrem: Got dem Vater sei lob und dem Sohn, ultimus versus hujus cantici genibus flexis
> canitur, loco Nun bitten wir. Nun bitten wir omittitur. Post concionem: O lamb Gottes
> unschuldig.

In the place of the *Patrem*: "To God the Father be praise, and to the Son"; the last verse of
this song is sung on bended knees, in the place of "Now pray we." "Now pray we" is omitted.
After the sermon: "O Lamb of God, innocent."

### 10.2 The *Leisen* at the high feasts, sung from the pulpit

A family of orders runs from Mecklenburg (1552) through Lüneburg (1564) and Wolfenbüttel
(1569) to Oldenburg (1573). In all of them the old German songs of the three feasts are sung
by the preachers "from the pulpit, when they begin the sermon, with the people". **Mecklenburg,
*Kirchenordnung*, 1552** (Sehling 5, p. 200):

<!-- doc 1922 -->
> die deudschen alten liedlin, als uff Nativitatis Ein kindelein so löbelich, uff ostern Christ
> ist erstanden, item, Also heilig ist der tag, uff pfingsten Nu bitten wir etc. Und sollen auch
> diese die prediger von der canzel, wenn sie die predig anfahen, mit dem volk singen.

the old little German songs, as on the Nativity "A little Child so worthy of praise," at
Easter "Christ is arisen," item "So holy is the day," at Pentecost "Now pray we," etc. And these
also the preachers shall sing with the people from the pulpit, when they begin the sermon.

**Lüneburg, *Kirchenordnung*, 1564** (Sehling 6/1, p. 545):

<!-- doc 2003 -->
> Darauf sol man ein Vater unser sprechen oder singen: Nu bitten wir den heiligen Geist. Umb die
> Weihnachten: Ein kindelein so löbelich etc. Umb die Ostern: Christ ist erstanden etc.

Thereupon one shall say an Our Father, or sing "Now pray we the Holy Ghost"; about Christmas, "A
little Child so worthy of praise," etc.; about Easter, "Christ is arisen," etc.

The Lüneburg city order of 1575 calls these *Leisen* a "motet". **Lüneburg, *Kirchenordnung*,
1575** (Sehling 6/1, p. 659):

<!-- doc 2017 -->
> darnegst singt man das evangelion deutsch, darauf eine mutet, die heiligen Wiegenachten: Ein
> kindelein so lobelich, umb Osteren: Christ ist erstanden, auf himmelfart: Christ fur gen
> himmel, umb Pfingsten und sunsten das jhar durch: Nun bitten wir den heiligen Geist.

next the gospel is sung in German; thereupon a "motet": at holy Christmas, "A little Child so
worthy of praise"; about Easter, "Christ is arisen"; at the Ascension, "Christ went up to
heaven"; about Pentecost and otherwise the year through, "Now pray we the Holy Ghost."

In Kurland the pastor intoned the *Leise* from the pulpit "after old custom". The list includes
Simeon's song for the Purification. **Kurland, *Kirchenordnung*, 1570** (Sehling 5, p. 88):

<!-- doc 1907 -->
> Und wenn die festtage verhanden, der lobgesang für der predigt auf der canzel nach alter
> gewonheit zu intonirn. Gelobet seistu, Jesu Christ. Ein kindelein, so löbelich. Herr nu lestu
> deinen diener. Christ ist erstanden. Christ fur zu himmel. Nu bitten wir den heiligen geist.
> Auf und nach pfingsten, so lang man wil. Auf trinitatis. Gott der vater wohne uns bei etc.

And when the feast days are at hand, the song of praise before the sermon is to be intoned in
the pulpit after the old custom: "Praised be thou, Jesu Christ"; "A little Child so worthy of
praise"; "Lord, now lettest thou thy servant"; "Christ is arisen"; "Christ went up to heaven";
"Now pray we the Holy Ghost," at and after Pentecost as long as one will; at Trinity, "God the
Father be with us," etc.

Hoya had "Gelobet seist du" sung three times running at Christmas. For Trinity it had "O Vater
unser, gnädiger Gott", which then served "the whole summer through". **Hoya, *Kirchenordnung*,
1581** (Sehling 6/2, pp. 1148–1149):

<!-- doc 2065 -->
> Im anfang der predigt auf die hohen fest singet man auf dem predigstuel die alten, gewönlichen
> gesänge: auf Ostern Christ ist erstanden etc., auf Weynachten Gelobet seystu, Jhesu Christ
> etc. drey mal nacheinander, auf Pfingsten Nu bitten wir den heiligen Geist mit den folgenden
> versen, am tage der heiligen dreyfaltigkeit O Vater unser, gne[…] diger Gott, sampt den
> zweyen folgenden versen. Und also gemelten gesang den ganzen sommer durch.

At the beginning of the sermon on the high feasts the old, accustomed songs are sung in the
pulpit: at Easter "Christ is arisen," etc.; at Christmas "Praised be thou, Jesu Christ," etc.,
three times one after another; at Pentecost "Now pray we the Holy Ghost" with the verses
following; on the day of the Holy Trinity "O Father of ours, gracious God," together with the
two verses following. And the said song so the whole summer through.

**Hildesheim (Stift), *Kirchenordnung für Steuerwald und Peine*, 1561** (Sehling 7/2.1, p. 782):

<!-- doc 2129 -->
> wan das aus ist, singet die ganze gemain: Wir glauben und darauf: Nun bitten wir den hailigen
> Gaist oder: Kom hailig Gaist, in Weyhnachten bis auf Lichtmes: Ein kindelein so löbelich, in
> Ostern bis auf Pfingsten: Christ ist erstanden, darauf volget die predige.

when that is out, the whole congregation singeth "We believe," and thereupon "Now pray we the
Holy Ghost" or "Come, Holy Ghost"; at Christmas until Candlemas, "A little Child so worthy of
praise"; at Easter until Pentecost, "Christ is arisen"; thereupon followeth the sermon.

**Schwarzburg, *Kirchenordnung*, 1574** (Sehling 2, p. 133):

<!-- doc 1230 -->
> Auf die hohen festa aber singt er von der canzel mit dem ganzen volk ein kurzes lied, welches
> uf solches fest verordnet ist, als uf weihnachten: Ein kindelein so löbelich, uf ostern:
> Christ ist erstanden, uf pfingsten: Nun bitten wir den heiligen geist, uf trinitatis: Gott der
> vater wohn uns bei.

But on the high feasts he singeth from the pulpit with all the people a short song which is
ordained for such feast: as at Christmas, "A little Child so worthy of praise"; at Easter,
"Christ is arisen"; at Pentecost, "Now pray we the Holy Ghost"; at Trinity, "God the Father be
with us."

**Worms, *Agendbüchlein*, 1560** (Sehling 19/1, p. 206):

<!-- doc 1069 -->
> darauff so singet der Chor das: Nun bitten wir den Heiligen Geist, oder, so es an hohen Festen
> ist, derselbigen Deutschen gesang eines auff die Festa verordnet, als zu Weihenachten: Ein
> Kindelein so löbeleich, Zu Ostern: Christ ist erstanden etc. Auff das Gesang volget alßbaldt
> die Predigt.

thereupon the choir singeth "Now pray we the Holy Ghost"; or, if it be on high feasts, one of
the German songs of the same ordained for the feasts, as at Christmas "A little Child so
worthy of praise," at Easter "Christ is arisen," etc. After the song the sermon followeth
straightway.

Bugenhagen's Braunschweig order of 1528 already has "Christ ist erstanden" at the start of the
Easter sermon, "after the accustomed manner", while "Christ lag" was farced into *Victimae*
(§8.3). The Hamburg order of 1529 repeats the rule (§8.3).

The Hessian *Agende* gives the congregation's prayer before the sermon as the Lord's Prayer or
a *Leise*. **Hessen, *Agende*, 1574** (Sehling 8, p. 412):

<!-- doc 2272 -->
> die ganze kirche eintrechtiglich singet das Vater unser oder einen andern gewönlichen gesang
> nach gelegenheit der zeit als: Ein kindelein so löbelich, Christ ist erstanden, Christ fuhr
> gen Himmel, Nun bitten wir den heiligen Geist etc.

the whole church singeth with one accord the Our Father, or another accustomed song according
to the occasion of the season, as: "A little Child so worthy of praise," "Christ is arisen,"
"Christ went up to heaven," "Now pray we the Holy Ghost," etc.

Verden's order has the preacher start the hymn himself and the congregation sing it to the end.
**Verden, *Kirchenordnung*, 1606** (Sehling 7/1, pp. 156–157):

<!-- doc 2090 -->
> Bißweilen mag er anstadt des Vater unsers den psalm Nu bitten wir den heiligen […] Geist
> anfangen und mit der gemeine zu end singen. Auf Weinachten soll man singen Ein kindelein so
> löbelich, auf Ostern Also heilig ist der tag oder Christ ist erstanden, auf himmelfahrt Christ
> fuhr gen himmel, auf Pfingsten Nu bitten wir den heiligen Geist, item Kom, heiliger Geist,
> Herre Gott, auf Trinitatis Gott der Vater wohne uns bey etc.

At times, in the stead of the Our Father, he may begin the psalm "Now pray we the Holy Ghost"
and sing it to the end with the congregation. At Christmas one shall sing "A little Child so
worthy of praise"; at Easter "So holy is the day" or "Christ is arisen"; at the Ascension
"Christ went up to heaven"; at Pentecost "Now pray we the Holy Ghost," item "Come, Holy Ghost,
Lord God"; at Trinity "God the Father be with us," etc.

### 10.3 Seasonal tables for the slot: the Lord's Prayer in Advent and Lent

Several orders give the whole year. In Lent (Lippe) or in Advent and Lent (Solms-Laubach) the
Lord's Prayer hymn (Luther's "Vater unser im Himmelreich", or another Our Father song) takes
the place of "Nun bitten". **Lippe, *Kirchenordnung*, 1571** (Sehling 21, p. 387):

<!-- doc 1462 -->
> so sol die Kirche ein Vater unser sprechen oder singen an Gebets statt die gewönlichen
> Gesenge nach gelegenheit der zeit und Festen, Als auff Ostern: Christ ist erstanden, bis auff
> Pfingsten. Von Pfingsten bis auff Weinachten: Nu bitten wir den Heiligen Geist. Auff
> Nativitatis Christi: Ein Kindelin so Löblich, bis an die Sontage der Fasten. Aber die Fasten
> uber sol das Vater unser oder sonst ein ander Bettpsalm gesungen werden.

then shall the church say an Our Father, or sing, in the stead of prayer, the accustomed songs
according to the occasion of the season and feasts: as at Easter, "Christ is arisen," until
Pentecost; from Pentecost until Christmas, "Now pray we the Holy Ghost"; at the Nativity of
Christ, "A little Child so worthy of praise," until the Sundays of Lent. But through Lent the Our
Father, or else another prayer-psalm, shall be sung.

**Solms-Laubach, *Kirchenordnung* [1576–1580]** (Sehling 9, pp. 359–360):

<!-- doc 2311 -->
> und wirdt daruf die predigt angefangen und nach der praefation von weihnachten biß uf
> purificationis Mariae gesungen: Ein kindelein so löbelich etc., von purificationis biß uf
> ostern: Unser vatter, der du bist in dem hiemel, von ostern biß ascensionis: Christ ist
> erstanden, von ascensionis biß pfingsten: Christ fur ghen hiemel, von pfingsten biß uff den
> advent: […] Nun bitten wir den heiligen geist, und: Gott, der vatter, wohn uns bei etc., vom
> advent biß uf weienachten: Unser vatter, der du bist in dem hiemel etc.

and thereupon the sermon is begun, and after the preface is sung, from Christmas until the
Purification of Mary, "A little Child so worthy of praise," etc.; from the Purification until
Easter, "Our Father, who art in heaven"; from Easter until the Ascension, "Christ is arisen";
from the Ascension until Pentecost, "Christ went up to heaven"; from Pentecost until Advent,
"Now pray we the Holy Ghost" and "God the Father be with us," etc.; from Advent until
Christmas, "Our Father, who art in heaven," etc.

Tangermünde (1603) keeps the Christmas *Leise* on every Sunday until Candlemas. **Tangermünde,
*Ritus*, 1603** (Sehling 3, p. 339):

<!-- doc 1788 -->
> ante concionem canitur: Der Tag, der ist so freuden etc. vel alia festo conveniens. Praeterea
> ab hoc festo diebus solis usque ad festum purificationis ante concionem mediam canitur: Ein
> Kindelein so etc. vel alia de tempore.

before the sermon is sung "The day that is so full of joy," etc., or another agreeable to the
feast. Moreover, from this feast on the Sundays until the feast of the Purification, before
the midday sermon is sung "A little Child so," etc., or another of the season.

The Ysenburg-Birstein order uses the Lord's Prayer hymn from Trinity until Christmas.
**Ysenburg-Birstein, *Kirchenordnung*, 1588** (Sehling 10, p. 620):

<!-- doc 228 -->
> singet oder betet die Christliche Gemeyn mit ihme das Vatter unser oder anstat desselbigen
> einen kurtzen Gesang, der sich auff jede Jahrszeit schicket, als auff Weyhenachten: Ein
> Kindelein so löbelich etc., Auff Ostern: Christ ist erstanden etc., Auff Ascensionis Domini:
> Christ fuhr gen Himmel, Unnd auff Pfingsten: Nun bitten wir den heiligen Geist etc.

the Christian congregation singeth or prayeth with him the Our Father, or instead of it a short
song fitting every season of the year, as at Christmas "A little Child so worthy of praise,"
etc.; at Easter "Christ is arisen," etc.; at the Ascension of the Lord "Christ went up to
heaven"; and at Pentecost "Now pray we the Holy Ghost," etc.

**Pomerania, *Kirchenordnung*, 1542** (Sehling 4, p. 356):

<!-- doc 1859 -->
> und sprecken ein vader unse, effte singen den lavesank, kum hillige geist here godt etc. In
> den winachten ein kindelein so lavelick, in ostern Christ is upgestanden, in den pingsten nu
> bidde wi den hilgen geist.

and say an Our Father, or sing the song of praise "Come, Holy Ghost, Lord God," etc.; at
Christmas, "A little Child so worthy of praise"; at Easter, "Christ is arisen"; at Pentecost,
"Now pray we the Holy Ghost."

**Transylvanian Saxons, *Kirchenordnung*, 1547**, German text (Sehling 24, p. 244):

<!-- doc 1669 -->
> Nach diesem ampt helt man gmeiniklich in steten die erste predig, vor welcher allzeit etwas
> gesungen wirdt, als: Der tag, der ist so freudenreich, oder: Christ ist erstanden, oder: Vom
> Heiligen Geist, oder sonst ein psalmen, wie es die zeit des jars bringt. Nach der predig singt
> man abermals etwas nach der selbigen zeit oder umb frieden und desgleichen.

After this office the first sermon is commonly held in the towns, before which something is
always sung, as "The day that is so full of joy," or "Christ is arisen," or "Of the Holy
Ghost," or else a psalm, as the season of the year bringeth. After the sermon something is
sung again after the same season, or for peace, and the like.

Waldeck sets the Lord's Prayer hymn, the Ten Commandments hymn, a seasonal German song and the
creed before the chief sermon. **Waldeck, *Kirchenordnung*, 1556** (Sehling 9, p. 273):

<!-- doc 2300 -->
> Vor der Hohen Predigt sol der Pfarrherr, Custos und Gemeyn das Vatter unser Martini Lutheri:
> Vatter unser im hymelreich, der du uns alle etc., Darauff die Zehen Gebott, Eyn deutsch
> gesenge und Collecten auß Viti Theodori oder andern, nach gelegenheyt der zeit bewerdt,
> Volgents den Glauben singen.

Before the high sermon the pastor, sexton and congregation shall sing Martin Luther's Our
Father, "Our Father in the kingdom of heaven, who all of us," etc.; thereupon the Ten
Commandments; a German song and collects out of Veit Dietrich or others, proved according to
the occasion of the season; following, the creed.

### 10.4 Chosen to fit the sermon

A few orders choose the hymn before the sermon by the sermon itself. At Thorn it was "a German
song of the season, or what the text in hand and the common need required". **Thorn,
*Kirchenordnung*, 1575** (Sehling 4, p. 237):

<!-- doc 1844 -->
> wann der prediger auf die canzel steiget, soll anfänglich das volk zum gebet vermahnet ein
> deutsches lied de tempore oder was der furhabende text und gemeine noth gefordert, gesungen,
> auch ein vaterunser gebetet und folgends die predigt gefordert.

when the preacher goeth up into the pulpit, the people shall first be exhorted to prayer, and
a German song of the season, or what the text in hand and the common need required, be sung,
an Our Father also prayed, and following that the sermon set forward.

Brieg asks that the hymn "agree with the sermon as much as possible", but not at the cost of the
songs the people already know. **Brieg, *Kirchenordnung*, 1592** (Sehling 3, p. 446):

<!-- doc 1809 -->
> Auf der canzel zum amt soll der pfarr die predigt mit einem christl. gesang und vater unser
> anfangen, es soll aber der gesang soviel möglich mit der predigt übereinstimmen und hiermit
> sollen andere christl. gute gesänge, welche dem gemeinen manne bekannt nicht unterworfen sein.

In the pulpit at the office the pastor shall begin the sermon with a Christian song and an Our
Father; but the song shall agree with the sermon as much as possible; and hereby other good
Christian songs which are known to the common man shall not be put under.

The Hohenlohe *Gesangsordnung* of 1596 gives a menu for this slot. "Nun bitten", "Wir glauben
all" or the sung Apostles' Creed are the defaults. The last two stanzas of "Es ist das Heil"
can be sung if its first stanzas were sung before the lesson. Several psalm-hymns can be
chosen "if it may fit the following sermon". **Hohenlohe, *Schul- und Gesangsordnung*, 1596**
(Sehling 15, p. 653):

<!-- doc 628 -->
> für der predigt soll der schuelmeister singen: Nun bitten wir etc. oder: Wir glauben all etc.
> oder: Ich glaub an Gott etc. oder (da man für der lection gesungen: Es ist das heyl uns etc.)
> vollend die zwey letste geScätz desselben gesangs: Sey lob und ehr etc., oder (da es sich zue
> folgender predigt sclricken möchte): Herr Christ, der einig etc., Auß tieffer nott etc., Nun
> welche hie ir hoffnung etc. oder auß des Lobwaßers psalmenbuchlein den 33. Psalm biß auf den
> 7. versicul.

before the sermon the schoolmaster shall sing "Now pray we," etc., or "We all believe," etc., or
"I believe in God," etc.; or (where "Salvation now is come to us," etc. was sung before the
lesson) finish the two last stanzas of the same song, "Praise and honour," etc.; or (where it
may fit the following sermon) "Lord Christ, the only," etc., "Out of the depths," etc., "Now
they that here their hope," etc.; or out of Lobwasser's psalm book the thirty-third psalm, as
far as the seventh verse.

### 10.5 To cover the preacher's going up

As with the creed (§9.3), the hymn before the sermon often filled the time while the preacher
climbed the pulpit. **Heilbronn, draft *Gottesdienstordnung*, 1532** (Sehling 17/1, p. 301):

<!-- doc 778 -->
> Uf dasselbig singt das volck ein theutschen psalmen oder zu einem vesttag ein theutsch
> lobgesang nach dem vest, darunder get der prediger uf die cantzel.

Thereupon the people sing a German psalm, or on a feast day a German song of praise after the
feast; meanwhile the preacher goeth up into the pulpit.

**Weißenburg, *Kirchenordnung*, 1528** (Sehling 11, p. 659):

<!-- doc 308 -->
> so sing der schuelmaister den teutschen glauben oder Kum, Heiliger Geist; indem so ge der
> diener auf die cancel und postulir das evangelium.

then let the schoolmaster sing the German creed or "Come, Holy Ghost"; meanwhile let the
minister go up into the pulpit and expound the gospel.

### 10.6 How fixed the slot was

**Fixed, with seasonal exchange.** Outside the festal seasons the hymn was "Nun bitten wir",
with "Komm heiliger Geist" or the Lord's Prayer hymn as the alternative. At the three (or
four, or five) high feasts the old *Leise* of the feast took its place, often for the whole
season to the next feast. Only a few late orders (Thorn 1575, Brieg 1592, Hohenlohe 1596) let
the sermon decide the hymn in this slot.

---

## 11. After the sermon: "Erhalt uns", the offertory, and the hymn that answers the sermon

The slot after the sermon (*post concionem*) did three jobs.

1. It was a prayer after the sermon, most often "Erhalt uns, Herr, bei deinem Wort". This was
   Luther's 1541/42 hymn "against the two arch-enemies of Christ and his holy Church, the Pope
   and the Turk", as the Pfalz-Zweibrücken songbook heads it.
2. It filled the old place of the offertory. The communicants came forward and the bread and
   wine were made ready while the people sang.
3. It covered the preacher's coming down from the pulpit, or his vesting for the altar.

Later orders added a fourth: to answer the sermon with a hymn on the same doctrine.

### 11.1 "Erhalt uns, Herr, bei deinem Wort"

Prussia sang "Erhalt uns" after every sermon and gave the reason: to pray that God would not
let his word be taken away. **Prussia, *Kirchenordnung und Ceremonien*, 1568** (Sehling 4, p. 81):

<!-- doc 1833 -->
> Wenn dieselbige aus ist, singet die ganze kirche wie nach aller predigt allezeit: Erhalt uns
> herr bei deinem wort etc., damit der fromme, treue gott demütig gebeten werde, dass er sein
> wort ja nicht lasse von uns genommen werden, sondern dasselbige wider allen widerstand aller
> rotten und tyrannen, die unter den namen des papstes und türken […].

When the same is out, the whole church singeth, as after every sermon always, "Keep us, Lord,
by thy word," etc., that the godly, faithful God may be humbly prayed that he suffer not his
word to be taken from us, but [keep] the same against all resistance of all sects and tyrants,
which under the names of the Pope and the Turk […].

In the Prussian villages the same hymn covered the priest's walk to the altar (Sehling 4, p. 84):

<!-- doc 1833 -->
> Nach dem gebet singet die ganze kirche allezeit: Erhalt uns, herr, bei deinem wort etc., wie
> droben vermeldet ist. Unterdess gehet der priester von der kanzel fur den altar.

After the prayer the whole church singeth always "Keep us, Lord, by thy word," etc., as is
mentioned above. Meanwhile the priest goeth from the pulpit before the altar.

The Schweinfurt order of 1543 quotes the hymn's first lines, with the Pope and the Turk.
**Schweinfurt, *Kirchenordnung*, 1543** (Sehling 11, p. 641):

<!-- doc 304 -->
> Wenn nun die predig aus ist, sol man drauf singen: Behalt uns, Herre, bei deinem wort und
> steur des babsts und türken mord etc.

When now the sermon is out, one shall sing thereupon: "Keep us, Lord, by thy word, and curb
the Pope's and Turk's murder," etc.

Schönburg sang it "when pressing need is at hand, as alas in these last times".
**Schönburg, *Kirchenordnung*, 1542** (Sehling 2, p. 171):

<!-- doc 1235 -->
> Nach der predigt schlägt der organista etwas, bis der priester über den altar kommt,
> praeparavitque panem et calicem offerendum. Wenn aber anbeiende noth vorhanden, als leider zu
> diesen letzten zeiten, soll alle wege nach ausgang der predigt der schulmeister anheben zu
> singen mit der ganzen ecclesia: Erhalt uns herr bei deinem wort etc. Verleih uns frieden etc.

After the sermon the organist playeth somewhat, until the priest cometh to the altar and hath
prepared the bread and the cup to be offered. But when pressing need is at hand, as alas in
these last times, the schoolmaster shall always, at the end of the sermon, begin to sing with
the whole church: "Keep us, Lord, by thy word," etc.; "Grant us peace," etc.

In Reuss the hymn after the sermon was always a song "for the common peace", begun from the
pulpit. **Reuss, *Kirchen-Ordnung* of Heinrich IV, 30 August 1552** (Sehling 2, pp. 153–154):

<!-- doc 1234 -->
> Nach der predigt sol man allezeit uf der canzel einen gesang anfahen umb gemeinen friede,
> […] als: Erhalt uns herr bei deinem etc., Verlei uns frieden etc., O herr gott gib [uns dein
> fried].

After the sermon a song for the common peace shall always be begun in the pulpit, […] as:
"Keep us, Lord, by thy," etc.; "Grant us peace," etc.; "O Lord God, give [us thy peace]."

**Ritzebüttel, *Kirchenordnung*, 1556** (Sehling 5, p. 558):

<!-- doc 1963 -->
> Na der predige singet men: Erholt uns here bi dinem worde bet tom ende, edder ein andere
> dudeschen psalm David na gelegenheit der tidt sampt volgender collecta: Here godt, giff frede
> in dinem lande.

After the sermon is sung "Keep us, Lord, by thy word" to the end, or another German psalm of
David according to the occasion of the season, with the collect following: "Lord God, give
peace in thy land."

The Hoya order of 1581 (Sehling 6/2, p. 1149) and the Hildesheim chapter order of 1561
(Sehling 7/2.1, p. 782; see §10.2) likewise set "Erhalt uns" after the sermon.

### 11.2 To cover the preacher's coming down, or his vesting

In Prussia (1544) the hymn after the sermon gave the priest time to come down from the pulpit,
"take a little breath", and find his way back to the altar. **Prussia, *Kirchenordnung*,
1544** (Sehling 4, p. 65):

<!-- doc 1833 -->
> Bald auf die predigt, wo die litania nicht gehalten wird, singt die ganze kirche ein
> christlich lied, als: Nun freuet euch, lieben christen gemein. Nun lob mein seel den herren.
> Oder das vater unser von wort zu wort one auslegung nach der melodei des herren bischofs von
> Pomezan Doctoris Pauli Sperati. Unter des gehet der priester von der canzel, mag ein wenig
> respiriren und sich wieder zum altar finden.

Straightway after the sermon, where the litany is not held, the whole church singeth a
Christian song, as "Now rejoice, dear Christians all," "Now praise, my soul, the Lord," or the
Our Father word for word without exposition, after the melody of the lord bishop of Pomesania,
Doctor Paul Speratus. Meanwhile the priest goeth from the pulpit, may take a little breath, and
find himself again at the altar.

At Verden the preacher who was to celebrate put his vestments back on while the congregation
sang out the hymn he had begun. **Verden, *Kirchenordnung*, 1606** (Sehling 7/1, pp. 157–158):

<!-- doc 2090 -->
> Wenn nu die predigt geschlossen und das gemeine gebet verrichtet, so soll alßdan der prediger
> einen psalmen, als Gott der Vater wohn uns bey etc. oder Es wolt uns Gott gnädig sein, item
> Sey lob und ehr mit hohem preyß etc. oder nach ge[…]legenheit der zeit einen andern, auf der
> kanzel anfahen. Und soll derselbige von dem chor oder der gemeine vollends zu ende hinaus
> gesungen werden. Unterdessen aber soll der prediger, der das ambt halten und die communion
> verrichten wil, seinen ornatum ecclesiasticum wieder anlegen.

When now the sermon is ended and the common prayer performed, the preacher shall then begin in
the pulpit a psalm, as "God the Father be with us," etc., or "May God be gracious unto us,"
item "Praise and honour with high price," etc., or another according to the occasion of the
season. And the same shall be sung fully out to the end by the choir or the congregation. But
meanwhile the preacher who will hold the office and perform the communion shall put on again
his church vestment.

**Hessen, *Agende*, 1574** (Sehling 8, p. 412). The Corvey order of 1603 copies it:

<!-- doc 2272 -->
> Allhie gehet der pfarherr vom predigstuhl ab, und wird underdes der christlich lobgesang
> gesungen: Lobet den Herren, alle heiden etc., oder sonst ein anderer christlicher kurzer
> gesang, als: Gott der Vatter wohn uns bei, etc.

Here the pastor goeth down from the pulpit, and meanwhile the Christian song of praise is sung,
"Praise the Lord, all ye heathen," etc., or else another short Christian song, as "God the
Father be with us," etc.

**Weißenburg, *Kirchenordnung*, 1528** (Sehling 11, p. 659):

<!-- doc 308 -->
> so heb der schulmaister an zu singen ein kurzen psalm: Es woll uns Gott gnedig sein oder So
> pitten wir den Heiligen Gaist oder sünst, was ihm gefelt, das kurz ist. Indem so get der
> diener von der cancel zu dem altar.

then let the schoolmaster begin to sing a short psalm, "May God be gracious unto us," or "Now
pray we the Holy Ghost," or else what pleaseth him, that is short. Meanwhile the minister goeth
from the pulpit to the altar.

**Hadeln, *Kirchenordnung*, 1526** (Sehling 5, p. 468):

<!-- doc 1955 -->
> Im affstigende van dem predigstole singet de magister einen psalm.

In the coming down from the pulpit the schoolmaster singeth a psalm.

### 11.3 A hymn in the place of the offertory

The Latin offertory chant was a proper, and most orders dropped it because of its sacrificial
texts. In many orders a German hymn took its place, sung while the bread and wine were
prepared. Calenberg says so in the rubric of its printed Mass. **Calenberg-Göttingen,
*Kirchenordnung*, 1542** (Sehling 6/2, p. 814):

<!-- doc 2036 -->
> Darnach gehet der priester wider vor den altar und singet der chor in mitteler zeit: Es wolt
> uns Gott gnedig sein etc. ader Gott der Vater wone uns bey etc. […] Darnach volget das
> offertorium. Anstat des offertorii sol man mit der gemein einen deutschen psalm singen.

Thereafter the priest goeth again before the altar, and the choir singeth in the meantime
"May God be gracious unto us," etc., or "God the Father be with us," etc. […] Thereafter
followeth the offertory. In the stead of the offertory a German psalm shall be sung with the
congregation.

The same order's German Christmas Mass names the hymn (Sehling 6/2, p. 821):

<!-- doc 2037 -->
> Offertorium. Anstat des offertorii singe man Ein kindelein so löbelich etc.

Offertory. In the stead of the offertory let "A little Child so worthy of praise," etc. be
sung.

The rubric in the general part of the order gives the reason: the priest must make himself
ready and prepare everything for the communion (Sehling 6/2, p. 795):

<!-- doc 2036 -->
> Und weil er sich da zur communion geschickt machen und alles bereiten mus, sol in mitler zeit
> die gemein einen feinen deutschen psalm singen.

And because he must there make himself ready for the communion and prepare all things, the
congregation shall meanwhile sing a fine German psalm.

**Dortmund, *Gottesdienstordnung*, 1554** (Sehling 21, p. 209):

<!-- doc 1446 -->
> Na der predeke mach men echter einen bequemen Lavesang vor dat Offertorium singen.

After the sermon one may again sing a fitting song of praise for the offertory.

**Lippe, *Deutsche Messe* [c. 1525–1538]** (Sehling 22, p. 568):

<!-- doc 1549 -->
> Dat offertorium Vor dat offertorium synget me eyn geystlick leidt, dat ys eyn psalme.

The offertory. For the offertory a spiritual song is sung, that is, a psalm.

The Naumburg order of 1527 sang "Aus tiefer Not" in the place of the offertory. **Naumburg,
*Kirchen-Ordnung* for St Wenzel, 1527** (Sehling 2, p. 60):

<!-- doc 1218 -->
> so hebt man an in stat des offertoriumbs zu singen durch die ganze kirche den vordeutschten
> psalm Davids de profundis clamavi ad te etc. also wie folget: Aus tiefer not schrei ich zu
> dir.

then one beginneth, in the stead of the offertory, to sing through the whole church the psalm
of David put into German, *De profundis clamavi ad te*, etc., as followeth: "Out of the depths
I cry to thee."

The Brandenburg order of 1540 kept the Latin offertory of the day in the collegiate churches
and let the villages sing a German psalm instead. **Brandenburg, *Kirchenordnung*, 1540**
(Sehling 3, p. 71):

<!-- doc 1746 -->
> und nach geendigter predig das offertorium von der dominica oder festen, aber auf den dörfern
> mag man dafur einen deudschen psalmen singen.

and after the sermon is ended, the offertory of the Sunday or feast; but in the villages one
may sing a German psalm for it.

In Corvinus's Lippe order the people sang Psalm 67 or "Dank sagen wir alle" while the priest
made ready the wine and bread. **Lippe, *Kirchenordnung* of Antonius Corvinus [1542]**
(Sehling 21, p. 345):

<!-- doc 1460 -->
> Na gheschener bicht synget dat volck: Edt wolde uns Godt gnedich syn edder: Danck segge wy
> alle etc., mydtler tydt beredet de prester wyn und brodt vor de communicanten.

After the confession is done, the people sing "May God be gracious unto us," or "Thanks say we
all," etc.; meanwhile the priest maketh ready wine and bread for the communicants.

In the Lutheran East Frisian liturgy of Engerhafe, organ and congregation sang "Herr Christ,
der einig Gottessohn" in alternation while the communicants came to the table.
**Engerhafe, *Liturgie*, 1583** (Sehling 7/1, p. 677):

<!-- doc 2119 -->
> Deinde pastor accedat ad mensam Domini, paret panem et infundat vinum in calicem. Organicen
> vero et ecclesia alternis canant hymnum Herr Christ, der einig Gottessohn, et interim
> communicantes ad mensam convenire poterunt.

Thereafter let the pastor go to the table of the Lord, prepare the bread and pour the wine
into the cup. But let the organist and the church sing by turns the hymn "Lord Christ, the
only Son of God," and meanwhile the communicants may come together to the table.

The Albertine order for Celle kept Latin here, with the people kneeling in prayer "in the stead
of the offertory". **Albertine Saxony, *Die Cellischen Ordnungen*, 1545** (Sehling 1, p. 300):

<!-- doc 33 -->
> Man möchte auch wol zu zeiten abwechseln und einen andern reinen lateinischen gesang dafur
> singen, under disem obgeschribenen gesange sal das volk nider knien und sein gebete thuen an
> stadt des offertorii.

One might also at times change about and sing another pure Latin song for it. During this song
written above the people shall kneel down and make their prayers in the stead of the offertory.

### 11.4 While the communicants come forward

Many orders tie the hymn to the movement of the communicants into the choir. It is sung "until
they all kneel". **Anhalt, *Kirchen-Ordnung* of Princes Johann and Georg, 3 August 1548** (Sehling 2, p. 554):

<!-- doc 1262 -->
> Nach der prediget weil die communicanten in den chor gehen, die menner zur rechten, die weiber
> zur linken hand, soll ein deutscher psalm gesungen werden, bis das sie al[le knien].

After the sermon, while the communicants go into the choir, the men to the right, the women to
the left hand, a German psalm shall be sung until they all [kneel].

**Soest, *Kirchenordnung*, 1532** (Sehling 22, p. 450):

<!-- doc 1527 -->
> so lange die preedike geendigt ys, alßden werdt men enen karten Psalm singen, midtler tidt
> gaen se ynt kor, setten sick dale up eer knee.

until the sermon is ended; then a short psalm shall be sung; meanwhile they go into the choir
and set themselves down upon their knees.

**Nördlingen, *Kirchenordnung* of Kaspar Löner, 1544** (Sehling 12, p. 312):

<!-- doc 372 -->
> Nach der predig sol der chor singen ein teusch lidlein, bis der celebrant zum communicieren
> den kelch und die ostien zubereitet, und die communicanten sollen sich für den alter fünden.

After the sermon the choir shall sing a little German song, until the celebrant hath prepared
the cup and the hosts for communicating; and the communicants shall find themselves before the
altar.

Pomerania (1535) used the Ten Commandments hymn or *Da pacem*. **Pomerania, *Kirchenordnung*,
1535** (Sehling 4, p. 341):

<!-- doc 1856 -->
> Wenn dat alle ute is, so singet men van den tein baden gades eder da pacem latinisch unde
> düdesch, eder sus wat anders. Under des vögen sick de communicanten to dem altar de manns up
> de rechte hand de frouwen up de luchtere hande.

When all that is out, one singeth of the ten commandments of God, or *Da pacem* in Latin and
German, or else somewhat other. Meanwhile the communicants betake themselves to the altar, the
men on the right hand, the women on the left.

Brieg asked that this hymn, too, agree with the sermon. **Brieg, *Kirchenordnung*, 1592**
(Sehling 3, p. 446):

<!-- doc 1809 -->
> Nach der predigt soll der cantor einen deutschen gesang singen, damit sich die communicanten
> können zum altar finden; es soll aber auch der gesang mit der predigt übereinstimmen.

After the sermon the cantor shall sing a German song, that the communicants may find their way
to the altar; but the song also shall agree with the sermon.

### 11.5 A hymn to answer the sermon

The Mecklenburg order of 1545 wanted a short hymn after the sermon, "commonly a prayer, which
the whole congregation can sing". **Mecklenburg, *Ordeninge der misse*, 1545** (Sehling 5, p. 154):

<!-- doc 1922 -->
> schal de pastor na dem gespraken bede, einen psalm anfangen, de nicht lank is, gemenlich ein
> gebet, den de ganze gemene singen kann, alse: Idt wolde uns godt gnedich sin, Here Christ
> etc. Wat kan uns kamen an vor not.

the pastor shall, after the prayer spoken, begin a psalm that is not long, commonly a prayer,
which the whole congregation can sing, as: "May God be gracious unto us," "Lord Christ," etc.,
"What need can come upon us."

Later orders ask that it agree with the sermon's teaching. **Rostock, *Conformitas
ceremoniarum*, c. 1560** (Sehling 5, p. 288):

<!-- doc 1936 -->
> Nach der predigt und dem gebet sol der pastor einen psalm anfahen, der mit der lere des
> evangelii sol übereinstimmen.

After the sermon and the prayer the pastor shall begin a psalm which shall agree with the
teaching of the gospel.

The Hanau-Lichtenberg order gives examples by Sunday. **Hanau-Lichtenberg,
*Kirchenordnung*, 1573** (Sehling 20/2, p. 54):

<!-- doc 1364 -->
> III. Die Predig sol alwegen mit eim Gesang, so mit uberein stimmet und sich darzu reimet,
> beschlossen werden, Als auff Misericordias Domini singt man: Auß tieffer not, Auff Jubilate:
> Ach Gott, vom Himel sihe darein, Auf Cantate: Ein feste Burg, Auff Trinitatis: Gott, der
> Vater, wohn uns bey etc.

III. The sermon shall always be concluded with a song which agreeth and rhymeth therewith: as
on Misericordias Domini one singeth "Out of the depths"; on Jubilate, "Ah God, from heaven look
down"; on Cantate, "A mighty fortress"; on Trinity, "God the Father be with us," etc.

In Marienhafe the hymn after the blessing was one "agreeing with the sermon". **Marienhafe,
*Kirchenordnung*, 1593** (Sehling 7/1, p. 697):

<!-- doc 2120 -->
> volgens der segen gesprochen und darauf ein psalm oder leid, auf der predigt stimmend, myt
> denn orgel ahnfangen und von chor und gemeine außgesungen etc.

following that the blessing spoken, and thereupon a psalm or song agreeing with the sermon,
begun with the organ and sung out by choir and congregation, etc.

The Hohenlohe *Gesangsordnung* of 1596 has the schoolmaster ready with a hymn chosen by the
doctrinal article the sermon chiefly treated. It gives twelve articles, each with its hymns.
**Hohenlohe, *Schul- und Gesangsordnung*, 1596** (Sehling 15, p. 653):

<!-- doc 628 -->
> Sontags wie auch an gemeinen feyertagen nach der predigt solle der schuelmaister widerumb mit
> einem gesang gefast sein, als, da die predigt fürnemblich were gerichtet gewesen auf den
> articul 1. Vom wort und sacramenten: Der IJerr ist mein getreuer hiert etc., 0 Gott, du
> liöchster gnadenhort etc., Gott, der Vatter etc., auß dem Lobwaßer den 93. Psalm: Gott als ein
> könig etc. 2. Vom gesatz und guetten werken: IJerr Christ, der einig Gottes etc., 0 Gott, du
> höchster etc., Nun bitten.

On Sundays, as also on common holy days, after the sermon the schoolmaster shall again be
provided with a song: as, when the sermon had been directed chiefly to the article (1) of the
word and sacraments, "The Lord is my faithful shepherd," etc., "O God, thou highest treasury
of grace," etc., "God the Father," etc., out of Lobwasser the ninety-third psalm, "God as a
king," etc.; (2) of the law and good works, "Lord Christ, the only [Son] of God," etc., "O God,
thou highest," etc., "Now pray we."

The list goes on through the articles on the gospel, sin and the merit of Christ, prayer, the
cross, persecution, earthly want and blessing, the transience of life, the pestilence,
idolatry, and the last day. When many communicants were waiting, a short hymn was to be sung
instead (Sehling 15, p. 654):

<!-- doc 628 -->
> Im fall aber am sontag vill communicanten fürhanden weren, alßdan umb der kurtze willen:
> Danksagen wir alle etc. oder auß Lobwaßer den 93. Psalm: Gott als ein könig etc., den 100.:
> Ihr völker auf der erden all etc. oder den 117.: Den Herrn lobt ihr etc. oder den 121.: Mein
> augen ich etc.

But in case there were many communicants on the Sunday, then for brevity's sake: "Thanks say
we all," etc., or out of Lobwasser the ninety-third psalm, "God as a king," etc., the hundredth,
"Ye peoples on the earth all," etc., or the hundred and seventeenth, "Praise ye the Lord," etc.,
or the hundred and twenty-first, "Mine eyes I," etc.

Reutlingen wanted variety here. It asked for "not always the old common fiddle", "Es woll uns
Gott genädig sein", even though that too was a fine psalm. **Reutlingen, *Ordnung der Schule
und des Kirchengesangs*, 1565/1566** (Sehling 17/2, p. 49):

<!-- doc 828 -->
> Nach der predig, so man communiciern will, sollen sie singen: Ehre sey dem vatter etc., oder:
> Sey lob und eher mit hohem preyß etc., unnd wa man nit communiciert, abermals ainen schönen
> psalmen und nit nur alwegen die alte, gemaine geigen: Es wölle uns Gott gegnädig sein, welcher
> schöner, herrlicher psalm doch auch nit underlassen, sonder beyweilen wie andere gesungen
> werden soll.

After the sermon, when there is to be communion, they shall sing "Glory be to the Father," etc.,
or "Praise and honour with high price," etc.; and where there is no communion, again a fair
psalm, and not only always the old common fiddle, "May God be gracious unto us"; which fair,
glorious psalm yet shall not be left off, but be sung at times like the others.

The Reutlingen school visitation of 1574 asked for a hymn "agreeable to the season or to the
text preached", and not a weary repetition of the one sung before the sermon. **Reutlingen,
*Artikel der Schulvisitation*, 1574** (Sehling 17/2, p. 58):

<!-- doc 830 -->
> Item, es solle allwegen nach der predig, sonderlich wann man das heilig nachtmal nit heltt,
> ein sonder gesang oder psalm ohngevar uff drey oder vier gesetz, minder oder mehr, der zeitt
> oder dem gepredigten text gemes, gesungen unnd der vor der predig gesungne (ohngeacht, das er
> nit gar zu endt gebracht) nit mit vertruß (wie bißanhero vilfelttig beschehen) widerholt
> werden.

Item, there shall always after the sermon, especially when the holy Supper is not held, be
sung a separate song or psalm of about three or four stanzas, less or more, agreeable to the
season or to the text preached; and the one sung before the sermon (notwithstanding that it was
not brought quite to the end) shall not be repeated to weariness, as hath hitherto often been
done.

### 11.6 One hymn split around the sermon

Some orders split a single hymn: the first stanzas before the sermon and the rest after it.
The Naumburg order does this with the Lord's Prayer hymn. **Naumburg, *Kirchen-Ordnung* for
St Wenzel, 1537/1538** (Sehling 2, p. 72):

<!-- doc 1219 -->
> Darauf ein kurzer psalm nach der zeit, oder Vorleih uns frieden gnediglich, Es wolt uns got
> gnedig sein, Die lezten drei gesetz, im Nun bitten wir den heiligen geist, Und die andern hohen
> fest de tempore, item Behalt uns herr bei deinem wort, Die lezten sechs gesez im vater unser,
> so man vor der predigt die ersten drei gesungen hat.

Thereupon a short psalm according to the season; or "Grant us peace graciously," "May God be
gracious unto us," the last three stanzas of "Now pray we the Holy Ghost," and on the other
high feasts of the season, item "Keep us, Lord, by thy word," the last six stanzas of the Our
Father, when the first three have been sung before the sermon.

**Anhalt, *Ordnung der deutschen Gesänge*, before 8 February 1551** (Sehling 2, p. 556), for
Christmas:

<!-- doc 1262 -->
> Am christag und ezliche tage darnach singe man vor der fruepredig drei versen von dem lobsang:
> Gelobet seistu Jesu Christ etc. und die ander versen nach der predig, in der messen vor dem
> evangelio singe man: Gelobet seistu Jesu Christ gar aus.

On Christmas Day and some days after, let three verses of the song of praise "Praised be thou,
Jesu Christ," etc. be sung before the early sermon, and the other verses after the sermon; in
the Mass before the gospel let "Praised be thou, Jesu Christ" be sung through entire.

The German school order of Öhringen had the schoolmaster sing, after the sermon, the last stanza
of the hymn he had sung before it. **Öhringen, *Kirchen- und Schulordnungen*, 1582**
(Sehling 15, p. 503):

<!-- doc 592 -->
> soll er ein psalmen singen, als: O Here Gott begnade mich etc. oder: Eß ist das heil uns
> kommen her etc. und dergleichen. […] Nach der predigt das letzt gesang des vorigen psalmen
> als: Sey lob und ehr mit hohem preiß oder dergleichen etwas kurztes.

he shall sing a psalm, as "O Lord God, be gracious unto me," etc., or "Salvation now is come to
us," etc., and the like. […] After the sermon the last stanza of the foregoing psalm, as "Praise
and honour with high price," or the like, somewhat short.

At Neuenrade, in Holy Week, the Passion hymn "Gott dem Vater sei Lob" was sung to its fifteenth
stanza before the sermon and taken up again there after it (Sehling 22, p. 531). The funeral
orders of Schwäbisch Hall and Limpurg split the burial hymn in the same way (§17.4).

### 11.7 How fixed the slot was

**A handful, with a trend toward the variable.** The Saxon, Prussian and northern orders
mostly fixed the slot on "Erhalt uns", with "Verleih uns Frieden", "Es woll uns Gott" or "Gott
der Vater wohn uns bei" as the alternatives. Where it was the offertory, any "German psalm"
would do. From the 1560s the Upper German, Hessian, Hohenlohe and East Frisian orders
increasingly wanted a hymn chosen to answer the sermon. That is the most topical choice of hymn
anywhere in the service.

---

## 12. The Sanctus: "Jesaia dem Propheten" and "Heilig ist Gott der Vater"

The German Sanctus had two forms:

- Luther's "Jesaia dem Propheten das geschah" (1526). This is a rhymed narrative of Isaiah 6,
  printed in the *Deutsche Messe*.
- A troped Trinitarian Sanctus, "Heilig ist Gott der Vater, heilig ist Gott der Sohn, heilig ist
  Gott der Heilige Geist", printed in Low German in Bugenhagen's Wolfenbüttel order.

The Latin Sanctus stayed in towns with schools and on feasts. In most orders the German
Sanctus followed the sermon and exhortation and led straight into the communion. In some it was
sung during the distribution itself (§14).

### 12.1 "Jesaia dem Propheten" as the communicants come forward

**Prussia, *Kirchenordnung*, 1544** (Sehling 4, p. 65):

<!-- doc 1833 -->
> Darauf singt der chor ader die kirche das deudsche sanctus oder das lied: Jesaia dem
> propheten das geschach, dar unter bald treten zum altar die communiciren wöllen, und darf der
> priester das sacrament nicht erheben, dann die elevation ist disfals unnötig, und aus dieser
> ursach abgethan.

Thereupon the choir or the church singeth the German Sanctus, or the song "Isaiah the prophet,
it befell," during which those that will communicate straightway step to the altar. And the
priest need not elevate the sacrament, for the elevation is herein unneedful, and for this
cause is done away.

**Nördlingen, *Ordnung der ceremonien* at St George's, 1555** (Sehling 12, p. 319):

<!-- doc 373 -->
> Das Sanctus aus dem Esaia teutsch, damit sich das volk zur communion im chor samele.

The Sanctus out of Isaiah in German, that the people may gather in the choir for the
communion.

Pomerania had the boys intone the words "Heilig ist Gott der Herre Zebaoth" inside Luther's
hymn, with the choir answering. **Pomerania, *Agenda*, 1569** (Sehling 4, p. 438):

<!-- doc 1865 -->
> De pastor schal ock vorschaffen, dat vor dat sanctus vaken gesungen werde: Esaia dem
> propheten dat geschach etc. unde dat de knaben allene dat sanctus darinne intoneren unde dat
> chor respondere.

The pastor shall also see to it that in the stead of the Sanctus there be often sung "Isaiah
the prophet, it befell," etc., and that the boys alone intone the Sanctus therein and the choir
answer.

Wittgenstein gives "Dank sagen wir alle" as an alternative in this slot. **Wittgenstein,
*Kirchenordnung*, 1563** (Sehling 22, p. 103):

<!-- doc 1493 -->
> Nach verrichter predige fange man den lobgesang an zusingen: Esaia, dem propheten, das
> geschach etc., oder: Danck sagen wir alle etc.

After the sermon is performed, let the song of praise be begun: "Isaiah the prophet, it
befell," etc., or "Thanks say we all," etc.

The later Kurpfalz text of 1577 gives the choice between "das sanctus, Isaia dem propheten,
Grates nunc omnes, danck sagen wir alle oder einen andern dergleichen kurtzen gesang"
(Sehling 14, p. 149, apparatus).

In Calenberg's German Masses the priest prayed a collect for the authorities in silence while
the Sanctus hymn was sung. **Calenberg-Göttingen, *Kirchenordnung*, 1542**, the German
Christmas Mass (Sehling 6/2, p. 821):

<!-- doc 2037 -->
> Hirauf folget das Sanctus. Jesaia dem propheten .... Die collecta, so der priester unter dem
> Sanctus betet. Barmherziger himlischer Vater.

Hereupon followeth the Sanctus, "Isaiah the prophet …". The collect which the priest prayeth
during the Sanctus: "Merciful heavenly Father …"

### 12.2 The Trinitarian German Sanctus

**Wolfenbüttel, *Kirchenordnung*, 1543** (Sehling 6/1, p. 59):

<!-- doc 1972 -->
> Up de latinische praefatio mach de ganze kercke frölick dat düdesch Sanctus singen. (Noten:)
> Hillich is Got, de Vader, hillich is Got, de Sone, hillich is Got, de hilge Geist. He is de
> Here Zebaoth. Alle werld is syner ehren vul. Hosianna in der höchde. Gelavet sy, de dar kumpt
> im namen des Heren. Hosianna in der höchde. (Ende der Noten). Sülck düdesch Sanctus mach men
> wol ock up ein andermal edder alle tidt singen under der communion neven andern gesengen.

After the Latin preface the whole church may joyfully sing the German Sanctus. (Notes:) "Holy
is God the Father, holy is God the Son, holy is God the Holy Ghost. He is the Lord of Sabaoth.
All the world is full of his glory. Hosanna in the highest. Blessed be he that cometh in the
name of the Lord. Hosanna in the highest." (End of notes.) Such German Sanctus may well be sung
another time also, or at all times, during the communion alongside other songs.

Stralsund kept the Latin Sanctus for feasts and the two German forms for the rest of the year.
**Stralsund, draft *Kirchenordnung*, 1555** (Sehling 4, p. 551):

<!-- doc 1889 -->
> Up de feste Sanctus agnus dei underwilen gesungen, und up de andern tide dudesk: Hilich is
> godt de vader, und wo idt ock doctor Martinus ut deme propheten Esaia vordudeschet hefft.

On the feasts the Sanctus and Agnus Dei are sung at times; and at the other times in German,
"Holy is God the Father," and as Doctor Martin hath also put it into German out of the prophet
Isaiah.

Mecklenburg allowed the towns to take the Sanctus melodies set in the songbooks for the feasts,
matched to their Kyries. The villages sang "Jesaia" or "Heilig ist Gott der Vater".
**Mecklenburg, *Ordeninge der misse*, 1545** (Sehling 5, p. 154):

<!-- doc 1922 -->
> Na der prefation singet men in den steden dat sanctus latine, to tiden Esaia dem propheten.
> Idt is ock nicht not, dat me stedes ein sanctus to latine singe, sünder de sülven to tiden
> nemen, de in den sankböken van den groten festen up de kyrie vorordent sint. Up den dörperen
> singe men dat Esaia, edder dat ander: Hillich is godt de vader, welck me in den steden ock to
> tiden singen mach.

After the preface one singeth in the towns the Sanctus in Latin, at times "Isaiah the prophet."
Neither is it needful always to sing one Sanctus in Latin; but at times take those which in the
songbooks of the great feasts are appointed to the Kyries. In the villages let "Isaiah" be
sung, or the other, "Holy is God the Father," which may also be sung at times in the towns.

In Harlingerland three boys knelt to sing the Benedictus. The *Et homo factus est* of the creed
was sung the same way. **Harlingerland, *Kirchenordnung*, 1573/74** (Sehling 7/1, p. 738):

<!-- doc 2122 -->
> vor der communion ordnen wir zu singende daß Sanctus latein und teutsch, alß solches in
> bemeltem psalmbock Lutheri zue finden, und daß mit sonderlicher andacht, durch drey knaben
> niedergekniet, daß Benedictus und in dem Symbolo Athanasii Et homo factus est gesxungen werden
> soll, alß den solcheß biß daher gebreuchlich gewesen.

Before the communion we ordain to be sung the Sanctus in Latin and German, as the same is to be
found in the said psalm book of Luther; and that with special devotion, by three boys kneeling,
the Benedictus, and in the creed the *Et homo factus est*, shall be sung, as the same hath
hitherto been customary.

### 12.3 At the elevation

Brandenburg kept the elevation. After it the collegiate churches sang the Latin responsory
*Tua est potentia* and the parishes a German hymn. **Brandenburg, *Kirchenordnung*, 1540**
(Sehling 3, p. 69):

<!-- doc 1746 -->
> Nach der elevation sol man in Thumen und stiften einen latinischen gesang singen, als das
> responsorium tua est potencia etc., in den pfarren aber einen deudschen gesang. Es wolt uns
> gott gnedig sein oder sei lob und dank mit hohem preis.

After the elevation one shall sing in cathedrals and collegiate churches a Latin song, as the
responsory *Tua est potentia*, etc.; but in the parishes a German song, "May God be gracious
unto us," or "Praise and thanks with high price."

### 12.4 In the place of Sanctus and Agnus

Hof allowed "Jesaia" in the place of the Latin Sanctus and Agnus, or after them when there were
many communicants. At Christmas it used "Vom Himmel hoch". **Hof, *Ordo ecclesiasticus*, 1592**
(Sehling 11, p. 426):

<!-- doc 294 -->
> Interdum loco Sanctus et Agnus (vel etiam praesentibus multis, qui participant de corpore et
> sanguire Christi, post illa) canitur: Esaia, dem propheten, das ge[schach].

Sometimes in the place of the Sanctus and Agnus (or also, when many are present who partake of
the body and blood of Christ, after them) is sung "Isaiah the prophet, it befell."

### 12.5 How fixed the slot was

**Fixed.** The choice was between the Latin Sanctus (graded, on feasts), Luther's "Jesaia", and
the Trinitarian "Heilig ist Gott der Vater". Rarely a hymn of thanks ("Dank sagen wir alle",
*Grates nunc omnes*) or a hymn of prayer at the elevation takes its place.

## 13. The Lord's Prayer and the Words of Institution

No troped or farced Paternoster or Words of Institution were found in the corpus. The Verba were
sung by the priest to Luther's tones, or read. The Lord's Prayer was often sung by the priest
in German, and sometimes by the whole congregation as Luther's metrical "Vater unser im
Himmelreich".

### 13.1 The congregation sings the Lord's Prayer hymn

In the Braunschweig villages the sexton and people sang Luther's "Vaterunser" after the
epistle, and the pastor sang the Lord's Prayer and the Verba before the communion (§3.3). In
Schwarzburg the people sang the Lord's Prayer themselves where there were no scholars.
**Schwarzburg and Stolberg, *Ordenunge der religion*, 1549** (Sehling 2, p. 130):

<!-- doc 1230 -->
> Wan nicht schuler sein, mach das valch selbs singen das vater unser, darnach geschicht di
> communio des volk etc. — Mach das volk singen: Gott sei gelobet und gebenedeit. Ader ander
> schone gesang.

Where there are no scholars, the people may themselves sing the Our Father; thereafter the
communion of the people taketh place, etc. The people may sing "God be praised and blessed," or
other fair songs.

At weekday communions in Riga the whole assembly sang the Lord's Prayer hymn, so that the
schoolboys were not kept from their lessons. **Riga, *Kirchenordnung*, 1530** (Sehling 5, p. 17):

<!-- doc 1897 -->
> Am wercktag aber, so die communicanten verhanden sind, singt man vor der predigt, wie
> gewonlich, aber bald nach der predigt, hebt man an das gesetzte lied des vater unsers, das es
> die ganze versammlung singe (da mit die knaben in der schulen an irer lere nicht verhindert
> werden). Darauf spricht der priester die wort der benedeiung über das brot, über den wein.

But on the working day, when communicants are present, one singeth before the sermon as is
customary; but straightway after the sermon one beginneth the set song of the Our Father, that
the whole assembly may sing it (that the boys in the school be not hindered in their learning).
Thereupon the priest speaketh the words of blessing over the bread and over the wine.

**Sayn, *Kirchenordnung*, 1590** (Sehling 19/1, p. 407):

<!-- doc 1090 -->
> Hernach sprech oder sing der Priester das Vatter unser und die Wort vom Leib und Blut Christi
> oder mag die Kirch das Vatter unser Teutsch miteinander singen.

Thereafter let the priest say or sing the Our Father and the words of the body and blood of
Christ; or the church may sing the Our Father in German together.

### 13.2 A communion hymn split around the consecration

A Henneberg village pastor began Hus's "Jesus Christus unser Heiland" before the Lord's Prayer
and the Verba, and had the people finish it during the distribution. **Queienfeld
(Henneberg), pastor's report, 1566** (Sehling 2, p. 344):

<!-- doc 1249 -->
> Nach der predigt, wen communicanten do sein, singen wir: Jesus Christus unser heiland etc.
> Darauf singe ich oder lese das vater unser. Darnach verba consecrationis. Darnach communicir
> ich die leut und das volk singt das: Jesus Christus vollend aus und: Gott sei gelobet und
> gebenedeiet etc.

After the sermon, when there are communicants, we sing "Jesus Christ our Saviour," etc.
Thereupon I sing or read the Our Father. Thereafter the words of consecration. Thereafter I
communicate the people, and the people sing "Jesus Christ" out to the end, and "God be praised
and blessed," etc.

In the Lutheran liturgy of Engerhafe the three stanzas of "O Lamm Gottes unschuldig" were
divided across the rite. The first came after the Verba, the second after the exhortation,
and the third after the absolution, and with the third the communion began. **Engerhafe,
*Liturgie*, 1583** (Sehling 7/1, pp. 678–680):

<!-- doc 2119 -->
> Canatur Imo O lamm Gottes unschuldig etc.

Let "O Lamb of God, innocent," etc. be sung the first time.

<!-- doc 2119 -->
> Canatur 2do O lamm Gottes unschuldig etc. et dicat sacerdos: Kniet nieder, geliebte im Herrn,
> erhebet eure herzen zu Gott und lasset uns andächtig beten.

Let "O Lamb of God, innocent," etc. be sung the second time, and let the priest say: "Kneel
down, beloved in the Lord, lift up your hearts to God, and let us pray devoutly."

<!-- doc 2119 -->
> Canatur 3tio O lamm Gottes unschuldig etc. et fiat communicatio his verbis.

Let "O Lamb of God, innocent," etc. be sung the third time, and let the communion be made with
these words.

---

## 14. Under the communion (*sub communione*)

Hymns during the distribution are named more often than hymns in any other slot. The core
never changed through the century:

- **"Jesus Christus unser Heiland, der von uns den Gotteszorn wandt"**, Luther's version of
  the Latin hymn ascribed to John Hus, and often called "Johann Hussen Lied";
- **"Gott sei gelobet und gebenedeiet"**, Luther's expansion of a medieval single stanza;
- **the German Sanctus**, "Jesaia dem Propheten";
- **Psalm 111** in German, "Ich danke dem Herrn von ganzem Herzen" (Luther's *Confitebor*);
- **the Agnus Dei**, Latin or German ("O Lamm Gottes unschuldig", "Christe, du Lamm Gottes").

Around this core stood hymns added "when there are many communicants". These were the Latin
responsory *Discubuit Jesus*, *O sacrum convivium*, *Pange lingua* (in Latin and German, "Mein
Zung erkling"), "Als Jesus Christus unser Herr" (Sebald Heyden), "Nun freut euch", "Was kann uns
kommen an für Not", "O Christ, wir danken deiner Güt", "Help Gott, dass mir's gelinge", a Passion
hymn in Lent, the festal hymns at the feasts, and the German Te Deum.

### 14.1 The core pair

**Prussia, *Artikel der Ceremonien*, 1525** (Sehling 4, p. 33):

<!-- doc 1832 -->
> Under solchem communicirn sol das volk mit dem chor singen das deütsch lied Jesus Christus
> unser heilaut, und nach der communication got sei gelobet etc.

During such communicating the people with the choir shall sing the German song "Jesus Christ
our Saviour," and after the communion "God be praised," etc.

**Eisfeld, *Verordnung der Visitatoren*, 1554** (Sehling 1, p. 562):

<!-- doc 84 -->
> Unter der communion sol man singen das lid Joannis Hussen: Jesus Christus unser heiland, oder
> got sei gelobet oder Christe du lamb gott[es].

During the communion the song of John Hus shall be sung, "Jesus Christ our Saviour," or "God be
praised," or "Christ, thou Lamb of God."

A Henneberg pastor calls Hus's hymn "the instructive and comforting song of the holy martyr
John Hus". **Herpf (Henneberg), *Kirchen-Ordnung*, 1566** (Sehling 2, p. 335):

<!-- doc 1248 -->
> Unter dieser und der allerheiligsten action singt der chor das lerhaftig und trostlich lied des
> heiligen merterers Johannis Huss Jesus Christus unser heiland etc. und darauf die danks[agung
> Gott sei gelobet].

During this and the most holy action the choir singeth the instructive and comforting song of
the holy martyr John Hus, "Jesus Christ our Saviour," etc., and thereupon the thanksgiving,
"God be praised."

Bremen in 1561 wanted Hus's hymn "in the ancient melody", that is, the Latin *Jesus Christus
nostra salus*, "and at times also in the new one composed by Luther". This order was written
against the Zwinglian party in Bremen, and it sets out the communion hymns in order.
**Bremen, *Kirchenordnung*, 1561** (Sehling 7/2.2, p. 510):

<!-- doc 2221 -->
> Placet igitur nobis, ut occinatur textus Esaiae alternis vicibus Latine vel Germanice. Hunc
> postea sequatur inter communicandum cantilena Johannis Huß in prisca melodia et interdum etiam
> in recenti per Lutherum composita. Adiiciatur quoque psalmus III una cum Agnus Dei, si magna
> est multitudo communicantium. Et tandem concludatur cum gratiarum actione: Gott sey gelobt
> etc.

It pleaseth us therefore that the text of Isaiah be sung, by turns in Latin or German. Let
there follow it, during the communicating, the song of John Hus in the ancient melody, and at
times also in the new one composed by Luther. Let there be added also the hundred and eleventh
psalm together with the Agnus Dei, if the multitude of communicants be great. And at length
let it be concluded with the thanksgiving "God be praised," etc.

### 14.2 As many hymns as there are communicants

Nearly every order measures the number of communion hymns by the number of communicants.
**Saxony (Albertine), *Kirchenordnung*, 1580** (Sehling 1, p. 369):

<!-- doc 44 -->
> Unter der communion, und so der communicanten viel sind, sol das agnus dei lateinisch, sampt
> den deudschen gesengen, als Esaia dem propheten das geschach, item der 111. psalm, ich danke
> dem herrn von ganzem herzen, oder, Jesus Christus unser heiland, item, gott sei gelobet, etc.
> eins oder mehr gesungen werden.

During the communion, and when the communicants are many, the Agnus Dei in Latin, together with
the German songs, as "Isaiah the prophet, it befell," item the hundred and eleventh psalm, "I
thank the Lord with all my heart," or "Jesus Christ our Saviour," item "God be praised," etc.,
one or more, shall be sung.

**Henneberg, *Kirchenordnung*, 1582** (Sehling 2, p. 309):

<!-- doc 1247 -->
> Unter der communion sol man singen: Jesus Christus unser heiland, item, Gott sei gelobet,
> oder, Esaia dem propheten das geschach, oder was sonsten von geistlichen gesengen sein mag, so
> dieser action gemess und bequem und die notdurft nach anzal der communicanten erfordert. Wann
> aber der communicanten so wenig, das auch obgemelter gesenge einer zu lang were, so sol
> darmit, so bald die communion geendet, auch aufgehört werden.

During the communion shall be sung "Jesus Christ our Saviour," item "God be praised," or
"Isaiah the prophet, it befell," or what else there may be of spiritual songs which are
agreeable and fitting to this action and which the need requireth according to the number of
communicants. But when the communicants are so few that even one of the aforesaid songs were too
long, then it shall be stopped as soon as the communion is ended.

At the Dresden Kreuzkirche all the listed hymns were sung if there were many communicants.
**Dresden, *Gottesdienst-Ordnung der Kreuzkirche*, 1574** (Sehling 1, p. 555):

<!-- doc 78 -->
> sub communione canitur vel agnus dei, sanctus, Gott sei gelobet und gebenedeiet, Jesus
> Christus unser heiland, mein zung erkling. Si multi sunt communicantes omnes hae cantilenae
> canuntur.

During the communion is sung either the Agnus Dei, the Sanctus, "God be praised and blessed,"
"Jesus Christ our Saviour," "My tongue, resound." If the communicants are many, all these songs
are sung.

The Lippe order puts the Agnus Dei, "O Lamm Gottes" and "O Christ, wir danken deiner Güt" on
the high feasts, and ends with a hymn of thanks. **Lippe, *Kirchenordnung*, 1571** (Sehling 21, p. 388):

<!-- doc 1462 -->
> Unter der Communion, weil das Sacrament dispensirt und ausgetheilet wirdt, soll die Kirche der
> Nachgesetzten Gesenge einen oder mehr, darnach der Communicanten viel oder wenig, singen, als:
> Jhesus Christus, unser Heylandt; Auff den Hohen Festagen: Agnus Dei, O Lamb Gottes, unschüldig,
> O Christ, wir dancken deiner güte. Nach der Communion sol vom Predicanten die Collecta
> gesungen, darauff die gewönliche segen oder Benedictio, Nume. 6, gegen dem Volcke gesprochen
> werden, Und entlich mit einem Danckliede Als: Gott sey gelobet, Oder: Sey lob und ehr mit hohem
> preiß von der gantzen Kirchen beschlossen werden.

During the communion, while the sacrament is dispensed and distributed, the church shall sing
one or more of the songs hereafter set, according as the communicants are many or few, as:
"Jesus Christ our Saviour"; on the high feast days, the Agnus Dei, "O Lamb of God, innocent,"
"O Christ, we thank thee for thy goodness." After the communion the collect shall be sung by the
preacher, thereupon the accustomed blessing or benediction (Numbers 6) spoken toward the people,
and at the last it shall be concluded by the whole church with a song of thanks, as "God be
praised," or "Praise and honour with high price."

Regensburg first sang the Latin Agnus Dei three times, slowly. If that was not long enough, a
Latin thanksgiving from the gradual followed. **Regensburg, *Wahrhaftiger Bericht*, 1542**
(Sehling 13, p. 393):

<!-- doc 432 -->
> Unter diser des volks speisung singet der schulmaister das Agnus Dei dreimal langsam. Wo aber
> der communicanten so vil sind, das die drei Agnus Dei nit gelangen mögen, bis man si alle
> verrichtet, so wirdet ein lateinische danksagung darzu gesungen, wie man die im gradual am
> bequemsten finden kan.

During this feeding of the people the schoolmaster singeth the Agnus Dei three times slowly. But
where the communicants are so many that the three Agnus Deis will not reach until all have been
served, then a Latin thanksgiving is sung thereto, as the most fitting can be found in the
gradual.

Hof lists what was to be added "for the multitude of communicants". Hof's sequences in Latin and
German come first, then *Discubuit*, then four German hymns, and then, if still needed, the short
hymns otherwise sung after the sermon. **Hof, *Ordo ecclesiasticus*, 1592** (Sehling 11, p. 426):

<!-- doc 294 -->
> His propter communicantium multitudinem non sufficientibus, addantur eodem modo, quo ad organa
> et choros, germanicae cantilenae NB. Item sequentiae notae, in lingua latina et germanica
> compositae ad festa praecipua. Praeterea responso[…]rium Discubuit Jesus, in secunda parte
> missalis latini. 1. Jesus Christus unser Heiland, Johann Hussens. 2. Ich dank dem Herrn von
> ganzem herzen. 3. Erbarm dich mein, o Herr Gott. 4. Es wolt uns Gott genedig sein. Alles nach
> zal und meng der communicanten, also das auch folgende gesanglein (welche sonsten am sontag,
> desgleichen mittwoch und freitag nach vollendter predigt gesungen werden) zu end der communion
> mit hinangehenk[et werden können].

These not sufficing because of the multitude of communicants, let German songs be added in the
same manner as regards organ and choirs. Note: item the known sequences, composed in the Latin
and German tongues, for the chief feasts. Moreover the responsory *Discubuit Jesus*, in the
second part of the Latin missal. 1. "Jesus Christ our Saviour," John Hus's. 2. "I thank the Lord
with all my heart." 3. "Have mercy on me, O Lord God." 4. "May God be gracious unto us." All
according to the number and multitude of the communicants, so that the following little songs
also (which are otherwise sung on Sunday, and likewise Wednesday and Friday, after the sermon
is ended) [may be] hung on at the end of the communion.

Wittenberg lists hymns "until the communion is over", including festal hymns. **Wittenberg,
*Kirchenordnung*, 1533** (Sehling 1, p. 705):

<!-- doc 148 -->
> Weil das volk communicirt, singt man sanctus; agnus dei; Jesus Christus unser heiland; got sei
> gelobt; das deutsch confitebor tibi; pange lingua lateinisch und dergleichen, auch deutsche
> gesenge vom feste etc. bis die communion aus ist.

While the people communicate, one singeth the Sanctus; the Agnus Dei; "Jesus Christ our
Saviour"; "God be praised"; the German *Confitebor tibi*; *Pange lingua* in Latin, and the like;
also German songs of the feast, etc., until the communion is over.

### 14.3 The song stops when the communion ends

Bugenhagen's orders stop the hymn at the end of the distribution, even in mid-hymn, and go
straight to the German Agnus Dei. **Pomerania, *Kirchenordnung*, 1535** (Sehling 4, p. 341):

<!-- doc 1856 -->
> De wile de communicatio waret, schal de kerke singen ein agnus dei latinisch eder düdesch: O
> lam gades etc., Jesus Christus etc., Godt si gelavet etc., den psalm confitebor; overst nicht
> lenger den de communicatio waret, wenn de lüde sind tom sacrament gangen, so singet me ein
> ander düdesch agnus dei: Christe, du lam gades etc.

While the communion lasteth, the church shall sing an Agnus Dei in Latin or German, "O Lamb of
God," etc., "Jesus Christ," etc., "God be praised," etc., the psalm *Confitebor*; but no longer
than the communion lasteth. When the people have gone to the sacrament, another German Agnus
Dei is sung, "Christ, thou Lamb of God," etc.

The appendix of the same order is sharper still: "all other singing shall then straightway
cease, notwithstanding that a song begun be not sung out with all its verses" (Sehling 4, p. 344):

<!-- doc 1856 -->
> Dat dudesche agnus dei; so balde de lüde communiceret hebben, alle andere sank sal denne flux
> uphören, unangesehn ein angehaven leed mit allen verschen nicht utgesungen si: Christe, du lam
> gades, de du drechst de sund der werld, vorbarm di unser.

The German Agnus Dei: as soon as the people have communicated, all other singing shall then
straightway cease, notwithstanding that a song begun be not sung out with all its verses:
"Christ, thou Lamb of God, that bearest the sin of the world, have mercy upon us."

**Mecklenburg, *Ordeninge der misse*, 1545** (Sehling 5, p. 155):

<!-- doc 1922 -->
> Me schal ock nicht lenger singen, alse de berichtinge waret, wen de uthe is, schal ock de sank
> uphören. Unde denne also vort in den steden und dörperen schal me anfangen: O lam gades
> unschüldig dre mal, edder Christe, du lam gades.

One shall also not sing longer than the communion lasteth; when that is out, the singing also
shall cease. And then forthwith in the towns and villages one shall begin "O Lamb of God,
innocent," three times, or "Christ, thou Lamb of God."

**Schleswig-Holstein, *Kirchenordnung*, 1542** (Sehling 23, p. 91):

<!-- doc 1576 -->
> So hevet de Scholemeister vort an: Jhesus Christus, unser Heiland etc., Edder wat anders, dat
> dem gelick ys. Wen de berichtinge uthe ys, so höret ock up de Sanck.

Then the schoolmaster beginneth forthwith "Jesus Christ our Saviour," etc., or something else
that is like it. When the communion is out, the singing also ceaseth.

**Hamburg, *Kirchenordnung*, 1556** (Sehling 5, p. 553):

<!-- doc 1963 -->
> Wenn nu de communicanten gan tom altare schollen de gesänge vam sacramente gesungen werden:
> Jesus Christus etc., Godt sie gelavet etc. effte na gelegenheit der feste süss ein gude gesang,
> doch also, dat de organiste stedes mank her spele, und dat de chore gelickwoll alle verse
> singe. Up den festen, wen dar veele communicanten sin, unde ock sünst up den sondagen, schall
> men mehr singen dat agnus dei latine, underwilen ock düdesch, Christe du lamme gades etc. Wenn
> nu de communion geschehen, schall dat chor uphören to singen.

When now the communicants go to the altar, the songs of the sacrament shall be sung, "Jesus
Christ," etc., "God be praised," etc., or, according to the occasion of the feasts, else a good
song; yet so that the organist play always in between, and that the choir nevertheless sing all
the verses. On the feasts, when there are many communicants, and also otherwise on the Sundays,
one shall sing more: the Agnus Dei in Latin, at times also in German, "Christ, thou Lamb of
God," etc. When now the communion hath taken place, the choir shall cease singing.

In the Kurpfalz order the minister could stop the singing if the service ran too long.
**Kurpfalz, *Kirchenordnung*, 1556** (Sehling 14, p. 165):

<!-- doc 480 -->
> Es were dann, das von wegen der communicanten anzahl oder anderer dergleichen zufälligen
> ursachen der actus etwas zu lang sein wolte, so mag der minister mit dem gesang abzubrechen
> bevehlen.

Unless it were that, by reason of the number of communicants or other such chance causes, the
action would grow somewhat too long; then the minister may command the singing to be broken off.

### 14.4 Stanzas between the actions

In the earliest Low German Mass from Schleswig-Holstein the choir sang one stanza of "Jesus
Christus unser Heiland" after the consecration of the bread, the next during the distribution of
the bread, and then fell silent until the cup. **Schleswig-Holstein, *Deutsche Messe* [after
1526]** (Sehling 23, pp. 56–57):

<!-- doc 1576 -->
> Nu hevet dat cor an to syngende: Jhesus Christus, unse hylant. Eyn versch dar van. Dar na kert
> sick de prester myt dem licham Cristi thom volchke.

Now the choir beginneth to sing "Jesus Christ our Saviour," one verse thereof. Thereafter the
priest turneth himself with the body of Christ to the people.

<!-- doc 1576 -->
> Unde singet ßo lange, dat de licham Christi vordelet is. Dar na swicht dat chor stille. Unde de
> prester hevet vordan an, dat bloth Christi tho consecrerende.

And [the choir] singeth so long until the body of Christ is distributed. Thereafter the choir
keepeth still, and the priest beginneth further to consecrate the blood of Christ.

Bugenhagen's Hamburg order has the same pattern for bread and cup: the song stops when the
communicants have received the bread, and after the cup the rest of the hymn is sung, or more
is begun. **Hamburg, *Kirchenordnung*, 1529** (Sehling 5, p. 529):

<!-- doc 1960 -->
> De wile singet dat volk: Jesus Christus etc., edder: God si gelavet und gebenediet etc. Wen
> averst de communicanten sin togegaen, so schall de sank uphoren und de prester neme den kelk
> und drege den bevel Christi vordtan.

Meanwhile the people sing "Jesus Christ," etc., or "God be praised and blessed," etc. But when
the communicants have come forward, the singing shall cease, and the priest shall take the cup
and set forth the command of Christ further.

### 14.5 The Latin pieces and the German hymns beside them

Brandenburg began with the Latin *Discubuit Jesus* and added German hymns if there were many
communicants. One German hymn was to be sung after the communion in any case. **Brandenburg,
*Kirchenordnung*, 1540** (Sehling 3, p. 70):

<!-- doc 1746 -->
> Darauf sol angefangen werden das responsorium discubuit Jesus latinisch und ob der
> communicanten viel weren, das man damit nicht zureichen mocht, sol man dem volk deudsch
> anfahen zu singen, gott sei gelobet, oder Jesus Christus, unser heiland, welcher gesenge
> einer, ob auch gleich das discubuit zureichet, dennoch gleichwol nach der communion sol
> gesungen werden.

Thereupon the responsory *Discubuit Jesus* shall be begun in Latin; and if the communicants were
many, so that it would not reach, one shall begin to sing German to the people, "God be
praised," or "Jesus Christ our Saviour"; one of which songs, even though the *Discubuit* should
suffice, shall nevertheless be sung after the communion.

**Kurpfalz, provisional *Kirchenordnung*, 1546** (Sehling 14, p. 97):

<!-- doc 472 -->
> Under der communion singt das volck den gesang Jhesus Cristus, unser heilandt, oder Gott sei
> gelobet oder sonst ein cristlichen teutschen psalmen oder auch der chor das responsorium:
> Discubuit Jesus cum discipulis suis oder das teutsche pange lingua. Nach der communion singt
> der chor die agnus Dei.

During the communion the people sing the song "Jesus Christ our Saviour," or "God be praised,"
or else a Christian German psalm; or the choir also the responsory *Discubuit Jesus cum
discipulis suis*, or the German *Pange lingua*. After the communion the choir singeth the Agnus
Dei.

**Bremen, *Kirchenordnung*, 1534** (Sehling 7/2.2, p. 460):

<!-- doc 2217 -->
> Darna treden de Communicanten tho, Am ersten de menne, darna de frowen. Under middeler tidt
> singet de Scholemester: O sacrum convivium Unde Jhesus Christus unse Heilandt edder Sanctus
> unde Agnus Dei.

Thereafter the communicants come forward, first the men, thereafter the women. In the meantime
the schoolmaster singeth *O sacrum convivium* and "Jesus Christ our Saviour," or the Sanctus and
Agnus Dei.

At Heilbronn the Latin and German *Pange lingua* were sung in alternation with "Gott sei
gelobet". **Heilbronn, *Kirchenordnung*, 1530** (Sehling 17/1, pp. 285–286):

<!-- doc 770 -->
> Darumb singt man den Himnum Pange lingua, latin und deutsch, mitt dem […] lobgesanng: Gott
> sey gelobett unnd gebenedeiet etc.

Therefore one singeth the hymn *Pange lingua*, Latin and German, with the song of praise "God
be praised and blessed," etc.

The Heilbronn song order of 1543 turns to the German and Latin Te Deum at great communions.
**Heilbronn, *Ordnung des Kirchengesangs*, 1543** (Sehling 17/1, p. 323):

<!-- doc 782 -->
> Unter dem Nachtmahl Sanctus oder Agnus dei (lat.) oder Pange lingua (lat./deutsch) mit Orgel.
> An hohen Festen oder bei viel Communicanten Te deum laudamus deutsch und latein und Orgel (1
> Vers um den andern). Beschluß: Grates nunc omnes auf der Orgel.

During the Supper, the Sanctus or Agnus Dei (Latin), or *Pange lingua* (Latin and German), with
the organ. On high feasts, or with many communicants, the *Te Deum laudamus* in German and Latin
with the organ (one verse after the other). Conclusion: *Grates nunc omnes* on the organ.

### 14.6 Other hymns in the slot

Bugenhagen allowed "often" other hymns: "Nun freut euch", the baptism hymn, and German hymns of
the feasts. **Wolfenbüttel, *Kirchenordnung*, 1543** (Sehling 6/1, p. 57):

<!-- doc 1972 -->
> Dewyle singet dat volk: Jhesus Christus, unse heiland etc. Edder: Got sy gelavet und
> gebenediet etc. Edder den psalm: Confitebor düdesch etc. Men mach tho tyden und wol vaken ock
> andere ledere under der communio singen, also: Nu frouet ju etc. Item van der döpe etc. und
> gude ledere, psalme und hymnos düdesch van den festen.

Meanwhile the people sing "Jesus Christ our Saviour," etc., or "God be praised and blessed,"
etc., or the psalm *Confitebor* in German, etc. One may at times, and well often, sing also other
songs under the communion, as "Now rejoice," etc., item the one of baptism, etc., and good songs,
psalms and hymns in German of the feasts.

**Rostock, *Conformitas ceremoniarum*, c. 1560** (Sehling 5, p. 288):

<!-- doc 1936 -->
> drauf sol der organist schlahen und die kirche singen Jesus Christus unser heiland, und dazu,
> wen der communicanten viel ist, gott sei gelobet und helf gott, das mirs gelinge.

thereupon the organist shall play and the church sing "Jesus Christ our Saviour," and thereto,
when the communicants are many, "God be praised" and "Help, God, that I may succeed."

**Engerhafe, *Liturgie*, 1583** (Sehling 7/1, p. 681):

<!-- doc 2119 -->
> Sub communione vero sive canatur: Was kan unß kommen an für not, od. O Christ, wir danken
> deiner güt, od. Jesus Christus, unser heyland, od. Nun freuet euch, lieben christengemein, et
> id genus alia cantica, sive ludatur organis.

But during the communion let there be sung either "What need can come upon us," or "O Christ, we
thank thee for thy goodness," or "Jesus Christ our Saviour," or "Now rejoice, dear Christians
all," and other songs of that kind; or let the organ be played.

At Ortenburg "at times also the Passion" was sung, according as the communicants were many or
few. **Ortenburg, 1563** (Sehling 13, p. 532):

<!-- doc 457 -->
> Unter solcher austailung aber hat der chor gesungen Jesus Christus, unser Herr, oder Jesus
> Christus unser Hailand, zu zeiten auch den passion, nachdem der communicanten vil oder wenig
> gewesen sind.

But during such distribution the choir hath sung "Jesus Christ our Lord," or "Jesus Christ our
Saviour," at times also the Passion, according as the communicants have been many or few.

Limpurg changed the communion hymn by season: the Passion in Lent and "Christ lag in
Todesbanden" on Easter Day. **Limpurg, *Kirchenordnung*, 1610** (Sehling 16, p. 620):

<!-- doc 729 -->
> Under dern Communion singe der Schuelmeister eintweder des Hussen gesang: Jesus Christus,
> unser haillandt etc. Oder: Nun frewet Euch, Lieben Christen gemain. Item: Gott sei gelobet und
> gebenedeyet. In der Fasten den Passion, am Ostertag: Christ lag inn todtes banden.

During the communion let the schoolmaster sing either Hus's song, "Jesus Christ our Saviour,"
etc., or "Now rejoice, dear Christians all"; item "God be praised and blessed." In Lent the
Passion; on Easter Day, "Christ lay in the bands of death."

At Strasbourg Psalm 51 was sung at "great communions". **Strasbourg, *Gottesdienstordnung*,
1577** (Sehling 20/1, p. 516):

<!-- doc 1336 -->
> Under der communion singt man entweder: Jesus Christus, unser heyland, Johan Hussen lied, oder:
> Gott sey gelobet und gebenedeyet, oder wens grosse communion sind: O herre Gott, begnade mich,
> oder sonst ein gesang de tempore.

During the communion one singeth either "Jesus Christ our Saviour," John Hus's song, or "God be
praised and blessed," or, when there are great communions, "O Lord God, be gracious unto me,"
or else a song of the season.

In the village order of Veit Dietrich's Nürnberg *Agendbüchlein*, Sebald Heyden's "Als Jesus
Christus unser Herr" was the first choice, with the shorter hymns "if that be too long".
**Nürnberg, Veit Dietrich, *Agendbüchlein*, 1545** (Sehling 11, p. 502):

<!-- doc 297 -->
> Inmittels sol die kirch singen den gesang Als Jesus Christus, unser Herr, oder, wo solches zu
> lang - Gott sei gelobet oder Jesus Christus unser Heiland.

Meanwhile the church shall sing the song "When Jesus Christ our Lord," or, where that is too
long, "God be praised," or "Jesus Christ our Saviour."

The Kassel general synod of 1607, as Hesse turned Reformed, kept "Gott sei gelobet". Beside it
stood Lobwasser's Psalms 23, 103 and 111, "according to the occasion and number of the
communicants". **Hessen-Kassel, *Abschied der Kasseler Generalsynode*, 1607** (Sehling 9, p. 75):

<!-- doc 2287 -->
> und, da coena Domini, under wehrender communion der gesang: Gott sey gelobt undt gebenedeiet
> etc. oder sonstenn als den Lobwasser der 23., 103., 111. psalm nach gelegenheitt undt anzall
> der communicanten.

and when the Lord's Supper is held, during the communion the song "God be praised and blessed,"
etc., or else, as out of Lobwasser, the twenty-third, hundred and third, hundred and eleventh
psalm, according to the occasion and number of the communicants.

### 14.7 Choir, people and organ

Brenz wanted the choir in Latin and the church in German by turns, so that the communicants
were admonished "not only inwardly but outwardly by the understandable song". **Schwäbisch Hall,
*Kirchenordnung*, 1527** (Sehling 17/1, p. 51):

<!-- doc 755 -->
> Hie zwuschen sol der Cor latheinisch und die kirch teutsch umbeinander singen, auff das die
> entpfaher des Sacraments und andere umbstender nit allein inwendig, sonder außwendig durch das
> verstendtlich gesang irs thuns ermant werden.

Herebetween the choir shall sing in Latin and the church in German by turns, that the receivers
of the sacrament and others standing about may be admonished of their doing, not only inwardly,
but outwardly through the understandable song.

Pomerania limited the organ during the communion, forbade worldly tunes on it, and had choir and
people sing alternate verses so that the hymns would be learned by all. **Pomerania, *Agenda*,
1569** (Sehling 4, p. 439):

<!-- doc 1865 -->
> Under der communion singet men: Jesus Christus unser heiland etc., edder: Godt si gelavet
> etc., edder: O lam gades unschüldich etc., Christe du lam gades, item: Ick danke dem herren van
> ganzem herten etc. mit der note, de im düdischen sankboke steit, unde der geliken düdische
> senge, de sick up de communion rimen. Item, discubuit Iesus, item de latinischen agnus dei,
> choral, item o sacrum convivium etc. Wenn dise gesenge under der communion gesungen werden,
> schölen de organisten eren gesank mit der orgel deste körter maken, unde nene weltlike,
> lichtverdige gesenge slan. De pastor schal vorschaffen, dat de orgeln der maten modereret
> werden, dat men de düdischen psalme under der communion mit der gemeine ganz tom ende singe,
> unde dat de vörgesetteden gesenge ummeschichtich gesungen werden, dat dat chor unde dat volk
> einen vers umme den andern singe, up dat se alle to gelick den schölern unde der gemeine
> gebrücklick werden.

During the communion one singeth "Jesus Christ our Saviour," etc., or "God be praised," etc., or
"O Lamb of God, innocent," etc., "Christ, thou Lamb of God," item "I thank the Lord with all my
heart," etc., with the note that standeth in the German songbook, and the like German songs that
rhyme with the communion. Item *Discubuit Jesus*, item the Latin Agnus Dei, in plainsong, item
*O sacrum convivium*, etc. When these songs are sung during the communion, the organists shall
make their song with the organ the shorter, and play no worldly, light songs. The pastor shall
see to it that the organs be so moderated that the German psalms during the communion be sung
wholly to the end with the congregation, and that the aforesaid songs be sung by turns, the
choir and the people one verse after another, that they may all alike become familiar to the
scholars and the congregation.

Schönburg let the organ play during the communion only on high feasts. **Schönburg,
*Kirchenordnung*, 1542** (Sehling 2, p. 171):

<!-- doc 1235 -->
> Sub communione mag man abwechselsweise singen das teutsche santus etc., als Jesus Christus,
> zuweilen das lateinische sanctus oder agnus dei novi testamenti. Der organista soll sub
> communione nicht schlagen, es sei denn an hohen festen.

During the communion one may sing by turns the German Sanctus, etc., as "Jesus Christ," at times
the Latin Sanctus or Agnus Dei of the New Testament. The organist shall not play during the
communion, unless on high feasts.

### 14.8 How fixed the slot was

**Fixed core, open margin.** Every order opens the slot with Hus's hymn, "Gott sei gelobet", the
German Sanctus or Psalm 111. What changed from service to service was not the choice but the
quantity, measured by the number of communicants. The hymns added at the margin were festal
hymns on feasts, the Passion in Lent, Latin chants where there was a school, and psalms of
penitence or thanks.

---

## 15. The Agnus Dei, the thanksgiving, and the close

### 15.1 "Christe, du Lamm Gottes" after the communion

In Bugenhagen's orders, and in those that followed them, the German Agnus Dei "Christe, du
Lamm Gottes" was sung after all had communicated. It was sung three times, the third time
ending "gib uns deinen Frieden". It served as the people's thanksgiving, addressed to Christ in
heaven. **Hamburg, *Kirchenordnung*, 1529** (Sehling 5, p. 529):

<!-- doc 1960 -->
> Wen se averst alle communiceret hebben und sint up eren steden, so singen se und alle volk to
> Christo im hemele dat dudesche agnus dei dremal also: Christe, du lam gades, de du drechst de
> sunde der werldt, erbarm di unser; tom drudden: giff uns dinen frede. Amen.

But when they have all communicated and are in their places, they and all the people sing to
Christ in heaven the German Agnus Dei three times, thus: "Christ, thou Lamb of God, that bearest
the sin of the world, have mercy upon us"; the third time, "give us thy peace. Amen."

The Braunschweig order of 1528 has the same rubric (Sehling 6/1, p. 442). The Albertine order
lets any of the German communion hymns be closed with "Christe, du Lamm Gottes". **Saxony
(Albertine), *Kirchenordnung*, 1539**, variants A and B (Sehling 1, p. 275):

<!-- doc 30 -->
> so man der deutschen gesenge (als Jesus Christus unser heiland u. s. w., item, das deudsche
> sanctus, Esaia dem propheten das geschah, item den psalm ich danke dem herrn von ganzem herzen
> u. s. w.) eines oder mehr gesungen hat, mag man mit dem folgenden deutschen agnus dei
> beschliessen: [folgen die Noten zu Christe du lamb gottes, der du tregst die sünd der welt,
> erbarm dich unser. Verleih uns dein [fried].

when one or more of the German songs have been sung (as "Jesus Christ our Saviour," etc., item
the German Sanctus, "Isaiah the prophet, it befell," item the psalm "I thank the Lord with all my
heart," etc.), one may conclude with the German Agnus Dei following: [the notes follow to
"Christ, thou Lamb of God, that bearest the sin of the world, have mercy upon us. Grant us thy
peace."]

**Mecklenburg, *Kirchenordnung*, 1552** (Sehling 5, p. 199):

<!-- doc 1922 -->
> Unter der communion singe man Jesus Christus, unser heiland. Item, Gott sei gelobet, Agnus
> dei, Esaia, dem propheten. Und so der communicanten viel sind, singe man den CXI. psalm: Ich
> danke dem herrn von ganzem herzen. Wie er im deudschen gesang buch stehet. Desgleichen andere
> deudsche geistliche lieder. Und zum beschlus: Christe, du lam gottes.

During the communion let "Jesus Christ our Saviour" be sung; item "God be praised," the Agnus
Dei, "Isaiah the prophet." And when the communicants are many, let the hundred and eleventh
psalm be sung, "I thank the Lord with all my heart," as it standeth in the German songbook;
likewise other German spiritual songs. And at the close, "Christ, thou Lamb of God."

At Suhl the boys sang songs of the season or of the sacrament during the communion, "and it is
commonly concluded with the song *Christe du Lamm Gottes*". **Suhl, *Ordnung des predigamts*,
1562** (Sehling 2, p. 351):

<!-- doc 1250 -->
> Communio sub quam canunt pueri de tempore aut sacramento, und wird gemeiniglich mit dem
> gesang: Christe du lamb gottes beschlossen.

The communion, during which the boys sing [songs] of the season or of the sacrament; and it is
commonly concluded with the song "Christ, thou Lamb of God."

Neuenrade has "Agnus Dei Düdsch" as the communicants go to the altar and "Gott sei gelobet"
after. **Neuenrade, *Kirchenordnung*, 1564** (Sehling 22, p. 519):

<!-- doc 1544 -->
> Als dan singet man Agnus Dei Düdsch, und gan de Communicanten thom Altar. Na dem Agnus Dei
> singet man: God sy gelovet, etc.

Then one singeth the Agnus Dei in German, and the communicants go to the altar. After the Agnus
Dei one singeth "God be praised," etc.

### 15.2 "Gott sei gelobet" as the thanksgiving

Luther's *Formula missae* already wanted "Gott sei gelobet" sung after the communion. He
dropped the stanza about receiving the sacrament at the hour of death "from the hands of the
consecrated priest". **Wittenberg, Luther, *Formula missae*, 1523** (Sehling 1, p. 9):

<!-- doc 2 -->
> Interim placet illam cantari post communionem: ʻGott sei gelobet und gebenedeiet, der uns
> selber hat gespeiset etct.ʼ Omissa ista particula: ʻUnd das heilige sacramente, an unserm
> letzten ende, aus des geweieten priesters hendeʼ.

Meanwhile it pleaseth [me] that this be sung after the communion: "God be praised and blessed,
who himself hath fed us," etc.; that little part being left out, "And the holy sacrament at our
last end, out of the consecrated priest's hands."

The Albertine order ends the service with it: "and therewith go home" (Sehling 1, p. 275):

<!-- doc 30 -->
> So mag man das volk singen lassen den gesang: gott sei gelobet und gebenedeiet und damit heim
> gehen.

Then the people may be let sing the song "God be praised and blessed," and therewith go home.

**Rothenberg, *Vereinigung*, 1618** (Sehling 13, p. 550):

<!-- doc 461 -->
> Unter derselben sing man psalm und gesäng, so darzu gehören. Nach vollendter communion sing
> man zur danksagung für dieselbe: Gott sei gelobet und gebenedeiet etc.

During the same let psalms and songs be sung that belong thereto. After the communion is ended
let "God be praised and blessed," etc. be sung for thanksgiving for the same.

### 15.3 The closing hymn

The last hymn of the service was one of a small group: "Gott sei gelobet", "Dank sagen wir
alle", "Sei Lob und Ehr mit hohem Preis" (the last stanza of "Es ist das Heil"), "Erhalt uns"
with "Verleih uns Frieden", *Da pacem*, "Es woll uns Gott genädig sein", or a festal hymn.
Tecklenburg closes with thanksgiving. **Tecklenburg, *Kirchenordnung*, 1543** (Sehling 22, p. 244):

<!-- doc 1505 -->
> Endtlich sal dat volck den heren loven und dancken em van ganßen herten mit dem gesange: Danck
> seggen wy alle etc., Mit fride und [frouwden of dergelichen duischer dancksegginge].

At the last the people shall praise the Lord and thank him with all their heart with the song
"Thanks say we all," etc., "In peace and [joy," or the like German thanksgiving].

Northeim closes with the prayer for peace, because "for temporal peace we are bound to pray at
all times". **Northeim, *Kirchenordnung*, 1539** (Sehling 6/2, p. 926):

<!-- doc 2047 -->
> Wir sehen auch fur gut an, das zu endlichem beschlus der gesang Da pacem, Domine in
> lateinischer oder deudscher sprache gesungen werde durch die knaben und schulmeister. Denn umb
> zeitlichen frid sind wir zu bitten allezeit schüldig.

We also think good that for the final close the song *Da pacem, Domine* be sung in the Latin or
German tongue by the boys and schoolmaster. For we are bound at all times to pray for temporal
peace.

In Mecklenburg priest, communicants and congregation knelt for "Erhalt uns" and "Verleih uns
Frieden". **Mecklenburg, *Ordeninge der misse*, 1545** (Sehling 5, p. 155):

<!-- doc 1922 -->
> Unde denne schal sick de prester vor dat altar up de knee setten. De ganze gemene schal ock so
> don, unde heven an: Erholt uns here bi dinem worde, de dre versche, unde denn: Vorlene uns
> frede gnedichlick, here godt etc.

And then the priest shall set himself upon his knees before the altar. The whole congregation
shall also do so, and begin "Keep us, Lord, by thy word," the three verses, and then "Grant us
peace graciously, Lord God," etc.

Buxtehude closed with *Da pacem* or "Verleih uns Frieden", sung without the organ, or "a psalm
fitting the present need", such as "Mitten wir im Leben sind". **Buxtehude, *Kirchenordnung*,
1552** (Sehling 7/1, p. 76):

<!-- doc 2082 -->
> To beschlute schall dat de chorr allene ahne de orgel singen: Da pacem, edder dudesch Vorlene
> uns frede, edder sunst einen psalm, de na ahnliggende nodt darto bequeme, alse Midden wy im
> levent sint, edder andere dem gelick.

At the close the choir alone, without the organ, shall sing *Da pacem*, or in German "Grant us
peace," or else a psalm fitting thereto according to the present need, as "In the midst of life
we are," or others like it.

**Hamburg, *Kirchenordnung*, 1556** (Sehling 5, p. 553):

<!-- doc 1963 -->
> Tom lesten schall dat chor Da pacem etc. singen effte düdesch vorlene uns frede etc. up
> sünderlicke feste averst einen andern gesank, de sick darbi wil schicken.

At the last the choir shall sing *Da pacem*, etc., or in German "Grant us peace," etc.; but on
special feasts another song that will fit thereto.

Hoya gives the festal closing hymns. **Hoya, *Kirchenordnung*, 1581** (Sehling 6/2, p. 1150):

<!-- doc 2065 -->
> Darnach singet man Es wol uns Gott genedig sein etc. An den festen aber singet man, was die
> fest mit sich bringen, als auf Weynachten Gelobet seystu, Jhesu Christ, sampt den folgenden
> versen, auf Ostern das kurze Jhesus Christus, unser heyland, der den tod uberwand, auf
> Pfingsten Kom, heiliger Geist, Herre Gott etc.

Thereafter one singeth "May God be gracious unto us," etc. But on the feasts one singeth what
the feasts bring with them, as at Christmas "Praised be thou, Jesu Christ," with the verses
following; at Easter the short "Jesus Christ our Saviour, who overcame death"; at Pentecost
"Come, Holy Ghost, Lord God," etc.

**Pomerania, *Agenda*, 1569** (Sehling 4, p. 439):

<!-- doc 1865 -->
> Tom beslute wert gesungen: Si loff unde ehre etc., edder: Erholt uns herre etc., Vorlene uns
> frede etc., O godt wi danken diner güde etc. unde der geliken.

At the close is sung "Praise and honour," etc., or "Keep us, Lord," etc., "Grant us peace," etc.,
"O God, we thank thee for thy goodness," etc., and the like.

**Hildesheim (Stift), *Kirchenordnung für Steuerwald und Peine*, 1561** (Sehling 7/2.1, p. 783):

<!-- doc 2129 -->
> wan das gescheen, singet der opferman mit dem volke zum lesten aus: Sei lob und ehr mit hohem
> preis.

when that is done, the sexton with the people singeth at the last, to the end: "Praise and honour
with high price."

In the Braunschweig villages two closing hymns alternated, one holy day after the other
(Sehling 6/1, p. 473):

<!-- doc 1988 -->
> Und zum besluß schal dan der opferman mit dem volk singen ein fiertag umb den andern: Es wolt
> unß Godt genedig sein und: Erhalt uns, Her, bei deinem wort.

And at the close the sexton shall sing with the people, one holy day after the other, "May God
be gracious unto us" and "Keep us, Lord, by thy word."

### 15.4 The closing hymn covers the priest's devesting

In the Hildesheim city order the closing hymn was sung while the celebrant took off his vestment
and knelt again at the altar to give thanks privately. **Hildesheim (city), *Kirchenordnung*,
1544** (Sehling 7/2.1, p. 855):

<!-- doc 2136 -->
> So hevet de scholmester an einen düdeschen, korten psalm, edder wat öhme gefellich unde
> darmede ein ende etc. Dewile överst de sank waret, tüt sick de prediger ut unde lecht dat
> missgewand tohope, kneet wedder nedder vor dem altare unde danket Godde hemehck vor sick
> sülvest.

Then the schoolmaster beginneth a German short psalm, or what pleaseth him, and therewith an end,
etc. But while the song lasteth, the preacher undresseth himself and layeth the Mass vestment
together, kneeleth down again before the altar, and thanketh God secretly for himself.

### 15.5 A custom found and left alone

A Henneberg pastor found "Verleih uns Frieden" sung at the very end in his parish. He left it,
since it could not be faulted. **Wasungen (Henneberg), pastor's report, 1566** (Sehling 2, p. 356):

<!-- doc 1250 -->
> So nu die communion geschehen, beschleust man mit der collecta und dem segen. Verleihe uns
> friden mit der anhengten collecta hab ich hie also gefunden, das mans gar am ent gesungen und
> damit beschlossen, welches weil es nit zu strafen, hab ichs auch nit endern wollen.

When now the communion is done, one concludeth with the collect and the blessing. "Grant us
peace," with the collect appended, I have found here thus: that it was sung at the very end and
therewith concluded; which, since it is not to be blamed, I also would not change.

### 15.6 How fixed the slots were

**Fixed, with a handful of choices and festal exchange.** The post-communion Agnus was "Christe,
du Lamm Gottes" or "O Lamm Gottes". The thanksgiving was "Gott sei gelobet", "Dank sagen wir
alle" or "Sei Lob und Ehr". The close was the prayer for peace and the word ("Verleih uns
Frieden", *Da pacem*, "Erhalt uns"), or Psalm 67. At the high feasts the festal hymn of the day
took the closing slot.

---

## 16. Vespers, matins, the catechism and the weekday services

### 16.1 Office hymns: only of the season, and only if pure

The Latin office hymn (*hymnus*) of matins and vespers stayed where there was a school. The
rule was that it be "of the season" and "pure". Hymns to the saints were dropped, and single
stanzas that invoked the saints or the cross were cut. **Transylvanian Saxons,
*Kirchenordnung*, 1547** (Sehling 24, p. 224, Latin; p. 245, German):

<!-- doc 1669 -->
> Hymnos praeterquam de tempore nullos admittimus.

We admit no hymns save those of the season.

<!-- doc 1669 -->
> Die hymnos helt man auch nach der zeit und keine andern.

The hymns also are kept according to the season, and no others.

Schleswig-Holstein warns against hymns that speak of the merit and invocation of the saints.
It names the *O crux ave* stanza of *Vexilla regis*. **Schleswig-Holstein,
*Kirchenordnung*, 1542** (Sehling 23, p. 143):

<!-- doc 1576 -->
> So erfordert ock de Godtsalicheit unde Christlike Gelove, Dat wy uns vor de Hymnos waren
> scholen, Darynne van vordenst unde Anropinge der Hilligen geschreven steit, den wol wolde
> hernamals ein Hölten Crütze upheven unde den godtlosen sang singen: O Crux, Ave spes unica
> etc.?

So also godliness and the Christian faith require that we beware of the hymns wherein is
written of the merit and invocation of the saints. For who would hereafter lift up a wooden
cross and sing the godless song, *O Crux, ave spes unica*, etc.?

The Ansbach chapter order of 1533 made the same cut. **Brandenburg-Ansbach, *Ordnung singens
und lesens bei den Stiften*, 1533** (Sehling 11, p. 316):

<!-- doc 276 -->
> dominica in passione Domini: In hymno Vexilla Regis soll der vers O crux, ave spes ausgelassen
> werden.

On Passion Sunday: in the hymn *Vexilla Regis* the verse *O crux, ave spes* shall be left out.

The Heilbronn song order of 1543 cuts the Marian stanza of the Candlemas hymn. **Heilbronn,
*Ordnung des Kirchengesangs*, 1543** (Sehling 17/1, p. 322):

<!-- doc 782 -->
> Lichtmeß: Hymnus: Quod chorus vatum (vor Tu libens votis, ist auszulassen).

Candlemas: hymn *Quod chorus vatum* (before *Tu libens votis*, which is to be left out).

At Hof the hymns of John the Baptist and the apostles were sung in the text "corrected in
Lossius". **Hof, *Ordo ecclesiasticus*, 1592** (Sehling 11, p. 423):

<!-- doc 294 -->
> H: Ut queant laxis (correctus in Lossio].

Hymn: *Ut queant laxis* (corrected in Lossius).

At Regensburg the vesper hymn of the season was sung "if it be not godless". **Regensburg,
*Kirchenordnung* of Justus Jonas, 1553** (Sehling 13, p. 419):

<!-- doc 440 -->
> und alspald darauf bede chör den hymnum de tempore, so er nit gotlos ist.

and straightway thereupon both choirs [sing] the hymn of the season, if it be not godless.

### 16.2 One hymn for a whole season

The office hymn changed by season, not by day. Hof kept the German Te Deum at vespers from
Michaelmas to Advent. **Hof, *Ordo ecclesiasticus*, 1592** (Sehling 11, p. 447):

<!-- doc 294 -->
> Vesperi. Hymnus: Herr Gott, dich loben wir. NB. Hymnus iste retinetur usque ad Adventum
> Christi.

At vespers. Hymn: "Lord God, we praise thee." N.B.: This hymn is kept until the Advent of Christ.

Heilbronn kept *O lux beata Trinitas* from Trinity to Advent. **Heilbronn, *Ordnung des
Kirchengesangs*, 1543** (Sehling 17/1, p. 321):

<!-- doc 782 -->
> Trinitatis bis Advent: Zu gewöhnlichen christlichen Antiphonen Hymnus: O lux beata Trinitas zu
> singen.

Trinity until Advent: with the customary Christian antiphons the hymn *O lux beata Trinitas* is
to be sung.

The Henneberg afternoon service opened with a seasonal hymn, played on the organ, then sung in
figured music, and then followed by the German Magnificat of the whole congregation.
**Henneberg, *Kirchenordnung*, 1582** (Sehling 2, p. 310):

<!-- doc 1247 -->
> und dann auf die hohe fest, als weinachten, das deutsche grates nunc omnes, und, Gelobet
> seistu Jesu Christ, bis ohngefehrlich umb purificationis, von dem sontage nach purificationis
> an, das deutsche Nunc dimittis, bis auf die fasten; durch die fasten bis auf ostern Christe der
> du bist tag und licht; von ostern bis zum auffarts tage Also heilig ist der tag, oder Christ
> ist erstanden, oder Christ lag in todes banden; vom auffarts tage an bis uf pfingsten, Christ
> fuhr gen himel; von pfingsten an, vom heiligen geist, bis aufs advent; im advent bis auf
> weinachten, Nu kom der heiden heiland, alle sontage nach mittage auf der orgel, wo die
> verhanden, geschlagen und darauf eben dasselbe als balden figuriret, als dann das magnificat
> durch den cantor und chor mit der ganzen gemeine gesungen werden.

and then on the high feasts, as Christmas, the German *Grates nunc omnes* and "Praised be thou,
Jesu Christ," until about the Purification; from the Sunday after the Purification, the German
*Nunc dimittis*, until Lent; through Lent until Easter, "Christ, who art the day and light";
from Easter until Ascension Day, "So holy is the day," or "Christ is arisen," or "Christ lay in
the bands of death"; from Ascension Day until Pentecost, "Christ went up to heaven"; from
Pentecost, [a song] of the Holy Ghost until Advent; in Advent until Christmas, "Now come, the
Saviour of the heathen": all Sundays in the afternoon played upon the organ, where there is one,
and thereupon the same straightway sung in figured music; then the Magnificat [shall be] sung by
the cantor and choir with the whole congregation.

In the Pomeranian *Agenda* vespers opened, kneeling, with *Veni sancte Spiritus* or a Latin
song of the season "pro ingressu vel egressu". The schoolmaster chose it with the pastor.
**Pomerania, *Agenda*, 1569** (Sehling 4, p. 435):

<!-- doc 1865 -->
> Erstlick singet men flexis genibus: Veni sancte spiritus; edder den ersten vers: Veni creator
> spiritus; edder Adesto deus unus etc., edder wat süs pro tempore evenkömlick is: Alse im
> advent: Veni domine visitare nos in pace etc.; umme winachten: Puer natus in Bethlehem, In
> dulci iubilo, Resonet in laudibus, Nunc angelorum gloria; umme paschen: Surrexit Christus
> hodie; umme pingsten: Spiritus sancti gratia, Veni maxime spiritus etc. Alse sölckes de
> scholmeister edder cantor, mit rat des pastorn, wert vor gut anseen, wat pro ingressu vel
> egressu deenstlick is.

First one singeth on bended knees *Veni sancte Spiritus*, or the first verse *Veni creator
Spiritus*, or *Adesto Deus unus*, etc., or what else is fitting for the season: as in Advent,
*Veni Domine visitare nos in pace*, etc.; about Christmas, *Puer natus in Bethlehem*, *In dulci
jubilo*, *Resonet in laudibus*, *Nunc angelorum gloria*; about Easter, *Surrexit Christus
hodie*; about Pentecost, *Spiritus sancti gratia*, *Veni maxime Spiritus*, etc.: as the
schoolmaster or cantor, with the counsel of the pastor, shall think good what is serviceable
for the entrance or the going out.

### 16.3 Latin for the school, German for the people

Bugenhagen kept the Latin office for the school, and moved the German hymns to the times when
the laity were present. **Hamburg, *Kirchenordnung*, 1529** (Sehling 5, p. 524):

<!-- doc 1960 -->
> Sulcke latinsche senge werden den leien ohre dudesche senge nicht vorhinderen, wente se werden
> gesungen werden, wen de leien in der karcken mit prediken tohorende nicht to schaffende
> hebben. Se werden doch sus genoch dudesch to singende krigen. Wente vor allen sermonen und na
> allen sermonen scollen [se dudesch singen].

Such Latin songs will not hinder the laity in their German songs, for they will be sung when
the laity have nothing to do in the church with hearing preaching. They will get enough to sing
in German otherwise. For before all sermons and after all sermons they shall [sing in German].

**Braunschweig, *Kirchenordnung*, 1528** (Sehling 6/1, p. 442):

<!-- doc 1983 -->
> Düdesche hymnos in der Advente, imme Wynachten bet up purificationis, up Paschen bet up
> Pynxten, imme Pynxten, van den festen edder sus andere hymnos mach me wol singen des
> hilgendages in der vesper, wen de leyen dar [synt].

German hymns in Advent, at Christmas until the Purification, at Easter until Pentecost, at
Pentecost, of the feasts, or else other hymns, may well be sung on the holy day at vespers,
when the laity are there.

**Hildesheim (city), *Kirchenordnung*, 1544** (Sehling 7/2.1, p. 856):

<!-- doc 2136 -->
> To den andern predigen ys ydt genoch, dat wy einen psalm vor unde einen psalm edder ledt na
> düdesch singen. Wenn överst unse scholkinder allene to der kercken komen, to singen unde to
> lesen, wat vorordent ys, so schal se nemandes vorhindern, latinisch to lesen unde to singen.

At the other sermons it is enough that we sing a psalm before and a psalm or song after in
German. But when our school children come alone to the church, to sing and to read what is
ordained, no one shall hinder them from reading and singing in Latin.

### 16.4 The German Te Deum sung verse by verse

The German canticles — the Te Deum, Magnificat, Benedictus and Nunc dimittis — were the
congregational pieces of the offices. The Te Deum was sung by alternating halves, the choir one
verse and the people the next. At Wittenberg a school usher stood in a stall in the middle of
the church to lead the people "until the people grow used to it". **Wittenberg,
*Kirchenordnung*, 1533** (Sehling 1, p. 705):

<!-- doc 148 -->
> und ein schulgesell soll in dem schulerstul mitten in der kirchen mit dem volk auf alle halbe
> vers, wie es gemacht ist, antworten. Er mag auch zum ersten etliche knaben in den stul zu hulf
> nehmen, bis das volk sich gewent, solch te deum mitzusingen.

and a school usher shall, in the scholars' stall in the midst of the church, answer every half
verse with the people, as it is made. He may also at first take some boys into the stall to
help, until the people grow used to singing along such Te Deum.

**Northeim, *Kirchenordnung*, 1539** (Sehling 6/2, p. 924):

<!-- doc 2047 -->
> Und wiewol man die latinische sprache aus der kirchen gar nicht komen lassen sol, so ist aber
> doch fur gut angesehen, das das Te Deum, damit auch in der kirchen die gemeine nicht
> vergeblich sey, auf die Sontage und hei[…]ligen tage deudsch gesungen werde, doch also, das
> der chor einen vers, die ganze kirche den andern singe.

And although the Latin tongue shall by no means be let go out of the church, yet it is thought
good that the Te Deum be sung in German on the Sundays and holy days, that the congregation too
be not in the church in vain; yet so that the choir sing one verse, the whole church the other.

At Calenberg the sexton came out of the choir to lead the congregation's half. **Calenberg-
Göttingen, *Kirchenordnung*, 1542** (Sehling 6/2, p. 792):

<!-- doc 2036 -->
> Nach dem responsorio das Te Deum laudamus deutsch, also das der chor einen vers, die gemein
> haussen den anderen singe. Sonderlich aber mus der opferman aus dem chor hie tretten und die
> gemein, das sie fein ordentlich singe, regiren.

After the responsory the *Te Deum laudamus* in German, so that the choir sing one verse, the
congregation outside the other. But especially here the sexton must step out of the choir and
govern the congregation, that it sing finely in order.

### 16.5 The evening *Salve* replaced

The late-medieval evening devotion of the *Salve Regina* was abolished, or turned to Christ.
**Plauen, *Ordnung der Ceremonien*, 1529** (Sehling 2, p. 111):

<!-- doc 1227 -->
> Ufn abend umb 5 ader 6 hor singen die knaben alle tage das „Salve Jesu Christe“ mit dem „Da
> pacem“ latinisch und einer deutschen collecta.

In the evening at five or six o'clock the boys sing every day the *Salve Jesu Christe* with the
*Da pacem* in Latin and a German collect.

At Heilbronn a German hymn took the place of the *Salve* as an evening blessing. **Heilbronn,
draft *Gottesdienstordnung*, 1532** (Sehling 17/1, p. 302):

<!-- doc 778 -->
> Zu nacht umb salve zeytt: Das an statt des vorigen salve zu einem schlaff segen der
> schulmaister mit seinen knaben ain theutsch loblich gsang als die letany oder das Mitten wir im
> leben seind oder Da pacem domine und dergleichen singe und mit einer colect beschlossen.

At night, at *Salve* time: that in the stead of the former *Salve*, for a blessing before
sleep, the schoolmaster with his boys sing a German song of praise, as the litany, or "In the
midst of life we are," or *Da pacem Domine*, and the like, and conclude with a collect.

The Hohenlohe order of 1553 abolished the *Salve Regina* outright, "because it is flat against
God's word and the honour of Christ" (Sehling 15, p. 74):

<!-- doc 539 -->
> Vom Salve Das Salve regina celi etc., so bißher gesungen worden, dieweyl es Gottes wort und
> der ehr Christi stracks zuwider, soll aller cüng abgetonn.

Of the *Salve*. The *Salve regina coeli*, etc., which hath hitherto been sung, because it is
flat against God's word and the honour of Christ, shall be wholly done away.

In the Kraichgau order of Neckarbischofsheim it stayed, "turned upon Christ and put into
German". **Neckarbischofsheim, *Kirchenordnung*, 1560** (Sehling 16, p. 672):

<!-- doc 742 -->
> darauf singt der Schulmaister das magnificat teusch Luc. 1. Darauf folgt das Salve Regina
> coeli, uf Christum gezogen und verteuscht.

thereupon the schoolmaster singeth the Magnificat in German, Luke 1. Thereupon followeth the
*Salve Regina coeli*, turned upon Christ and put into German.

### 16.6 The catechism service: the hymn of the chief part

The catechism service chose its hymn by the chief part being taught. This is the clearest
case in the corpus of a hymn chosen by its doctrine, and it is nearly universal:

| Chief part | Hymn |
|---|---|
| Ten Commandments | "Dies sind die heilgen zehn Gebot"; "Mensch, willst du leben seliglich" |
| Creed | "Wir glauben all"; "Ich glaub an Gott" |
| Lord's Prayer | "Vater unser im Himmelreich" |
| Baptism | "Christ unser Herr zum Jordan kam" |
| Lord's Supper | "Jesus Christus unser Heiland"; "Gott sei gelobet" |
| Keys / Confession | "Aus tiefer Not"; "Erbarm dich mein"; "So wahr ich leb" |

**Lippe, *Kirchenordnung*, 1571** (Sehling 21, p. 386):

<!-- doc 1462 -->
> Darauff singe die Kirche auch einen Christlichen deutschen Psalm, dem Artickel des Catechismi,
> so deßmals Tractirt, gemeß, Als Bey der Erklerung des Decalogi: Die Zehen Gebott, Item:
> Mensch, wiltu leben seeliglich etc., Des Symboli: Den Glauben und andere darzu dienliche
> Psalm, Des Vater unsers: Vater unser, der du bist im Himmel, leret uns Jhesus Christ; Item:
> Vater unser im Himelreich, Der Heiligen Tauffe: Durch Adams fall Und: Christ, unser Herr, zum
> Jordan kam etc., Des Hochwirdigen Sacraments des Altars: Was kan uns kommen an für not, Item:
> Jhesus Christus, unser Heilandt, Damit die Gesenge, darinnen die Heilige Göttliche schrifft
> mit schönen, runden Worten zusammengefasset, den Ungelerten und Jungen Leuten bekant und
> gemein werden.

Thereupon let the church also sing a Christian German psalm agreeable to the article of the
catechism then treated: as at the exposition of the Decalogue, "The Ten Commandments," item
"Man, wilt thou live blessedly," etc.; of the creed, "The Creed" and other psalms serving
thereto; of the Our Father, "Our Father, who art in heaven, as Jesus Christ teacheth us," item
"Our Father in the kingdom of heaven"; of holy baptism, "Through Adam's fall," and "Christ our
Lord to Jordan came," etc.; of the most worthy sacrament of the altar, "What need can come upon
us," item "Jesus Christ our Saviour": that the songs, wherein the holy divine Scripture is
summed up in fair round words, may become known and common to the unlearned and young folk.

Grubenhagen kept the same hymn for as long as the one chief part was being taught. **Grubenhagen,
*Kirchenordnung*, 1581** (Sehling 6/2, p. 1046):

<!-- doc 2058 -->
> Hierbey kan man auch allezeit etwas singen, das sich auf das stück des catechismi reimet,
> welchs erkleret worden, als, wenn man die zehen gebot ausleget und solang man damit umbgehet,
> kan man singen: Diss sind die heiligen zehen gebot etc., oder: Mensch, wiltu leben seliglich
> etc., und also fortan mit den andern, damit das junge volk die christlichen, geistreichen
> gesenge, die ihnen oft eine gute auslegung und herrlich liecht geben, auch im gedechtnis und
> herzen tiefer haften, mögen fassen.

Herewith one can also always sing something that rhymeth with the part of the catechism that
hath been expounded: as when the Ten Commandments are expounded, and as long as one is busied
therewith, one can sing "These are the holy ten commandments," etc., or "Man, wilt thou live
blessedly," etc.; and so forth with the others; that the young folk may grasp the Christian,
spiritual songs, which often give them a good exposition and glorious light, and that they may
cleave the deeper in memory and heart.

A Henneberg pastor did the same. **Queienfeld (Henneberg), pastor's report, 1566** (Sehling 2, pp. 344–345):

<!-- doc 1249 -->
> Singen erstlichen im anfang die zehen gepot, so lang man leret von den zehen gepoten und
> darnach von den dreien heubtartikel des glaubens, so lang man auch […] davon predigt, und also
> fortan bis zu ende des catechismi.

[We] sing first at the beginning the Ten Commandments, as long as the Ten Commandments are
taught; and thereafter [the hymn] of the three chief articles of the creed, as long as that also
is preached; and so forth to the end of the catechism.

In the Hoya villages the catechism service opened with Speratus's "Nun lasst uns Christen
fröhlich sein", and then took the hymn of each chief part. **Hoya, *Kirchenordnung*, 1581**
(Sehling 6/2, p. 1150):

<!-- doc 2065 -->
> anfahen, einen psalm zu singen von dem catechismo, welcher in dem psalmbüchlein gefunden wird
> und heist Nu last uns Christen frölich sein etc. Darnach, in der verhandlung des decalogi,
> singet man Diß sind die heiligen zehen gebot. In der tractation des glaubens singet man Wir
> gleuben. Uber dem Vater unser singet man Vater unser im himelreich. Uber der lehr von der taufe
> singet man Christ, unser Herr, zum Jordan kam; in der verhandlung des nachtmals Jhesus
> Christus, unser heyland; auch zu zeiten andere feine lutherische psalmen, auf das die leute
> einen psalm nach dem andern lernen sin[gen].

[they shall] begin to sing a psalm of the catechism, which is found in the psalm book and is
called "Now let us Christians be joyful," etc. Thereafter, in the treating of the Decalogue, one
singeth "These are the holy ten commandments"; in the treating of the creed, "We believe"; over
the Our Father, "Our Father in the kingdom of heaven"; over the teaching of baptism, "Christ our
Lord to Jordan came"; in the treating of the Supper, "Jesus Christ our Saviour"; and at times
also other fine Lutheran psalms, that the people may learn to sing one psalm after another.

Hohenlohe opened the catechism "with a song of that chief part which the pastor has in hand to
treat" (Sehling 15, p. 654):

<!-- doc 628 -->
> Es soll auch der catechismus mit einem gesang angefangen werden von demjenigen hauptstuck, so
> der pfarrherr zu tractieren fürhanden.

The catechism also shall be begun with a song of that chief part which the pastor hath in hand
to treat.

The Kurland order taught the Latvian peasants the catechism hymns first, one before and one
after, "until the un-German people can learn and profit more". **Kurland, *Kirchenordnung*,
1570** (Sehling 5, p. 91):

<!-- doc 1907 -->
> Es sollen aber für allen andern psalmen sich die undeutschen pfarherren der ordnung des
> catechismi befleissigen und den leuten singen leren. 1. Die zehen gebot, Dis sind die heiligen
> zehen gebot. 2. Den glauben, Wir gleuben all einen gott. 3. Das vater unser, Vater unser im
> himmelreich. 4. Die taufe, Christ, unser herr, zum Jordan kam. 5. Das sacrament des altars,
> Jesus Christus, unser heiland. Gott sei gelobet. 6. Das gloria. Allein gott in der höhe sei
> ehr. Dis sollen sie ersten nacheinander, das eine stücke für, das ander nach, singen leren, und
> in den gebrauch bringen, bis das undeutsch v[olk mehr lernen und proficirn mag].

But the pastors of the un-German [the Latvians] shall, before all other psalms, apply themselves
to the order of the catechism and teach the people to sing: 1. The Ten Commandments, "These are
the holy ten commandments." 2. The creed, "We all believe in one God." 3. The Our Father, "Our
Father in the kingdom of heaven." 4. Baptism, "Christ our Lord to Jordan came." 5. The sacrament
of the altar, "Jesus Christ our Saviour," "God be praised." 6. The Gloria, "To God alone on high
be glory." These they shall first teach them to sing one after another, the one piece before,
the other after, and bring them into use, until the un-German people may learn and profit more.

Wertheim calls "Nun freut euch" a good paraphrase of the whole creed. **Wertheim,
*Kirchenordnung*, c. 1555** (Sehling 11, p. 716):

<!-- doc 323 -->
> Das auch der catechismus im schwang gehe, soll man für der predigt singen die zehen gebot,
> nemblich in schöner paraphrasi darüber. […] Auch so tut das lied: Nun freut euch lieben
> Christen gemein genugsam verlesung von allen artikeln des glaubens und ist auf den glauben ein
> gut paraphrasis.

That the catechism also may be in practice, the Ten Commandments shall be sung before the
sermon, namely in the fair paraphrase thereof. […] Also the song "Now rejoice, dear Christians
all" doeth sufficient rehearsal of all the articles of faith, and is a good paraphrase upon the
creed.

### 16.7 Weekday services: reusing the Sunday hymn

At Hof, the Wednesday service repeated the hymn of the Sunday before. On Friday the German hymn
of the Sunday vespers was sung again. **Hof, *Ordo ecclesiasticus*, 1592** (Sehling 11, p. 429):

<!-- doc 294 -->
> II. Die Mercurii per duos choros plerumque repeti[…]tur cantilena diei dominici vel festi
> pracedentis. Die Veneris hymnus germanicus ad vespertinas preces praecedentis dominicae vel
> festi cantatur.

II. On Wednesday the song of the preceding Sunday or feast is for the most part repeated by two
choirs. On Friday the German hymn of the evening prayers of the preceding Sunday or feast is
sung.

Regensburg sang a German psalm on weekdays "for the people's sake, that the people may learn the
same and in time sing along". **Regensburg, *Kirchenordnung* of Hieronymus Noppus, 1543**
(Sehling 13, p. 408):

<!-- doc 436 -->
> Das alda erstlich gesungen werd ein psalm oder sünst ein gesang zu teutsch, umbs volks
> willen, das das volk dieselben lerne und mit der zeit mitsingen müge, darzu sie den sollen in
> der predigt zuweilen vermanet werden.

That there first be sung a psalm or else a song in German, for the people's sake, that the
people may learn the same and in time may sing along; whereto they shall at times be exhorted in
the sermon.

In wartime Neuenstein held a daily prayer service at noon. After the prayer it sang one of seven
psalm-hymns of trust and defence, in fixed order, "one each day, and no other". **Neuenstein,
*Befehle wegen des Gebetsgottesdienstes*, 1588–1594** (Sehling 15, p. 540):

<!-- doc 604 -->
> volgents umgewechselter weiß alweg nach dem gebett diser psalmen einen. als nembhchen: 1. Ein
> veste burg ist unser Gott etc., 2. Gib fridt zu unser zeit etc., 3. Erhalt unß, Her, bey
> deinem wort etc. und Verleyhe uns friden gnediglich etc., 4. Wo Gott der Herr nicht bey uns
> helt etc., 5. Wer Gott nicht mit uns dise zeit etc., 6. Ach Gott, vom himel silie darein etc.,
> 7. In dich hab ich gehoffet herr etc. nachsingen laßen und daruf mit dem segen beschheßen,
> also clas allen tag in der gantzen wochen einer umb den andern in obgesatzter ordnung nach dem
> gebett und sonst kein anderer gesungen werde.

following that, changing about, always after the prayer [let] one of these psalms be sung after,
namely: 1. "A mighty fortress is our God," etc.; 2. "Give peace in our time," etc.; 3. "Keep
us, Lord, by thy word," etc., and "Grant us peace graciously," etc.; 4. "Where God the Lord
standeth not by us," etc.; 5. "Were God not with us at this time," etc.; 6. "Ah God, from heaven
look down," etc.; 7. "In thee have I hoped, Lord," etc.; and thereupon conclude with the
blessing; so that every day in the whole week one after the other in the order set above be sung
after the prayer, and no other.

The Hohenlohe *Gesangsordnung* of 1596 likewise rotated Lobwasser's Psalms 20, 61 and 79 on the
Friday prayer days, the last "because of the present great need of the Turk", "one Friday after
the other in order" (Sehling 15, pp. 655–656).

---

## 17. Hymns at the occasional rites

The rites outside the Sunday service had their own small sets of hymns. Each rite drew on a
fixed handful. The choice within the handful was left to the pastor or schoolmaster, or to the
family's wishes and purse.

| Rite | Hymns named |
|---|---|
| Baptism | "Christ unser Herr zum Jordan kam"; "Vater unser"; stanzas of "Durch Adams Fall"; "Herr, schaff uns wie die kleinen Kind" |
| Wedding | Ps 128 "Wohl dem, der in Gottes Furcht steht"; Ps 127 "Wo Gott zum Haus nicht gibt sein Gunst"; "Nun bitten"; Te Deum; "Dein Eh sollst du bewahren rein" (the sixth commandment) |
| The sick and dying | "Aus tiefer Not"; "Mit Fried und Freud"; "Nun freut euch"; the baptism and communion hymns |
| Burial | "Mitten wir im Leben sind" (with or after *Media vita*); "Mit Fried und Freud"; "Aus tiefer Not"; "Nun lasst uns den Leib begraben"; "Wir glauben all"; *Si bona suscepimus*; *Jam moesta quiesce* |
| Ordination and installation | "Nun bitten" or "Komm heiliger Geist"; "Wir glauben"; Te Deum or "Dank sagen wir alle"; *Veni creator*; *Veni sancte Spiritus* |
| Thanksgiving days | Te Deum; Ps 124 "Wo Gott der Herr nicht bei uns hält"; Ps 127 |

### 17.1 Baptism

Hof gives a reason for singing at baptism at all: so that two actions do not follow each other
without a song, with an unaccustomed silence between them. Before a baptism at the weekday
service, the hymn stanza sung was the one that matched the catechism lesson just read.
**Hof, *Ordo ecclesiasticus*, 1592** (Sehling 11, p. 430):

<!-- doc 294 -->
> soll nach geendter lection zu den festen und sontägen zur vesper (nun mehr stracks nach der
> predigt) etwas gesungen werden, uf das nicht zwen actus ohne ein gesang, ufeinander folgen
> und ein ungewöhnlich stillschweigen sich dazwischen zutrage. Und weil man an den zehen
> geboten lieset, soll allweg dasselbig gebot aus den lengeren zehen geboten gesungen werden,
> von welchem in gedachter lection gehandelt worden. Weil man an dem glauben lieset, soll bei
> dem ersten artikel gesungen werden: Gott der Vater wohn uns bei, bei dem andern: Jesus
> Christus wohn uns bei, bei dem dritten: Heiliger Geiste wohn uns bei etc. Weil man von dem
> Vaterunser lieset, soll zu einer iden bit ein gesetz aus dem Vaterunser doctoris Martini
> gesungen werden. Wann von der tauf gelesen wird, soll gesungen werden das gesetz aus dem
> gesang Christ unser Herr zum Jordan kam, so die ordnung der erklerung mit sich bringt. Wann
> man vom ambt der schlüssel oder absolution lieset, soll gesungen werden: So war ich leb.

after the lesson is ended, on the feasts and Sundays at vespers (now straightway after the
sermon), something shall be sung, that two actions may not follow one upon the other without a
song, and an unaccustomed silence fall between. And while the Ten Commandments are being read,
that same commandment out of the longer Ten Commandments shall always be sung which was treated
in the said lesson. While the creed is being read, at the first article shall be sung "God the
Father be with us"; at the second, "Jesus Christ be with us"; at the third, "Holy Ghost be with
us," etc. While the Our Father is being read, to every petition a stanza out of Doctor Martin's
Our Father shall be sung. When baptism is read of, that stanza out of the song "Christ our Lord
to Jordan came" shall be sung which the order of the exposition bringeth with it. When the
office of the keys or absolution is read of, "As truly as I live" shall be sung.

Through the rest of the year the baptism hymn ran on from one baptism to the next. One stanza was
sung before the baptism and the next after it, and when the hymn was finished it began again
(Sehling 11, p. 431):

<!-- doc 294 -->
> Hernach durchs ganze jahr: Christ unser Herr zum Jordan kam, (ein gesetz vor, das andere nach
> der tauf und, wann es aus ist, widerumb forne angehaben). Zum beschlus des actus diurni mag
> man bisweilen die ubrigen gesetz an diesem gesang bis zum end singen.

Thereafter through the whole year, "Christ our Lord to Jordan came" (one stanza before, the next
after the baptism, and when it is out, begun again from the front). At the close of the daily
service one may at times sing the remaining stanzas of this song to the end.

**Ysenburg-Birstein, *Kirchenordnung*, 1588** (Sehling 10, p. 628):

<!-- doc 228 -->
> So soll der Schulmeister erstlich einen Tauffgesang singen, Als: Christ, unser Herr, zum
> Jordan kam, oder: Herr, schaff uns wie die kleinen Kind etc.

Then the schoolmaster shall first sing a baptismal song, as "Christ our Lord to Jordan came," or
"Lord, make us as the little children," etc.

**Mansfeld, *Kirchen-Agenda*, 1580** (Sehling 2, p. 236):

<!-- doc 1241 -->
> Bei der taufe pfleget man an etlichen orten auf dem lande zu singen. Vater unser im
> himmelreich. Oder. Christ unser herr zum Jordan kam. Oder. Etliche vers aus dem gesange, Durch
> Adams fall ist ganz verderbt etc.

At baptism it is the custom in some places in the country to sing "Our Father in the kingdom of
heaven," or "Christ our Lord to Jordan came," or some verses out of the song "Through Adam's fall
is all corrupt," etc.

**Cochstedt, *Kirchen-Ordnung*, 1556** (Sehling 2, p. 484):

<!-- doc 1260 -->
> Zur taufe wird gesungen durch die schüler: Christ unser herr zum Jordan.

At baptism the scholars sing "Christ our Lord to Jordan."

In Lüneburg, children were baptized between the epistle and the gospel of the Sunday Mass. The
litany-hymn "Nim von uns" was then left out (§8.9).

### 17.2 Weddings

The wedding psalms were Psalm 127 and Psalm 128, in their metrical forms. **Saxony
(Albertine), *Kirchenordnung*, 1539**, variants (Sehling 1, p. 274):

<!-- doc 30 -->
> Erstlich, das man singe den 127. psalm, oder den 128. Nach dem psalmen sol eine lectio aus eim
> evangelisten, oder S. Paulus episteln einer gelesen werden, die hiezu dienet, als nemlich, das
> evangelium Johannis am 2. capitel, es ward ein hochzeit zu Cana in Galilea etc. item zun
> Ephesern am 5. capitel, oder dergleichen. Darnach singe man, nu bitten wir den heiligen geist.

First, that the hundred and twenty-seventh psalm be sung, or the hundred and twenty-eighth.
After the psalm a lesson shall be read out of one of the evangelists or of St Paul's epistles
that serveth hereto, namely the gospel of John in the second chapter, "There was a marriage in
Cana of Galilee," etc., item to the Ephesians in the fifth chapter, or the like. Thereafter let
"Now pray we the Holy Ghost" be sung.

**Ysenburg-Birstein, *Kirchenordnung*, 1588** (Sehling 10, p. 632):

<!-- doc 228 -->
> Vor der Predigt soll man den 127. Psalmen: Wo Gott der Herr nicht gibt sein gunst etc. unnd
> den Christlichen Glauben singen. Darauff folget die Predigt mit dem Gebett, wie sonst die
> gewöhnlichen Wochenpredigt gehalten werden. Nach gehaltener Predigt singt man den 128. Psalmen:
> Wol dem, der in Gottes Forchte stehet etc.

Before the sermon shall be sung the hundred and twenty-seventh psalm, "Where God the Lord giveth
not his favour," etc., and the Christian creed. Thereupon followeth the sermon with the prayer,
as the customary weekday sermons are otherwise held. After the sermon is held, the hundred and
twenty-eighth psalm is sung, "Blessed is he that standeth in God's fear," etc.

In Hof, and in the Henneberg village of Goldlauter, the sixth commandment was sung after the
marriage, from Luther's Ten Commandments hymn, with its last stanza. **Hof, *Ordo
ecclesiasticus*, 1592** (Sehling 11, p. 430):

<!-- doc 294 -->
> vor der copulation gesungen: Wol dem, der in Gottes furchten steht, post copulationem: Wo Gott
> zum haus nicht gibt sein etc. oder aber: Dein eh soltu bewahren rein ex decalogo germanico
> Lutheri addito ultimo Das helf uns der Herr Jesu Christ.

before the marriage is sung "Blessed is he that standeth in God's fear"; after the marriage,
"Where God to the house giveth not his," etc., or else "Thy marriage shalt thou keep pure," out
of Luther's German Decalogue, with the last [stanza] added, "Help us to this, Lord Jesu Christ."

**Goldlauter (Henneberg), *Kirchen-Ordnung*, 1566** (Sehling 2, p. 333):

<!-- doc 1248 -->
> so pfleg man erstlich zu singen das Veni sancte in kurzer melodei und halt darauf Ein feste
> burg und darnach den glauben, unterdes gehen die leut zum opfer. Demnach thue ich ein
> hochzeitpredigt auf der canzel. Nach der predigt singt man: Wol dem der in gottes furchten
> stehet und werden beide eheleut […] zusamen gegeben […] Zum beschluss singt man wider das
> sechste gebot: Dein ehe soltu bewaren rein, und Das helfe uns der herr Jesus Christ.

then it is the custom first to sing the *Veni sancte* in the short melody, and thereupon "A
mighty fortress," and thereafter the creed; meanwhile the people go to the offering. Then I
hold a wedding sermon in the pulpit. After the sermon is sung "Blessed is he that standeth in
God's fear," and both spouses are joined together […]. At the close is sung again the sixth
commandment, "Thy marriage shalt thou keep pure," and "Help us to this, the Lord Jesus Christ."

Osnabrück sang the German or Latin Te Deum and Psalm 128 before the bridal Mass. **Osnabrück
(Stift), *Kirchenordnung*, 1543** (Sehling 7/1, p. 225):

<!-- doc 2096 -->
> Und so de brudt worde tor kercken gahn, soll men vor der brudtmisse singen: Te Deum laudamus
> dudesch effte latein und den psalm Woll dem, de in Gades fruchten steit etc.

And when the bride goeth to church, there shall be sung before the bridal Mass the *Te Deum
laudamus* in German or Latin, and the psalm "Blessed is he that standeth in God's fear," etc.

In Hamburg the families could hire the organist and cantor for more. **Hamburg,
*Kirchenordnung*, 1529** (Sehling 5, p. 516):

<!-- doc 1960 -->
> Dar machme denne in der karcken up den orgelen spelen und singen mit den scholeren Te deum
> laudamus, edder wat anders van gade, edder ock in figurativis etc., wo de lude idt denne mit
> dem organisten und cantoren vor ohre drankgelt hebben bestellet.

There one may then in the church play upon the organs and sing with the scholars *Te Deum
laudamus*, or something else of God, or also in figured music, etc., as the folk have then
ordered it with the organist and cantor for their drink-money.

Hohenlohe gave a wedding set for weekday weddings. **Hohenlohe, *Schul- und Gesangsordnung*,
1596** (Sehling 15, p. 656):

<!-- doc 628 -->
> Zun hochzeiten in der wochen Fur der predigt soll gesungen werden: Nun welche hie etc., Es
> sind doch seelig alle, die etc. Nach der predigt für der eheeinleitung: Es woll uns Gott
> genädig sein etc. oder ein Gloria. Nach einleitung der ehe: Woll dem, der in Gottes forcht
> etc.

At weddings in the week: before the sermon shall be sung "Now they that here," etc., "Blessed
are all they that," etc.; after the sermon, before the marriage, "May God be gracious unto us,"
etc., or a Gloria; after the marriage, "Blessed is he that in God's fear," etc.

### 17.3 The sick and the dying

The Regensburg order gives a short list of hymns for those who attended the dying: "grounded
psalms and songs", not "old erroneous prayers and sayings". **Regensburg, *Kirchenordnung* of
Hieronymus Noppus, 1543** (Sehling 13, p. 410):

<!-- doc 436 -->
> inen das vaterunser und den glauben fürsprechen und, wus zeit hat, gegründete psalm und
> geseng, als: Aus tiefer not schrei ich zu dir etc., In fried und freud ich far dahin, Nun
> freut euch, lieben christen gemein, von der tauf, vom sacrament des leibs und bluts etc.,
> nicht alte, irrige gebet und spruch.

[they shall] say the Our Father and the creed before them, and, where there is time, grounded
psalms and songs, as "Out of the depths I cry to thee," etc., "In peace and joy I now depart,"
"Now rejoice, dear Christians all," [the songs] of baptism, of the sacrament of the body and
blood, etc.; not old, erroneous prayers and sayings.

### 17.4 Burial

The burial hymn named first everywhere is Luther's "Mitten wir im Leben sind", often after the
Latin *Media vita*. The Saxon Visitation Articles of 1528 already ask for it. **Saxony
(Ernestine), *Unterricht der Visitatoren*, 1528** (Sehling 1, p. 170):

<!-- doc 9 -->
> und bei dem begrebnis, das deudsche gesang, mitten in dem leben, singen lassen.

and at the burial let the German song "In the midst of life" be sung.

Brandenburg sets the hymns by the course of the procession: "Mitten wir im Leben" on the way,
"Aus tiefer Not" if the way was long, and Simeon's song on the return to church. **Brandenburg,
*Kirchenordnung*, 1540** (Sehling 3, p. 81):

<!-- doc 1746 -->
> so man die leiche tregt, mag man singen, media vita und die drei deutsche vers, mitten wir im
> leben sind, und so der weg zu lang, das deudsche deprofundis, aus tiefer not, oder sonst das
> responsorium libera me domine. Und so man vom begrebnis widerum in die kirchen gehet, alsdenn
> mag man singen, mit fried und freud ich fahr dahin.

when the corpse is carried, one may sing *Media vita* and the three German verses, "In the midst
of life we are," and, if the way be too long, the German *De profundis*, "Out of the depths," or
else the responsory *Libera me Domine*. And when one goeth again from the burial into the
church, then one may sing "In peace and joy I now depart."

Hof adds "Aus tiefer Not" "with the slow melody" when needed, and graded its funerals by the
number of school classes that attended. **Hof, *Ordo ecclesiasticus*, 1592** (Sehling 11, p. 475):

<!-- doc 294 -->
> Hinc germanicae sequuntur cantilenae, etiam in particularibus funeribus, quibus tertiani,
> quartani et quintani, in hieme, ast in aestate etiam sextani intersunt cantore duce,
> usurpandae videlicet: Mitten wir im leben sind. Gott der Vater wohn uns bei. Mit fried und
> freud ich fahr dahin Lutheri. Item si necessitas postulat, praenotatis, antequam pueri templum
> d. Laurentii ingressi sunt, finitis adiiciuntur: Aus tiefer not, mit der langsamen melodie zu
> singen. Erbarm dich mein, o Herre Got.

Hence follow German songs, to be used also at private funerals, at which the third, fourth and
fifth classes attend under the cantor's lead in winter, and in summer the sixth also, namely:
"In the midst of life we are"; "God the Father be with us"; Luther's "In peace and joy I now
depart." Item, if need require, when the aforesaid are finished before the boys have entered St
Lawrence's church, there are added "Out of the depths," to be sung with the slow melody, and
"Have mercy on me, O Lord God."

Several orders split the burial hymn around the sermon. **Schwäbisch Hall, *Kirchenordnung*,
1543/1615** (Sehling 17/1, p. 174):

<!-- doc 763 -->
> soll man singen: Nun laßt Uns den Leib begraben etc. biß auff den Verß: Nun lassen wir Ihn hie
> schlaffen etc. Darauff soll der Kirchendiener Einer, an den es begeret worden, ein Christliche,
> gebürliche unnd dem gegenwertigen Handel gemäße Leichpredigt thuon.

one shall sing "Now let us bury the body," etc., until the verse "Now let we him sleep here,"
etc. Thereupon one of the ministers, of whom it hath been desired, shall hold a Christian,
fitting funeral sermon, agreeable to the present business.

**Limpurg, *Kirchenordnung*, 1610** (Sehling 16, p. 623):

<!-- doc 729 -->
> In der Kirchen zu Münster, wan die gemain sich versamblet, eintweder das gesang: Mitten wir im
> Leben sind etc. wider ganz und nach der Predigt: Nun last uns den leib begraben etc. Oder diß
> Gesang vor der Predigt biß auff die zwei lezste gesäz: Nun lassen wir ihn hie schlaffen etc.
> Und dieselbige als dann nach der Predigt.

In the church at Münster, when the congregation assembleth, either the song "In the midst of
life we are," etc., again wholly, and after the sermon "Now let us bury the body," etc.; or this
song before the sermon until the two last stanzas, "Now let we him sleep here," etc., and the
same then after the sermon.

**Hohenlohe, *Schul- und Gesangsordnung*, 1596** (Sehling 15, p. 656):

<!-- doc 628 -->
> In der proceßion hinauß mit der leich biß zum grab und in die kirchen hinein für der predigt
> soll man singen: Mitten wir im leben etc., Mit fridt und freyd etc., Gott der Vatter wohn uns
> bey etc., Wenn mein stundlein vorhanden ist etc. Nach der predigt aber soll man bey dem grab
> singen: Nun last unß den leib etc.

In the procession out with the corpse to the grave, and into the church before the sermon,
shall be sung "In the midst of life," etc., "In peace and joy," etc., "God the Father be with
us," etc., "When my last hour is come," etc. But after the sermon "Now let us [bury] the body,"
etc. shall be sung at the grave.

**Schwarzburg, *Kirchenordnung*, 1574** (Sehling 2, p. 136):

<!-- doc 1230 -->
> Als dan wird der cörper in die erde begraben, die schul knaben singen, weil man begrebt, den
> gesang Lutheri: Nu last uns den leib begraben.

Then the body is buried in the earth; the school boys sing, while it is being buried, Luther's
song "Now let us bury the body."

The Kurland order lists the hymns for before the funeral sermon, "as many as it pleaseth".
**Kurland, *Kirchenordnung*, 1570** (Sehling 5, p. 105):

<!-- doc 1907 -->
> Mit fried und freud ich fahr dahin. Erbarme dich meiner, o herre gott. Aus tiefer noth. Mitten
> wir im leben. Das responsorium. Si bona suscepimus et similia. Ich gleub an gott vater,
> almechtigen. Wir gleuben. Diese psalmen und gesengen brauchet man so viel für der leichpredigt
> als gefellig.

"In peace and joy I now depart." "Have mercy on me, O Lord God." "Out of the depths." "In the
midst of life." The responsory *Si bona suscepimus* and the like. "I believe in God the Father
Almighty." "We believe." These psalms and songs one useth before the funeral sermon, as many as
it pleaseth.

**Rostock, *Conformitas ceremoniarum*, c. 1560** (Sehling 5, p. 290):

<!-- doc 1936 -->
> Bei den leichen der frommen christen sollen gesungen werden lateinisch und deutesch, si bona
> suscepimus. Media vita. Scio quod redemptor meus. Mit fried und freud. Aus tiefer not. Erbarm
> dich meiner. Nu last uns den leib begraben.

At the funerals of godly Christians shall be sung, in Latin and German, *Si bona suscepimus*,
*Media vita*, *Scio quod redemptor meus*, "In peace and joy," "Out of the depths," "Have mercy
on me," "Now let us bury the body."

The words "of godly Christians" matter. Singing was an honour, and it could be withheld. A
later Nürnberg regulation, printed with the Brandenburg-Nürnberg order, forbids the hymns of
Christian hope for those who died unrepentant, because of the offence. It gives them the
penitential hymns instead. **Brandenburg-Nürnberg, *Kirchenordnung*, 1533**, later appendix
(Sehling 11, p. 202):

<!-- doc 270 -->
> denen können die ordentliche lieder: Mit fried und freud ich fahr dahin nach Gottes willen
> etc. und andere dergleichen christliche gesänger, so sich auf solche fälle nicht schicken, für
> dem haus und im fortgehen, ärgernis zu vermeiden, nicht gesungen werden. Sondern für der tür
> wäre zu singen: Mitten wir im leben sind etc., in fortgehen aber: So wahr ich lebe, spricht
> dein Gott etc. item, andere bußlieder.

for these the ordinary songs, "In peace and joy I now depart according to God's will," etc., and
other such Christian songs as fit not such cases, cannot be sung before the house and in the
going forth, to avoid offence. But before the door there might be sung "In the midst of life we
are," etc., and in the going forth, "As truly as I live, saith thy God," etc., item other songs
of repentance.

At Strasbourg there was no singing unless it was asked for, and then no funeral sermon either.
**Strasbourg, *Gottesdienstordnung*, 1577** (Sehling 20/1, p. 518):

<!-- doc 1336 -->
> vor und nach der predigt singt entweder: Mitten wir im leben sind, oder: Mit fried und freud
> ich fahr dahin, item: Nun last uns den leib begraben. Wo es aber nit begert wird, gleich wie
> man nicht singt, also thut man auch keine leichpredigt.

before and after the sermon is sung either "In the midst of life we are," or "In peace and joy I
now depart," item "Now let us bury the body." But where it is not desired, even as one singeth
not, so one also holdeth no funeral sermon.

The Leiningen order abolished the old "singing over" the dead with holy water, but allowed the
scholars to sing German hymns. **Leiningen-Westerburg, *Kirchenordnung*, 1566** (Sehling 19/1, p. 267):

<!-- doc 1074 -->
> alles Bäpstisch gepreng mit Weywasser, Besingen und andern etc. abgeschaffen sein. Dann solches
> nicht allein ohne Gottes wort, sondern auch wider Gottes wort angerichtet, als sol es zur
> seligkeit fürderlich sein. Wo nun schulen sindt, mögen die schüler wol etliche teutsche Gesang
> singen, Als: Mitten wir im leben sind, Nun lessest du deinen diener im friede fahren etc.

all popish pomp with holy water, singing over [the dead], and other things, etc. [shall] be
done away. For such was set up not only without God's word but also against God's word, as
though it should be furthersome to salvation. Now where there are schools, the scholars may well
sing some German songs, as "In the midst of life we are," "Now lettest thou thy servant depart in
peace," etc.

The Goslar order of 1528 left the whole matter to "a godly, reasonable, learned pastor".
**Goslar, Amsdorf, *Vom teglichen gots dinst*, 1528** (Sehling 7/2.2, pp. 237–238):

<!-- doc 2187 -->
> Das eyn caplan, der custer, ouch dy schuller mit gehen, las ich gescheen, und singen deutzsch
> und lateyn Media vita, eyn psalm etc. Daß alles stehet bey eym frommen, vornunfftigen,
> gelerten pfarhern zu […] myndern und zu meren, das ehrs orden, wys am besten und nutzten dem
> volck seyn wirt.

That a chaplain, the sexton and also the scholars go along, I allow to be done, and [that they]
sing in German and Latin *Media vita*, a psalm, etc. All this standeth with a godly, reasonable,
learned pastor to lessen and to increase, that he order it as it shall be best and most
profitable for the people.

### 17.5 Ordination and installation

The ordination and installation rites of the Württemberg family open with "Nun bitten". The
creed is sung after the sermon, and the service closes with the Te Deum or the German *Grates*.
**Württemberg, *Synodalordnung*, 1547** (Sehling 16, p. 159):

<!-- doc 660 -->
> Unnd so das volgkh inn der kirchen versamlet, soll man annfangen unnd singen: Nun piten wier den
> hailgen gaist, etc. Uf dis gesanng solle der dechan oder einer der Consiliariis uffsteen unnd ein
> Predig thun von Ministerio verbi […] Nach der Predig soll gesungen werdenn der Glaub.

And when the people are assembled in the church, one shall begin and sing "Now pray we the Holy
Ghost," etc. After this song the dean or one of the councillors shall stand up and hold a sermon
of the ministry of the word […]. After the sermon the creed shall be sung.

Lippe (1571) copies the rite, and the superintendent steps before the altar during the creed
(Sehling 21, p. 438):

<!-- doc 1462 -->
> so das Volck in der Kirchen versamblet, anfangs singen: Nu bitten wir den Heiligen Geist etc.,
> Auff diß Gesang der Superintendens oder sein Adjunct auffstehen und ein Predigt thun vom
> Ministerio verbi.

when the people are assembled in the church, [they shall] sing at the beginning "Now pray we the
Holy Ghost," etc.; after this song the superintendent or his adjunct [shall] stand up and hold a
sermon of the ministry of the word.

**Lauenburg, *Kirchenordnung*, 1585** (Sehling 5, p. 408):

<!-- doc 1953 -->
> Das volk sol zuvor in der kirchen vorsamlet, etliche psalmen absingen, und darnach zu letzt
> darauf folgen: Nu bitten wir den heiligen geist. Oder: Kom heiliger geist, herre gott.

The people, first assembled in the church, shall sing some psalms, and thereafter at the last
there shall follow "Now pray we the Holy Ghost," or "Come, Holy Ghost, Lord God."

The Brandenburg installation adds Psalm 67 and the Te Deum. **Brandenburg, *Visitations- und
Consistorialordnung*, 1573** (Sehling 3, p. 109):

<!-- doc 1748 -->
> nach gesprochenen vater unser sol die gemeine singen: Nun bitten wir den heiligen geist, und Es
> wolt uns gott gnedig sein und seinen segen geben etc., item das te deum laudamus etc.

after the Our Father is spoken the congregation shall sing "Now pray we the Holy Ghost," and
"May God be gracious unto us and give his blessing," etc., item the *Te Deum laudamus*, etc.

The Hessian ordination closes with the Te Deum "where there are schools", or "Dank sagen wir
alle". **Hessen, *Agende*, 1574** (Sehling 8, p. 455):

<!-- doc 2272 -->
> Zum beschluß soll die gemeine singen Te Deum laudamus, teutsch, oder latinisch, wo schulen
> vorhanden sein, oder Danksagen wir alle, Gott unserm Herrn Christo etc., oder einen andem
> dergleichen lobgesang.

At the close the congregation shall sing *Te Deum laudamus*, in German, or in Latin where there
are schools, or "Thanks say we all to God our Lord Christ," etc., or another such song of
praise.

The Merseburg draft for Luther's ordinations has *Veni creator* sung while ordinator and
ordinands kneel. **Merseburg, *Ordinations-Ordnung*, 1545** (Sehling 2, p. 7):

<!-- doc 1210 -->
> Credo in unum. Populus: wir glauben. Chor: Veni creator, unter dem der herr ordinator sampt dem
> ordinanden fur den altar zugleich niederknien solten.

*Credo in unum*. The people: "We believe." The choir: *Veni creator*, during which the lord
ordinator together with the ordinands should kneel down together before the altar.

### 17.6 Days of thanksgiving and extraordinary occasions

Michaelmas in Schleswig-Holstein was a harvest thanksgiving, with the Te Deum after the sermon.
**Schleswig-Holstein, *Kirchenordnung*, 1542** (Sehling 23, p. 95):

<!-- doc 1576 -->
> De dach Michaelis ys eine gemene dancksegginge vor alle fruchte, de wy des Jars gesamlet und
> entfangen hebben. Darumme schal de gantze vorsamlinge vorth na der predigen singen tho der
> dancksegginge mit groter andacht: Te Deum Laudamus etc.

The day of Michael is a common thanksgiving for all the fruits which we have gathered and
received in the year. Therefore the whole congregation shall, straight after the sermon, sing
for the thanksgiving with great devotion *Te Deum Laudamus*, etc.

Lüneburg kept an annual day for the city's deliverance. On it hymns took the place of the
propers: Psalm 127 (figural) and Psalm 124 after the epistle, and Psalm 124 again with Psalm 3 at
matins. **Lüneburg, *Kirchenordnung*, 1575** (Sehling 6/1, p. 663):

<!-- doc 2017 -->
> Ad missam: 4. Introitum: Benedicite de angelis, 5. das Kyrie figuraliter, item: Et in terra
> pax, darnegst: Alleine Godt in der hohe sey ehr, 6. post lectionem epistolae: Nisi Dominus
> aedificaverit domum, 7. Wo Godt nicht mit uns ist, 8. canitur evangelion, 9. Nun bitten wir den
> heiligen Geist, 10. fit contio sacra, 11. post concionem canitur litania.

At the Mass: 4. the introit *Benedicite* of the angels; 5. the Kyrie in figured music, item *Et
in terra pax*, next "To God alone on high be glory"; 6. after the reading of the epistle, *Nisi
Dominus aedificaverit domum*; 7. "Were God not with us"; 8. the gospel is sung; 9. "Now pray we
the Holy Ghost"; 10. the holy sermon is held; 11. after the sermon the litany is sung.

At Nördlingen's thanksgiving day on 7 January, Psalm 124 could be sung instead of a figured
piece, "that the congregation also may have cause to thank God". **Nördlingen,
*Kirchenordnung*, 1579** (Sehling 12, p. 388):

<!-- doc 375 -->
> Singet der chorus ein stuck figuraliter oder, damit die gemein auch Gott zu danken ursach habe,
> kan der psalm Wo Gott der Herr nicht bei uns helt etc. gesungen werden.

The choir singeth a piece in figured music; or, that the congregation also may have cause to
thank God, the psalm "Where God the Lord standeth not by us," etc. may be sung.

At an execution in Regensburg the crowd sang "Nun bitten" while the condemned man began to recite
the creed. **Regensburg, *Kirchenordnung* of Justus Jonas, 1553**, with the order for the
condemned (Sehling 13, p. 426):

<!-- doc 440 -->
> Deinde ut palam profiteatur fidem ac recitet symbolum apostolicum: Credo in Deum Patrem etc.
> Sub illius autem inchoatione cantabit turba circumstans cantilenam: Nun bitten wir den Heilgen
> Geist.

Then that he openly profess the faith and recite the Apostles' Creed, *Credo in Deum Patrem*,
etc. But at the beginning of it the crowd standing about shall sing the song "Now pray we the
Holy Ghost."

---

## 18. How hymns were chosen: the reasons given

The orders seldom explain a single choice. They often state the rules by which choices were to
be made. Ten kinds of reason recur. They are gathered here with the quotations not already given
in the sections on the slots.

### 18.1 From Scripture, and "pure"

The first test is always the text. Anything sung, Latin or German, must come from Scripture or
be proved by it. **Hamburg, *Kirchenordnung*, 1529**, section "Van singende" (Sehling 5, p. 516):

<!-- doc 1960 -->
> Alle singent dudesch und latinsch, wo gesecht, schall ut de hilligen schrift sin, edder mit
> gades klare worde und dem christliken loven beweret, alse Paulus singen leret, Ephes. 5. Alse
> ock de olden christene doctores gesungen hebben und singen laten, done me vam salve regina und
> andere unchristliken sengen nicht wuste.

All singing, German and Latin, as hath been said, shall be out of the holy Scripture, or proved
by God's clear words and the Christian faith, as Paul teacheth to sing, Ephesians 5; as also the
old Christian doctors sang and caused to be sung, when men knew nothing of the *Salve regina* and
other unchristian songs.

Buxtehude applies the test to the Latin chants. It keeps those "agreeable to divine Scripture"
and drops the rest. **Buxtehude, *Kirchenordnung*, 1552** (Sehling 7/1, p. 77):

<!-- doc 2082 -->
> Alle latinische gesenge, godtliker schrift gemete, de wente anher in der kercken in der misse,
> metten und vesper to besunder tydt gesungen, scholen beholden, gebruket und to ohrer tydt
> gesungen werden. De averst undenstlick, godtliker schrift ungemete unde unrecht, scholen nicht
> gesungen werden.

All Latin songs agreeable to divine Scripture which have hitherto been sung in the church at Mass,
matins and vespers at their special time shall be kept, used and sung at their time. But those
that are unserviceable, not agreeable to divine Scripture, and wrong, shall not be sung.

Worms admits hymns as well as psalms, because Paul commended both. But no new hymn is to be
brought in without the superintendent and preachers. **Worms, *Agendbüchlein*, 1560** (Sehling 19/1, p. 208):

<!-- doc 1069 -->
> Dieweil der heilige Apostel Paulus nicht allein die Psalmen Davids, sondern auch andere
> Geistliche […] Lieder und Lobgesäng den Christen hat commendirt und befohlen, So verwerffen wir
> dieselbigen auch nicht, doch so ferne sie Christlich und inn der Heiligen Schrifft gegründet
> seien. Allein das man keinen newen Gesang ohne der Supperattendenten und Predicanten rhat und
> vorwissen inn der Kirchen einführe.

Since the holy apostle Paul hath commended and enjoined to Christians not only the psalms of
David but also other spiritual songs and hymns of praise, we also reject them not, yet so far
as they be Christian and grounded in holy Scripture. Only that no new song be brought into the
church without the counsel and foreknowledge of the superintendents and preachers.

In Württemberg every communion hymn beyond the named ones had to be "examined and admitted" by
the superintendents first. **Württemberg, *Kirchenordnung*, 1536** (Sehling 16, p. 109):

<!-- doc 651 -->
> oder andere lobgesang, die rein […] unnd vorhin von den superattendenten besichtiget,
> examiniert und zugelassen seien.

or other songs of praise which are pure […] and have been beforehand viewed, examined and
admitted by the superintendents.

### 18.2 Fitting the feast and the season

The Saxon Visitation Articles of 1528 thought it "unseemly that the songs are quite alike at
all feasts". **Saxony (Ernestine), *Unterricht der Visitatoren*, 1528** (Sehling 1, p. 169):

<!-- doc 9 -->
> Dieweil es auch ein ungestalt ist, das die gesang gar gleich sind an allen festen, were gut,
> das man an den herrlichsten festen sünge, die lateinische introitus, glor[ia].

Since it is also unseemly that the songs are quite alike at all feasts, it were good that on the
most glorious feasts one sang the Latin introits, Gloria [etc.].

Bugenhagen asked the schoolmasters to see that "the songs rhyme finely with the feasts". Where no
proper song existed, they were to take "the most joyful psalms or songs". **Braunschweig,
*Kirchenordnung*, 1528** (Sehling 6/1, p. 442). The same sentence recurs in Mecklenburg (1545):

<!-- doc 1983 -->
> De scholemeystere scholen darup sehn, dat de senge sick fyn rymen mit den festen, wen se neyne
> senge darto hebben, so nemen se de frolikesten psalmen edder lede unde sehn jo darup, dat de
> gesenge uth der reynen scrift syn unde reyn unde lustich unde vorstentlick vor de leyen uth
> Gades wörde gemaket.

The schoolmasters shall see to it that the songs rhyme finely with the feasts. When they have no
songs for them, let them take the most joyful psalms or songs, and see always that the songs be
out of the pure Scripture, and pure and pleasant and understandable for the laity, made out of
God's word.

The Kurpfalz order of 1556 wants the songs to follow "the teaching and the order of the
season", so that the church is reminded of the necessary articles "both with preaching and
singing". **Kurpfalz, *Kirchenordnung*, 1556** (Sehling 14, p. 165):

<!-- doc 480 -->
> Man soll sich auch fleissigen, das sich die gsang nach der leer und zeitordnung richten, als
> nemlich: auf den Christag und nachvolgenden festen von der geburt Christi, zur Ostern von der
> urstend Christi, damit die kirch der nötigen stuck der leer des christlichen glaubens, beid,
> mit predigen und singen, wol erinnert werde.

One shall also be diligent that the songs be ordered after the teaching and the order of the
season: namely, on Christmas Day and the feasts following, of the birth of Christ; at Easter, of
the resurrection of Christ; that the church may be well reminded of the necessary pieces of the
teaching of the Christian faith, both with preaching and singing.

The Sayn *Kirchenzuchtordnung* of 1582 repeats this almost word for word (Sehling 19/1, p. 369).
Hanau-Lichtenberg (1573) opens its three rules with the same point (§11.5).

The Württemberg court church order of 1560 made the court preachers settle the hymns with the
choirmaster, so that the singing followed the season and not "his own nod". **Württemberg,
*Hofkirchenordnung*, 1560** (Sehling 16, p. 428):

<!-- doc 686 -->
> Es sollen auch allwegen die Hof Prediger sich mit dem Cappell maister vergleichen, was er singen
> solle, unnd das sich das gesannge de tempore, obgemellter Ordnung nach, schickhe unnd nit, wie
> bißher beschehen, ad nutum ipsius gesungen werdenn.

The court preachers shall also always agree with the choirmaster what he shall sing, and that
the singing fit the season according to the order above, and be not sung at his own nod, as
hath hitherto been done.

### 18.3 Fitting the gospel and the sermon

The later orders go further. The hymn is to agree with the gospel and "the chief teaching of the
sermon". **Öhringen, *Kirchen- und Schulordnungen*, 1582**, the German school order (Sehling 15, p. 503):

<!-- doc 592 -->
> Er soll sich vermög unser kirchenordnung jedertzeit soviel muglich befleissen, solche psalmen
> zu singen, die mit den gewöhnlichen evangeliis und der haubtlehr der predigt ubereinstimmen. Er
> soll sich auch am sontag mit dem organisten zuvor underreden und vergleichen, was er singen
> wöll, damit es kein confuss und unordnung geb.

He shall, according to our church order, be diligent at all times as much as possible to sing
such psalms as agree with the customary gospels and the chief teaching of the sermon. He shall
also on the Sunday speak beforehand with the organist and agree what he will sing, that there be
no confusion and disorder.

The Hohenlohe *Gesangsordnung* of 1596 gives the reason in its closing paragraph. When the
hymns are fitted to the sermons, the common man will feel that the singing is "no superfluous or
vain ceremony" but "a short summary and pleasant instruction". It also forbids cutting psalms off
in the middle. **Hohenlohe, *Schul- und Gesangsordnung*, 1596** (Sehling 15, p. 657):

<!-- doc 628 -->
> das die pfarrherr mit guettem bedacht, sovil müglich, alle gesang vor und nach auf die
> predigten richten wöllen, damit der gemein man vermittelst göttlicher gnaden in seinem hertzen
> empfinde, das das gesang nicht ein übrige oder vergebenliche ceremonia, sonder ein kurtzer
> begriff und lustige underweißung ist, dardurch uns allerley, so zur seeligkeit zu wissen
> nottwendig, gantz schön und lieblich zue hertzen gefurt werde.

that the pastors, with good consideration, as much as possible, will direct all songs before and
after to the sermons; that the common man, by means of divine grace, may feel in his heart that
the singing is not a superfluous or vain ceremony, but a short summary and pleasant instruction,
whereby all manner of things necessary to be known for salvation are brought home to our hearts
most fairly and lovely.

The Kassel general synod of 1607 asked for the hymn numbers to be posted on a board at the church
doors, and for an order of hymns "by the seasons of the year and fitted to the texts that are to
be preached". **Hessen-Kassel, *Abschied der Kasseler Generalsynode*, 1607** (Sehling 9, pp. 75–76):

<!-- doc 2287 -->
> das die psalmen, so in der versamblung gesungen werden sollen, jederzeitt von dem glöckner oder
> opfferman, der sich des psalmens bei dem, so die predig halten wirdt, zuevorderst zuerkundigen
> hette, auff ein tefflein, an den pforden der kirchen oder wie es sich sonsten der kirchen
> beschaffenheitt nach fuglich thun lassen wolte, mit der zall bezeichnett wurde.

that the psalms which are to be sung in the assembly be at all times marked with their number by
the bell-ringer or sexton (who should first inquire of the psalm from him that is to hold the
sermon) upon a little board at the doors of the church, or as it might otherwise be fitly done
according to the condition of the church.

<!-- doc 2287 -->
> das es nicht undienlich wehre, das die psalmen undt andere christliche geseng in eine gewiesse
> ordnung nach den zeitten des jahrs undt die sich auff die textus, wel[…]che gepredigt werden
> solten, accommodirt, verfast undt den pfarhern, sonderlich auff dem landt, communicirt wurden.

that it were not unserviceable that the psalms and other Christian songs be drawn up into a
certain order according to the seasons of the year, and accommodated to the texts which should
be preached, and communicated to the pastors, especially in the country.

### 18.4 That the people may learn them: few, familiar, often repeated

A second group of reasons concerns the congregation's knowledge. The fewer the hymns, the sooner
they are learned. The Sponheim order uses the longest hymns before the sermon and the shortest
after it. It also prints a short list of hymns to be used "often and before others".
**Hintere Grafschaft Sponheim, *Kirchen- und Zensurordnung*, 1590/91** (Sehling 18, p. 657):

<!-- doc 1021 -->
> Inn stetten und flecken, do schulen sein, mag man in den kirchen die lieder und psalmen fast
> gebrauchen, die in der kirchenordnung zu finden, doch mit diesem gemeinen bescheidt, das
> annfangs und vor der predig die lengste, nach der predig aber die kurzste gesungen werden. Und
> damit das gemein volck mit vielen gesangen nit beschwert, sondern desto eher mit singen lernen,
> ist vonnöten, das etlich furnembste psalmen und lieder zum offtermahlen und fur andern,
> schweren und ihnen uhntauglichen liedern gebraucht werden. Und sollenn demnach volgende lieder
> offt und fur andern gebraucht werden, doch wo etwan ein gemein albereit etliche mehr lieder, so
> in der kirchenordnung begrieffen, gelernet hette, sollen dieselbe hiemit uhnverbotten sein.

In towns and market towns where there are schools, the songs and psalms that are found in the
church order may for the most part be used in the churches; yet with this common direction, that
at the beginning and before the sermon the longest, but after the sermon the shortest be sung.
And that the common people be not burdened with many songs, but the sooner learn to sing, it is
needful that some chief psalms and songs be used oftener and before others, [rather than] hard
songs unfit for them. And accordingly the following songs shall be used often and before others;
yet where a congregation hath already learned more songs contained in the church order, these
shall hereby not be forbidden.

Danzig wanted the same hymns used "two [Sundays] running", especially those that contained the
parts of the catechism. **Danzig, *Kirchenordnung*, 1557**, as summarised and quoted by Sehling
(Sehling 4, p. 168):

<!-- doc 1844 -->
> Ein Psalm, 2 oder 3 „nach der zeit gelegenheit, welche die ganze kirche auch lernen und
> mitsingen sol und darum oft sollen einerlei gesenge etliche zwei nach einander gebraucht werden,
> namentlich diejenigen, in welchen die stücke des catechismi ordentlich gefasset“.

A psalm, two or three, "according to the occasion of the season, which the whole church also
shall learn and sing along; and therefore the same songs shall often be used some two [times]
one after another, namely those in which the pieces of the catechism are orderly comprised."

Mecklenburg sang German hymns before and after the weekday sermons "that they may become known
and common to the people, and hearts be thereby stirred to prayer". **Mecklenburg,
*Kirchenordnung*, 1552** (Sehling 5, p. 201):

<!-- doc 1922 -->
> An solchen tagen sollen vor und nach der predigt deudsche geistliche lieder gesungen werden,
> damit sie dem volk bekant und gemein werden, und die herzen dadurch zum gebet erwecket werden.
> Als sonderlich: Vater unser im himelreich, Wo gott der herr nicht bei uns wer, Ein feste burg
> etc.

On such days German spiritual songs shall be sung before and after the sermon, that they may
become known and common to the people, and hearts be thereby stirred up to prayer; as especially
"Our Father in the kingdom of heaven," "Were God the Lord not with us," "A mighty fortress,"
etc.

Reutlingen listed the psalm-hymns that had once been "common and known in the church" and wanted
all of them brought back. The feast hymns it did not list, "for they are otherwise known well
enough". **Reutlingen, *Ordnung der Schule und des Kirchengesangs*, 1565/1566** (Sehling 17/2, p. 51):

<!-- doc 828 -->
> Dise psalmen seind alle sampt in der kirchen gemain und bekant gewesen, sollen derowegen alle
> wider darein gebracht werden. Die geseng uf die sonderliche hohe fest haben wir nit hieher
> verzaichnen wöllen, dan sie sonst gnugsamlich bekant seind.

These psalms have all been common and known in the church; they shall therefore all be brought
back into it. The songs for the special high feasts we have not wished to list here, for they
are otherwise known well enough.

Hesse wanted the sung psalms explained in sermons, "for what one understandeth not goeth slowly
to the heart". **Hessen, *Kirchenordnung*, 1566** (Sehling 8, p. 255):

<!-- doc 2257 -->
> sonderlich aber gehets ohn frucht nit abe, wenn die psalmen ausgelegt werden, zuvoraus die, so
> von der ganzen gemein gesungen; denn also verstehen sie alles besser, was in der h. versamlung
> von der kirchen verricht wird. Es werden auch die gemüter under dem singen desto mehr zur
> andacht und gottseliger betrachtung entzündet; denn was man nit verstehet, gehet einem langsam
> zu herzen.

But especially it goeth not off without fruit when the psalms are expounded, above all those
that are sung by the whole congregation; for so they understand the better all that is done by
the church in the holy assembly. The minds also are the more kindled to devotion and godly
meditation under the singing; for what one understandeth not goeth slowly to the heart.

**Sayn, *Kirchenzuchtordnung*, 1582** (Sehling 19/1, p. 369):

<!-- doc 1090 -->
> sollen die pastorn das volck ermahnen, das sie die christliche lieder unndt psalmen lehrnen
> unndt mit gemeinen kirchengesang unsern hern Gott helffen loben unndt preisen, das sie durch die
> geseng gottlichs worts, so darinnen verfaßet, erinnert unndt daraus ahn rechten erkendnus
> Gottes, ahn glaube, liebe, gedult unndt ahn allen andern tugenden gebeßert werden. Unndt damit
> eine guete ordnung unndt gleichheit in den gesengen getroffen werde, sollen die lieder
> furnemblich, so doctoris Martini Luther[i sind] […].

the pastors shall exhort the people to learn the Christian songs and psalms and to help praise
and extol our Lord God with the common singing of the church, that through the songs they may be
reminded of God's word that is comprised therein, and thereby be bettered in the right knowledge
of God, in faith, love, patience and all other virtues. And that a good order and uniformity may
be kept in the songs, the songs chiefly that are Doctor Martin Luther's [shall be used] […].

### 18.5 Luther's hymns first

From the 1560s several orders put Luther's hymns ahead of all others. The Prussian order of 1568
gives the reason: in them "the whole holy catechism" is set out "with rich, fair and mighty
exposition". **Prussia, *Kirchenordnung und Ceremonien*, 1568** (Sehling 4, p. 75):

<!-- doc 1833 -->
> Es sollen aber nicht allerlei deutsche lieder gesungen werden in der kirche, in dörfern sowohl
> als in stedten, sondern vornehmlich Lutheri psalmen behalten und getrieben werden, denn
> darinnen hat man gar schön den ganzen heiligen catechismum mit reicher, schöner und gewaltiger
> auslegung, erstlich der zehn gebot in zweien gesengen: Dies sind die heiligen zehn gebot etc.
> und: Mensch, willst du leben seliglich etc.; zum andern, die artikel unsers christlichen
> glaubens im: Wir glauben all’ an einen gott etc., zum dritten das gebet im: Vater unser im
> himmelreich etc., den ganzen schatz der heiligen taufe im: Christ, unser herr, zum Jordan kam
> etc., und denn allen nöthigen bericht von dem heiligen abendmahl im: Jesus Christus, unser
> heiland etc., und: Gott sei gelobet etc. Wer denn das summa summarum sammt dem nutzen und
> frommen darvon kurz beisammen haben will, der singe: Nu freut euch, lieben christen gemein
> etc., oder D. Sperati gar schönen psalmen: Es ist das heil uns kommen her etc.

But not all manner of German songs shall be sung in the church, in villages as in towns, but
chiefly Luther's psalms shall be kept and used. For in them one hath most fairly the whole holy
catechism with rich, fair and mighty exposition: first, of the Ten Commandments in two songs,
"These are the holy ten commandments," etc., and "Man, wilt thou live blessedly," etc.; secondly,
the articles of our Christian faith in "We all believe in one God," etc.; thirdly, the prayer
in "Our Father in the kingdom of heaven," etc.; the whole treasure of holy baptism in "Christ our
Lord to Jordan came," etc.; and then all needful instruction of the holy Supper in "Jesus Christ
our Saviour," etc., and "God be praised," etc. Whoso then will have the sum of sums, together
with the use and profit thereof, briefly together, let him sing "Now rejoice, dear Christians
all," etc., or Doctor Speratus's most fair psalm, "Salvation now is come to us," etc.

It then turns on the new hymn-writers (Sehling 4, p. 76):

<!-- doc 1833 -->
> Dass also nicht von nöten ist, allerlei neue lieder aufzuraffen und in die kirchen zu bringen,
> wir haben sie gottlob gut, als sie künden gemacht werden, und mangelt nirgend an, denn dass man
> des teuren schatzes müde und überdrüssig ist, lust und liebe hat, was neues vorzunehmen, bis man
> endlich schier gar von den herrlichen psalmen Lutheri kömmet und ein jeder sein eigen gedicht
> furtreget, welches doch Luthero nicht kan das wasser reichen in genere dictionis oder ponderibus
> rerum. Darum sollen die pfarherren zusehen, den schulmeistern nicht gestatten, ihres gefallens zu
> singen, sondern daran sein, dass die gesenge droben gehalten und fleissig getrieben werden.

So that it is not needful to snatch up all manner of new songs and bring them into the churches.
We have them, God be praised, as good as they can be made, and there is lack nowhere, save that
men are weary and tired of the precious treasure and have lust and love to take up something new;
until at last they come away almost wholly from the glorious psalms of Luther, and everyone
bringeth forward his own poem, which yet cannot hold a candle to Luther in the kind of diction
or the weight of matter. Therefore the pastors shall see to it that they suffer not the
schoolmasters to sing at their own pleasure, but take care that the songs above be kept and
diligently used.

Hoya says the same, and warns that where everyone wants to be a poet, error easily takes root.
It also places boys among the people to teach them. **Hoya, *Kirchenordnung*, 1581** (Sehling 6/2, p. 1151):

<!-- doc 2065 -->
> Die pastorn sollen mit fleis erhalten die psalmen, so vom Doctore Luthero gemacht und man von
> anfang des evangelii gehabt und gesungen, und dieselben fleissig treiben und grossen fleis dran
> wenden, das die leute in der kirchen stets den andern verß singen mögen und der chor so lang
> schweigen. Zu solcher beförderung kan man ein bar knaben unter dem volk stehen oder sitzen
> lassen, die da singen und sich die leute bey denselben also zum singen gewehnen. Man mag auch
> wol andere christliche gesenge, sofern sie rein und Gottes wort gemeß sein, gebrauchen, doch der
> neuerung nicht zuviel machen noch die alten geseng verwerfen. Dann es befindet sich, wo jederman
> tichter sein und seine eigene geseng machen und gebrauchen wil, das leichtlich irrung mit
> einwurzeln mögen.

The pastors shall diligently keep the psalms that were made by Doctor Luther and that have been
had and sung from the beginning of the gospel, and use them diligently, and bestow great
diligence that the people in the church may always sing the second verse and the choir meanwhile
keep silence. For the furtherance of this a pair of boys may be made to stand or sit among the
people, who sing, so that the people accustom themselves to singing along with them. Other
Christian songs also may well be used, so far as they be pure and agreeable to God's word; yet
let not too much novelty be made, nor the old songs rejected. For it is found that where every
man will be a poet and make and use his own songs, error may easily take root therewith.

**Harlingerland, *Kirchenordnung*, 1573/74** (Sehling 7/1, p. 738):

<!-- doc 2122 -->
> Der zwölfte articul. Sectio prima. Von den gesängen, so man in der kirchen gebrauchen soll.
> Ordnen wir, daß die psalmen, so von Doct. Luthero, sel. gedechtniß, gemacht und in den
> psalmboeken gefunden werden, vor andern am meisten sollen gesungen und gebrauchet werden. Jedoch
> wollen wir hiemit an die löbliche gesenge, latein oder teutsch, auf den hohen festtagen bestimpt
> und in dem göttlichen worte fundiret, nit verworfen haben.

The twelfth article, first section: of the songs which shall be used in the church. We ordain
that the psalms which were made by Doctor Luther of blessed memory and are found in the psalm
books shall be sung and used most of all, before others. Yet hereby we will not have rejected the
praiseworthy songs, Latin or German, appointed for the high feast days and grounded in the divine
word.

The same order forbids schoolmasters and sextons to sing hymns "at their pleasure" without the
pastor's knowledge. It forbids songs the people are not used to, and songs "that have the same
tune as worldly songs", at which the common man might take offence (Sehling 7/1, p. 739):

<!-- doc 2122 -->
> auch den scholemeistern und kostern befehlen, daß sie ohne furwißen der pastorn ihres gefallenß
> die psalme nit singen, dazue noch das kaspelsvolk nit gewehnet, noch sonsten die, so weltlicher
> lieder gleiche weiße haben, doran sich der gemeine man ergern möchte.

also command the schoolmasters and sextons that they sing not the psalms at their pleasure
without the foreknowledge of the pastors, [nor such] as the parish folk are not yet used to, nor
otherwise those that have the same tune as worldly songs, whereat the common man might be
offended.

Mansfeld built its seasonal hymn plan from Luther's songbook. It marked with an asterisk the
hymns in that book by "other excellent men". It did not bind other territories to its order.
**Mansfeld, *Kirchen-Agenda*, 1580** (Sehling 2, p. 235):

<!-- doc 1241 -->
> haben demnach d. Luthers deutsches gesang büchlein für uns genomen, und dieselben gesenge so
> darinnen verfasset sein, auf die festa und gemeinen sontage und sonst auf andere tage
> abgetheilet, wie wir vermeinen nach unserem einfalde, das sie zu den predigten am bequemesten
> und den leuten aufs beste einzubilden sein solten. Weil aber in dem gesang büchlein Lutheri,
> auch anderer fürtrefflicher leute gute und geistreiche gesenge mit einverleibet seind, haben
> wir dieselben nicht aussen lassen wollen, sondern an gelegene orter mit hinzu gesetzet, und zum
> unterscheid von doct. Luthers gesengen mit diesem zeichen * notiren wollen.

We have therefore taken Doctor Luther's German songbook before us, and divided the songs contained
therein among the feasts and common Sundays and otherwise other days, as we suppose in our
simplicity that they should be most fitting to the sermons and best to be impressed upon the
people. But because in Luther's songbook good and spiritual songs of other excellent men also
are incorporated, we would not leave them out, but have set them in at fitting places, and to
distinguish them from Doctor Luther's songs we have marked them with this sign: *.

The same Mansfeld article explains why hymns had spread so fast: "as all men are by nature
inclined to sing and have pleasure in music" (Sehling 2, p. 235):

<!-- doc 1241 -->
> Wie nu alle menschen natürlich zu singen geneiget sein und zur musica lust haben, also haben
> sie solche gesenge mit grosser begirde angenomen und aus denselben den grund der warheit fest
> und stark gefasset.

As now all men are naturally inclined to sing and have pleasure in music, so have they received
such songs with great desire, and out of them grasped the ground of the truth firmly and
strongly.

At Langenburg in Hohenlohe the question became a dispute in 1592. The pastor there, Mögner,
objected that singing only Luther's hymns would mean giving up long-used songs by Spengler,
Speratus, Kreuziger, Jonas and others. He appealed to the last paragraph of the 1578 order, to
sing "at all times what is serviceable and answerable to the matter" (Sehling 15, p. 625):

<!-- doc 624 -->
> so wöllen wir, laut des letzten paragraphi hei den gsengen j ederzeit singen, was zur sach
> dienstlich und verantwortlich.

so will we, according to the last paragraph on the songs, sing at all times what is serviceable
and answerable to the matter.

### 18.6 Against private choice and novelty; the authorized books

Hof defended its whole plan against any "unskilled scholar" who might change it at his pleasure.
**Hof, *Ordo ecclesiasticus*, 1592** (Sehling 11, p. 455):

<!-- doc 294 -->
> sintemal nicht einem iden unverstendigen schuler geburen will, in unser schönen und wolbedachten
> kirchenordnung seines gefallens umbzusturen und, was ime in seinem namen gutdeucht, in der
> gemein Gottes zu singen, sintemal die alten auch leut gewesen und freilich ohn großen vorbedacht
> nichts furgenommen haben.

since it will not become every unskilled scholar to overturn at his pleasure our fair and
well-considered church order, and to sing in the congregation of God what seemeth good to him in
his own name; since the old ones were also men, and surely undertook nothing without great
forethought.

Pfalz-Zweibrücken closed its songbook with a ban on novelty, "that constant uniformity be kept,
as well in singing as in preaching". **Pfalz-Zweibrücken, *Kirchenordnung*, 1557**, songbook
(Sehling 18, p. 255):

<!-- doc 968 -->
> Diser obgesetzten Kirchengeseng sollen sich die Pfarrherr und Kirchendiener gebrauchen und ferner
> kein newerung einfüren, damit so wol im Gesang alß in der Predig und teglichen lehre
> Christliche, bestendige gleychheyt gehalten werde.

These church songs set above the pastors and ministers shall use, and bring in no further
novelty, that Christian, constant uniformity be kept as well in singing as in preaching and
daily teaching.

Grubenhagen tied the whole service to Johann Spangenberg's cantional. **Grubenhagen,
*Kirchenordnung*, 1581** (Sehling 6/2, p. 1048):

<!-- doc 2058 -->
> sollen dieselben mit gebürlicher modestien und bescheidenheit ordentlich und gleichstimmig
> gehalten und nichts neues von jemands erdacht oder fürgenommen werden. Wann denn lange zeit hero
> das cantional oder missal des alten herrn Johan Spangenberges in unserm fürstenthumb ublich
> gewesen und dasselbe jeder kirchen in verwahrung und brauch beygelegt worden, sol ein jeder auf
> die Sontag, fest und aposteltage in haltung des kirchenampts mit lectionen, singen, collecten,
> introiten, Kyrie, Patrem, praefationen, hymnis, und was dergleichen mehr ist, nach ordnung der
> zeit sich vleissig richten.

the same shall be held with due modesty and discretion, orderly and with one voice, and nothing
new be devised or undertaken by anyone. Since, then, the cantional or missal of the old master
Johann Spangenberg hath long been customary in our principality, and the same hath been given to
every church for keeping and use, every one shall diligently order himself by it on the Sundays,
feasts and apostles' days in holding the office, with lessons, singing, collects, introits,
Kyrie, *Patrem*, prefaces, hymns and whatever more there is of the like, according to the order of
the season.

Oldenburg required "a right, pure cantional", Spangenberg's or Lossius's, with Luther's German
songbook. **Oldenburg, *Kirchenordnung*, 1573** (Sehling 7/2.1, p. 1085):

<!-- doc 2149 -->
> Zu der behülf ist vonnöten, das in allen kirchen und schulen ein rechtes, reines cantional
> stetigs zur hand sey, als nemlich des alten herrn Johan. Spangebergii oder Lucae Lossii sampt
> dem deudschen gesangbuch D. Martini Lutheri.

For the furtherance of which it is needful that in all churches and schools a right, pure
cantional be always at hand, as namely that of the old master Johann Spangenberg or of Lucas
Lossius, together with the German songbook of Doctor Martin Luther.

It adds that the Luther songbook must be one "printed at no suspect place and unfalsified". This
was aimed at the Reformed-leaning printings of the 1560s and 1570s (Sehling 7/2.1, p. 1087):

<!-- doc 2149 -->
> und mag vor der prediger [!] ein deudschen psalm aus Lutheri gesangbuch, das an keinen
> verdechtigem ort gedruckt und unvorfelschet ist gesungen werden.

and before the sermon a German psalm may be sung out of Luther's songbook, [one] that is printed
at no suspect place and is unfalsified.

Rostock required Lossius in every church, and one melody everywhere. **Rostock, *Conformitas
ceremoniarum*, c. 1560** (Sehling 5, pp. 288–289):

<!-- doc 1936 -->
> Es wird für gut angesehen und notig eracht, das man in allen kirchen halten sol Lucae Lossii
> psalmodia und sol sich das chor darnach richten.

It is thought good and needful that Lucas Lossius's *Psalmodia* be kept in all churches, and the
choir order itself thereby.

<!-- doc 1936 -->
> Es sollen sich auch die schulmeister und cantores bevleissigen, das in allen gesengen musste
> einerlei melodia gehalten werden.

The schoolmasters and cantors also shall be diligent that in all songs one melody be kept.

The Pomeranian *Agenda* ordered every church to buy Lossius's cantional (§8.6).

### 18.7 Latin and German

The orders agree that the congregation sings in German. They differ on how much Latin to keep,
and why. Bugenhagen defended the Latin chants for the sake of the Latin school children. He
reproved those who would have "all things and singing in German, as though it were wrong to sing
a Latin word". **Braunschweig, *Kirchenordnung*, 1528** (Sehling 6/1, p. 438):

<!-- doc 1983 -->
> Wy laven overs nicht, ock schelden nicht, sonder seggen, dat de id eyn weynich to nowe nemen, de
> alle dink unde sank so willen düdesch hebben, gelick efft id unrecht were, eyn latinisch wort
> edder eyn ander to syngen. Dewile doch Paulus recht, me schal mit tungen reden nicht vorbeden.
> Wen de leyen de düdesche misse hebben, so scholen se den latinischen kynderen unde andern to
> gude holden, dat se to tiden singen eyn latinisch Gloria in excelsis, eyn Haleluja, Sanctus,
> Agnus unde sundergen sank, alse sequentien in den dren groten festen, doch düdesch dar mank edder
> darneven gesungen.

We praise not, nor do we chide, but say that they take it a little too strictly who will have all
things and singing in German, as though it were wrong to sing a Latin word or another; since Paul
saith rightly that one shall not forbid to speak with tongues. When the laity have the German
Mass, they shall bear with the Latin children and others, that these sing at times a Latin
*Gloria in excelsis*, an alleluia, Sanctus, Agnus, and special songs, as sequences on the three
great feasts; yet with German sung in among them or beside them.

East Frisia kept the Latin "because we will that the Latin tongue, together with all good arts,
as music, be kept in honour". **Ostfriesland, *Kirchenordnung*, 1535** (Sehling 7/1, p. 380):

<!-- doc 2107 -->
> Wente wy willen, dat de latinische sprake sampt alle gude kunsten, alze de musica, in den
> kercken und scholen in eheren geholden werden.

For we will that the Latin tongue, together with all good arts, as music, be held in honour in the
churches and schools.

Hohenlohe kept the Latin for the schools and added German "for the unlearned and those
inexperienced in the Latin tongue". **Hohenlohe, *Kirchenordnung*, 1553** (Sehling 15, p. 60):

<!-- doc 539 -->
> umb derselbigen willen die lateinische gesang im prauch behalten und darneben auch die teutsche
> gesang vonwegen der ungelerten und d[er lateynischen sprach unerfahren].

for its sake keep the Latin songs in use, and beside them also the German songs, because of the
unlearned and those inexperienced in the Latin tongue.

Hesse (1574) reasoned from 1 Corinthians 14: whoever does not understand cannot say Amen. It
allowed Latin only before the congregation had gathered, and at vespers when few were there. It
also limited the singing before the sermon to half an hour on feast days and a quarter of an hour
on weekdays. **Hessen, *Agende*, 1574** (Sehling 8, p. 411):

<!-- doc 2272 -->
> Wie kann aber einer Amen sagen, zu dem, das er nicht verstehet und nit weiß, was damit gemeint
> ist? 1. Cor. 14. Derhalben, gleich wie alle predigten, gebet und danksagung in bekanter teutscher
> sprach geschehen, also soll auch der gesang, wann der ganze gemeine hauf beieinander ist, teutsch
> sein. Dieweil aber doch in stedten, da mancherlei leut seind, viel erfunden werden, so in schulen
> erzogen und das latein verstehen, dergleichen oftmals frembde leut, welchen diese sprach wol
> bekant, zu den gemeinen versamblungen sich verfügen, mag underweilen im anfang, ehe die ganze
> gemein zusammenkompt, und zur vesper, wann ohn das wenig leut vorhanden, ein lateinischer psalm
> oder introitus gesungen werden, doch daß auf den dorfen durchaus, in stedten aber mehrerteils
> allein teutsche gesenge im gemeinen brauch seien und bleiben. Es söllen auch die gesenge aufs
> kürzest angestellet und vor der predigt auf die feiertage über eine halbe, auf die werktage aber
> über ein vierteil stunde aufs höchste nicht erstreckt werden, damit das volk nicht aufgehalten
> und, ehe dann die predigt angehet, zum überdruß verursacht werden möge.

But how can one say Amen to that which he understandeth not and knoweth not what is meant
thereby? 1 Corinthians 14. Therefore, as all sermons, prayer and thanksgiving are done in the
known German tongue, so also the singing, when the whole common multitude is together, shall be
German. But since in towns, where there are many kinds of people, many are found who were brought
up in schools and understand Latin, and likewise strangers often come to the common assemblies to
whom this tongue is well known, a Latin psalm or introit may be sung at times at the beginning,
before the whole congregation cometh together, and at vespers, when few people are present
anyway; yet so that in the villages wholly, and in the towns for the most part, only German songs
be and remain in common use. The songs also shall be set as short as may be, and before the
sermon shall not be stretched on feast days over half an hour, and on working days over a quarter
of an hour at the most, that the people be not held up, and be caused to weariness before the
sermon beginneth.

Sayn called Latin singing in the papacy "a special punishment of God", citing Isaiah 28 and
1 Corinthians 14 (Sehling 19/1, p. 369):

<!-- doc 1090 -->
> das es bißher beschehen im bapstumb, vor ein sonderlich straff Gottes zu achten, wie Esaias 28
> unndt S. Paulus 1. Corinth. 14 bezeugen. Unndt hatt das ansehen, das solch kirchen gesangh, so
> in unbekanter sprach beschehen, soll seines […] wercks verdienst halben Gottes zorn versohnen.

that it hath hitherto happened in the papacy is to be counted a special punishment of God, as
Isaiah 28 and St Paul, 1 Corinthians 14, bear witness. And it hath the appearance that such
church singing, done in an unknown tongue, was supposed by the merit of its work to reconcile
God's wrath.

### 18.8 Length

Long singing was to be avoided "that such Christian and wholesome ceremonies may remain pleasant
to the people and not become tedious". **Pomerania, *Kirchenordnung*, 1535** (Sehling 4, p. 341):

<!-- doc 1856 -->
> Lange singent dar etlike prestere lust to hebben, schal ut orsake vormeeden werden, dat sulke
> christlike unde heelsamen ceremonien dem volke lüstich bliven, unde nicht vordreetlick werden.

Long singing, wherein some priests have pleasure, shall for this cause be avoided: that such
Christian and wholesome ceremonies may remain pleasant to the people and not become tedious.

Two, or at most three, pieces of figured music at one service are enough, "that the people also
may have room to praise God with song". **Wolfenbüttel, *Kirchenordnung*, 1543** (Sehling 6/1, p. 54):

<!-- doc 1972 -->
> Twe gude stücke edder thom högesten dre in figurativis sind up eine tidt genoch, dat dat volk ock
> rhum hebbe, Got mit sange tho lavende, besundergen under der communion, alse Christus secht:
> Sülck doht tho myner gedechtnisse.

Two good pieces, or at the most three, in figured music are enough at one time, that the people
also may have room to praise God with song, especially during the communion, as Christ saith:
"This do in remembrance of me."

Schönburg held weekday singing and preaching together to one hour, "so the people are kept
willing to go to the sermon and can also come home to work". **Schönburg, *Kirchenordnung*,
1542** (Sehling 2, p. 171):

<!-- doc 1235 -->
> Summa, dass allezeit in der wochen, an werktagen alles singen und predigen in einer stunde
> geschehen und nicht darüber. Se behält man das volk willig zur predigt gehen und kan auch anheimb
> kommen zur arbeit.

In sum, that always in the week, on working days, all singing and preaching be done in one hour
and not beyond. So the people are kept willing to go to the sermon, and can also come home to
work.

### 18.9 The organ

The organ was allowed, "neither commanded nor forbidden". It was not a way of serving God, but
like a trumpet that moves people to pray, hear the word, and come to church. **Bremen,
*Kirchenordnung*, 1534** (Sehling 7/2.2, p. 461):

<!-- doc 2217 -->
> Orgelen unde Musica, de fry syn, noch gebaden noch vorbaden, mach me gebruken, nicht darumme,
> Godt darmede tho denende unde Affgöderye tho stercken unde den rechten Gades denst tho weren,
> alse de Papisten don, sunder alse eine trammete edder süs ein geschrey, dar de minschen mede
> beweget werden unde orsake averkamen, unde tho bidden unde flitich Gades wort tho hören, gelick
> alse Helizeus an der Harpen wyssagede, unde yn de Kercken tho ghande unde tho blivende.

Organs and music, which are free, neither commanded nor forbidden, may be used; not in order to
serve God therewith and to strengthen idolatry and hinder the right service of God, as the
Papists do; but as a trumpet or else a cry, whereby men are moved and get occasion both to pray
and diligently to hear God's word, even as Elisha prophesied at the harp, and to go into the
church and abide there.

Heilbronn grounded the organ in the Psalms and in the pleasure of melody, which stirs the heart.
**Heilbronn, *Kirchenordnung*, 1543** (Sehling 17/1, p. 317):

<!-- doc 781 -->
> unnd dieweil gott in allen dingen in Orgeln, Cimbalen unnd Saitenspielen globt werden soll, wie
> in den hailligen psalmen geschriben ist, und auch der menschen hertz nicht allein durch solche
> liebliche melodey erfreyt und erwechkt, die gottlichen gutthaten zu berichten.

and since God is to be praised in all things, in organs, cymbals and stringed instruments, as is
written in the holy psalms, and the heart of men also is not only gladdened and awakened by such
lovely melody to tell of the divine benefits […].

The organist was to play only after the choir or church had begun, and to agree with the
schoolmaster beforehand. **Buxtehude, *Kirchenordnung*, 1552** (Sehling 7/1, p. 78):

<!-- doc 2082 -->
> schall der organiste in der misse, metten und vesper spelen, dat de chorr edder de ganze kercke
> vorher anhevet und singet. Der schulmeister schall sick stedes vorher mit dem organisten des
> sanges halven vorgliken, alle unschicklicheit und confusion to vorhodende.

the organist shall play at Mass, matins and vespers that which the choir or the whole church
first beginneth and singeth. The schoolmaster shall always agree beforehand with the organist
touching the singing, to prevent all unseemliness and confusion.

Harlingerland forbade organists to play worldly songs. **Harlingerland, *Kirchenordnung*,
1573/74** (Sehling 7/1, p. 739):

<!-- doc 2122 -->
> Und nachdeme an örtern, daselbst örgeln sind, die organisten unfieisig werden befunden und
> weltliche lieder schlagen, dorauß ergerniß erfolgen, aber gleichwoll in der heiligen schrift
> dieselben nit verbotten, sondern damit den allmechtigen zu loben und preisen, ordnen wir, daß
> die organisten mit ernste ihreß dienstes wahrnehmen und herrliche geistliche stucke, der
> hilligen schrift einhell[ig, schlagen].

And since in places where there are organs the organists are found unfaithful and play worldly
songs, whereof offence followeth, although these [organs] are not forbidden in holy Scripture,
but [given] to praise and extol the Almighty therewith, we ordain that the organists attend to
their service earnestly and [play] glorious spiritual pieces, agreeing with holy Scripture.

In polyphonic settings for the court chapel of Württemberg the familiar tune was to be kept in the
tenor or another voice, so the people could recognize it. **Württemberg, *Hofkirchenordnung*,
1560** (Sehling 16, p. 427):

<!-- doc 686 -->
> Zum beschluß soll man alwegen ein teutschen Psalmen singen unnd sich in Compositionibus
> befleissenn, daß die gewonlichen, gepreuchige Melodi uff den Tenor oder ein anndere Stim
> gerichtet werde.

At the close a German psalm shall always be sung, and in the compositions care shall be taken
that the customary, familiar melody be set in the tenor or another voice.

### 18.10 Freedom

Many orders end their rules on singing with a clause of freedom, or leave the choice to the
pastor, and some say plainly that such ceremonies are not laws. Northeim: "such things must be
free and subject to no law" (§8.1). Goslar (1528) left the burial singing to "a godly, reasonable,
learned pastor" (§17.4). Mansfeld did not bind others to its plan (§18.5). Nördlingen's St
George's order (1555), after Naumburg, lets the Gloria be dropped when the hymns after the epistle
are long, "for such ceremonies shall at all times be free for the pastor to change according to
the people's convenience". **Nördlingen, *Ordnung der ceremonien* at St George's, 1555**
(Sehling 12, p. 322):

<!-- doc 373 -->
> Man mag auch wol das Gioria in excelsis außen lassen, wenn die geseng nach [der] epistel etwas
> lang sind; denn solche ceremonien sollen one das dem pfarher nach des volks bequemhait zu endern
> alle zeit frei stehen.

One may also well leave out the *Gloria in excelsis* when the songs after the epistle are somewhat
long; for such ceremonies shall at all times be free for the pastor to change according to the
people's convenience.

---

## 19. Concordance of the orders quoted

Every order quoted in this guide is listed below by region. The table gives:

- **Sehling**: the volume and pages in Sehling's edition.
- **Doc**: the `eko.db` document that holds the text, for full-text lookup. A single database
  record may hold several orders.
- **Hymn practice**: a short note on what the order contributes.
- **§**: the sections where the order is quoted.

**Luther; Saxony and Thuringia; the Harz counties, Magdeburg, Halberstadt and Anhalt**

| Order | Sehling | Doc | Hymn practice | § |
|---|---|---|---|---|
| Wittenberg, Luther, *Formula missae*, 1523 | 1, pp. 8–9 | 2 | wish for vernacular songs near gradual, Sanctus, Agnus; "Gott sei gelobet" after communion | 3.2, 15.2 |
| Wittenberg, Luther, *Deutsche Messe*, 1526 | 1, pp. 14–15 | 3 | German psalm at opening; hymn after epistle; "Wir glauben all"; Sanctus, "Gott sei gelobet", Hus hymn at communion | 3.2 |
| Saxony (Ernestine), *Unterricht der Visitatoren*, 1528 | 1, pp. 169–170 | 9 | songs to differ at feasts; "Mitten wir im Leben" at burial | 17.4, 18.2 |
| Saxony (Albertine), *Kirchenordnung*, 1539 | 1, pp. 271–275 | 30 | sequence or German psalm "as the season requireth"; village hymn "pro introitu"; "Christe du Lamm" to close; wedding psalms | 5.1, 8.1, 15.1, 15.2, 17.2 |
| Albertine Saxony, *Die Cellischen Ordnungen*, 1545 | 1, p. 300 | 33 | Latin chant with kneeling prayer "an stadt des offertorii" | 11.3 |
| Saxony (Albertine), *Kirchenordnung*, 1580 | 1, p. 369 | 44 | communion hymns "one or more" by number of communicants | 14.2 |
| Dresden, *Gottesdienst-Ordnung der Kreuzkirche*, 1574 | 1, p. 555 | 78 | all communion hymns sung when communicants are many | 14.2 |
| Eisfeld, *Verordnung der Visitatoren*, 1554 | 1, p. 562 | 84 | Hus's hymn at communion | 14.1 |
| Pirna, *Kirchenordnung* of Anton Lauterbach, 1555 | 1, pp. 642–643 | 119 | two German hymns per Sunday, by the sense of epistle and gospel | 8.7 |
| Weissenfels, *Ordnung der geseng*, 1578 | 1, pp. 693–694 | 145 | one hymn per Sunday "that fitteth season and gospel" (table in `hymns.db`) | 8.6 |
| Wittenberg, *Kirchenordnung*, 1533 | 1, pp. 704–705 | 148 | German Benedictus first; farced sequences; communion hymns "until the communion is over"; German Te Deum | 4.3, 6.1, 8.2, 14.2, 16.4 |
| Merseburg, *Ordinations-Ordnung*, 1545 | 2, p. 7 | 1210 | *Veni creator* at ordination | 17.5 |
| Naumburg, St Wenzel, *Kirchen-Ordnung*, 1527 | 2, p. 60 | 1218 | "Nun bitten" with added stanza; "Aus tiefer Not" for the offertory | 10.1, 11.3 |
| Naumburg, St Wenzel, *Kirchen-Ordnung*, 1537/1538 | 2, pp. 71–78 | 1219 | three introit-hymns in rotation; troped German Kyries; "All Ehr und Lob"; hymns split around sermon | 5.2, 6.4, 7.4, 8.6, 11.6 |
| Plauen, *Ordnung der Ceremonien*, 1529 | 2, p. 111 | 1227 | *Salve Jesu Christe* | 16.5 |
| Schwarzburg and Stolberg, *Ordenunge der religion*, 1549 | 2, p. 130 | 1230 | people sing the Lord's Prayer hymn | 13.1 |
| Schwarzburg, *Kirchenordnung*, 1574 | 2, pp. 133, 136 | 1230 | *Leisen* from the pulpit; burial hymn | 10.2, 17.4 |
| Reuss, *Kirchen-Ordnung* of Heinrich IV, 1552 | 2, pp. 153–154 | 1234 | song for peace after every sermon | 11.1 |
| Schönburg, *Kirchenordnung*, 1542 | 2, p. 171 | 1235 | "Erhalt uns" in need; no organ at communion; one-hour weekday rule | 11.1, 14.7, 18.8 |
| Mansfeld, *Kirchen-Agenda*, 1580 | 2, pp. 234–238 | 1241 | complaint that Luther's hymns are forgotten; seasonal plan with `*` for non-Luther hymns; baptism hymns | 4.2, 8.7, 17.1, 18.5 |
| Henneberg, *Kirchenordnung*, 1582 | 2, pp. 309–311 | 1247 | prose "Komm, heiliger Geist" to the Latin tune; communion hymns by number; seasonal afternoon hymn | 4.1, 14.2, 16.2 |
| Belrieth and Einhausen (Henneberg), 1566 | 2, p. 330 | 1248 | psalm while people gather | 4.2 |
| Goldlauter (Henneberg), 1566 | 2, p. 333 | 1248 | wedding hymns; sixth commandment | 17.2 |
| Herpf (Henneberg), 1566 | 2, pp. 334–335 | 1248 | German *Kyrie summum*; Hus's "instructive and comforting" hymn | 6.4, 14.1 |
| Meiningen, *Gottesdienst-Ordnungen*, 1562/1566 | 2, p. 340 | 1248 | Gloria left out in winter | 7.5 |
| Obermassfeld (Henneberg), 1566 | 2, p. 343 | 1249 | troped Kyrie "Kyrie, Gott Vater in Ewigkeit" | 6.4 |
| Queienfeld (Henneberg), 1566 | 2, pp. 344–345 | 1249 | Hus hymn split around the consecration; catechism hymn held through each part | 13.2, 16.6 |
| Suhl, *Ordnung des predigamts*, 1562 | 2, p. 351 | 1250 | "Christe du Lamm" to close the communion | 15.1 |
| Sulzfeld and Klein-Bardorf, 1566 | 2, pp. 352–353 | 1250 | German Benedictus for introit; festal hymns for introit | 4.3, 5.4 |
| Wasungen (Henneberg), 1566 | 2, p. 356 | 1250 | three short German Kyries; "Verleih uns Frieden" at the end | 6.4, 15.5 |
| Halle, *Kirchen-Ordnung*, 1543 | 2, p. 436 | 1257 | introit-psalms chosen so the people learn them | 5.6 |
| Aschersleben, *Kirchen-Agenda*, 1575 | 2, p. 478 | 1260 | credal slot rotated over four Sundays | 9.1 |
| Cochstedt, *Kirchen-Ordnung*, 1556 | 2, p. 484 | 1260 | baptism hymn | 17.1 |
| Anhalt, *Kirchen-Ordnung*, 1548 | 2, p. 554 | 1262 | psalm while communicants go into the choir | 11.4 |
| Anhalt, *Ordnung der deutschen Gesänge*, before 1551 | 2, pp. 555–556 | 1262 | German hymns "woven into" sequences; seasonal hymns for three slots; Trinity hymns kept four Sundays | 8.3, 8.7, 11.6 |
| Harzgerode, *Kirchenordnunge*, 1534 (?) | 2, p. 586 | 1263 | Latin and German Gloria by turns; farced sequences | 7.2, 8.3 |

**Franconia, Nürnberg, Nördlingen, the Upper Palatinate and Regensburg**

| Order | Sehling | Doc | Hymn practice | § |
|---|---|---|---|---|
| Nürnberg, Döber's German Mass in the New Hospital, 1525 | 11, p. 56 | 250 | "Nun bitten" printed as the introit | 5.3 |
| Brandenburg-Nürnberg, *Kirchenordnung*, 1533, later appendix | 11, p. 202 | 270 | penitential hymns only for the unrepentant dead | 17.4 |
| Brandenburg-Ansbach, *Ordnung singens und lesens bei den Stiften*, 1533 | 11, p. 316 | 276 | *O crux ave* cut | 16.1 |
| Brandenburg-Ansbach, *Auctuarium*, 1548 | 11, pp. 329–330 | 278 | pure sequences; psalm-hymns for impure graduals "for the people's sake" | 5.2, 8.2 |
| Hof, *Ordo ecclesiasticus*, 1592 | 11, pp. 423–475 | 294 | full Sunday table by slot; kneeling "Nun bitten"; communion hymns by number; baptism, wedding and burial hymns; plan defended against changes | 3.1, 4.1, 6.4, 8.4, 8.8, 10.1, 12.4, 14.2, 16.1, 16.2, 16.7, 17.1, 17.2, 17.4, 18.6 |
| Nürnberg, Veit Dietrich, *Agendbüchlein*, 1545 | 11, p. 502 | 297 | "Als Jesus Christus" at communion | 14.6 |
| Schweinfurt, *Kirchenordnung*, 1543 | 11, p. 641 | 304 | "Erhalt uns" after the sermon | 11.1 |
| Schweinfurt, *Gottesdienstordnung*, 1576 | 11, p. 646 | 304 | four-week plan; "Wir glauben" for "Nun bitten" in Advent | 9.4 |
| Weißenburg, *Kirchenordnung*, 1528 | 11, p. 659 | 308 | hymns covering the preacher's going up and coming down | 10.5, 11.2 |
| Wertheim, *Kirchenordnung*, c. 1555 | 11, p. 716 | 323 | Ten Commandments hymn; "Nun freut euch" as a paraphrase of the creed | 16.6 |
| Nördlingen, *Kirchenordnung* of Kaspar Löner, 1544 | 12, pp. 311–312 | 372 | "Komm heiliger Geist" / "Nun bitten" graded by feast; "All Ehr und Lob"; hymn while the elements are prepared | 4.1, 7.4, 10.1, 11.4 |
| Nördlingen, *Ordnung der ceremonien* at St George's, 1555 | 12, pp. 318–323 | 373 | Gloria left out in Advent; post-epistle list; Sanctus while people gather; freedom clause | 7.5, 8.7, 12.1, 18.10 |
| Nördlingen, *Kirchenordnung*, 1579 | 12, pp. 375–388 | 375 | introit dropped for long psalms and cold; baptism of Christ hymn; thanksgiving day | 5.6, 8.7, 17.6 |
| Pfalz-Neuburg, *Kirchenordnung*, 1543 | 13, p. 72 | 386 | people sing "Wir glauben" while priest sings the *Credo* | 9.1 |
| Regensburg, *Wahrhaftiger Bericht*, 1542 | 13, p. 393 | 432 | Latin Agnus three times; Latin thanksgiving if needed | 14.2 |
| Regensburg, *Kirchenordnung* of Hieronymus Noppus, 1543 | 13, pp. 408–410 | 436 | weekday psalm "that the people may learn"; hymns for the dying | 16.7, 17.3 |
| Regensburg, *Kirchenordnung* of Justus Jonas, 1553 | 13, pp. 419–426 | 440 | Prussian litany and "Erhalt uns" after the epistle; office hymn "if not godless"; "Nun bitten" at an execution | 8.9, 16.1, 17.6 |
| Regensburg, *Kirchenordnung*, 1567 | 13, p. 462 | 450 | "Erhalt uns" as "sequence of the season" | 8.9 |
| Ortenburg, *Gottesdienstordnung*, 1563 | 13, p. 532 | 457 | the Passion at communion | 14.6 |
| Rothenberg, *Vereinigung*, 1618 | 13, p. 550 | 461 | "Gott sei gelobet" as thanksgiving | 15.2 |

**The Palatinate, Württemberg, Hohenlohe and Swabia**

| Order | Sehling | Doc | Hymn practice | § |
|---|---|---|---|---|
| Kurpfalz, provisional *Kirchenordnung*, 1546 | 14, pp. 96–97 | 472 | pure sequence or tract; *Discubuit* and German *Pange lingua* | 8.1, 14.5 |
| Kurpfalz, *Kirchenordnung*, 1556 (with 1577 variants) | 14, pp. 149, 165 | 480 | songs by teaching and season; minister may stop the singing | 12.1, 14.3, 18.2 |
| Hohenlohe, *Kirchenordnung*, 1553 | 15, pp. 60, 74 | 539 | Latin kept beside German; *Salve Regina* abolished | 16.5, 18.7 |
| Öhringen, *Kirchen- und Schulordnungen*, 1582 | 15, p. 503 | 592 | hymns to agree with gospel and sermon; last stanza after sermon | 11.6, 18.3 |
| Neuenstein, *Befehle wegen des Gebetsgottesdienstes*, 1588–1594 | 15, p. 540 | 604 | seven psalm-hymns rotated daily | 16.7 |
| Langenburg, *Befehl an den Pfarrer*, 1592 | 15, p. 625 | 624 | dispute over singing only Luther's hymns | 18.5 |
| Hohenlohe, *Schul- und Gesangsordnung*, 1596 | 15, pp. 653–657 | 628 | hymns before and after the sermon by twelve doctrinal articles; catechism, wedding, burial and communion hymns; rationale | 10.4, 11.5, 16.6, 17.2, 17.4, 18.3 |
| Württemberg, *Kirchenordnung*, 1536 | 16, pp. 107, 109 | 651 | creed or psalm while pastor goes to altar; hymns examined by superintendents | 9.3, 18.1 |
| Württemberg, *Synodalordnung*, 1547 | 16, p. 159 | 660 | installation hymns | 17.5 |
| Württemberg, *Kirchenordnung*, 1553 | 16, p. 252 | 671 | opening hymn before the sermon | 3.4 |
| Württemberg, *Hofkirchenordnung*, 1560 | 16, pp. 427–428 | 686 | choirmaster to follow the season; familiar tune in the tenor | 18.2, 18.9 |
| Limpurg, *Kirchenordnung*, 1610 | 16, pp. 620, 623 | 729 | communion hymn by season; burial hymn split | 14.6, 17.4 |
| Neckarbischofsheim, *Kirchenordnung*, 1560 | 16, p. 672 | 742 | *Salve Regina coeli* "turned upon Christ" | 16.5 |
| Schwäbisch Hall, Brenz, *Kirchenordnung*, 1527 | 17/1, pp. 49, 51 | 755 | people to learn the German Gloria; Latin and German by turns at communion | 7.3, 14.7 |
| Schwäbisch Hall, *Kirchenordnung*, 1543/1615 | 17/1, p. 174 | 763 | burial hymn split around sermon | 17.4 |
| Heilbronn, *Kirchenordnung*, 1530 | 17/1, pp. 285–286 | 770 | *Pange lingua* Latin and German at communion | 14.5 |
| Heilbronn, draft *Gottesdienstordnung*, 1532 | 17/1, pp. 301–302 | 778 | hymn while preacher goes up; German song for the *Salve* | 10.5, 16.5 |
| Heilbronn, *Kirchenordnung*, 1543 | 17/1, p. 317 | 781 | organ grounded in the Psalms | 18.9 |
| Heilbronn, *Ordnung des Kirchengesangs*, 1543 | 17/1, pp. 321–323 | 782 | seasonal office hymns; stanza cut; Te Deum at great communions | 14.5, 16.1, 16.2 |
| Reutlingen, *Ordnung der Schule und des Kirchengesangs*, 1565/1566 | 17/2, pp. 49, 51 | 828 | opening hymn until the preacher is up; "not always the old common fiddle"; list of psalm-hymns | 4.1, 11.5, 18.4 |
| Reutlingen, *Artikel der Schulvisitation*, 1574 | 17/2, p. 58 | 830 | hymn after sermon to fit the text; no repetition | 11.5 |
| Pfalz-Zweibrücken, *Kirchenordnung*, 1557, songbook | 18, pp. 248, 255 | 968 | three German Kyrie-Gloria pairs; no novelty | 6.4, 18.6 |
| Pfalz-Zweibrücken, *Ordnung der Kirchengesänge*, 1565 | 18, pp. 337, 340 | 985 | three-week plan with slot labels; "Nun bitten" every Sunday (table in `hymns.db`) | 3.1, 10.1 |
| Hintere Grafschaft Sponheim, *Kirchen- und Zensurordnung*, 1590/91 | 18, p. 657 | 1021 | longest hymns before sermon, shortest after; short canon | 18.4 |

**Hesse, Nassau, the Middle Rhine, Westphalia, Strasbourg**

| Order | Sehling | Doc | Hymn practice | § |
|---|---|---|---|---|
| Hessen, *Kirchenordnung*, 1566 | 8, pp. 248, 255 | 2257 | psalms while people gather; Ps 51 for the confession; preach on the sung psalms | 4.2, 4.5, 18.4 |
| Hessen, *Agende*, 1574 | 8, pp. 411–412, 455 | 2272 | "Komm heiliger Geist" kneeling, with rationale; creed options; *Leisen*; hymn while pastor comes down; language and length rules | 4.1, 9.1, 10.2, 11.2, 17.5, 18.7 |
| Hessen-Kassel, *Abschied der Kasseler Generalsynode*, 1607 | 9, pp. 75–76 | 2287 | Lobwasser psalms; hymn boards; call for a seasonal and sermon table | 14.6, 18.3 |
| Waldeck, *Kirchenordnung*, 1556 | 9, p. 273 | 2300 | Lord's Prayer hymn, Ten Commandments and creed before the sermon | 10.3 |
| Solms-Laubach, *Kirchenordnung* [1576–1580] | 9, pp. 359–360 | 2311 | seasonal table before the sermon | 10.3 |
| Ysenburg-Birstein, *Kirchenordnung*, 1588 | 10, pp. 620, 628, 632 | 228 | *Leisen* or Lord's Prayer before the sermon; baptism and wedding hymns | 10.3, 17.1, 17.2 |
| Worms, *Agendbüchlein*, 1560 | 19/1, pp. 206, 208 | 1069 | "Nun bitten" or *Leise* before the sermon; no new hymn without superintendent | 10.2, 18.1 |
| Leiningen-Westerburg, *Kirchenordnung*, 1566 | 19/1, p. 267 | 1074 | German hymns at burial instead of the old "singing over" | 17.4 |
| Sayn, *Kirchenzuchtordnung*, 1582 | 19/1, p. 369 | 1090 | Latin singing as God's punishment; people to learn the hymns | 18.4, 18.7 |
| Sayn, *Kirchenordnung*, 1590 | 19/1, p. 407 | 1090 | church sings the Lord's Prayer | 13.1 |
| Strasbourg, *Ordnung des Herren Nachtmal*, 1525 | 20/1, p. 156 | 1279 | Ps 51 or Ps 130 "an stat des Introits" | 5.3 |
| Strasbourg, *Gottesdienstordnung*, 1577 | 20/1, pp. 516, 518 | 1336 | Ps 51 at great communions; no singing, no funeral sermon | 14.6, 17.4 |
| Hanau-Lichtenberg, *Kirchenordnung*, 1573 | 20/2, p. 54 | 1364 | three rules: season, few hymns, hymn matched to sermon | 11.5 |
| Herford, *Kirchenordnung*, 1532 | 21, pp. 176–177 | 1442 | sequences cut and farced; Our Father or "Nun bitten" before sermon | 8.2, 10.1 |
| Dortmund, *Gottesdienstordnung*, 1554 | 21, pp. 208–209 | 1446 | introit defined as the gathering song; hymn for the offertory | 4.2, 11.3 |
| Lippe, *Kirchenordnung* of Antonius Corvinus [1542] | 21, p. 345 | 1460 | Ps 67 or "Dank sagen" while bread and wine are prepared | 11.3 |
| Lippe, *Kirchenordnung*, 1571 | 21, pp. 386–396, 438 | 1462 | village Kyrie while people gather; seasonal slot before sermon; catechism hymns; communion hymns | 4.2, 10.3, 14.2, 16.6, 17.5 |
| Wittgenstein, *Kirchenordnung*, 1563 | 22, pp. 102–103 | 1493 | festal hymns for introits; German Gloria answer; psalm-hymns rotated | 5.4, 7.4, 8.8, 12.1 |
| Wittgenstein, *Kirchenordnung* [1565] | 22, p. 116 | 1493 | "Aus tiefer Not" as a confession | 4.5 |
| Tecklenburg, *Kirchenordnung*, 1543 | 22, pp. 243–244 | 1505 | German psalm for the introit; thanksgiving hymns to close | 5.1, 15.3 |
| Soest, *Kirchenordnung*, 1532 | 22, p. 450 | 1527 | three kneeling boys sing *Veni sancte*; psalm while communicants kneel | 4.1, 11.4 |
| Neuenrade, *Kirchenordnung*, 1564 | 22, pp. 519, 530–531 | 1544 | seasonal post-epistle table; German Agnus | 8.7, 15.1 |
| Lippe, *Deutsche Messe* [c. 1525–1538] | 22, pp. 565–568 | 1549 | "Aus tiefer Not" as introit; early Low German "Allein Gott"; hymn for the offertory | 5.3, 7.3, 11.3 |

**Lower Saxony, Bremen and East Frisia**

| Order | Sehling | Doc | Hymn practice | § |
|---|---|---|---|---|
| Wolfenbüttel, *Kirchenordnung*, 1543 | 6/1, pp. 54–59 | 1972 | German Benedictus without organ; "Allein Gott" inside the Latin Gloria; Trinitarian German Sanctus; figured-music limit | 4.3, 6.1, 7.1, 12.2, 14.6, 18.8 |
| Wolfenbüttel, *Kirchenordnung*, 1569 | 6/1, p. 143 | 1974 | Latin for the scholars, German psalm for the people | 8.1 |
| Braunschweig, Bugenhagen, *Kirchenordnung*, 1528 | 6/1, pp. 438–442 | 1983 | Greek Kyrie defended; songs to rhyme with the feasts; psalm while communicants go to choir; Latin not forbidden | 6.3, 7.3, 9.2, 16.3, 18.2, 18.7 |
| Braunschweig, *Ordnung der ceremonien auf den dorfern*, undated | 6/1, p. 473 | 1988 | whole village service in hymns | 3.3, 15.3 |
| Lüneburg, *Kirchenordnung*, 1564 | 6/1, pp. 543–545 | 2003 | litany-hymn after the epistle; baptism there; *Leisen* before the sermon | 8.9, 10.2 |
| Lüneburg, *Reformatio coenobiorum*, 1555 | 6/1, p. 614 | 2009 | Latin and German Gloria by turns | 7.2 |
| Lüneburg, *Kirchenordnung*, 1575 | 6/1, pp. 659, 663 | 2017 | creed without organ; *Leisen* as "motet"; deliverance-day hymns | 9.2, 10.2, 17.6 |
| Calenberg-Göttingen, *Kirchenordnung*, 1542 | 6/2, pp. 792–795, 814 | 2036 | village psalm for four chants; hymn "anstat des offertorii"; farced sequences; German Te Deum | 5.1, 8.3, 11.3, 16.4 |
| Calenberg-Göttingen, *Kirchenordnung*, 1542, the German Masses | 6/2, pp. 820–825 | 2037 | German sequences; "Mit Fried und Freud" for the gradual; festal *Leise* for the offertory | 8.4, 8.5, 11.3, 12.1 |
| Northeim, *Kirchenordnung*, 1539 | 6/2, pp. 924–926 | 2047 | chant while people gather; choice is free; *Da pacem* to close; German Te Deum | 4.2, 8.1, 15.3, 16.4 |
| Grubenhagen, *Kirchenordnung*, 1581 | 6/2, pp. 1046, 1048 | 2058 | catechism hymn held through each part; Spangenberg's cantional | 16.6, 18.6 |
| Hoya, *Kirchenordnung*, 1581 | 6/2, pp. 1148–1151 | 2065 | German Te Deum at opening; *Leisen* in pulpit; festal closing hymns; Luther's hymns first | 4.4, 10.2, 15.3, 16.6, 18.5 |
| Buxtehude, *Agende*, 1526 | 7/1, p. 70 | 2082 | seasonal hymn before the sermon | 10.1 |
| Buxtehude, *Kirchenordnung*, 1552 | 7/1, pp. 74–78 | 2082 | introit kept if scriptural; creed as offertory without organ; organist to follow the choir | 5.1, 9.2, 15.3, 18.1, 18.9 |
| Verden, *Kirchenordnung*, 1606 | 7/1, pp. 155–158 | 2090 | *Veni sancte* at the altar; gospel-matched psalm; *Leisen*; hymn while preacher vests | 4.1, 8.6, 10.2, 11.2 |
| Osnabrück (Stift), *Kirchenordnung*, 1543 | 7/1, pp. 224–225 | 2096 | creed after the sermon; wedding Te Deum and Ps 128 | 9.2, 17.2 |
| Osnabrück (city), *Kirchenordnung*, 1543 | 7/1, p. 258 | 2099 | "Allein Gott" inside the Latin Gloria | 7.1 |
| Ostfriesland, *Kirchenordnung*, 1535 | 7/1, pp. 376, 380 | 2107 | Kyrie and Gloria as in "Allein Gott"; Latin kept in honour | 6.5, 18.7 |
| Engerhafe, *Liturgie*, 1583 | 7/1, pp. 677–681 | 2119 | offertory hymn with organ; "O Lamm Gottes" split across the rite; communion hymns | 11.3, 13.2, 14.6 |
| Marienhafe, *Kirchenordnung*, 1593 | 7/1, pp. 695, 697 | 2120 | Kyrie "Ach Vater" and Te Deum at opening; hymn agreeing with the sermon | 4.4, 11.5 |
| Harlingerland, *Kirchenordnung*, 1573/74 | 7/1, pp. 738–739 | 2122 | Luther's hymns first; no secular tunes; kneeling boys at the Sanctus | 12.2, 18.5, 18.9 |
| Hildesheim (Stift), *Kirchenordnung für Steuerwald und Peine*, 1561 | 7/2.1, pp. 781–783 | 2129 | German Te Deum at opening; *Leisen*; closing hymn | 4.4, 10.2, 15.3 |
| Hildesheim (city), *Kirchenordnung*, 1544 | 7/2.1, pp. 852–856 | 2136 | hymn covering the prayers at the step and the devesting; Latin for the school | 4.6, 15.4, 16.3 |
| Oldenburg, *Kirchenordnung*, 1573 | 7/2.1, pp. 1085–1089 | 2149 | sexton among the people for the German *Et in terra*; cantionals; "unfalsified" Luther songbook | 7.3, 18.6 |
| Goslar, Amsdorf, *Vom teglichen gots dinst*, 1528 | 7/2.2, pp. 237–238 | 2187 | burial singing left to the pastor | 17.4 |
| Goslar, SS. Simon and Jude, *Neugestaltung des Gottesdienstes*, 1560 | 7/2.2, p. 320 | 2204 | people sing while they gather for the sermon | 4.2 |
| Bremen, *Kirchenordnung*, 1534 | 7/2.2, pp. 460–464 | 2217 | hymns until the last bell; creed as offertory; *O sacrum convivium*; organ as a trumpet | 4.2, 9.2, 14.5, 18.9 |
| Bremen, *Kirchenordnung*, 1561 | 7/2.2, pp. 510, 513 | 2221 | German songs until the people gather; Hus hymn in the old melody | 4.2, 14.1 |

**Schleswig-Holstein, Hamburg, Lauenburg and Hadeln, Mecklenburg, Livonia**

| Order | Sehling | Doc | Hymn practice | § |
|---|---|---|---|---|
| Schleswig-Holstein, *Deutsche Messe* [after 1526] | 23, pp. 56–57 | 1576 | troped Low German Kyrie; stanzas of "Jesus Christus" between the actions | 6.4, 14.4 |
| Hadersleben, *Artikel*, 1528 | 23, p. 64 | 1576 | Latin sequences "with the *Leisen* in them" | 8.3 |
| Schleswig-Holstein, *Kirchenordnung*, 1542 | 23, pp. 89–95, 143 | 1576 | German psalm for introit in villages; three sequences only; song stops with the communion; *O crux ave* condemned; Michaelmas Te Deum | 5.1, 8.2, 14.3, 16.1, 17.6 |
| Hamburg, *Kirchenordnung*, 1529 | 5, pp. 491, 516–530 | 1958, 1960 | "for the people's sake"; introits and joyful songs; farced sequences; creed as offertory; German Agnus; "Van singende"; wedding music | 3.4, 5.4, 8.3, 9.2, 14.4, 15.1, 16.3, 17.2, 18.1 |
| Hamburg, *Kirchenordnung*, 1556 | 5, p. 553 | 1963 | organ between the verses; choir stops with the communion; *Da pacem* to close | 14.3, 15.3 |
| Ritzebüttel, *Kirchenordnung*, 1556 | 5, pp. 557–558 | 1963 | prose "Komm heiliger Geist" for the introit; three German Kyries; "Erhalt uns" after sermon | 5.5, 6.4, 11.1 |
| Lauenburg, *Kirchenordnung*, 1585 | 5, p. 408 | 1953 | installation hymns | 17.5 |
| Hadeln, *Kirchenordnung*, 1526 | 5, p. 468 | 1955 | creed and psalm covering the preacher's movements | 9.3, 11.2 |
| Mecklenburg, *Ordeninge der misse*, 1545 | 5, pp. 151–155 | 1922 | *Leise* as introit; German *Kyrie summum* taught to villages; organ-farced sequences; gospel-matched psalms; Sanctus forms; kneeling close | 5.4, 6.4, 8.3, 8.6, 11.5, 12.2, 14.3, 15.3 |
| Mecklenburg, *Kirchenordnung*, 1552 | 5, pp. 199–201 | 1922 | *Leisen* from the pulpit; "Christe du Lamm" to close; hymns "that they may become known" | 10.2, 15.1, 18.4 |
| Rostock, *Conformitas ceremoniarum*, c. 1560 | 5, pp. 288–290 | 1936 | psalm agreeing with the gospel; "Help Gott" at communion; Lossius and one melody | 11.5, 14.6, 17.4, 18.6 |
| Riga, *Kirchenordnung*, 1530 | 5, pp. 15, 17 | 1897 | Latin or German introit; Kyrie in three tongues; Lord's Prayer hymn at weekday communion | 5.1, 6.2, 13.1 |
| Kurland, *Kirchenordnung*, 1570 | 5, pp. 88, 91, 105 | 1907 | litany-hymn after the epistle; *Leisen* intoned in the pulpit; catechism hymns for Latvians; burial hymns | 8.9, 10.2, 16.6, 17.4 |

**Brandenburg, Silesia, Prussia, Pomerania, Poland, Transylvania**

| Order | Sehling | Doc | Hymn practice | § |
|---|---|---|---|---|
| Brandenburg, *Kirchenordnung*, 1540 | 3, pp. 69–81 | 1746 | hymn at the elevation; village psalm for the offertory; *Discubuit* and German hymns; burial hymns by the course of the procession | 11.3, 12.3, 14.5, 17.4 |
| Brandenburg, *Visitations- und Consistorialordnung*, 1573 | 3, p. 109 | 1748 | installation hymns | 17.5 |
| Tangermünde, *Ritus*, 1603 | 3, p. 339 | 1788 | Christmas *Leise* until Candlemas | 10.3 |
| Liegnitz, *Kirchenordnung*, 1542 | 3, p. 439 | 1809 | creed after the sermon | 9.2 |
| Brieg, *Kirchenordnung*, 1592 | 3, p. 446 | 1809 | Athanasian creed from Triller; hymns to agree with sermon, but known hymns not put under | 9.1, 10.4, 11.4 |
| Teschen, *Kirchenordnung*, 1584 | 3, p. 462 | 1815 | German or Bohemian hymn for the introit | 5.1 |
| Prussia, *Artikel der Ceremonien*, 1525 | 4, pp. 32–33 | 1832 | German psalms for introits; Kyrie in three tongues; Hus hymn and "Gott sei gelobet" | 5.1, 6.2, 14.1 |
| Prussia, *Kirchenordnung*, 1544 | 4, pp. 64–65 | 1833 | rotating introit-psalms; alleluia and psalm list; hymn while priest "takes breath"; Sanctus while communicants come forward | 5.2, 8.7, 11.2, 12.1 |
| Prussia, *Kirchenordnung und Ceremonien*, 1568 | 4, pp. 75–84 | 1833 | Latin and German Gloria by turns; farced sequences; "Nun bitten" before, "Erhalt uns" after every sermon; Luther's hymns first | 7.2, 8.3, 9.1, 10.1, 11.1, 18.5 |
| Danzig, *Kirchenordnung*, 1557, in Sehling's summary | 4, p. 168 | 1844 | same hymns two Sundays running | 18.4 |
| Thorn, *Kirchenordnung*, 1575 | 4, p. 237 | 1844 | hymn before sermon by text and need | 10.4 |
| Pomerania, *Kirchenordnung*, 1535 | 4, pp. 340–344 | 1856 | German Benedictus; Ten Commandments or *Da pacem* while communicants gather; song stops with communion; against long singing | 4.3, 11.4, 14.3, 18.8 |
| Pomerania, *Kirchenordnung*, 1542 | 4, p. 356 | 1859 | Ps 51 for introit; lay "Allein Gott"; gospel-matched psalms; seasonal slot before sermon | 5.2, 7.2, 8.6, 10.3 |
| Pomerania, *Agenda*, 1569 | 4, pp. 435–440 | 1865 | Te Deum for village introit; both German Glorias; gospel-matched psalm; Lossius; boys intone the Sanctus; organ at communion; closing hymns (table in `hymns.db`) | 4.4, 5.2, 7.2, 8.6, 12.1, 14.7, 15.3, 16.2 |
| Stralsund, draft *Kirchenordnung*, 1555 | 4, p. 551 | 1889 | two German Sanctus forms | 12.2 |
| Kronstadt, Honterus, *Reformationsbüchlein*, 1543 | 24, p. 183 | 1666 | German songs after the epistle "if not repugnant to Scripture" | 8.1 |
| Transylvanian Saxons, *Kirchenordnung*, 1547 | 24, pp. 223–245 | 1669 | German Benedictus for the abolished procession; hymn before the sermon by season; office hymns of the season only | 4.3, 10.3, 16.1 |
