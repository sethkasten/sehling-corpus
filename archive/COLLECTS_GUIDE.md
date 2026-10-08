# Collect, Secret and Postcommunion in the Sehling Church Orders

This guide follows the three **presidential prayers** of the medieval Mass through the
evangelical church orders printed in Emil Sehling's *Die evangelischen Kirchenordnungen des XVI.
Jahrhunderts*:
- the **collect** (*collecta*, *oratio*), said after the Gloria and before the epistle;
- the **secret** (*secreta*, *oratio super oblata*), said silently over the gifts at the end of
  the offertory;
- the **postcommunion** (*postcommunio*, *complenda*, *ad complendum*), said after the
  communion;
- on the weekdays of Lent, a fourth: the **prayer over the people** (*oratio super populum*),
  said after the postcommunion before the dismissal.

In the medieval rite all three were **proper**: each Sunday and feast had its own set, printed
together in the Missal. They were also **multiplied**. A Mass of the day could add the collect
of a commemorated feast or octave, or a votive prayer (for peace, for rain, for the ruler). Each
added collect brought its own secret and postcommunion with it, so that two collects meant two
secrets and two postcommunions.

For each prayer the guide asks:
- What did the Lutheran orders **keep** of the old system?
- What did they **strip**?
- What did they **add**?
- What did they **alter**?

It gives particular attention to the claim that the postcommunion was **standardized into a
fixed prayer**, Luther's thanksgiving of 1526, and to the other postcommunions that stood beside
it, among them versions of the old Missal prayers.

**How the guide is laid out.**
- §1 summarizes the findings, and §2 sets out the method and cautions.
- §3 describes the medieval system and Luther's two rulings, of 1523 and 1526.
- §4 deals with the collect, §5 with the secret, and §6 with the postcommunion and, in §6.6, the
  Lenten prayer over the people.
- §7 sets out what was kept, stripped, added and altered.
- §8 is a table by order, and §9 a concordance.
- Appendix A lists the postcommunion texts and their sources.

**Conventions**

- **Quotations.** Every quotation is Sehling's text as it stands in the `eko.db` database built
  from the digitized edition.
  - Footnote numbers, sigla, folio markers and interleaved apparatus are left out.
  - Sehling's own supplied words in square brackets are kept, as are "[!]", "[sic]" and his
    other signs.
  - "[Noten:]" marks and the like are omitted.
  - Spelling and punctuation are as printed, including plain OCR errors.
  - "[…]" marks an omission.
  - Every quotation has been checked against the database text, allowing for OCR noise: at least
    90 per cent of its words must be found there in order. Its page has been checked against the
    edition's page markers.
  - Each quotation is preceded by an HTML comment, invisible when rendered, that names the
    `eko.db` document it was checked against.
- **Translations.** The English is formal-equivalence, in the idiom of the Authorized Version:
  - Word order and clause structure are kept where English allows.
  - Liturgical stock phrases are given in their familiar forms. For example, *Oremus* and "Last
    uns bitten" are "Let us pray".
  - Words the translation supplies are in square brackets.
- **Latin sources.** Where a German prayer renders a Missal prayer, the Latin is given from the
  Roman Missal of the period. Where Sehling's editors identify the source, this is said. Where
  the identification is this guide's own, that is said too.
- **Citations.** Citations are in the form "Sehling volume, page".
  - The half-volumes of the edition are written 6/1, 6/2, 7/1, 7/2.1, 7/2.2, 17/1, 20/1 and so
    on, following the digitized volumes.
  - Each order is named by place, title and date as they appear in Sehling's running heads.
    Where a passage is Sehling's own introduction or apparatus, this is said.
- **Traditions.** Most of the orders cited are Lutheran, and they are not marked. Every order of
  another tradition is marked where it is cited, by its name in brackets after the order, as
  "Kurpfalz 1563 (Reformed)". The traditions follow the inventory in
  [`CHURCH_ORDERS_GUIDE.md`](CHURCH_ORDERS_GUIDE.md), §3:
  - **Moderate Reformed**: the Bucerian and related orders that stood between the Lutheran and
    the Swiss Reformed: Bucer's Strasbourg and the Upper German cities before the Interim,
    Philip of Hesse's church to 1566, Hermann von Wied's Cologne order, and Colmar after 1578;
  - **Radical Reformation**: Thomas Müntzer's Allstedt orders.
  - The mark follows the order cited, not the territory, since a territory could change its
    tradition: Strasbourg is Moderate Reformed until the Interim of 1548 and Lutheran after it.
  - Orders made under or for the Augsburg Interim of 1548 are marked as Interim orders
    (`CHURCH_ORDERS_GUIDE.md`, §4).

---

## Contents

- [1. Summary of findings](#1-summary-of-findings)
- [2. Scope, sources and cautions](#2-scope-sources-and-cautions)
- [3. The medieval system and Luther's rulings](#3-the-medieval-system-and-luthers-rulings)
- [4. The collect](#4-the-collect)
- [5. The secret](#5-the-secret)
- [6. The postcommunion](#6-the-postcommunion)
- [7. Kept, stripped, added, altered](#7-kept-stripped-added-altered)
- [8. Table by order](#8-table-by-order)
- [9. Concordance of the orders quoted](#9-concordance-of-the-orders-quoted)
- [Appendix A. The postcommunion texts and their sources](#appendix-a-the-postcommunion-texts-and-their-sources)

---

## 1. Summary of findings

**1. Luther set the pattern in two steps** (§3).
- **1523, *Formula missae*.** One collect of the day only, "if it be godly". No secret, because
  it fell with the offertory. The proper postcommunions were rejected because "they almost all
  sound of sacrifice". In their place came two of the priest's ablution prayers, *Quod ore
  sumpsimus* and *Corpus tuum*, the same every Sunday.
- **1526, *Deutsche Messe*.** One German collect, and one fixed German thanksgiving after the
  communion: "Wir danken dir, allmächtiger Herr Gott, dass du uns durch diese heilsame Gabe hast
  erquicket …". Sehling's Verden editor, after P. Drews, traces this prayer to the Missal
  postcommunion of the eighteenth Sunday after Pentecost, *Gratias tibi referimus … sacro munere
  vegetati*. Luther changed its petition from "make us worthy" to "make it prosper in us unto
  faith and love".

**2. The collect: kept, proper, and mostly from the Missal** (§4).
- **Kept de tempore.** Every order with a Mass has a collect after the Gloria, of the season or
  feast. The territorial orders print German series by the church year (Saxony 1539 and 1580,
  Lüneburg 1564, Wolfenbüttel 1569, Henneberg 1582, Grubenhagen 1581, Oldenburg 1573, Verden
  1606, Osnabrück 1618).
- **From the Missal.** Sehling's editors trace many of these collects to Missal collects
  (*Excita*, *Concede … nova per carnem nativitas*, *Deus qui hodierna die corda fidelium*),
  mostly by way of the Wittenberg hymnbook of 1533 and the translations of Michael Coelius.
- **Reduced to one, with exceptions.** Luther's rule of one collect was common (Volprecht 1524,
  Mecklenburg 1545). But a **second collect for need** survived: Mecklenburg allows it, and
  Ansbach 1548 requires two, the first for spiritual and the second for temporal things. Hof
  1592 has the votive "for rain and fair weather". The collect for peace after *Verleih uns
  Frieden* (*Deus, a quo sancta desideria*) became the standing second collect at the end of the
  service.
- **Purged.** Collects asking the intercession of the saints went (Hannover 1536). The rest were
  kept "if pure" (Amberg 1550, Henneberg 1582).
- **Added.** Veit Dietrich's **gospel collects** (from 1546) were written on the day's gospel
  rather than the season. Wolfenbüttel 1569 and Soest 1609 allow them. In Buxtehude 1565 each
  Sunday has two collects, a Missal collect before the sermon and Dietrich's after it.
- **Altered.** Collects moved into German so the people could answer Amen (Coburg 1554/55,
  Wolfstein 1574). Hof 1592 still teaches the medieval rules for the collect conclusions.

**3. The secret: abolished** (§5).
- **No secret in any order.** No order keeps a secret, and the corpus has no German version of
  one. It fell with the offertory: Prussia 1525 lists "offertory, secret, *canon minor* and
  *maior*" among the things "of necessity left out".
- **Remnants.** What remains is:
  - the secret's sung ending *Per omnia saecula saeculorum. Amen* before the Preface (Müntzer
    (Radical Reformation), Lippe, Calenberg-Göttingen);
  - its name and place in Dortmund 1554, where the priest makes "an open prayer for all
    magistrates, estates and needs of the whole Christendom" instead;
  - collects for the Church and rulers said aloud under the Sanctus (Döber 1525, Brandenburg
    1540, Calenberg-Göttingen 1542, Pfalz-Neuburg 1543).

**4. The postcommunion: an ordinary prayer, but never only one** (§6).
- **Luther's 1523 prayers.** They were kept in Latin as the priest's devotion (Brandenburg 1540,
  Pfalz-Neuburg 1543) and put into German as the *Complenda* (Strasbourg 1524, Moderate
  Reformed).
- **Proper postcommunions kept for a time.** Some orders kept the proper postcommunions of the
  Missal:
  - the Nürnberg parish Mass and Volprecht (1524), and Coburg 1524;
    - Müntzer (1524, Radical Reformation), with German versions of the Easter postcommunion
      *Spiritum nobis … tuae caritatis infunde* and the Pentecost *Sancti Spiritus … infusio*;
  - Erfurt (1525), which adds the Trinity *Proficiat*;
  - **Calenberg-Göttingen 1542**, which prints, for each feast, Luther's thanksgiving followed
    by a proper postcommunion from the Missal (Advent *Suscipiamus*, Easter, Pentecost). This is
    the last order in the corpus to do so.
- **Luther's thanksgiving became the ordinary.** From the 1530s it is the standard Lutheran
  postcommunion, and some orders still call it "the complenda" (Hatzkerode, Reuss 1552, Breslau
  1550).
- **The alternatives beside it.** Almost every order prints one or two alternatives, "or this":
  - the **Nürnberg thanksgiving of 1533** ("Wir sagen deiner göttlichen Mildigkeit Lob und
    Dank"), an expansion of *Quod ore sumpsimus*. Brandenburg 1540 and Pfalz-Neuburg 1543 sing
    it with Luther's "under one conclusion", as two collects;
  - a German version of the **Corpus Christi collect** *Deus, qui nobis sub sacramento mirabili*
    ("Ach du lieber Herre Gott, der du uns bei diesem wunderbarlichen Sakrament …"): Mecklenburg
    1545, Buxtehude 1565, Oldenburg 1573, Saxony and Mansfeld 1580, Grubenhagen 1581, Nördlingen
    1579;
  - **Döber's prayer** of 1525, taken up by Mecklenburg;
  - Prussia 1544's second collect, sung on alternate Sundays.
- **Without communicants.** Where no one communicated, a free collect, or a "thanksgiving for
  the word of God heard" (Lippe 1571), took the postcommunion's place.

**5. The Lenten prayer over the people: gone from the Mass, kept once in the office** (§6.6).
- **Not at the Mass.** No order keeps the *oratio super populum* or its bidding *Humiliate
  capita vestra Deo* at the end of the Mass. The blessing "over the people" at the end of the
  Lutheran Mass is the Aaronic blessing.
- **At Lauds, in Ansbach.** The Brandenburg-Ansbach order for the collegiate churches (1533)
  strikes out the Lenten Lauds collects that "speak of the fast". In their place it allows "the
  *super populum* that followeth": the prayer over the people of the same day, which asks for
  God's protection without reference to fasting.

**6. The overall pattern** (§7).
- **Kept:** the collect of the day, mostly from the Missal; the shape *Dominus vobiscum*,
  *Oremus*, prayer and long conclusion, *Amen*; the idea of a closing prayer after the
  communion, still often called the *complenda*.
- **Stripped:** the secret entirely; the Lenten *super populum* at the Mass; the proper
  postcommunion (after a transition ending in 1542); commemorations of saints; the automatic
  multiplication of collects.
- **Added:** Luther's fixed thanksgiving; the Nürnberg thanksgiving; Dietrich's gospel collects;
  collects for rulers under the Sanctus; the peace collect at the end.
- **Altered:** Latin to German; the postcommunion from a proper to an ordinary, with
  alternatives; the sacrificial petitions of the old prayers recast as petitions for faith, love
  and the fruit of the sacrament.

---

## 2. Scope, sources and cautions

**What was searched.** The `eko.db` database was searched for the three prayers by name, in
Latin, German and Low German spellings:
- *collecta*, *collecte*, *collecten*, *oratio*, *gebet*;
- *secreta*, *secret*, *stillmesse*, *super oblata*;
- *complenda*, *complende*, *postcommunio*, *post communionem*, *danksagung*, *dancksegginge*;
- *super populum*, *super plebem*, *humiliate capita*, *inclinate capita*, "über das Volk",
  "neiget eure Häupter".

It was also searched for the opening words of the prayers that the orders use after the
communion: *Quod ore sumpsimus*, *Corpus tuum*, *Proficiat*, "Wir danken dir … heilsame Gabe",
"Wir sagen deiner göttlichen Mildigkeit", "wunderbarlichen Sakrament", "heiligen Mut, guten
Rat". Sehling's editorial notes that identify Missal sources ("Röm. Meßbuch", "Missale",
"lateinisches Meßgebet") were read for every order quoted. The passages were then read in
context.

**Related guides.** Three earlier guides overlap with this one:
- [`CANON_IN_GERMAN_MASSES.md`](CANON_IN_GERMAN_MASSES.md) prints the eucharistic part of the
  early German Masses in full, including their offertory, Sanctus collects, thanksgivings and
  postcommunions. Where a text is printed there, this guide cites it rather than repeating it.
- [`PROPERS_GUIDE.md`](PROPERS_GUIDE.md) deals with the other proper parts of the Mass: introit,
  lessons, gradual, offertory chant, Preface, communion chant.
- [`HYMN_PRACTICE_GUIDE.md`](HYMN_PRACTICE_GUIDE.md) deals with the hymns, including *Verleih
  uns Frieden*, after which the peace collect is sung.

Later guides take up related subjects:
- [`MASS_ORDO_GUIDE.md`](MASS_ORDO_GUIDE.md) covers the salutation and collect in the order of
  the Mass, and the service when nobody communicated (§§8, 14).
- [`GENERAL_PRAYERS_TEXT_GUIDE.md`](GENERAL_PRAYERS_TEXT_GUIDE.md) covers the three collects
  read from the pulpit as a family of the general prayer (§15).
- [`OFFICES_GUIDE.md`](OFFICES_GUIDE.md) covers the collects of Matins and Vespers (§§7.1, 7.5).
- [`EXTRAORDINARY_RITES_GUIDE.md`](EXTRAORDINARY_RITES_GUIDE.md) covers the Litany and its
  collects (§22).
- [`LITURGICAL_CALENDAR_GUIDE.md`](LITURGICAL_CALENDAR_GUIDE.md) covers the seasons whose
  collects were kept (§12).

Where an order gives the collect to a deacon or junior minister, as at Hof, see
[`MINOR_ORDERS_DEACONS_ELDERS_GUIDE.md`](MINOR_ORDERS_DEACONS_ELDERS_GUIDE.md).

**Cautions.** Four things limit what the corpus can show:
- **Silence is not absence.** Many orders say only "a collect" or "the collect with the
  blessing", without saying which. Where an order prints a collect series, it may not print the
  rubric for using it, and the reverse.
- **Sources of the German prayers.** The identification of a German prayer with a Latin one is
  in most cases Sehling's editors'. Where the identification is this guide's own, it is marked
  as such. The German is often free.
- **The Missal used.** The editors cite the Roman Missal of their own day, or a diocesan Missal
  (Bamberg, Verden, Bremen, Magdeburg). The Latin texts given here are those of the Roman
  Missal. The Sarum Missal shares most of these collects and postcommunions with the Roman,
  though it numbers the Sundays after Trinity rather than after Pentecost. The German texts
  therefore cannot show whether a prayer came by a Sarum or a Roman route; in the German lands
  the source was in any case the local diocesan Missal.
- **Beyond the corpus.** The corpus ends in the early seventeenth century. It says nothing
  directly about the later Lutheran service books, including the Common Service and its
  postcommunions. §6.2 notes the points of contact.

---

## 3. The medieval system and Luther's rulings

### 3.1 What the reformers inherited

**The three prayers.** In the late-medieval Mass the celebrant said three variable prayers, each
ending with the long conclusion (*Per Dominum nostrum …*):
- the **collect** after the Gloria, sung aloud;
- the **secret** at the end of the offertory, said silently over the bread and wine, of which
  only the closing *Per omnia saecula saeculorum* was sung aloud, as the opening of the Preface
  dialogue;
- the **postcommunion** or *complenda* after the communion, sung aloud.

**Proper and multiplied.** All three changed with the day. They were also added to.
Commemorations of a feast falling on the same day, of an octave, or of a season brought their
own collect, secret and postcommunion. Votive prayers (for peace, for the ruler, for rain or
fair weather) were added in the same way. Sehling's editors gloss the terms where the orders use
them: the *complenda* is "the closing collect" ("die Schlußkollekte", Sehling 20/1, p. 123, n.
29) and "today called the postcommunion" (Sehling 11, p. 49, n. 24).

### 3.2 Luther's *Formula missae*, 1523: one collect, no secret, a new postcommunion

**"Hireling collects."** Luther's preface to the *Formula missae* lists the collects among the
late accretions that made the Mass a sacrifice. **Luther, *Formula missae et communionis*,
1523** (Sehling 1, p. 4):

<!-- doc 2 -->
> ibi cepit missa fieri sacrificium, ibi addita offertoria et collectae mercenariae, ibi
> sequentiae et prosae inter Sanctus et Gloria in excelsis insertae.

there the Mass began to be made a sacrifice; there were added the offertories and the hireling
collects; there the sequences and proses were inserted between the Sanctus and the Gloria in
excelsis.

**The collect: kept, but only one.** The collect of the day is kept, "if only it be godly", and
Luther notes that the Sunday collects mostly are. But it is to be said alone: no commemorations,
no second or third collect. **Luther, *Formula missae et communionis*, 1523** (Sehling 1, p. 5):

<!-- doc 2 -->
> Tertio, sequens oratio illa seu collecta, modo sit pia (ut fere sunt, quae dominicis diebus
> habentur), perseveret ritu suo, sed ea duntaxat unica. Post hanc lectio epistolae.

Thirdly, the prayer or collect which followeth, if only it be godly (as for the most part are
those which are appointed for the Lord's days), let it continue in its accustomed rite, but that
one alone. After this the reading of the epistle.

**The secret: gone with the offertory.** Luther rejects the whole offertory, "whence also it is
called the offertory", because from there on "almost everything soundeth and savoureth of
oblation" (Sehling 1, p. 5). The secret, the prayer over the oblation, falls with it. The text
and the details are given in [`CANON_IN_GERMAN_MASSES.md`](CANON_IN_GERMAN_MASSES.md), §3.1.

**The postcommunion: the proper *complenda* replaced.** The proper postcommunions are rejected
for the same reason: "they almost all sound of sacrifice". In their place Luther puts two of the
priest's private prayers from the ablutions, said aloud in the collect tone. **Luther, *Formula
missae et communionis*, 1523** (Sehling 1, p. 6):

<!-- doc 2 -->
> Sed loco complendae seu ultimae collectae, quia fere sacrificium sonant, legatur in eodem tono
> oratio illa: 'Quod ore sumpsimus, domine'. Poterit et illa legi: 'Corpus tuum, domine, quod
> sumpsimus etc.' mutato numero in pluralem.

But in the place of the complenda or last collect, because they almost all sound of sacrifice,
let that prayer be read in the same tone: "What we have taken with our mouth, O Lord". That
other also may be read: "Thy body, O Lord, which we have received, etc.", the number being
changed into the plural.

The two prayers are:
- ***Quod ore sumpsimus***: *Quod ore sumpsimus, Domine, pura mente capiamus, et de munere
  temporali fiat nobis remedium sempiternum.* "What we have taken with our mouth, O Lord, may we
  receive with a pure mind; and from a temporal gift may it become for us an everlasting
  remedy."
- ***Corpus tuum***: *Corpus tuum, Domine, quod sumpsi, et Sanguis, quem potavi, adhaereat
  visceribus meis …* "Thy Body, O Lord, which I have taken, and thy Blood, which I have drunk,
  cleave unto my inmost parts …"

**What this did to the system.** In one stroke the *Formula missae* reduced the three proper
prayers to one. The collect stayed proper. The secret was gone. The postcommunion became, for
the first time, an **ordinary**: the same prayer every Sunday.

### 3.3 Luther's *Deutsche Messe*, 1526: one collect and a fixed thanksgiving

**The collect.** The *Deutsche Messe* gives one collect, read by the priest "facing the altar"
on a fixed pitch. The example printed is a German collect from the Missal. **Luther, *Deutsche
Messe und ordnung gottis diensts*, 1526** (Sehling 1, p. 14):

<!-- doc 3 -->
> Darnach lieset der priester eine collecten ins F faut in unisono, wie folget. Almechtiger
> Gott, der du bist ein beschutzer aller die auf dich hoffen, an welchs gnad niemand ichts
> vermag noch etwas fur dir gild, lasse deine barmherzigkeyt uns reichlich widerfarn, auf das
> wir durch dein heiliges eingeben denken was recht ist, und durch deine kraft auch dasselbige
> volbringen umb Jesus Christus unsers hern willen. Amen.

Thereafter the priest readeth a collect on F fa ut in unison, as followeth: Almighty God, who
art the protector of all that hope in thee, without whose grace no man is able to do aught, nor
is anything of worth before thee; let thy mercy richly come upon us, that by thy holy
inspiration we may think those things that be right, and by thy power also perform the same; for
Jesus Christ our Lord's sake. Amen.

**Its source.** The first half is the collect *Protector in te sperantium, Deus, sine quo nihil
est validum, nihil sanctum: multiplica super nos misericordiam tuam* (third Sunday after
Pentecost, the fourth after Trinity). The editors of the Lüneburg order identify the Missal
prayer (Sehling 6/1, p. 572, n. 70). The second half follows, in this guide's reading, the
Rogate collect *Deus, a quo bona cuncta procedunt … ut cogitemus, te inspirante, quae recta
sunt, et te gubernante eadem faciamus*. The *Deutsche Messe* collect thus fuses two Missal
collects into one German prayer.

**The postcommunion: a single fixed thanksgiving.** After the communion the *Deutsche Messe* has
one prayer, with no alternative, followed by the Aaronic blessing. **Luther, *Deutsche Messe und
ordnung gottis diensts*, 1526** (Sehling 1, p. 16):

<!-- doc 3 -->
> Darnach folget die collecten mit dem segen. Wir dancken dir, almechtiger herre gott, das du
> uns durch dise heilsame gabe hast erquicket und bitten deine barmherzigkeit, das du uns solchs
> gedeien lassest zu starckem glauben gegen dir und zu brinstiger liebe unter uns allen, umb
> Jhesus Christus unsers herrn willen. Amen.

Thereafter followeth the collect with the blessing. We give thanks unto thee, Almighty Lord God,
that thou hast refreshed us through this salutary gift; and we beseech thy mercy, that thou
wouldest make the same to prosper in us unto strong faith toward thee and unto fervent love
among us all; for Jesus Christ our Lord's sake. Amen.

**Its source.** This is not a new composition but an old postcommunion, recast. The editor of
the Verden order of 1606 points to P. Drews, who traced it to the postcommunion of the
eighteenth Sunday after Pentecost. **Verden, *Kirchenordnung*, 1606, editor's note**
(Sehling 7/1, p. 161, n. 81):

<!-- doc 2090 -->
> zum lateinischen Ursprung der Kollekte (Postcommunio der Messe des 18. Sonntags nach Pfingsten
> im Missale): P. Drews, Beiträge zu Luthers liturgischen Reformen. 1910, 95f.

on the Latin origin of the collect (the postcommunion of the Mass of the eighteenth Sunday after
Pentecost in the Missal): P. Drews, *Beiträge zu Luthers liturgischen Reformen*, 1910, pp. 95f.

The Latin is *Gratias tibi referimus, Domine, sacro munere vegetati: tuam misericordiam
deprecantes, ut dignos nos eius participatione perficias*: "We give thee thanks, O Lord, being
quickened by the sacred gift, beseeching thy mercy that thou wouldest make us worthy of the
partaking thereof." Luther kept the frame ("we give thanks … refreshed by the gift … we beseech
thy mercy"). He changed the petition: not that we be made **worthy** of the sacrament, but that
it **prosper in us** unto faith toward God and love toward one another.

**The result.** One proper postcommunion of the year, made over, became the fixed postcommunion
of the *Deutsche Messe*. Through the Saxon and Low German orders it became the ordinary Lutheran
postcommunion (§6.3).

---

## 4. The collect

### 4.1 One collect, or two

**Luther's rule: one.** The *Formula missae* allowed "that one alone" (§3.2). The early Nürnberg
Masses follow it:
- **Volprecht's Mass, 1524**, lists the parts of the Mass with what is "always said" and "never
  said". Of the collect it says: "only one is said". **Nürnberg, *Deutsche Messe des Priors
  Volprecht*, 1524** (Sehling 11, p. 39):

<!-- doc 247 -->
> Gl[or]ia in excelsis Deo semper dicitur. Collecta: una t[ant]um d[ici]tur. Ep[isto]la,
> Graduale, v[ersus], Alleluja, v[ersus].

Gloria in excelsis Deo is always said. Collect: one only is said. Epistle, gradual, verse,
Alleluia, verse.

- **The Nürnberg parish churches, 1524**: "the celebrant sings the Sunday prayer, *Sancti tui
  nominis* etc." (Sehling 11, p. 46). Sehling's note explains: "the prayer falling on the Sunday
  in question (the collect)".

**The memorial collect survives as a prayer "for need".** Mecklenburg 1545 keeps Luther's rule
but leaves room for a second collect in time of need. It also forbids reading the same collect
every time, and reading a collect out of its season. **Mecklenburg, *Ordeninge der misse*,
1545** (Sehling 5, p. 152):

<!-- doc 1922 -->
> Me schal ock men eine collecten tor tidt lesen. Idt were den sake, dat ander grot noth
> vorhanden were, de noch ein ander gebet vorderde. Ein ider wert de gebede ordenen na
> gelegenheit, dat nicht stedes ein collecte gelesen werde. Ock nicht in dem osterfeste, de
> collecten van den winachten, sonder ordentlick hir mede handelen, wo truwen husholderen to
> behort.

One shall also read but one collect at a time, unless it were that some other great need were at
hand which required yet another prayer. Each shall order the prayers according to the occasion,
that not always the same collect be read; nor at the feast of Easter the collects of Christmas;
but [each shall] deal herein in order, as becometh faithful stewards.

**Two collects as the rule: Ansbach 1548.** The Ansbach *Auctuarium* of 1548, an Interim order,
goes back to the medieval pattern of a collect of the day followed by a second, votive collect.
It requires two, and fixes their subjects: the first for spiritual things, the second for
temporal goods. **Brandenburg-Ansbach-Kulmbach, *Auctuarium*, 1548**
(Interim order; Sehling 11, p. 330):

<!-- doc 278 -->
> Auf solch gesang volgen in der kirchenordnung etlich viel gestelte collecten oder gebet,
> daraus jedesmals zwo collecten nach gelegenhait der zeit für allerlei anligen der christenhait
> und des volks genommen werden solln. Doch das die erste collect allwegen für gaistliche sachen
> sei und die ander umb zeitliche gueter als frid, gut wetter, für die frucht des feldes etc.,
> allerding, wie in der kirchenordnung vermeldet wurd.

After such singing there follow in the church order very many collects or prayers set forth, out
of which each time two collects shall be taken according to the occasion of the time, for all
manner of concerns of Christendom and of the people; yet so that the first collect be always for
spiritual things, and the second for temporal goods, as peace, good weather, for the fruit of
the field, etc., altogether as is set forth in the church order.

**"One or more."** Other orders leave the number open:
- **Henneberg**: a pastor's report has "a collect or two, as need requireth" after the sermon
  (Sehling 2, p. 330).
- **Wolfstein 1574**: "one or more collects according to the occasion of the time etc., and
  these shall be in German and not Latin" (Sehling 13, p. 576).

**The second collect for peace.** The commonest second prayer is the collect for peace. Luther's
*Verleih uns Frieden* was sung at the end of the service with a German collect after it, "Herr
Gott, himlischer Vater, der du heiligen Mut, guten Rat und rechte Werke schaffst …". This is the
Missal collect of the Mass for peace, *Deus, a quo sancta desideria, recta consilia, et iusta
sunt opera* (Sehling 6/2, p. 819, n. 71). It appears in at least twelve orders of the corpus,
from Saxony 1539 to Schaumburg 1614. In Calenberg-Göttingen 1542 it follows the proper
postcommunion, so that the Advent Mass ends with two collects, the proper one and the one for
peace (§6.2).

**Hof 1592: "of the season, or for rain".** At Vespers the Hof deacon sings "the collect of the
season, or also for rain and fair weather" (Sehling 11, p. 429). The votive collects *ad
petendam pluviam* and *ad poscendam serenitatem* of the Missal survive here by name.

### 4.2 The collect of the day kept, in German

**Saxony 1539.** The order of Duke Henry has the collect "in Latin or German, the common one or
*quotidianam*, or *de festis*, as they stand hereafter at the end". **Saxony, *Kirchenordnunge
zum anfang*, 1539** (Sehling 1, p. 274):

<!-- doc 30 -->
> Darnach eine collecten, auch latinisch oder deudsch, die gemeine oder quotidianam, oder de
> festis, wie sie hernach zu end stehen.

Thereafter a collect, also in Latin or German, the common one or [the] daily one, or [one] of
the feasts, as they stand hereafter at the end.

The collects at the end are headed "collects or prayers which one may read in the church under
the office of the Mass (before the epistle) and also otherwise" (Sehling 1, p. 275). They are
grouped by season: Advent, Christmas, and so on.

**Collect series by the church year.** The later territorial orders print a series of German
collects for the seasons and feasts:
- **Saxony 1580** and **Mansfeld 1580** (Sehling 1, p. 375; 2, pp. 227–229);
- **Lüneburg 1564** and **Wolfenbüttel 1569** (Sehling 6/1, pp. 568–572 and 178–179);
- **Henneberg 1582** (Sehling 2, p. 317);
- **Grubenhagen 1581** (Sehling 6/2, pp. 1076–1081);
- **Verden 1606** and **Osnabrück 1618** (Sehling 7/1), **Oldenburg 1573** (Sehling 7/2.1) and
  **Schaumburg 1614** (Sehling 7/2.2).

Henneberg introduces its series as "pure collects", partly in use before, partly new.
**Henneberg, *Kirchen ordnung* of Georg Ernst, 1582** (Sehling 2, p. 317):

<!-- doc 1247 -->
> Volgen die collecten, nach ordnung der zeit und festen im jar. Auf das die pfarrherrn und
> kirchendiener die versikel und reine collecten beisamen haben mögen, ist fur gut angesehen
> worden, dieselben hiernach zu setzen. Und sind solche gutes teils hiebevor auch, ausserhalb
> etlicher, welche zum teil nach gelegenheit dieser ordnung und dann auch sonsten von neuem
> hinzugesetzt worden, in unserer kirchen gebreuchlich gewesen, und erstlich die, so auf gewise
> fest und zeiten, volgends andere gemeine, so nach gelegenheit jeder vorfallender not und
> sonsten pflegen gesungen zu werden.

Here follow the collects, according to the order of the seasons and feasts in the year. That the
pastors and ministers of the church may have the versicles and pure collects together, it hath
been thought good to set them down hereafter. And such have for a good part been in use in our
churches heretofore also, except some which have been newly added, partly by occasion of this
order and partly otherwise; and first those [appointed] for certain feasts and seasons, then
other common ones, which are wont to be sung according to the occasion of every need that
falleth out, and otherwise.

**The proper collect kept with its versicle.** Henneberg's "versicles and pure collects" keep
another medieval habit: the collect introduced by a seasonal versicle. Its Advent set begins
"Bereitet den weg dem herrn, halleluja" (Sehling 2, p. 317). Hof 1592 does the same before its
festal collects ("Uns ist ein kind geboren", Sehling 11, p. 413).

**What the German collects are.** Sehling's editors trace most of the seasonal collects of the
Saxon and Lower Saxon series back to the **Wittenberg hymnbook of 1533**, and through it to the
Missal. Lüneburg's Advent collect is a typical case. **Lüneburg, *Kirchenordnung*, 1564**
(Sehling 6/1, pp. 542–543):

<!-- doc 2003 -->
> Darauf wende sich der priester widerumb jegen den altar und singe eine collecten de tempore
> oder festo oder die sich zu der materien schicken auf folgende melodey: […] Last uns beten:
> Allmechtiger Herre Gott, weck uns auf, das wir bereit sein, wenn […] dein Son kümpt, ihn mit
> freuden zu empfahen und dir mit reinem herzen zu dienen durch denselbigen deinen Son Jhesum
> Christum, unsern Herrn.

Thereupon let the priest turn again toward the altar and sing a collect of the season or of the
feast, or one that agreeth with the matter, to the following melody: […] Let us pray. Almighty
Lord God, stir us up, that we may be ready, when thy Son cometh, to receive him with joy and to
serve thee with a pure heart; through the same thy Son Jesus Christ our Lord.

This is the Advent collect *Excita, Domine, corda nostra ad praeparandas Unigeniti tui vias: ut
per eius adventum purificatis tibi mentibus servire mereamur*. Sehling's editors identify it as
the collect of the second Sunday in Advent (Sehling 6/2, p. 1077, n. 86; 7/1, p. 93, n. 7). "Mit
reinem herzen zu dienen" is *purificatis mentibus servire*. The Missal's "prepare the ways of
thine Only-begotten" becomes "that we may be ready … to receive him with joy". The same collect
stands in Saxony 1580, Mansfeld 1580, Grubenhagen 1581, Buxtehude 1565 and Ysenburg-Birstein
1588.

**Other Missal collects identified by the editors.** In the notes to Lüneburg, Grubenhagen,
Osnabrück and Oldenburg the editors identify, among others:
- Christmas: *Concede, quaesumus, omnipotens Deus, ut nos Unigeniti tui nova per carnem
  nativitas liberet* (third Mass of Christmas; Sehling 7/1, p. 271; 7/2.1, p. 1134);
- Ascension: *Concede, quaesumus, omnipotens Deus, ut qui hodierna die Unigenitum tuum … ad
  caelos ascendisse credimus* (Sehling 6/2, p. 1078, n. 97);
- Pentecost: *Deus, qui hodierna die corda fidelium Sancti Spiritus illustratione docuisti*
  (Sehling 6/2, p. 1079, n. 99);
- the third Sunday after Easter (Sehling 6/1, p. 573, n. 76).

Pentecost is identified in Osnabrück too (Sehling 7/1, p. 275). The introduction to the
Oldenburg order sums up its very large collection: of all its collects only two are its own, and
of these "the one rests upon a Latin Mass prayer" (Sehling 7/2.1, p. 962).

### 4.3 The collects purged

**"If it be pure."** The condition Luther set ("if only it be godly") recurs:
- **Amberg 1550**: "the collect of the season, if it be pure, and the epistle in Latin"
  (Sehling 13, p. 286).
- **Henneberg 1582**: "pure collects" (above).

**Collects removed.** The collects that went were those of the saints, and above all those that
asked for the intercession of Mary and the saints. Hannover 1536 names them with the Marian
antiphons. **Hannover, *Kirchenordnung*, 1536** (Sehling 6/2, p. 1009):

<!-- doc 2051 -->
> Was wider Gottes wort ist, lassen wir nimer singen oder lesen, es sey deudsch oder latin.
> Darumb haben wir abgestelt das Salve regina, Regina celi, Sub tuum presidium und etliche
> collecten, darinnen die ehre, so allein unserm einigen mitler Jhesu Christo zugehört, allzu
> grob den creaturn zugelegt wird.

Whatsoever is against God's word we will never suffer to be sung or read, be it German or Latin.
Therefore we have put away the Salve regina, the Regina caeli, the Sub tuum praesidium, and
certain collects wherein the honour that belongeth to our one Mediator Jesus Christ alone is all
too grossly given to the creatures.

**Luther on the office collects.** Already in 1523 Luther had set aside the antiphons,
responsories and collects "of the saints and of the cross" until "they be swept", "for there is
grievous much filth therein" (Sehling 1, p. 3).

### 4.4 New collects added: the gospel collects

**Veit Dietrich's collects.** The chief addition was a new kind of collect: one written on the
**gospel of the day**, as a summary of the sermon, rather than on the season. The source was
Veit Dietrich's *Kinderpostille* and *Summarien* (from 1546). Wolfenbüttel 1569 allows them in
place of the season's collect. **Wolfenbüttel, *Kirchenordnung*, 1569** (Sehling 6/1, p. 179):

<!-- doc 1974 -->
> Es mögen auch zu zeiten auf den Sontagen und feirtagen die collecten accommodiret werden auf
> die lehre, so aus dem evangelio gehandelt wird, wie solche collecten in der kinderpostillen
> Viti Didrichs zu finden sind.

There may also at times on the Sundays and holy days the collects be accommodated to the
doctrine that is handled out of the gospel, as such collects are to be found in the children's
postil of Veit Dietrich.

Other orders allow the same:
- **Lippe, Corvinus's order of 1542**: a later hand adds that "there stand also certain fine
  collects in the postil of Veit Dietrich, appointed for all Sundays and feasts"
  (Sehling 21, p. 352, apparatus).
- **Soest 1609**: "a collect … that agreeth with the gospel, or else a common collect for the
  grace of the Holy Ghost for the sermon" (Sehling 22, p. 488).
- **Lüneburg 1564**: "or one that agreeth with the matter" (above).

**Two collects again: one before and one after the sermon.** In the Buxtehude agenda of 1565
each Sunday has two collects, the old and the new. Sehling's introduction describes the
arrangement. **Buxtehude, *Agende*, 1565, editor's introduction** (Sehling 7/1, p. 67):

<!-- doc 2080 -->
> In der ersten Kollektensammlung für die Sonn- und Festtage des Jahres wechselt meistens ein
> dem Missale entlehntes, freilich ins Niederdeutsche und teilweise sehr frei übertragenes Gebet
> mit einer Evangelienkollekte Veit Dietrichs, wobei das eine Gebet vor, das andere nach der
> Predigt zu sprechen ist. Diesem Kollektenzyklus liegt eine in verschiedenen Ausgaben
> erschienene Sammlung des Mansfelder Hofpredigers Michael Coelius (1492-1559) zugrunde. Eine
> zweite Kollektensammlung gegen Schluß der Agende stellt alte lateinische Meßgebete,
> stellenweise etwas überarbeitet, zusammen.

In the first collection of collects for the Sundays and feasts of the year there alternate for
the most part a prayer borrowed from the Missal (rendered, indeed, into Low German and in part
very freely) and a gospel collect of Veit Dietrich, the one prayer to be said before the sermon
and the other after it. Underlying this cycle of collects is a collection by the Mansfeld court
preacher Michael Coelius (1492–1559), which appeared in various editions. A second collection of
collects toward the end of the agenda brings together old Latin Mass prayers, here and there
somewhat revised.

An example of the Missal collect "before the sermon" is that of the third Sunday after Epiphany,
*Omnipotens sempiterne Deus, infirmitatem nostram propitius respice, atque ad protegendum nos
dexteram tuae maiestatis extende*. Sehling's note cites the Verden Missal for it
(Sehling 7/1, p. 98, n. 62). **Buxtehude, *Agende*, 1565** (Sehling 7/1, p. 98):

<!-- doc 2082 -->
> Am drudden Sondag. Gebett vor der predig. Almechtige Herr Godt, du woldest gnedichlick
> behertigen unsere swackheit und dyne gewaldigen hand utrecken, uns vor unsern vienden to
> schutten, dorch Jhesum Christum, unsern Hern. Amen.

On the third Sunday. Prayer before the sermon. Almighty Lord God, mayest thou graciously take to
heart our weakness, and stretch forth thy mighty hand to defend us against our enemies; through
Jesus Christ our Lord. Amen.

**Michael Coelius.** The editors name the source of many of these German Missal collects: the
collection of the Mansfeld court preacher **Michael Coelius**, who "translated a Latin Mass
prayer into German for his collection of collects"
(Sehling 7/2.1, p. 1137, n. 35; 7/1, p. 92, n. 1). The old proper collects thus came into the
Lutheran orders by two routes. The first was Luther's circle and the Wittenberg hymnbooks
(1529–1533). The second was Coelius's translations.

### 4.5 Language, voice and form

**Latin or German.** The early orders allowed either:
- **Bremen 1534**: "a collect in Latin out of the Mass book, or in German out of the hymnbook"
  (Sehling 7/2.2, p. 459);
- **Saxony 1539**: "also in Latin or German" (above);
- **Amberg 1550**: the collect of the season, in Latin (above).

Later orders required German, so that the people could say the Amen. **Coburg, *Vorschaffung* of
the visitation of 1554/55** (Sehling 1, p. 544):

<!-- doc 74 -->
> Zum dritten, das keine collecten lateinisch, sondern alle sampt deutsch gesungen werden,
> dormit das volk vorstehen und amen dorzu singen moge.

Thirdly, that no collects be sung in Latin, but all together in German, that the people may
understand, and sing Amen thereto.

Wolfstein 1574 says the same ("in German and not Latin", Sehling 13, p. 576). Mecklenburg 1545
has the collect read "with a loud voice, that the whole church may say Amen and so cry unto God
with the priest" (Sehling 5, p. 152).

**Facing the altar.** Luther's *Deutsche Messe* has the collect read "with the face turned to
the altar", the epistle "with the face turned to the people" (Sehling 1, p. 14). Lüneburg 1564
keeps the rule (above). Hof 1592 has the deacon sing the collect "facing the people" (*spectans
populum*, Sehling 11, p. 425).

**The conclusions.** Hof 1592 keeps the medieval rules for ending a collect, set out as in the
old rubrics. **Hof, *Ordo ecclesiasticus*, 1592** (Sehling 11, p. 411):

<!-- doc 294 -->
> Notio de collectis! Quandocunque oratio dirigitur ad Patrem solum, in fine dicatur: Per
> Dominum nostrum Jesum Christum etc. Si vero dirigitur ad Patrem et Filii mentio fit in ipsa,
> in fine dicatur: per eundem Dominum nostrum Jesum Christum. Si oratio dirigitur ad Filium
> solum, finis sic formetur: Qui cum Patre et Spiritu Sancto vivis et regnas Deus per omnia etc.

A note on the collects! Whensoever the prayer is directed to the Father alone, let there be said
at the end: Through our Lord Jesus Christ, etc. But if it be directed to the Father, and mention
of the Son be made in it, let there be said at the end: through the same our Lord Jesus Christ.
If the prayer be directed to the Son alone, let the ending be formed thus: Who with the Father
and the Holy Ghost livest and reignest, God, world without end, etc.

**Hof's collects at Mass.** At the Mass itself Hof's deacon sings "the collect of the season, or
one directed to the Lord's Supper". After the communion he sings "a collect, for example the
thanksgiving for the Lord's Supper received" (Sehling 11, pp. 425–426). Its example of a Mass
collect is the *Deutsche Messe* collect "O allmechtiger Gott, der du bist ein beschützer aller"
(Sehling 11, p. 425).

---

## 5. The secret

### 5.1 Abolished with the offertory

**No order keeps the secret as a prayer over the gifts.** The secret was the offertory's own
prayer: it asked God to receive the gifts offered. Luther's rejection of the offertory (§3.2)
took it with it, and the orders that name the secret do so only to say it is left out:
- **Volprecht, 1524**: "the offertory is never said, because Christ was once offered for our
  sins" (Sehling 11, p. 39). There is no secret in his list.
- **The Nürnberg parish Mass, 1524**: after the Creed the celebrant goes straight to *Dominus
  vobiscum* and *Sursum corda*, "the offertory and the lesser canon being omitted" (*offertorio
  ac canone minore omissis*, Sehling 11, p. 47).
- **Prussia 1525** names the secret outright. **Prussia, *Artikel der ceremonien und anderer
  kirchenordnung*, 1525** (Sehling 4, p. 32):

<!-- doc 1832 -->
> Volgt die prefation, welche der priester deütsch singet samt den evangelischen worten der
> gebenedeiung oder consecration oder brod und wein (den offertorium, secret, canon minor und
> maior werden notwendig ausgelassen).

There followeth the Preface, which the priest singeth in German, together with the evangelical
words of the blessing or consecration of bread and wine (for the offertory, the secret, the
lesser and the greater canon are of necessity left out).

**Never a German secret.** The Lutheran orders translated collects and postcommunions from the
Missal, but the corpus has no German version of any secret. The secrets were the prayers that
most plainly asked God to accept an offering. Unlike the collects, they could not be "purified"
by a light change of wording.

### 5.2 What took the secret's place

**Its last words.** The secret ended aloud with *Per omnia saecula saeculorum. Amen*, which ran
straight into *Dominus vobiscum* and *Sursum corda*. Three German Masses keep this ending before
the Preface dialogue, though the silent prayer is gone:
- Müntzer (Radical Reformation): "durch alle ewigkeit der ewigkeit. Amen";
- Lippe: "Durch alle ewicheit der ewicheit amen";
- Calenberg-Göttingen 1542: "Gott sey preis von ewigkeit zu ewigkeit. Amen".

See [`CANON_IN_GERMAN_MASSES.md`](CANON_IN_GERMAN_MASSES.md), §1.1 and §4.1.

**An open prayer at the same place.** Dortmund 1554 keeps the heading *Secreta* and says what is
to be done there instead. The silent prayer over the gifts becomes an open prayer for the
magistrates and the needs of Christendom, if the general prayer has not already been said after
the sermon. **Dortmund, *Gottesdienstordnung*, 1554** (Sehling 21, p. 209):

<!-- doc 1446 -->
> Secreta Vor de Secreta mach de Prester ein apen gebedt don vor alle Overicheit, stenden unde
> nodtsaken der gantzen Christenheit, dar he medde an de Prefation kome, so he na der predike
> dat gemene bedt nicht gedan hedde edder sus ein ander na gelegenheit der tydt.

Secret. In place of the Secret the priest may make an open prayer for all magistrates, estates
and needs of the whole Christendom, wherewith he may come to the Preface, if he have not made
the common prayer after the sermon; or else another, according to the occasion of the time.

**Collects under the Sanctus.** In several orders the space between the offertory and the Verba
was filled with **collects said aloud** for the Church and the magistrates. They stood under the
Sanctus, before or after the Verba:
- **Döber, Nürnberg 1525**: an optional "common prayer, to be said on a holy day when there is
  much people, after the Preface or before the Sanctus, as one will" (Sehling 11, p. 55). See
  [`CANON_IN_GERMAN_MASSES.md`](CANON_IN_GERMAN_MASSES.md), §8.11.
- **Brandenburg 1540**: four German collects under the Latin Sanctus (§12.2 of that guide).
- **Calenberg-Göttingen 1542**: "the collect which the priest prayeth under the Sanctus", headed
  "Für die oberkeit". It is printed in every proper Mass of the order: "Folget die collecten,
  welche der priester under dem Sanctus betet: Barmherziger himlischer Vater …"
  (Sehling 6/2, p. 819, and again in each proper Mass, pp. 821–833). See §13.1 of that guide.
- **Pfalz-Neuburg 1543**: three collects under the Sanctus, after the Verba (§14.4 of that
  guide).

These are not secrets. They are not proper to the day, they say nothing of gifts, and they are
said aloud. But they occupy the secret's place, and like the medieval memorial collects they
pray for the ruler and for peace.

**A prayer over the gifts, once.** Only Pfalz-Neuburg 1543 has a prayer said over the bread and
wine before the Verba: Osiander's "Wir bringen … dise deine gaben". It is a new composition, not
a secret. See [`CANON_IN_GERMAN_MASSES.md`](CANON_IN_GERMAN_MASSES.md), §14.2.

**In sum.** Of the three proper prayers the secret alone vanished without a successor of its own
kind. What survives is its closing doxology, its place (filled with intercessions), and in one
order its name.

---

## 6. The postcommunion

### 6.1 Luther's 1523 substitutes: *Quod ore sumpsimus* and *Corpus tuum*

**In Latin.** Brandenburg 1540 and Pfalz-Neuburg 1543 keep both of Luther's prayers in Latin.
The priest says them "bowing", after the German thanksgiving (Sehling 3, p. 70; 13, p. 76). The
texts are given in [`CANON_IN_GERMAN_MASSES.md`](CANON_IN_GERMAN_MASSES.md), §12.8 and §14.8.
Here they have become the priest's own devotion again, said after the people's thanksgiving,
which is what they had been in the Roman rite.

**In German.** The Strasbourg Mass of Theobald Schwarz (1524, Moderate Reformed) gives *Quod ore
sumpsimus* in German under the old name *Complenda*. It also allows "any other that seemeth
Christian". **Strasbourg, the early agendas: Schwarz's German Mass, 1524**
(Moderate Reformed; Sehling 20/1, p. 123):

<!-- doc 1279 -->
> Complenda Laßt uns bitten: Das wir mit mund haben zu uns genomen, verlyhe uns, herr, uff das
> wir dasselbig mit reynem gemüt annemen, und das uns von der zeytlichen goben werde eyne ewige
> artzenyg, durch Christum Jesum, unsern herrn, Amen. Vel aliam aliquam, que Christiana videtur.

Complenda. Let us pray. What we have taken with our mouth, grant us, O Lord, that we may receive
the same with a pure mind; and that from the temporal gift there may be made unto us an
everlasting medicine; through Christ Jesus our Lord. Amen. Or some other that seemeth Christian.

The printed *Teutsche Meß* of 1524 has the same text (Sehling 20/1, p. 133). The Strasbourg
*Ordenung und inhalt Teutscher Mess* (also Moderate Reformed) explains the term for the people:
"Complenda: the conclusion with a common prayer" (Sehling 20/1, p. 135). Volprecht's German Mass
has a German *Quod ore* too ([`CANON_IN_GERMAN_MASSES.md`](CANON_IN_GERMAN_MASSES.md), §7.2).

### 6.2 Proper postcommunions kept

**Not every early order followed Luther.** Several kept the proper *complenda* of the day,
either in Latin or in a German version.

**Nürnberg, 1524.** The Latin Mass of the Nürnberg parish churches ends with the day's
postcommunion. **Nürnberg, *Gottesdienstordnung der Pfarrkirchen*, 1524** (Sehling 11, p. 49):

<!-- doc 249 -->
> Demum offitium cum oratione, quam complendam vocant, concludatur.

Finally let the office be concluded with the prayer which they call the complenda.

The Coburg proposal of 1524, which follows the Nürnberg Mass ("the offertory and the lesser
canon left out"), likewise ends with "the collect which they call the complenda, and the
Benedicamus with the blessing, as is customary" (Sehling 1, p. 542).

**Volprecht, 1524.** Volprecht's outline of the Latin Mass has "*Complenda de quo sit missa*":
the postcommunion of whatever Mass is being said (Sehling 11, p. 39). Sehling's note: "namely
the one falling due in each case". His German Mass for Trinity ends with the Trinity
postcommunion, *Proficiat nobis ad salutem corporis et animae*, in German (Sehling 11, p. 42).
See [`CANON_IN_GERMAN_MASSES.md`](CANON_IN_GERMAN_MASSES.md), §7.2.

**Müntzer, 1524** (Radical Reformation). Each of Müntzer's five German Masses ends with a
"prayer at the end of the office", most of them German versions of the Missal postcommunion. For
Easter it is the Easter postcommunion, *Spiritum nobis, Domine, tuae caritatis infunde: ut quos
sacramentis paschalibus satiasti, tua facias pietate concordes*. **Allstedt, Thomas Müntzer,
*Deutsch evangelisch messe*, 1524** (Radical Reformation; Sehling 1, p. 503):

<!-- doc 51 -->
> Unser osterlamp Christus ist geopfert vor uns alleluia alleluia. […] Gepet am ende des ampts
> der ersteung. O herr geuss in uns den geist der liebe und die du hast gesettiget mit deinem
> osterlamb mache eintrechtig in deiner liebe durch Jesum etc.

Christ our Passover is sacrificed for us, alleluia, alleluia. […] Prayer at the end of the
office of the Resurrection. O Lord, pour into us the spirit of love, and those whom thou hast
filled with thine Easter lamb make of one mind in thy love; through Jesus, etc.

The other postcommunions of Müntzer's Masses (Radical Reformation):
- **Pentecost**: *Sancti Spiritus, Domine, corda nostra mundet infusio* ("O herr vorlei uns die
  gnad des heiligen geists, auf das der thau deiner güte …", Sehling 1, p. 504).
- **Advent**: a new prayer, "O herr gott, steh hart bei uns"
  ([`CANON_IN_GERMAN_MASSES.md`](CANON_IN_GERMAN_MASSES.md), §4.4).
- **Christmas and the Passion**: prayers in the same form, "O gütiger gott eröffne uns den
  abgrund unser selen …" and "O herr gib deinem armen volke zu erkennen deine veterliche zucht
  und ruthe …" (Sehling 1, p. 502). This guide has not found a Missal source for them.

**Erfurt, 1525.** The Erfurt *Deutsches Kirchenamt* takes over the offices of Müntzer (Radical
Reformation) and adds one for Trinity. Its "prayer at the end of the office" is the Trinity
postcommunion *Proficiat*. **Erfurt, *Deutsches Kirchenamt*, 1525** (Sehling 2, p. 378):

<!-- doc 1251 -->
> Gebet am ende des ampts: O herre got, lass uns zu nutz kummen des leibes und der seelen die
> entphahunge des heiligen sacraments und das ewige bekentnus des [der] heiligen und der
> selbstendigen, ungetheilten dreivaltigkeit. Der du lebest und regirest, got, mit dem son und
> heiligem geiste von ewigkeit zu ewigkeit. Amen.

Prayer at the end of the office: O Lord God, let the receiving of the holy sacrament profit us
for body and soul, and the everlasting confession of the holy and self-subsistent, undivided
Trinity. Who livest and reignest, God, with the Son and the Holy Ghost, from everlasting to
everlasting. Amen.

The Latin is *Proficiat nobis ad salutem corporis et animae, Domine Deus noster, huius
sacramenti susceptio: et sempiterna sanctae Trinitatis eiusdemque individuae Unitatis
confessio*. Erfurt's Pentecost office has Müntzer's Pentecost postcommunion (Sehling 2, p. 377).

**Calenberg-Göttingen, 1542.** The fullest survival is in the Calenberg-Göttingen order. Its
proper Masses for Advent, Christmas, Purification, the Passion, Easter, Ascension and Pentecost
each have, in order:
1. the collect of the day after the Gloria;
2. a collect for the magistrates under the Sanctus (§5.2);
3. in every Mass but Advent, a fixed thanksgiving after the communion ("Die danksagung"),
   usually Luther's;
4. after the *Agnus Dei*, a second, **proper** postcommunion, headed "Die collecta". Some are
   Missal postcommunions, others collects from the Wittenberg hymnbook (Passion, Sehling 6/2, p.
   827).

Sehling's editors identify several of these proper prayers as Missal postcommunions. The Advent
Mass, which has no thanksgiving, ends with the proper postcommunion and then the *Da pacem* with
its collect: two collects after the communion, the proper one and the one for peace, as in the
medieval rite. **Calenberg-Göttingen, *Kirchenordnung*, 1542, Advent** (Sehling 6/2, p. 819):

<!-- doc 2037 -->
> Collect. Herre, las uns entpfangen an mittel des tempels deine barmherzigkeit, auf das wir mit
> billicher ehr vorgehen der herrligkeit, die an jenem tage uber uns komen wird. Das Da paoem
> zum beschlus: […] Verley uns friden gnediglich, Herr Gott, zu unsern zeiten, es ist doch ja
> kein ander nicht, der fur uns künde streiten, denn du, unser Gott, alleine. Gott, gib frid in
> deinem lande! Glück und heil zu allem stande! Herr Gott, himlischer Vater, der du heiligen
> muth, guten rath und rechte werke schaffest, gib deinen dienern frid, welchen die welt nicht
> kan geben, auf das unsere herzen an deinen geboten hangen und wir unsere zeit durch deinen
> schutz still und sicher fur feinden leben durch Jhesum Christ, deinen Sohn, unsern Herren.
> Amen.

Collect. Lord, let us receive thy mercy in the midst of thy temple, that we may go before the
glory which shall come upon us at that day with fitting honour. The *Da pacem* for the
conclusion: […] Grant us peace graciously, Lord God, in our days; there is indeed none other
that could fight for us but thou, our God, alone. God, give peace in thy land! Fortune and
welfare to every estate! Lord God, heavenly Father, who workest holy desire, good counsel and
right works, give unto thy servants peace, which the world cannot give, that our hearts may
cleave to thy commandments, and that we may pass our time by thy defence quiet and safe from
enemies; through Jesus Christ, thy Son, our Lord. Amen.

The first prayer is the postcommunion of the first Sunday in Advent: *Suscipiamus, Domine,
misericordiam tuam in medio templi tui: ut reparationis nostrae ventura solemnia congruis
honoribus praecedamus*. Sehling's note gives the Latin phrase *in medio templi tui*
(Sehling 6/2, p. 819, nn. 69–69a). The German changes "the coming solemnities of our redemption"
into "the glory which shall come upon us at that day", turning the prayer from Christmas to the
Last Day. The peace collect is the Missal's *Deus, a quo sancta desideria* (n. 71).

**The Easter Mass of the same order** has, after Luther's thanksgiving and the *Agnus Dei*, a
version of the Easter postcommunion. It is shorter and freer than Müntzer's.
**Calenberg-Göttingen, *Kirchenordnung*, 1542, Easter** (Sehling 6/2, p. 829):

<!-- doc 2037 -->
> Die danksagung. Wir danken dir, almechtiger Gott .... […] Das Agnus Dei. O lamb Gottes
> unschuldig ... […] Herr, uberschütte uns mit deinem Geiste, das wir in steter liebe und
> einigkeit leben, deiner auferstehung und zukunft niemer vergessen. Amen. Die benedictio. Der
> Herr segne dich ....

The thanksgiving. We give thanks unto thee, Almighty God … […] The Agnus Dei. O Lamb of God,
unspotted … […] Lord, pour out upon us thy Spirit, that we may live in constant love and
concord, and never forget thy resurrection and thy coming again. Amen. The blessing. The Lord
bless thee …

Sehling's note: "On the following prayer compare the Roman Missal … (postcommunion on Easter
Sunday and Easter Monday)" (Sehling 6/2, p. 829, n. 37a). The order's Pentecost Mass has the
Pentecost postcommunion of Müntzer (Radical Reformation) in the same place
(Sehling 6/2, p. 834). The order's common Mass, used outside the feasts, has in this slot the
priest's prayer for peace *Domine Iesu Christe, qui dixisti* in German. See
[`CANON_IN_GERMAN_MASSES.md`](CANON_IN_GERMAN_MASSES.md), §13.3.

**Where the line ends.** Calenberg-Göttingen 1542 is the last order in the corpus to print
proper postcommunions for the feasts. After it the proper postcommunion is gone from the Mass.
Some of these prayers survived as collects for other uses: the Corpus Christi collect became an
alternative postcommunion (§6.4), and the Easter prayer for love and concord passed into the
German collect books.

**A note on the Common Service.** The modern Common Service tradition, with its Sarum-derived
postcommunion beside Luther's, lies outside the corpus, which ends in the early seventeenth
century. Two things in the corpus bear on it:
- The **Easter postcommunion *Spiritum nobis … tuae caritatis infunde*** is one of the Missal
  postcommunions that evangelical orders put into German and used after the communion: first
  Müntzer (Radical Reformation), then the Lutheran Calenberg-Göttingen.
- The Sarum and Roman Missals share most of their collects and postcommunions. The corpus
  therefore cannot show whether a given prayer reached a later book from the Sarum or the Roman
  Missal. The German orders took theirs from the German diocesan Missals.

### 6.3 Luther's thanksgiving becomes the ordinary postcommunion

**From 1526 on.** Luther's thanksgiving "Wir danken dir, allmächtiger Herr Gott, dass du uns
durch diese heilsame Gabe hast erquicket" (§3.3) became the standard postcommunion of the
Lutheran orders. The editor of the Verden order lists where it stands
(Sehling 7/1, p. 161, n. 81):
- Lüneburg and Wolfenbüttel;
- Lippe, Spiegelberg and Pyrmont 1571;
- Oldenburg 1573;
- Grubenhagen and Hoya 1581;
- Lauenburg;
- Osnabrück 1618;
- and, he adds, "elsewhere also widely spread".

To these the corpus adds Saxony 1539 and 1580, Mansfeld 1580, Prussia 1544, Mecklenburg 1545,
Calenberg-Göttingen 1542, Brandenburg 1540, Pfalz-Neuburg 1543, Hatzkerode, Nördlingen 1579 and
others.

**Still called the *complenda*.** Some orders keep the old name for the new prayer. The
Hatzkerode order calls Luther's thanksgiving "the complenda". **Hatzkerode, *Kirchenordnunge*,
1534(?)** (Sehling 2, p. 587):

<!-- doc 1263 -->
> sol er sich umb keren und die salutatio singen: Der herr sei mit euch, dann wider zum altar
> gewant, die complende: Wir danken dir cet. oder dergleichen; zuletzt sol er sich wieder umb
> wenden und den segen singen: Der herr segne dich cet.

he shall turn about and sing the salutation, The Lord be with you; then, turned again to the
altar, the complenda: We give thanks unto thee, etc., or the like; and last he shall turn about
again and sing the blessing, The Lord bless thee, etc.

The term occurs also in Reuss 1552 ("the complenda after the use of our church … which one
singeth toward the people", Sehling 2, p. 154), in Breslau 1550 ("then one readeth the
complenda", Sehling 3, p. 404) and in the Wendish service at Senftenberg 1555 ("together with
the complenda and the Aaronic blessing", Sehling 1, p. 672). Other orders call it simply "a
collect of thanksgiving" (*eine Collecten thor dancksegginge*, Schleswig-Holstein 1542, Sehling
23, p. 91).

**The salutation and the "Let us give thanks".** The thanksgiving keeps the frame of the old
postcommunion: *Dominus vobiscum*, *Oremus*, the prayer, *Amen*. Two orders add a bidding to
give thanks:
- **Mecklenburg 1545**: "Segget dank dem heren. Darup antwordet de kercke: Gade si loff unde
  dank" (Sehling 5, p. 155);
- **Saxony 1580**: "Last uns dem herrn danken und beten" (below).

Nördlingen 1579 puts a **versicle** before each, as before a medieval collect: 1 Cor 11:26 ("So
oft ir von disem brot esset …") before Luther's thanksgiving, and 1 Cor 11:27 before the
alternative. It appoints them for Palm Sunday and Maundy Thursday, "and also all Sundays and
holy days after the communion held" (Sehling 12, p. 382).

### 6.4 The alternatives

**The ordinary was not alone.** Most orders print Luther's thanksgiving with one or two
alternatives, "or this". The alternatives come from four sources.

**(a) The Nürnberg thanksgiving of 1533.** Brandenburg-Nürnberg 1533 orders "a common prayer in
German, spoken openly", which "shall be a thanksgiving". It is a new composition, longer than
Luther's, and asks that what was received with the mouth be grasped by faith.
**Brandenburg-Nürnberg, *Kirchenordnung*, 1533** (Sehling 11, p. 197):

<!-- doc 270 -->
> Wann nun das volk alles verricht ist, soll man aber ein gemain gebet in teutsch offenlich
> sprechen. Das soll ein danksagung sein also: Laßt uns bitten! O almechtiger, ewiger Got. Wir
> sagen deiner götlichen miltigkeit lob und dank, das du uns mit dem hailsamen flaisch und blut
> deines ainigen Suns Jesu Christi, unsers Herrn, gespeist und getrenkt hast, und bitten dich
> demütiglich, du wöllest durch deinen Heiligen Gaist in uns würken, wie wir dis heilig
> sacrament mit dem mund haben empfangen, das wir auch also dein götliche gnad, vergebung der
> sünde, verainigung mit Christo und ewigs leben, so darinnen angezaigt und zugesagt ist, mit
> festem glauben mögen begreifen und ewiglich behalten. Durch unsern Herrn Jesum Christum,
> deinen Sun, der mit dir in ainigkeit des Heiligen Gaists lebt und herschet, warer Gott, immer
> und ewiglich. Amen.

Now when all the people have been communicated, there shall again be spoken openly a common
prayer in German. This shall be a thanksgiving, thus: Let us pray. O almighty, everlasting God,
we give praise and thanks unto thy divine bounty, that thou hast fed us and given us to drink
with the wholesome flesh and blood of thine only Son Jesus Christ our Lord; and we humbly
beseech thee that thou wouldest work in us by thy Holy Ghost, that as we have received this holy
sacrament with the mouth, so we may also with firm faith lay hold on and for ever retain thy
divine grace, forgiveness of sins, union with Christ and everlasting life, which are therein
shown forth and promised. Through our Lord Jesus Christ, thy Son, who with thee in the unity of
the Holy Ghost liveth and reigneth, true God, ever and everlastingly. Amen.

The phrase "as we have received … with the mouth, so … with firm faith" is Luther's *Quod ore
sumpsimus … pura mente capiamus* opened out. The 1533 prayer is thus the third stage of the 1523
substitute: Latin ablution prayer, then plain German, then a doctrinal expansion.

**(b) Two collects "under one conclusion".** Brandenburg 1540 joins the Nürnberg prayer and
Luther's into a single "thanksgiving" (Sehling 3, p. 70). Pfalz-Neuburg 1543 does the same and
names the old technique: two collects sung "under one conclusion", the way the medieval rite
joined a postcommunion and a commemoration. **Pfalz-Neuburg, *Kirchenordnung*, 1543**
(Sehling 13, p. 76):

<!-- doc 386 -->
> Darnach soll er dise zwo collecten unter einem beschluß in gewonlichem ton singen oder mit
> vernemlicher stimme sprechen. Laßt uns beten: O almechtiger, ewiger Gott. Wir sagen deiner
> götlichen miltigkeit lob und dank, das du uns mit dem heilsamen fleisch und blut deines
> einigen Sons Jesu Christi, unsers Herrn, gespeiset und getrenket hast […]. Ein ander gebet.
> Wir danken dir auch, Herr Jesu Christe, das du uns durch dise heilsame gabe deines leibs und
> bluts hast erquicket, und bitten deine barmherzigkeit, das du uns solchs gedeihen lassest zu
> einem starken glauben gegen dir und zu brünstiger lieb unter uns allen, der du mit Got dem
> Vater in einigkeit des Heiligen Geists lebest und regirest immer und ewiglich. Chorus: Amen.

Thereafter he shall sing these two collects under one conclusion in the accustomed tone, or say
them with an audible voice. Let us pray. O almighty, everlasting God, we give praise and thanks
unto thy divine bounty, that thou hast fed us and given us to drink with the wholesome flesh and
blood of thine only Son Jesus Christ our Lord […]. Another prayer. We thank thee also, Lord
Jesus Christ, that thou hast refreshed us through this salutary gift of thy body and blood; and
we beseech thy mercy that thou wouldest make the same to prosper in us unto a strong faith
toward thee and unto fervent love among us all; who with God the Father in the unity of the Holy
Ghost livest and reignest ever and everlastingly. Choir: Amen.

Pfalz-Neuburg addresses Luther's prayer to **Christ** ("Herr Jesu Christe") and closes it with
the conclusion for a prayer to the Son. Calenberg-Göttingen 1542 has the same two-part
thanksgiving in its common Mass, "which shall be made in all Masses after the communion"
(Sehling 6/2, p. 816; see [`CANON_IN_GERMAN_MASSES.md`](CANON_IN_GERMAN_MASSES.md), §13.3).
Oldenburg 1573 gives the Nürnberg prayer as an alternative (Sehling 7/2.1, p. 1145).

**(c) The Corpus Christi collect.** The most widespread alternative is a German version of the
collect of Corpus Christi, *Deus, qui nobis sub sacramento mirabili passionis tuae memoriam
reliquisti: tribue, quaesumus, ita nos corporis et sanguinis tui sacra mysteria venerari, ut
redemptionis tuae fructum in nobis iugiter sentiamus*. Sehling's editors trace it to the
Wittenberg hymnbook of 1533 (Sehling 6/2, p. 1076, n. 81). The identification with the Missal
collect is this guide's. **Saxony, *Ordnung* of Duke August, 1580** (Sehling 1, p. 369):

<!-- doc 44 -->
> Nach der communion lese man der nachfolgenden collecten eine, und beschliesse mit der
> benediction. Collecten. Last uns dem herrn danken und beten. Wir danken dir allmechtiger herre
> gott, das du uns durch diese heilsame gaben hast erquicket, und bitten deine barmherzigkeit,
> das du uns solches gedeien lassest, zu starkem glauben gegen dir, und zu brünstiger liebe
> unter uns allen, durch Jesum Christum deinen sohn, unsern herrn, Antwort. Amen. Oder diese.
> Ach du lieber herre gott, der du uns bei diesem wunderbarlichen sacrament deines leidens
> zugedenken und predigen befohlen hast, verleihe uns, das wir solch deines leibes und bluts
> sacrament also mögen brauchen, das wir dein erlösung in uns teglich fruchtbarlich empfinden,
> Antwort. Amen.

After the communion let one of the following collects be read, and let him conclude with the
blessing. Collects. Let us give thanks unto the Lord and pray. We give thanks unto thee,
Almighty Lord God, that thou hast refreshed us through these salutary gifts; and we beseech thy
mercy, that thou wouldest make the same to prosper in us unto strong faith toward thee and unto
fervent love among us all; through Jesus Christ thy Son our Lord. Answer: Amen. Or this. O thou
dear Lord God, who in this wonderful sacrament hast commanded us to remember and to preach thy
passion; grant us so to use this sacrament of thy body and blood, that we may daily perceive in
us fruitfully thy redemption. Answer: Amen.

The Latin "hast left us a memorial of thy passion" becomes "hast commanded us to remember and to
preach thy passion" (1 Cor 11:26). "To venerate the sacred mysteries" becomes "so to use this
sacrament". The petition *ut redemptionis tuae fructum in nobis iugiter sentiamus* is kept
almost word for word: "das wir dein erlösung in uns teglich fruchtbarlich empfinden". The same
pair (Luther's, "or this" the Corpus Christi collect) stands in:
- Mecklenburg 1545 (below);
- Buxtehude 1565, where the Corpus Christi collect comes **first** (Sehling 7/1, p. 125);
- Mansfeld 1580 (Sehling 2, p. 227);
- Grubenhagen 1581 (Sehling 6/2, p. 1076);
- Oldenburg 1573 (Sehling 7/2.1, p. 1145);
- Nördlingen 1579 (Sehling 12, p. 382).

Grubenhagen 1581 also uses it in its old place, as the collect for Maundy Thursday ("Die coenae
Domini", Sehling 6/2, p. 1078). The Württemberg order of 1536 has it among its collects as the
*Oratio de Eucharistia* (Sehling 16, p. 125).

**(d) Döber's prayer of 1525.** Döber's Nürnberg Mass of 1525 has a postcommunion that Sehling's
editor thought "apparently newly made" (Sehling 11, p. 55, n. 22). **Nürnberg, *Deutsche Messe
des A. Döber*, 1525** (Sehling 11, pp. 54–55):

<!-- doc 250 -->
> Darnach die collecten spricht zum volk: Last uns bitten: O Herr, allmechtiger Got, verleih uns
> in unser gemüt und herzen, das wir durch den zeitlichen tod […] deines Suns, welche dise
> wirdige geheimnus bedeuten, das wir getrauen, das du uns geben hast das ewig leben durch den
> Christum, unsern Herrn. Amen.

Thereafter he saith the collect to the people: Let us pray. O Lord Almighty God, grant us in our
minds and hearts that, through the temporal death of thy Son, which this worthy mystery
signifieth, we may trust that thou hast given us everlasting life; through Christ our Lord.
Amen.

Its pairing of "temporal" with "signifieth" and "everlasting" recalls the Corpus Christi
postcommunion *Fac nos, quaesumus, Domine, divinitatis tuae sempiterna fruitione repleri: quam
pretiosi Corporis et Sanguinis tui temporalis perceptio praefigurat*. It may be a free reworking
of it; this is a suggestion, not Sehling's identification. Mecklenburg took Döber's prayer into
its list of three.

**Mecklenburg's three.** Mecklenburg 1545 offers all three kinds: Luther's, Döber's, and the
Corpus Christi collect. **Mecklenburg, *Ordeninge der misse*, 1545** (Sehling 5, p. 155):

<!-- doc 1922 -->
> Darup de prester: Latet uns beden. Wi danken di allmechtige here godt, dat du uns dorch düsse
> heilsame gave dines lives unde blodes heffst erquicket, und bidden dine barmherticheit, dat du
> uns sülckes gedien latest to starkem loven jegen di, unde to füriger leve mank uns allen,
> dorch unsen heren Jesum Christum, amen. Edder to tiden dit gebet. O here almechtige vader
> vorlene uns in unse gemöte unde herte, dat wi dorch den tidtliken dot dines söns, welckeren
> düsse werdige hemelicheit bedüdet, getrüwen, dat du uns gegeven heffst dat ewige levent, dorch
> Jesum Christum, unsen heren, amen. Edder düsse. Ach du leve here godt, de du uns bi düssem
> wunderbarliken sacramente dines lidens to gedenken unde predigen bevalen heffst, vorlene uns,
> dat wi sölck dines lives unde blodes sacramente also mögen bruken, dat wi dine erlösinge in
> uns dagelick fruchtbarlick erfinden, dorch Jesum Christum, amen.

Thereupon the priest: Let us pray. We give thanks unto thee, Almighty Lord God, that thou hast
refreshed us through this salutary gift of thy body and blood; and we beseech thy mercy, that
thou wouldest make the same to prosper in us unto strong faith toward thee and unto fervent love
among us all; through our Lord Jesus Christ. Amen. Or at times this prayer: O Lord, almighty
Father, grant us in our minds and hearts that, through the temporal death of thy Son, which this
worthy mystery signifieth, we may trust that thou hast given us everlasting life; through Jesus
Christ our Lord. Amen. Or this: O thou dear Lord God, who by this wonderful sacrament hast
commanded us to remember and to preach thy passion; grant us so to use this sacrament of thy
body and blood, that we may daily perceive in us fruitfully thy redemption; through Jesus
Christ. Amen.

**(e) Alternating Sundays: Prussia 1544.** The Prussian order of 1544 has two postcommunions
sung "to alternate every other Sunday". The second is a new prayer on the fruit of the passion.
**Prussia, *Kirchenordnung*, 1544** (Sehling 4, p. 66):

<!-- doc 1833 -->
> Darnach wendet sich der priester zum volk und singt: Der herre sei mit euch, und wendet sich
> widder noch dem altar, singt der collecten eine mit gewönlichem accent etc. umb den andern
> soutag abzuwechseln. Erste collect. Wir danken dir etc. […] Ein ander collect. O warhaftiger
> got, barmherziger vater, wir bitten dich herzlich, las uns dürftigen des heiligen leidens
> unsers herren nutz und frucht, das ist gnade und vergebung unser sünden mit gleubigem herzen
> rechtschaffen ergreifen, gleich wie wir durch deines heiligen sones wort seinen heiligen leib
> und sein theures blut, welche er für uns gegeben und vergossen hat, unter dem brot und wein
> warlich haben empfangen, durch denselbigen unsern herren Jesum Christum, deinen sohn, der mit
> dir lebet und hirschet von ewigkeit zu ewigkeit. Amen.

Thereafter the priest turneth to the people and singeth: The Lord be with you; and turneth again
to the altar, [and] singeth one of the collects with the customary accent, etc., to alternate
every other Sunday. First collect: We give thanks unto thee, etc. […] Another collect: O true
God, merciful Father, we heartily beseech thee, let us needy ones rightly lay hold with
believing heart on the profit and fruit of the holy passion of our Lord, that is, grace and the
forgiveness of our sins, even as through the word of thy holy Son we have truly received under
the bread and wine his holy body and his precious blood, which he gave and shed for us; through
the same our Lord Jesus Christ, thy Son, who liveth and reigneth with thee from everlasting to
everlasting. Amen.

The Prussian articles of 1525 had already provided "two common collects or complendas for the
end of the Mass, to alternate through the whole year". Sehling does not print them
(Sehling 4, p. 37).

**(f) Later replacements.** Late orders sometimes replace Luther's short prayer with a longer
one. At Engerhafe in East Frisia (1583) "a trinitarian thanksgiving has taken the place of
Luther's short thanksgiving collect (postcommunion)", as Sehling's editor notes in comparing it
with the order of 1535 (Sehling 7/1, p. 681, n. 34). The thanksgiving with the *Placeat* in
Kantz's Mass of 1522 is treated in [`CANON_IN_GERMAN_MASSES.md`](CANON_IN_GERMAN_MASSES.md),
§2.7.

### 6.5 When there was no communion

**A collect instead.** Without communicants the Lutheran Mass ended after the sermon, and the
postcommunion slot was filled with "a collect" of the pastor's choice, not with the thanksgiving
for the sacrament:
- **Saxony 1580**: "But where no communicants are present, it shall be concluded after the
  sermon, or a chapter of Holy Scripture read, with a Christian collect and the customary
  blessing" (Sehling 1, p. 369).
- **Soest 1609**: "When there are no communicants, the preacher may conclude with a collect of
  his own choice" (*arbitraria collecta*, Sehling 22, p. 495).
- **Lippe 1571**: a collect "or thanksgiving for the word of God heard". **Lippe,
  *Kirchenordnung*, 1571** (Sehling 21, p. 397):

<!-- doc 1462 -->
> Darauff eine Collecten oder Dancksagung für das gehörte Wort Gottes singen und mit einem
> Christlichen Liede beschliessen.

Thereupon sing a collect or thanksgiving for the word of God which hath been heard, and conclude
with a Christian hymn.

The thanksgiving for the gift of the sacrament became, in the service without communion, a
thanksgiving for the gift of the Word.

The service when nobody communicated is treated in [`MASS_ORDO_GUIDE.md`](MASS_ORDO_GUIDE.md),
§14, and the Litany sung in place of the Mass in
[`EXTRAORDINARY_RITES_GUIDE.md`](EXTRAORDINARY_RITES_GUIDE.md), §22.1.

### 6.6 The prayer over the people (*oratio super populum*)

**The medieval use.** On the weekdays of Lent the Missal added a fourth proper prayer after the
postcommunion. The deacon bade the people *Humiliate capita vestra Deo*, "Bow down your heads
before God", and the priest said the *oratio super populum*, a prayer over the people, before
the dismissal. In the Breviary the same prayers served as collects of the office on the Lenten
weekdays.

**Not at the Mass.** No Lutheran order in the corpus keeps the *super populum* at the end of the
Mass. The bidding *Humiliate capita vestra Deo* does not occur, in Latin or in German. The
corpus was searched for *super populum*, *super plebem*, *humiliate capita*, *inclinate capita*
and German phrases such as "neiget eure Häupter". The Lutheran Mass had no weekday Lenten Masses
to carry the prayer. Its place at the end of the Sunday Mass was held by the postcommunion
collect and the Aaronic blessing. The orders describe that blessing in the same words: "the
blessing over the people out of the book of Numbers"
(*benediction uber das volk aus dem buch numeri*, Gnandstein 1539, Sehling 1, p. 564). Müntzer
(Radical Reformation) describes his postcommunion the same way: "after the communion one giveth
thanks to God over the people, and blesseth the Lord" (Sehling 1, p. 506). Neither is a *super
populum* prayer.

**In the office: Ansbach 1533.** The one place where the *super populum* survives by name is in
the Divine Office of the collegiate churches. The Brandenburg-Ansbach order of 1533 for the
singing and reading in the *Stifte* goes through the Breviary and strikes out what is unfit. In
Lent it strikes out the collects at Lauds (*super Benedictus*) that "speak of the fast" as a
work, day by day. For their place it allows the *super populum* prayers.
**Brandenburg-Ansbach-Kulmbach, *Ordnung singens und lesens bei den Stiften*, 1533**
(Sehling 11, p. 315):

<!-- doc 276 -->
> In die Cinerum collecta super Benedictus Concede nobis, Domine praesidia und andere collecten
> mer, die von der vasten lauten als Inchoata ieiunia und Adesto, Domine, supplicacionibus
> nostris etc., und der hymnus Ex more docti sollen nicht gehalten werden. Weiter sollen sie
> underlassen dominica Invocavit: die collect super Bened[ictus] Deus, qui ecclesiam tuam, […]
> feria secunda nach Reminiscere: die collect super Benedictus Praesta, quaesumus, omnipotens
> Deus, familia tua etc., feria quarta: die collecta super Benedictus Populum tuum, Domine etc.,
> feria quinta: die collect super Benedictus Praesta nobis Domine, quaesumus, feria sexta: super
> Benedictus collect Da, quaesumus, omnipotens Deus etc., sabbato: super Benedictus collecta
> Da,quaesumus, Domine nostris effectum; und an diser stat mogen sie allwegen nemen die
> nachvolgende super populum;

On Ash Wednesday the collect at the Benedictus, *Concede nobis, Domine, praesidia*, and other
collects more which speak of the fast, as *Inchoata ieiunia* and *Adesto, Domine,
supplicationibus nostris*, etc., and the hymn *Ex more docti*, shall not be kept. Further they
shall leave out: on the Sunday Invocavit, the collect at the Benedictus *Deus, qui ecclesiam
tuam*; […] on the Monday after Reminiscere, the collect at the Benedictus *Praesta, quaesumus,
omnipotens Deus, familia tua*, etc.; on the Wednesday, the collect at the Benedictus *Populum
tuum, Domine*, etc.; on the Thursday, the collect at the Benedictus *Praesta nobis, Domine,
quaesumus*; on the Friday, at the Benedictus the collect *Da, quaesumus, omnipotens Deus*, etc.;
on the Saturday, at the Benedictus the collect *Da, quaesumus, Domine, nostris effectum*; and in
this place they may always take the *super populum* that followeth.

**What the rule means.** The list goes on through the weeks of Oculi, Laetare and Judica
(Sehling 11, pp. 315–316).
- **What it strikes out.** The Lauds collects of the Lenten weekdays are the collects of the
  day's Mass. Many of them ask that bodily fasting be made fruitful or meritorious. An example
  is the Monday after Reminiscere: *Praesta, quaesumus, omnipotens Deus, ut familia tua, quae se
  affligendo carnem ab alimentis abstinet, sectando iustitiam a culpa ieiunet*. Another is the
  Wednesday: *Populum tuum, Domine, propitius respice: et quos ab escis carnalibus praecipis
  abstinere, a noxiis quoque vitiis cessare concede*.
- **What it puts in their place.** "The *super populum* that followeth" is the prayer over the
  people of the same day, which stands after the postcommunion in the Missal. These prayers ask
  for God's protection, mercy and guidance of his people, without reference to the fast. For the
  same Monday it is *Adesto supplicationibus nostris, omnipotens Deus: et quibus fiduciam
  sperandae pietatis indulges, consuetae misericordiae tribue benignus effectum*.

The identification of these texts is this guide's. Sehling's editor gives no note on the
passage.

**The result.** The Lenten prayer over the people outlived the Lenten collect in this one
Lutheran order. It did so not at the end of the Mass but at Lauds, and for a doctrinal reason:
of the day's two proper prayers it was the one that said nothing of fasting as a work. Ansbach's
handling matches Luther's test for the collect in 1523, "if only it be godly" (§3.2). The corpus
shows no other Lutheran use of the *super populum*.

---

## 7. Kept, stripped, added, altered

**Table 1. The prayers, compared with the medieval system**

| | Collect | Secret | Postcommunion | Prayer over the people (Lent) |
|---|---|---|---|---|
| **Medieval use** | Proper to the day; sung after the Gloria; multiplied by commemorations and votive collects | Proper to the day; said silently over the gifts; multiplied with the collects | Proper to the day; sung after the communion; multiplied with the collects | Proper to the Lenten weekdays; after the postcommunion, with the bidding *Humiliate capita vestra Deo*; also used as an office collect |
| **Kept** | The collect of the season or feast (§4.2), mostly German versions of the Missal collects; the salutation, *Oremus*, long conclusion and Amen (§4.5); the seasonal versicle (Henneberg 1582, Hof 1592) | Only the closing *Per omnia saecula saeculorum. Amen* (Müntzer (Radical Reformation), Lippe, Calenberg-Göttingen), and the name in Dortmund 1554 (§5.2) | A collect after the communion, with salutation and Amen; often still called the *complenda* (§6.3). Proper postcommunions kept in Nürnberg and Volprecht 1524, Coburg 1524, Müntzer 1524 (Radical Reformation), Erfurt 1525 and Calenberg-Göttingen 1542 (§6.2) | Only in the office: Ansbach 1533 allows the day's *super populum* at Lauds (§6.6) |
| **Stripped** | Collects of the saints and those asking their intercession (Hannover 1536); the automatic commemorations (Luther: "that one alone") | The prayer itself, everywhere (Prussia 1525: "of necessity left out"); no German secret exists | The proper postcommunion (Luther 1523: "they almost all sound of sacrifice"); gone from the printed orders after 1542 | At the Mass, everywhere; neither the prayer nor the bidding occurs |
| **Added** | Veit Dietrich's gospel collects (Wolfenbüttel 1569, Soest 1609, Buxtehude 1565); new "common" collects for need; the collect for peace after *Verleih uns Frieden* | Open prayers for the magistrates and Christendom in its place (Dortmund 1554); collects for rulers under the Sanctus (Döber 1525, Brandenburg 1540, Calenberg-Göttingen 1542, Pfalz-Neuburg 1543) | Luther's fixed thanksgiving (1526); the Nürnberg thanksgiving (1533); Döber's prayer (1525); Prussia's second collect (1544); a collect or thanksgiving for the Word when there is no communion (Lippe 1571) | — |
| **Altered** | Latin to German "that the people may say Amen" (Coburg 1554/55); one collect as the norm, a second only "for need" (Mecklenburg 1545) or by rule for temporal goods (Ansbach 1548); the Advent *Excita* reworded ("weck uns auf, dass wir bereit sein") | — | Proper to ordinary; Luther's 1523 ablution prayers made public, then expanded (Nürnberg 1533); the Missal postcommunion *Gratias tibi referimus* recast as Luther's thanksgiving; the Corpus Christi collect turned into a postcommunion; two thanksgivings joined "under one conclusion" (Brandenburg 1540, Pfalz-Neuburg 1543) | Moved from the end of the Mass to Lauds, in place of collects that "speak of the fast" (Ansbach 1533) |

**Table 2. Did the medieval "two collects, two secrets, two postcommunions" survive?**

| Feature | Survives? | Where |
|---|---|---|
| More than one collect before the epistle | **Yes, in some orders** | Ansbach 1548 (two, by rule); Mecklenburg 1545 (a second "for need"); Wolfstein 1574 and Henneberg ("one or more") |
| A matching second secret | **No** | The secret is gone altogether |
| A matching second postcommunion | **No, but two postcommunions do occur**, not tied to the collects | Brandenburg 1540 and Pfalz-Neuburg 1543 (Nürnberg and Luther thanksgivings "under one conclusion"); Calenberg-Göttingen 1542 (Luther's thanksgiving plus the proper postcommunion of the feast) |
| A votive prayer at the end | **Yes** | The collect for peace after *Verleih uns Frieden* (twelve or more orders); Hof 1592's collect "for rain and fair weather" |
| Rules for the conclusions | **Yes** | Hof 1592 (§4.5) |
| The Lenten prayer over the people | **Not at the Mass**; once in the office | Ansbach 1533, at Lauds (§6.6) |

---

## 8. Table by order

**Key.**
- **L**: Latin. **G**: German or Low German.
- **Proper**: varies with the day. **Fixed**: the same every time.
- **—**: absent or abolished. **?**: not stated.
- "Luther": Luther's thanksgiving of 1526. "Nürnberg": the Brandenburg-Nürnberg thanksgiving of
  1533. "Corpus Christi": the German Corpus Christi collect.

| Order | Vol. | Collect | Second collect | Secret | Postcommunion | Alternatives |
|---|---|---|---|---|---|---|
| Luther, *Formula missae*, 1523 | 1 | L, proper, "one alone" | — | — | L, fixed: *Quod ore*, *Corpus tuum* | either of the two |
| Volprecht, Nürnberg, 1524 | 11 | L "one only"; G proper (Trinity) | — | — | L proper (*de quo sit missa*); G *Proficiat* (Trinity) | — |
| Nürnberg parish Mass, 1524 | 11 | L proper (*Sancti tui nominis*) | — | — (with the offertory) | L proper (*complenda*) | — |
| Coburg proposal, 1524 | 1 | ? | ? | — (with the offertory) | "the complenda" | — |
| Müntzer, Allstedt, 1524 (Radical Reformation) | 1 | G proper (Missal) | — | *Per omnia* only | G proper (Missal postcommunions) | — |
| Strasbourg, Schwarz, 1524 (Moderate Reformed) | 20/1 | G | ? | — | G *Quod ore* as *Complenda* | "any other that seemeth Christian" |
| Döber, Nürnberg, 1525 | 11 | ? | Optional "common prayer" before the Sanctus | — | G, new (Döber's) | — |
| Erfurt, *Deutsches Kirchenamt*, 1525 | 2 | G proper | — | ? | G proper (Pentecost, *Proficiat*) | — |
| Prussia, *Artikel*, 1525 | 4 | Proper series by the year | ? | — ("of necessity left out") | Two common complendas, alternating | — |
| Luther, *Deutsche Messe*, 1526 | 1 | G, one, facing the altar | — | — | G fixed (Luther) | — |
| Ansbach, *Ordnung … bei den Stiften*, 1533 | 11 | (office) Lenten Lauds collects "of the fast" struck out | — | — | — | the day's *super populum* at Lauds in their place |
| Brandenburg-Nürnberg, 1533 | 11 | ? | ? | ? | G fixed (Nürnberg) | — |
| Hatzkerode, 1534(?) | 2 | ? | ? | ? | Luther, called "the complenda" | "or the like" |
| Bremen, 1534 | 7/2.2 | L from the Missal or G from the hymnbook | ? | ? | ? | — |
| Hannover, 1536 | 6/2 | Purged (saints' collects removed) | ? | ? | ? | — |
| Württemberg, 1536 | 16 | Collect series | ? | ? | ? | Corpus Christi as *Oratio de Eucharistia* |
| Saxony (Duke Henry), 1539 | 1 | L or G, "common or of the feasts" | Peace collect | ? | ? | — |
| Brandenburg, 1540 | 3 | ? | Four G collects under the Sanctus | — | G: Nürnberg + Luther under one conclusion; then L *Corpus tuum*, *Quod ore* | — |
| Calenberg-Göttingen, 1542 | 6/2 | G proper (Müntzer (Radical Reformation), Missal) | Collect for rulers under the Sanctus; peace collect at the end | *Per omnia* as "Gott sey preis …" | G: Luther (Nürnberg + Luther in the common Mass) then G proper (Missal) | *Qui dixisti* in the common Mass |
| Schleswig-Holstein, 1542 | 23 | ? | ? | ? | "a collect of thanksgiving" | — |
| Pfalz-Neuburg, 1543 | 13 | ? | Three collects under the Sanctus | Osiander's prayer over the gifts (new) | G: Nürnberg + Luther (to Christ) under one conclusion; then L *Corpus tuum*, *Quod ore* | — |
| Prussia, *Kirchenordnung*, 1544 | 4 | ? | ? | ? | Luther | second collect on alternate Sundays |
| Mecklenburg, 1545 | 5 | G "one at a time" | A second "for great need" | ? | Luther | Döber's; Corpus Christi |
| Ansbach, *Auctuarium*, 1548 | 11 | Two by rule: spiritual, then temporal | (the second) | ? | ? | — |
| Amberg, 1550 | 13 | L of the season "if it be pure" | ? | ? | Postcommunion "probably that of Pfalz-Neuburg" (editor) | — |
| Breslau, 1550 | 3 | ? | ? | ? | "the complenda" | — |
| Reuss, 1552 | 2 | ? | ? | ? | "the complenda after our church's use", toward the people | — |
| Dortmund, 1554 | 21 | ? | ? | Open prayer for rulers "in place of the Secret" | ? | — |
| Coburg, 1554/55 | 1 | G only, "that the people may sing Amen" | ? | ? | ? | — |
| Senftenberg, 1555 | 1 | ? | ? | ? | "the complenda", in Wendish for the Wends | — |
| Lüneburg, 1564 | 6/1 | G of the season or feast "or that agreeth with the matter" | ? | ? | Luther | ? |
| Buxtehude, *Agende*, 1565 | 7/1 | Two: Missal (before the sermon), Dietrich (after) | ? | ? | Corpus Christi first | Luther |
| Wolfenbüttel, 1569 | 6/1 | G series; may be Dietrich's gospel collects | ? | ? | Luther | ? |
| Lippe, 1571 | 21 | ? | ? | ? | Luther | without communion: a collect or thanksgiving for the Word |
| Oldenburg, 1573 | 7/2.1 | Very large G series (Wolfenbüttel's and more) | Peace collect | ? | Luther | Corpus Christi; Nürnberg |
| Wolfstein, 1574 | 13 | G, "one or more" | (as needed) | ? | ? | — |
| Nördlingen, 1579 | 12 | ? | ? | ? | Luther, after a versicle from 1 Cor 11:26 | Corpus Christi, after 1 Cor 11:27 |
| Saxony (Duke August), 1580; Mansfeld, 1580 | 1; 2 | G series | Peace collect (Mansfeld) | ? | Luther | Corpus Christi |
| Grubenhagen, 1581 | 6/2 | G series (Missal) | Peace collect | ? | Luther | Corpus Christi (also on Maundy Thursday) |
| Henneberg, 1582 | 2 | G "pure collects" by season, with versicles | Common collects "for every need" | ? | ? | — |
| Engerhafe, 1583 | 7/1 | ? | ? | ? | Trinitarian thanksgiving in place of Luther's | — |
| Hof, 1592 | 11 | Of the season or "directed to the Lord's Supper"; L at Vespers | "For rain and fair weather" (Vespers) | ? | A collect, e.g. the thanksgiving for the Supper received | — |
| Verden, 1606 | 7/1 | G series | ? | ? | Luther | ? |
| Soest, 1609 | 22 | "That agreeth with the gospel", or one for the Spirit | ? | ? | ? | without communion: a collect of free choice |
| Schaumburg, 1614 | 7/2.2 | G series | Peace collect | ? | ? | ? |
| Osnabrück, (1588) 1618 | 7/1 | G series (Missal, Coelius) | ? | ? | Luther | ? |

---

## 9. Concordance of the orders quoted

Every order quoted or cited in this guide is listed below by region. The table gives:
- **Sehling**: the volume and pages in Sehling's edition.
- **Doc**: the `eko.db` document that holds the text, for full-text lookup. A single database
  record may hold several orders.
- **§**: the sections where the order is quoted or cited ("A" = Appendix A).

**Saxony, Thuringia and central Germany**

| Order | Sehling | Doc | § |
|---|---|---|---|
| Luther, *Formula missae et communionis*, 1523 | 1, pp. 3–6 | 2 | 3.2, 4.1, 4.3, 6.1, A |
| Allstedt, Thomas Müntzer, *Deutsch evangelisch messe*, 1524 (Radical Reformation) | 1, pp. 500–504 | 51, 52 | 5.2, 6.2, A |
| Coburg, *Gottesdienst-Ordnung* (proposal), 1524 | 1, p. 542 | 72 | 6.2 |
| Allstedt, Thomas Müntzer, *Ordnung und berechnunge des teutschen ampts*, 1523/24 (Radical Reformation) | 1, p. 506 | 52 | 6.6 |
| Erfurt, *Deutsches Kirchenamt*, 1525 | 2, pp. 376–378 | 1251 | 6.2, A |
| Luther, *Deutsche Messe und ordnung gottis diensts*, 1526 | 1, pp. 14, 16 | 3 | 3.3, 4.5, A |
| Hatzkerode, *Kirchenordnunge*, 1534(?) | 2, p. 587 | 1263 | 6.3 |
| Gnandstein, visitation articles, 1539 | 1, p. 564 | 85 | 6.6 |
| Albertine Saxony, *Kirchenordnunge zum anfang* (Duke Henry), 1539 | 1, pp. 274–278 | 30 | 4.1, 4.2, 4.5 |
| Reuss, *Kirchen-Ordnung* of Heinrich IV, 1552 | 2, p. 154 | 1234 | 6.3 |
| Coburg, *Vorschaffung* of the visitation of 1554/55 | 1, p. 544 | 74 | 4.5 |
| Senftenberg, *Kirchen-Ordnung*, 1555 | 1, p. 672 | 136 | 6.3 |
| Albertine Saxony, *Ordnung* of Duke August, 1580 | 1, pp. 369, 375 | 44 | 4.2, 6.3, 6.4, 6.5 |
| Mansfeld, *Kirchen-agenda*, 1580 | 2, pp. 227–231 | 1241 | 4.2, 6.4 |
| Henneberg, *Kirchen ordnung* of Georg Ernst, 1582 | 2, pp. 317, 320 | 1247 | 4.1, 4.2, 4.3 |
| Henneberg, a pastor's report | 2, p. 330 | 1248 | 4.1 |

**Franconia, the Upper Palatinate and Swabia**

| Order | Sehling | Doc | § |
|---|---|---|---|
| Nürnberg, *Deutsche Messe des Priors Volprecht*, 1524 | 11, pp. 39, 42 | 247 | 4.1, 5.1, 6.2, A |
| Nürnberg, *Gottesdienstordnung der Pfarrkirchen*, 1524 | 11, pp. 46–49 | 249 | 3.1, 4.1, 5.1, 6.2 |
| Nürnberg, *Deutsche Messe des A. Döber*, 1525 | 11, pp. 54–55 | 250 | 5.2, 6.4, A |
| Brandenburg-Ansbach-Kulmbach, *Ordnung singens und lesens bei den Stiften*, 1533 | 11, pp. 315–316 | 276 | 6.6 |
| Brandenburg-Nürnberg, *Kirchenordnung*, 1533 | 11, p. 197 | 270 | 6.4, A |
| Württemberg, *Gemein kirchenordnung*, 1536 | 16, p. 125 | 651 | 6.4 |
| Pfalz-Neuburg, *Kirchenordnung*, 1543 | 13, p. 76 | 386 | 5.2, 6.1, 6.4 |
| Brandenburg-Ansbach-Kulmbach, *Auctuarium*, 1548 (Interim order) | 11, p. 330 | 278 | 4.1 |
| Amberg (Kuroberpfalz), *Kirchenordnung*, 1550 | 13, p. 286 | 411 | 4.3, 4.5 |
| Wolfstein, *Christliche Instructio* of Thomas Stieber, 1574 | 13, p. 576 | 463 | 4.1, 4.5 |
| Nördlingen, *Kirchenordnung*, 1579 | 12, p. 382 | 375 | 6.3, 6.4 |
| Hof, *Ordo ecclesiasticus*, 1592 | 11, pp. 411–429 | 294 | 4.1, 4.2, 4.5 |

**Brandenburg, Prussia, Silesia, Mecklenburg**

| Order | Sehling | Doc | § |
|---|---|---|---|
| Prussia, *Artikel der ceremonien und anderer kirchenordnung*, 1525 | 4, pp. 32, 37 | 1832, 1833 | 5.1, 6.4 |
| Brandenburg, *Kirchen-ordnung* of Joachim II, 1540 | 3, p. 70 | 1746 | 5.2, 6.1, 6.4 |
| Prussia, *Kirchenordnung*, 1544 | 4, p. 66 | 1833 | 6.4 |
| Mecklenburg, *Ordeninge der misse*, 1545 | 5, pp. 152, 155 | 1922 | 4.1, 4.5, 6.3, 6.4 |
| Breslau, 1550 | 3, p. 404 | 1807 | 6.3 |

**Lower Saxony, Westphalia and the North**

| Order | Sehling | Doc | § |
|---|---|---|---|
| Bremen, *Kirchenordnung*, 1534 | 7/2.2, p. 459 | 2217 | 4.5 |
| Hannover, *Kirchenordnung*, 1536 | 6/2, p. 1009 | 2051 | 4.3 |
| Calenberg-Göttingen, *Kirchenordnung*, 1542 | 6/2, pp. 816–834 | 2036, 2037 | 4.1, 5.2, 6.2, 6.4, A |
| Lippe, Corvinus's *Zeremonienordnung*, [1542] | 21, p. 352 | 1460 | 4.4 |
| Schleswig-Holstein, *Christlyke Kercken Ordeninge*, 1542 | 23, p. 91 | 1576 | 6.3 |
| Dortmund, *Gottesdienstordnung*, 1554 | 21, p. 209 | 1446 | 5.2 |
| Lüneburg, *Kirchenordnung*, 1564 | 6/1, pp. 542–543, 568–573 | 2003, 2005 | 3.3, 4.2, 4.4 |
| Buxtehude, *Agende*, 1565 (and Sehling's introduction) | 7/1, pp. 67, 92–98, 125 | 2080, 2082 | 4.2, 4.4, 6.4 |
| Wolfenbüttel, *Kirchenordnung*, 1569 | 6/1, pp. 178–179 | 1974 | 4.2, 4.4 |
| Lippe, *Kirchenordnung*, 1571 | 21, p. 397 | 1462 | 6.5 |
| Oldenburg, *Kirchenordnung*, 1573 (and Sehling's introduction) | 7/2.1, pp. 962, 1134–1145 | 2142, 2151 | 4.2, 4.4, 6.4 |
| Grubenhagen, *Kirchenordnung*, 1581 | 6/2, pp. 1076–1081 | 2058 | 4.2, 6.4 |
| Engerhafe, *Liturgie*, 1583 | 7/1, p. 681 | 2119 | 6.4 |
| Ysenburg-Birstein, *Kirchenordnung*, 1588 | 10, p. 622 | 228 | 4.2 |
| Verden, *Kirchenordnung*, 1606 | 7/1, p. 161 | 2090 | 3.3, 4.2, 6.3, A |
| Soest, *Kirchenordnung*, 1609 | 22, pp. 488, 495 | 1538 | 4.4, 6.5 |
| Schaumburg, *Kirchenordnung*, 1614 | 7/2.2, p. 150 | 2178 | 4.1, 4.2 |
| Osnabrück, *Agende*, (1588) 1618 | 7/1, pp. 270–278 | 2100 | 4.2, 6.3 |

**Strasbourg**

| Order | Sehling | Doc | § |
|---|---|---|---|
| Strasbourg, the early agendas: Schwarz's German Mass and the *Teutsche Meß*, 1524 (Moderate Reformed) | 20/1, pp. 123, 133, 135 | 1279 | 3.1, 6.1, A |

---

## Appendix A. The postcommunion texts and their sources

The prayers used after the communion in the corpus, with their Latin sources where one exists.
"Ed." means that Sehling's editors make the identification; "this guide" means that the
identification is this guide's own. The texts and translations are given in the sections named.

| German incipit | Latin source | Identified by | Orders | § |
|---|---|---|---|---|
| (Latin) *Quod ore sumpsimus, Domine, pura mente capiamus* | Priest's prayer at the ablutions, Ordo Missae | Luther 1523 | Luther 1523; Brandenburg 1540; Pfalz-Neuburg 1543 | 3.2, 6.1 |
| (Latin) *Corpus tuum, Domine, quod sumpsimus …* | Priest's prayer at the ablutions, Ordo Missae | Luther 1523 | Luther 1523; Brandenburg 1540; Pfalz-Neuburg 1543 | 3.2, 6.1 |
| "Das wir mit mund haben zu uns genomen, verlyhe uns, herr …" | *Quod ore sumpsimus* | Evident from the text | Strasbourg 1524 (*Complenda*; Moderate Reformed); Volprecht 1524 | 6.1 |
| "Die empfahung deines sacraments, o Herr, unser Gott …" / "O herre got, lass uns zu nutz kummen … die entphahunge des heiligen sacraments" | *Proficiat nobis ad salutem corporis et animae* (Trinity Sunday, postcommunion) | Canon guide (Volprecht); this guide (Erfurt) | Volprecht 1524 (Trinity); Erfurt 1525 (Trinity) | 6.2 |
| "O herr geuss in uns den geist der liebe …" / "Herr, uberschütte uns mit deinem Geiste …" | *Spiritum nobis, Domine, tuae caritatis infunde* (Easter, postcommunion) | Ed. (Calenberg-Göttingen); this guide (Müntzer) | Müntzer 1524 (Radical Reformation); Calenberg-Göttingen 1542 | 6.2 |
| "O herr vorlei uns die gnad des heiligen geists, auf das der thau deiner güte …" | *Sancti Spiritus, Domine, corda nostra mundet infusio* (Pentecost, postcommunion) | Ed. (Calenberg-Göttingen); canon guide | Müntzer 1524 (Radical Reformation); Erfurt 1525; Calenberg-Göttingen 1542 | 6.2 |
| "Herre, las uns entpfangen an mittel des tempels deine barmherzigkeit …" | *Suscipiamus, Domine, misericordiam tuam in medio templi tui* (1st Sunday in Advent, postcommunion) | Ed. | Calenberg-Göttingen 1542 | 6.2 |
| "O herr gott, steh hart bei uns …" | none known (new) | Canon guide | Müntzer 1524 (Advent; Radical Reformation) | 6.2 |
| "Wir danken dir, allmechtiger Herr Gott, das du uns durch diese heilsame gabe hast erquicket …" | *Gratias tibi referimus, Domine, sacro munere vegetati* (18th Sunday after Pentecost, postcommunion) | Ed. (Verden, after Drews) | Luther 1526, and nearly every later order | 3.3, 6.3 |
| "O almechtiger, ewiger Got. Wir sagen deiner götlichen miltigkeit lob und dank …" | none (new); expands *Quod ore sumpsimus* | This guide | Brandenburg-Nürnberg 1533; Brandenburg 1540; Calenberg-Göttingen 1542; Pfalz-Neuburg 1543; Oldenburg 1573 | 6.4 |
| "O Herr, allmechtiger Got, verleih uns … das wir durch den zeitlichen tod deines Suns …" | "apparently newly made" (ed.); perhaps from *Fac nos … quam pretiosi Corporis et Sanguinis tui temporalis perceptio praefigurat* (Corpus Christi, postcommunion) | Ed.; suggestion of this guide | Döber 1525; Mecklenburg 1545 | 6.4 |
| "Ach du lieber Herre Gott, der du uns bei diesem wunderbarlichen sacrament deines leidens zu gedenken und predigen befohlen hast …" | *Deus, qui nobis sub sacramento mirabili passionis tuae memoriam reliquisti* (Corpus Christi, collect) | This guide; ed. trace it to the Wittenberg hymnbook of 1533 | Württemberg 1536; Mecklenburg 1545; Buxtehude 1565; Oldenburg 1573; Nördlingen 1579; Saxony 1580; Mansfeld 1580; Grubenhagen 1581 | 6.4 |
| "O warhaftiger got, barmherziger vater … las uns dürftigen des heiligen leidens unsers herren nutz und frucht … ergreifen" | none known | — | Prussia 1544 (alternate Sundays) | 6.4 |
| "O Herr Jhesu Christe, der du deinen apostelen gesagt hast: Meinen friden geb ich euch …" | *Domine Iesu Christe, qui dixisti apostolis tuis* (Ordo Missae, prayer for peace) | Ed. | Calenberg-Göttingen 1542 (common Mass) | 6.2 |
| "Herr Gott, himlischer Vater, der du heiligen muth, guten rath und rechte werke schaffest …" (after *Verleih uns Frieden*) | *Deus, a quo sancta desideria, recta consilia, et iusta sunt opera* (Mass for peace) | Ed. | Saxony 1539; Calenberg-Göttingen 1542; Henneberg 1582; Grubenhagen 1581; Oldenburg 1573; Schaumburg 1614; and others | 4.1, 6.2 |
