# The Propers of the Mass in the Sehling Church Orders

This guide follows the **propers of the Mass**, the parts that change with the day, through the
evangelical church orders printed in Emil Sehling's *Die evangelischen Kirchenordnungen des XVI.
Jahrhunderts*. The propers covered are the introit, the prophecy or Old Testament lesson, the
epistle, the gradual, the alleluia and tract, the gospel, the offertory, the Proper Preface and
the communion chant. For each it asks:
- Was it **kept**, and where?
- **Who sang or read it**: the cantor and the school choir, the celebrant, the congregation, the
  organ? Was it sung in alternation?
- Was it in **Latin or German**?
- Were the **historic tunes** kept, cut, or replaced with new music: new tones, polyphony?

For the **Proper Prefaces** it asks also:
- On which days of the season, feast or saint were they used?
- Which Prefaces did each order have?

**Appendix A** renders every Proper Preface in the corpus:
- in the original language, Latin and German or Low German;
- with a formal-equivalence translation in the idiom of the Authorized Version;
- with the list of the orders that carry each text.

Where the corpus has both the Latin and a German translation, both are given. The English is
then made from the Latin, with notes on where the German shortens, adds to or changes it.

**How the guide is laid out.**
- §1 summarizes the findings, and §2 sets out the method and cautions.
- §3 describes the three ways the orders dealt with the propers.
- §§4–9 take the propers in turn: introit, lessons, gradual, offertory, Preface, communion.
- §10 deals with the music.
- §11 is a table by order, and §12 a concordance.

**Conventions**

- **Quotations.** Every quotation is Sehling's text as it stands in the `eko.db` database built
  from the digitized edition.
  - Footnote numbers, sigla, folio markers and interleaved apparatus are left out.
  - Sehling's own supplied words in square brackets are kept, as are "[!]", "[sic]" and his
    other signs. So are the bracketed alternatives that some orders print themselves.
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
  - Liturgical stock phrases are given in their familiar forms. For example, *Vere dignum et
    iustum est* is "It is very meet and right".
  - Words the translation supplies are in square brackets.
- **Citations.** Citations are in the form "Sehling volume, page".
  - The half-volumes of the edition are written 6/1, 6/2, 7/1, 7/2.1, 7/2.2, 17/1, 19/2, 20/1
    and so on, following the digitized volumes.
  - Each order is named by place, title and date as they appear in Sehling's running heads.
    Where a passage is Sehling's own introduction or apparatus, this is said.
- **Traditions.** Most of the orders cited are Lutheran, and they are not marked. Every order of
  another tradition is marked where it is cited, by its name in brackets after the order, as
  "Kurpfalz 1563 (Reformed)". The traditions follow the inventory in
  [`CHURCH_ORDERS_GUIDE.md`](CHURCH_ORDERS_GUIDE.md), §3:
  - **mediating**: orders that stood between the Lutheran and the Reformed: the Upper German
    cities of Bucer's circle before the Interim, Philip of Hesse's church, Hermann von Wied's
    Cologne order, and the Philippist churches of Bremen and Colmar;
  - **Radical Reformation**: Thomas Müntzer's Allstedt orders.
  - The mark follows the order cited, not the territory, since a territory could change its
    tradition: Strasbourg is mediating until the Interim of 1548 and Lutheran after it.
  - Orders made under or for the Augsburg Interim of 1548 are marked as Interim orders
    (`CHURCH_ORDERS_GUIDE.md`, §4).
  - The orders that took over Müntzer's German propers (Erfurt 1525,
    Calenberg-Göttingen 1542, Lippe 1571) are Lutheran; only Müntzer's own Allstedt orders are
    marked.

---

## Contents

- [1. Summary of findings](#1-summary-of-findings)
- [2. Scope, sources and cautions](#2-scope-sources-and-cautions)
- [3. Three ways of handling the propers](#3-three-ways-of-handling-the-propers)
- [4. The introit](#4-the-introit)
- [5. The lessons: prophecy, epistle and gospel](#5-the-lessons-prophecy-epistle-and-gospel)
- [6. Gradual, alleluia and tract](#6-gradual-alleluia-and-tract)
- [7. The offertory](#7-the-offertory)
- [8. The Proper Preface](#8-the-proper-preface)
- [9. The communion chant (*communio*)](#9-the-communion-chant-communio)
- [10. The music: old chant, cut chant, new tones, polyphony and organ](#10-the-music-old-chant-cut-chant-new-tones-polyphony-and-organ)
- [11. Table by order](#11-table-by-order)
- [12. Concordance of the orders quoted](#12-concordance-of-the-orders-quoted)
- [Appendix A. The Proper Prefaces: texts and translations](#appendix-a-the-proper-prefaces-texts-and-translations)

---

## 1. Summary of findings

**1. Three models, often combined.** The orders handle the propers in one of three ways (§3):
- **Keep them in Latin**, sung by the school choir: the *Formula missae* line.
- **Translate them into German prose**, sung to the old tones: Müntzer 1524 (Radical
  Reformation), Erfurt 1525, Calenberg-Göttingen 1542.
- **Replace them with German hymns** sung by the congregation: the *Deutsche Messe* line.

Most territorial orders allowed all three by place and day:
- Latin "where there is a school", "in the towns", "on the feasts";
- German psalms "in the villages" and on ordinary Sundays.

The constant condition is that a proper must be **from Scripture and "pure"**. In practice this
meant ***de tempore*, not *de sanctis*** (§3.1, §6.2).

**2. The introit was the most widely kept proper** (§4).
- **Luther's approval.** Luther approved the Sunday and festal introits "if taken from
  Scripture" (1523).
- **Who sang it.** The **school** sang it in Latin, under the cantor or schoolmaster, while the
  priest read it quietly. Villages sang a German psalm instead.
- **Fallbacks.** Where boys could not learn every Sunday's introit, they repeated *Benedicta sit
  sancta Trinitas* or *Spiritus Domini* (Hatzkerode, Heilbronn, Kurpfalz, Hamburg 1556).
- **German introits.** These appear in Müntzer (Radical Reformation), Erfurt and Hof 1592.
  Wittgenstein 1555 allows the festal introits to be sung in German in the villages.
- **Organ and polyphony.** By the later century the introit was often played by the organ in
  alternation with the choir, or sung *figuraliter* (Nördlingen 1579, Hof 1592).

**3. No Old Testament "prophecy" before the epistle survives as a regular lesson** (§5.1).
- **At the Mass.** The prophetic lessons that remain are the historic epistles taken from a
  prophet (Hof 1592). On some feasts a chapter of the feast's history is read instead
  (Pfalz-Neuburg 1543).
- **At the office.** Old Testament lessons belong to Matins and Vespers. They were read in the
  old **prophecy tone**, whose cadence is written out in solmization (Hamburg 1529, Pomerania
  1535, Wittenberg 1533).

**4. The epistle and gospel of the day were kept everywhere, and read toward the people**
(§5.2–5.3).
- **Exceptions.** Müntzer (Radical Reformation), and Nürnberg and Brandenburg-Nürnberg in the
  1520s–30s, read whole chapters in sequence.
- **Three practices of language and tone:**
  - **German in new tones.** Luther's *Deutsche Messe* has the epistle in the eighth tone and
    the gospel in the fifth. The Saxon orders send pastors to copy "the tone and accent
    customary at Wittenberg".
  - **German read without notes**, for intelligibility (Mecklenburg).
  - **Latin chanted "in the old customary melody", then read in German** (Schwäbisch Hall 1526,
    Hamburg 1556, Brieg 1592). Brandenburg's visitors required this in 1573.

**5. The gradual and alleluia survived as a Latin choir piece, cut short** (§6).
- **Cut short.** Luther limited the gradual to two verses, and kept the alleluia in Lent as "the
  perpetual voice of the church". Bugenhagen's northern orders cut off the jubilus, "the many
  notes which one was wont to hang on behind".
- **Replaced.** In villages, and where the text was "not pure", a German psalm took the place.
- **German graduals.** Müntzer (Radical Reformation) and Erfurt have them. Nürnberg sang its
  gradual "in a tone made for it".

**6. The offertory chant was the proper most often dropped** (§7).
- **Dropped.** It went with the offertory prayers as part of the "abomination" of sacrifice
  (Luther 1523). Volprecht says it is "never said, because Christ was once offered for our
  sins".
- **Kept.** A few orders kept the Latin offertory as a Scripture text sung by the choir:
  Wittenberg 1525, Brandenburg 1540, Ansbach 1548, Amberg 1550.
- **Translated.** Müntzer (Radical Reformation) and Erfurt translated it.
- **Replaced.** Most replaced it with a German psalm or the creed hymn.

**7. The Proper Preface survived chiefly on the feasts, in Latin, to the Missal tones** (§8).
- **Cut.** Luther cut the Preface short in 1523 and dropped it in 1526. Prussia abolished it
  outright.
- **The usual rule.** Most orders from Duke Henry's Saxon order of 1539 on adopted the rule:
  **the Latin Preface on the feasts, the exhortation on ordinary Sundays**.
- **The feasts.** The proper Prefaces were those of the feasts of Christ: Christmas, Epiphany,
  Easter, Ascension, Pentecost, Trinity.
- **Ordinary Sundays.** Bugenhagen's northern orders chose the **Trinity Preface** "made against
  the Arians" (Hamburg 1529, Wolfenbüttel 1543, Herford 1532, Wittenberg 1533). Wolfenbüttel
  1543 dropped even the common Preface as "needless".
- **Saints' days.** Sanctoral Prefaces were excluded as impure. The exceptions are:
  - **Michaelmas**, with the common Preface (Hoya, Osnabrück, Lippe);
  - the **Marian and Apostles' Prefaces** in Dortmund's Low German set of 1554, the Apostles'
    made to speak of the apostles' "doctrine";
  - Müntzer's rewording (Radical Reformation) of the Marian Preface for Advent.
- **Who sang.** The priest sang the Preface at the altar; the choir answered and sang the
  Sanctus.
- **Language.** In Lippe 1571 and Mecklenburg the towns had Latin and the villages German.

**8. The communion chant was optional from the start and was mostly replaced by hymns** (§9).
- **Optional.** Luther says "If one will sing the communion, let it be sung".
- **Kept in Latin.** Volprecht, Ansbach 1536 and Brandenburg 1540 kept it.
- **German.** Müntzer (Radical Reformation) and Erfurt translated it.
- **Polyphony.** In the larger churches festal motets "*sub communione*" took its place, among
  them Clemens non Papa's *Pascha nostrum* at Hof.

**9. The old melodies were kept, trimmed, and supplemented** (§10).
- **Kept.** The Latin propers kept the plainchant of the old books, standardized in **Lossius's
  *Psalmodia***. Rostock made it binding around 1560, and Hof used it in 1592.
- **Trimmed.** They were trimmed by verse and melisma.
- **New tones.** German texts got new or adapted tones.
- **Polyphony.** From the 1530s the feasts brought **polyphonic** introits, Masses and motets:
  "choraliter or figuraliter". Hof 1592 names Senfl, Lassus, Clemens, Victoria, Walter, Isaac
  and Josquin.
- **Organ.** The organ alternated with the choir in the introit and the ordinary.

**10. Appendix A gives every Proper Preface in the corpus.**
- **Latin.** The Latin set (Christmas, Epiphany, Easter, Ascension, Pentecost, Trinity, common)
  belongs to the Lower Saxon and Westphalian orders, Lüneburg 1564 to Verden 1606.
- **German translations of the Latin:**
    - **Müntzer's** (1524, Radical Reformation), carried on by Erfurt, Calenberg-Göttingen and
      the Lippe villages;
    - **Strasbourg's** (1524, mediating);
  - **Dortmund's** Low German (1554), which alone translates the whole Roman series, Lent,
    Cross, the Virgin and the Apostles included.
- **New German Prefaces.** There are four:
  - Grubenhagen's Isaiah 53 Preface for Maundy Thursday (1581);
  - Lippe's Michaelmas Preface on the forgiveness of sins (1571);
  - Kurland's Christmas and Pentecost Prefaces (1570), built on the Easter Preface.

---

## 2. Scope, sources and cautions

**What was searched.** The `eko.db` database was searched for every proper by name, in Latin,
German and Low German spellings:
- *introitus*;
- *prophetia*, *lectio*;
- *epistola*;
- *graduale*, *alleluia*, *tractus*;
- *evangelium*;
- *offertorium*;
- *praefatio*, *Vorrede*;
- *communio*, *sub communione*.

It was also searched for the singers (*Schüler*, *Knaben*, *Chor*, *Cantor*, *Organist*), for
the languages (*lateinisch*, *deutsch*, *düdesch*), and for the music (*Noten*, *Ton*, *tonus*,
*Melodei*, *figuraliter*, *choraliter*, *mensur*). The Proper Prefaces were searched for by the
opening words of each Latin text and of the known German translations. The passages were then
read in context.

**Related guides.** Two earlier guides overlap with this one:
- [`HYMN_PRACTICE_GUIDE.md`](HYMN_PRACTICE_GUIDE.md) deals with the **hymns** that replaced the
  introit, gradual, sequence, offertory and communion. This guide deals with the propers
  themselves: the Latin chant, German prose versions, and the lessons and Prefaces.
- [`CANON_IN_GERMAN_MASSES.md`](CANON_IN_GERMAN_MASSES.md) gives the German **common** Prefaces
  of the early German Masses (Kantz, Worms (mediating), Volprecht, Döber, Bremen) and the
  Preface sections of Müntzer (Radical Reformation), Strasbourg (mediating), the Kiel Mass and
  Lippe. Those texts are cited here, not repeated, except where a Proper Preface is concerned.

**Cautions.** Four things limit what the corpus can show:
- **Silence is not absence.** Many orders say only "the introit" or "the gradual", or "as
  hitherto", and assume the old books. Where an order is silent, the Latin chant may well have
  gone on.
- **Sehling did not print everything.** The edition leaves out much musical and liturgical
  matter. The notated Prefaces of Mecklenburg (1545, 1552), Pomerania (1542), Mansfeld (1580)
  and Buxtehude (1565) are described but not printed (Appendix A, introduction). Hof's tables of
  introits and motets are printed, but its notes are not.
- **Notes are marked, not reproduced.** Where an order prints music, the edition shows
  "[Noten:]" and "[Ende der Noten]". The texts are given, but not the melodies. Sehling's
  editors often identify the melody in the *Handbuch der deutschen evangelischen Kirchenmusik*.
- **Town and village differ.** A territorial order often sets one practice for the towns with
  Latin schools and another for the villages. Both are reported here.

**Terms.**
- ***de tempore***: of the season, or of the Sunday.
- ***de sanctis***: of the saints.
- ***dominica***: of the Sunday.
- ***de festo***: of the feast.
- ***choraliter***: in plainchant.
- ***figuraliter***, ***in mensuris***, "mensur": in mensural polyphony.
- ***organicen***: the organist.
- ***Schüler***, ***Knaben***, ***Chor***: the Latin school, which was the choir.
- ***Amt***: the Mass, "the office".

---

## 3. Three ways of handling the propers

The orders deal with the propers in one of three ways, and many combine them by place and by
day:
- **keep them in Latin**, sung by the school (§3.1);
- **translate them into German prose**, sung to the old tones (§3.2);
- **replace them with German hymns** sung by the congregation (§3.3).

### 3.1 Latin propers, sung by the school (the *Formula missae* line)

**Luther's position.** Luther's *Formula missae* (1523) keeps the sung propers of the Sundays
and the feasts of Christ:
- the introit (§4.1);
- the gradual of two verses with the alleluia (§6.1);
- the communion "if one will" (§9.1).

It rejects the offertory as the beginning of the "abomination" of the sacrifice (§7.1). The rule
is that what is sung *de tempore*, from Scripture, may stay. Luther says the Sunday propers
"alone still bear witness to the ancient purity, except the canon" (Sehling 1, p. 4).

**Wittenberg 1525.** A Wittenberg report of 1525 on "how it is held for a time with the
ceremonies of the Mass" lists the parts sung. They include, at that date, even the offertory.
**Wittenberg, *Wie es einer zeit mit den ceremonien der messe gehalten*, 1525**
(Sehling 1, p. 698):

<!-- doc 147 -->
> doch umb etlicher sachen umbs glauben willen lasset man singen de tempore, und nit de sanctis,
> und singet introitum, kyrieleison, gloria in excelsis, et in terra, collecta, oder preces,
> epistel, gradualia, on sequens, evangelium, credo, offertorium, prefatio, sanctus, on canonen
> maior und minor, dieweil die geschrift nit gemess seind.

[…] yet for certain causes touching the faith one letteth sing *de tempore*, and not *de
sanctis*; and one singeth the introit, Kyrie eleison, Gloria in excelsis, Et in terra, the
collect or prayers, the epistle, the graduals (without sequence), the gospel, the Creed, the
offertory, the preface, the Sanctus; without the greater and lesser canon, since these are not
agreeable to Scripture.

**Who sang the Latin propers.** In the orders that kept the Latin propers, they were sung by the
**school choir** under the cantor or schoolmaster: the introit, gradual, alleluia, sometimes the
offertory, and the communion. The priest sang the collect, epistle, gospel and Preface. Latin
was defended as **training for the boys**. Veit Dietrich's Nürnberg *Agendbüchlein* (1545) has
the scholars sing the introit "if it be agreeable to Scripture, or a German psalm". It adds that
"where there are schools, the Latin tongue also be exercised with singing in the church".
**Nürnberg, *Agendbüchlein* of Veit Dietrich, 1545** (Sehling 11, p. 495):

<!-- doc 297 -->
> Dieweil sollen die schuler den introitum, so er der schrift gemeß ist, singen oder ein
> teutschen psalm, nachdem es im gebrauch ist, doch das, wo schulen sind, die lateinisch sprach
> auch mit dem gesang in der kirchen geübet werde.

Meanwhile shall the scholars sing the introit, if it be agreeable to scripture, or a German
psalm, according as it is in use; yet so that, where there are schools, the Latin tongue be also
exercised with singing in the church.

**The territorial orders.** The Latin propers were kept in this way in the territorial orders of
Albertine Saxony (1539, 1580), Brandenburg (1540), Brandenburg-Nürnberg (1533), Pfalz-Neuburg
(1543), Mecklenburg (1545, 1552), Pomerania (1535, 1542, 1569), Hohenlohe (1553), Amberg (1550,
1555), Regensburg (1553, 1567), Hamburg (1556), Wolfenbüttel (1543, 1569), Lüneburg (1564), Hoya
and Grubenhagen (1581) and Hof (1592). Each has its own limits, given in the sections that
follow.

**Brandenburg 1540** is the most conservative. It keeps the Latin offertory and communion as
well, in the collegiate churches and towns. The parishes and villages get German psalms (§7.2).

### 3.2 German prose propers, sung to the old tones

**Müntzer** (Radical Reformation). Müntzer's *Deutsch evangelisch Messe* (Allstedt 1524) is the
first full set. For each of five offices (Advent, Christmas, Passion, Easter, Pentecost) it has
a German introit with its whole psalm, Kyrie, Gloria, collect, epistle, gradual and alleluia,
gospel, offertory, Preface, Sanctus, Agnus Dei and communion. It is printed with notes.
Müntzer's own explanation says the people are "led with the customary singing, in their own
tongue, as children are brought up with milk". **Allstedt, Thomas Müntzer, *Ordnung und
berechnunge des teutschen ampts*, 1523/24** (Sehling 1, pp. 504–505):

<!-- doc 52 -->
> Demnach so nimpt man bei uns den eingang der geheim gotis aus dem psalter, do der schlussel
> David auf der schultern Christi ist, zu eröffnen alles, was gesungen wirt. Auf das man je
> klerlich sehe, one stückwerk, singet man den ganzen psalm, wie im anfang der christenheit
> durch die frommen nachfolger der heiligen aposteln geschach. […] Hirnach wirt gesungen das
> gradal und alleluia, auf das der mensche geherzt werd, sich festiglich auf gotis wort
> zuverlassen. […] Zum andern ist zu wissen, das wir alzeit ein ganz capitel anstat der epistel
> und evangelion lesen, auf das die stuckwerkische weise damit vorworfen werden, und das die
> heilige schrift der biblien dem volk gemein werde, […] und die leut mit gewonlichem gesange,
> mit eigener sprache geleitet werden, wie die kinder mit milch erzogen

Accordingly with us the entrance of the mystery of God is taken out of the Psalter, where the
key of David is on the shoulder of Christ, to open all that is sung. That it may be seen
clearly, without piecework, the whole psalm is sung, as was done in the beginning of Christendom
by the godly followers of the holy apostles. […] After this the gradual and alleluia are sung,
that a man may be heartened to rely firmly on God's word. […] Secondly, be it known that we
always read a whole chapter instead of the epistle and gospel, that the piecemeal manner may
thereby be cast off, and the holy scripture of the Bible be made common to the people, […] and
the people be led with the customary singing, in their own tongue, as children are brought up
with milk […]

**Erfurt and Calenberg.** The **Erfurt *Deutsches Kirchenamt*** (1525) reprints Müntzer's
offices, labels each piece (*Introitus*, *Gradual*, *Offertorium*, *Prefatio*, *Commun.*) and
adds one for Trinity (Sehling 2, pp. 376–380). **Calenberg-Göttingen 1542** gives a notated
German Mass for the Sundays and the feasts with German epistles, gospels, alleluias and
Prefaces, but it has a German psalm "in place of the offertory" (Sehling 6/2, pp. 813–833).
Sehling's editors trace its Prefaces to Müntzer and to the Erfurt *Kirchenamt*.

**Strasbourg 1524** (mediating). The **Strasbourg *Teutsche Meß*** of 1524 gives German Prefaces
for the feasts (Sehling 20/1, pp. 133–134). Its Augsburg reprint explains each Latin heading for
the reader: "Introitus – Das nennet man anfang oder eingang", "that is called the beginning or
entrance" (p. 135). Its successors drop the Preface (§8.1).

**Later German prose propers.** These are fewer:
- Wittgenstein 1555 lets the festal introits be "learned and sung in German in the villages"
  (§4.4).
- Hof 1592 has German prose introits for ordinary Sundays (§4.4).
- The German Prefaces of Lippe 1571, Kurland 1570 and Grubenhagen 1581 are given in Appendix A.

### 3.3 Hymns in place of the propers (the *Deutsche Messe* line)

Luther's *Deutsche Messe* (1526) replaces the introit with "a spiritual song or a German psalm",
and the gradual with a German hymn ("Nu bitten wir" or another). It has no offertory and no
Preface. It keeps the epistle and gospel, sung in German to new tones (§5.3). This model, and
the choice of hymns, is the subject of the hymn-practice guide (`HYMN_PRACTICE_GUIDE.md`, §§3–5,
8, 11, 14). Here it matters only as the third option, which most orders allowed side by side
with the first:
- "**in the towns** Latin, **in the villages** German";
- "**where there is a school**" Latin, otherwise a German psalm;
- Latin "**on the feasts**", German on ordinary Sundays.

**Albertine Saxony.** Duke Henry's Saxon order of 1539 makes the arrangement for ordinary use.
**Albertine Saxony, *Kirchenordnunge zum anfang* (Duke Henry's *Agende*), 1539**
(Sehling 1, p. 271):

<!-- doc 30 -->
> sollen die schuler singen: Erstlich den introitum von der dominica, oder festen, darauf das
> kyrie eleison, gloria in excelsis, und et in terra latinisch, darnach die collecten deudsch
> oder latinisch, darauf die epistel gegen dem volk deudsch, darnach ein sequenz, oder deudschen
> psalm, oder andern geistlichen gesang, wie solches ein jede zeit erfordert. Darnach das
> evangelium von der dominica oder vom fest, auch gegen dem volk deudsch gelesen, darauf den
> glauben gesungen, wir gleuben all an einen gott etc.

[…] the scholars shall sing: first the introit of the Sunday or of the feast, thereafter the
Kyrie eleison, Gloria in excelsis and Et in terra in Latin; thereafter the collects in German or
Latin; thereafter the epistle toward the people in German; thereafter a sequence, or a German
psalm, or other spiritual song, as each season requireth. Thereafter the gospel of the Sunday or
of the feast, also read toward the people in German; thereupon the Creed sung, "Wir glauben all
an einen Gott" etc.

---

## 4. The introit

### 4.1 Luther's rule: the Sunday and festal introits, if from Scripture

The *Formula missae* approves "the introits of the Sundays and of the feasts of Christ", Easter,
Pentecost and Christmas, though Luther would rather have the whole psalms "from which they are
taken, as of old". Introits of the saints may be kept by those who wish, "when they are taken
from the psalms or other Scriptures". **Luther, *Formula missae et communionis*, 1523**
(Sehling 1, p. 5):

<!-- doc 2 -->
> Primo, introitus dominicales et in festis Christi, nempe paschatis, pentechostes, nativitatis,
> probamus et servamus, quamquam psalmos mallemus, unde sumpti sunt, ut olim, sed nunc sic usui
> recepto indulgebimus. Quod si qui apostolorum, virginis aliorumque sanctorum introitus (quando
> e psalmis aut aliis scripturis sumpti sunt) probare volent, non damnamus.

First, the introits of the Sundays and of the feasts of Christ, to wit of Easter, Pentecost and
the Nativity, we approve and keep; although we had rather have the psalms, whence they are
taken, as of old; but now we will indulge the received use. But if any will approve the introits
of the apostles, of the Virgin and of other saints (when they are taken out of the psalms or
other scriptures), we condemn it not.

The rest of the century repeats the condition "if it be taken from Holy Scripture" or "so far as
it is pure" almost word for word:
- Brandenburg-Nürnberg 1533 (Sehling 11, p. 188);
- Weißenburg 1528 (11, p. 659);
- Hohenlohe 1553 (15, p. 68);
- Mecklenburg 1545 (5, p. 151);
- Teschen 1584 (3, p. 462);
- Henneberg (Meiningen) 1566 (2, p. 339).

### 4.2 Who sang it: the school, in Latin, with a German psalm for the villages

**The school sang it.** The introit was sung by the **school**: the schoolmaster or cantor with
the boys, "as was customary". The priest might read it quietly at the altar meanwhile. The
Brandenburg-Nürnberg order of 1533 sets out the arrangement that became standard in the south.
**Brandenburg-Nürnberg, *Kirchenordnung*, 1533** (Sehling 11, p. 188):

<!-- doc 270 -->
> darnach den introitum lesen, doch das er aus der heiligen schrift genummen sei. Dieweil sollen
> die schuler, wo man schul hat, den introitum auch singen lateinisch. Wo man aber als in
> dörfern zu solichem lateinischen gesang nicht leut hette, soll man ein christenlich teutsch
> gesang nach gelegenheit jedes orts singen. Wo aber das volk solich geseng nicht könte, sollens
> die pfarherr anrichten zu lernen.

[…] thereafter [let the priest] read the introit, provided it be taken out of holy scripture.
Meanwhile let the scholars, where there is a school, sing the introit also in Latin. But where,
as in villages, there are no folk for such Latin singing, a christian German song shall be sung,
according to the occasion of each place. And where the people could not [sing] such songs, the
pastors shall set about teaching them.

**Where there was no choir.** In Pfalz-Neuburg 1543, "where there is no choir, as in the country
in villages", the **priest himself** sings or reads the introit (Sehling 13, p. 70).

**Saxony.** Duke Henry's Saxon order of 1539 and the Electoral Saxon order of 1580 both open the
Mass with "the scholars shall sing: first the introit of the Sunday or feast"
(Sehling 1, pp. 271, 368).

**The north.** The northern orders have the same division. Mecklenburg 1545 has the cantor or
schoolmaster "in the towns" begin the introit in Latin, "or sing at times a German psalm". It
gives the introits of the chief feasts by incipit. In the villages, between Christmas and
Candlemas, the German stanzas of "Ein Kindelein so löbelich" serve as the introit.
**Mecklenburg, *Ordeninge der misse*, 1545** (Sehling 5, p. 151):

<!-- doc 1922 -->
> Hirna schall in den steden de cantor edder scholmester den introitum anfangen to latin, effte
> singen under tiden enen düdeschen psalm. Erbarme di miner o here godt, etc. Menn kan dat jar
> aver in den steden singen de introitus, de nicht wedder de hillige schrift sint. In den hogen
> festen, winachte: Puer natus etc. In die Epiphanie: Ecce advenit etc. In die Purificationis
> singe me vor enen introitum de veer schonen versche. Ein kindelin etc. Welck ock de sondage
> twischen winachten und lechtmissen up den dörpern schal vor enen introitum gesungen werden.
> […] In den ostern: Resurrexi, Ascensionis: Viri Galilei. In den pinxsten: Spiritus domini.
> Trinitatis: Benedicta sit sancta tri[nitas].

Hereafter in the towns shall the cantor or schoolmaster begin the introit in Latin, or sing at
times a German psalm, "Have mercy upon me, O Lord God", etc. One may through the year in the
towns sing the introits that are not against holy scripture. On the high feasts, at Christmas:
*Puer natus* etc. On Epiphany: *Ecce advenit* etc. On the Purification let the four goodly
verses be sung for an introit, "A little child so laudable" etc.; which also on the Sundays
between Christmas and Candlemas shall be sung in the villages for an introit. […] At Easter:
*Resurrexi*; at the Ascension: *Viri Galilaei*; at Pentecost: *Spiritus Domini*; on Trinity:
*Benedicta sit sancta Trinitas*.

**Hesse, late in the century.** The Hessian *Agende* of 1574 (mediating) allows a Latin psalm
"or introit" only where there are people who understand it, and only "at the beginning, before
the whole congregation cometh together". In the villages German songs only are to be sung, and
in the towns German songs for the most part. **Hesse, *Agende*, 1574**
(mediating; Sehling 8, p. 411):

<!-- doc 2272 -->
> ein lateinischer psalm oder introitus gesungen werden, doch daß auf den dorfen durchaus, in
> stedten aber mehrerteils allein teutsche gesenge im gemeinen brauch seien und bleiben.

[…] a Latin psalm or introit [may] be sung; yet so that in the villages throughout, but in the
towns for the most part, only German songs be and remain in common use.

**Sung slowly.** Calenberg-Göttingen 1542 has the choir sing the introit "**right slowly, so
that it become not an ass's braying**" (Sehling 6/2, p. 793).

### 4.3 The Trinity or Holy Ghost introit as a fallback

Where the boys could not learn a new introit each Sunday, the orders let them repeat one. The
usual choices were *Benedicta sit sancta Trinitas* (Trinity) or *Spiritus Domini* (Pentecost).
Hatzkerode (about 1534) allows the Trinity introit "where the Sunday introits were too hard for
the boys". It adds that they "should yet learn them in time, since they are taken from
Scripture". **Hatzkerode, *Kirchenordnunge*, 1534(?)** (Sehling 2, p. 586):

<!-- doc 1263 -->
> darnach den introitum von fest ader de tempore, zuweilen de S. Trinitate nach gefallen des
> pfarhers, wo die sontage introitus den knaben zu swer weren. Doch sollen sie die, weil sie aus
> der schrift genommen, mit der zeit auch lernen.

[…] thereafter the introit of the feast or of the season, sometimes of the Holy Trinity at the
pastor's pleasure, where the Sunday introits were too hard for the boys. Yet they shall learn
them also in time, since they are taken out of scripture.

**Other orders with the same fallback.**
- **Heilbronn's song order of 1543** begins "**Every Sunday hath its own introit, which shall be
  sung to the organ**". For a schoolmaster who finds that too much, it provides a reduced cycle:
  from Easter to Pentecost the Easter introit, from Trinity *Benedicta* (Sehling 17/1, p. 322).
- **Kurpfalz 1546** names "the introit of the season, or of the Holy Trinity, or of the Holy
  Ghost" (Sehling 14, p. 96).
- **Hamburg 1556** keeps the Latin introit for feasts, and "sometimes also on the Sundays *de
  Trinitate* or *de Spiritu sancto*" (Sehling 5, p. 552).

### 4.4 German introits

**Müntzer and Erfurt.** Müntzer's *Deutsch evangelisch Messe* (1524, Radical Reformation) and
the Lutheran Erfurt *Deutsches Kirchenamt* (1525) translate the introits into German prose, with
their psalm verse and *Gloria Patri*, and sing them to the Latin melody (§3.2). Erfurt's
Christmas introit is an example. **Erfurt, *Deutsches Kirchenamt*, 1525, "das ampt von der
gepurt Christi"** (Sehling 2, p. 379):

<!-- doc 1251 -->
> Introitus: Uns ist ein kind geboren, und ein sohn ist uns gegeben, welches hirschaft ist auf
> seiner schuldern. Und sein nam wurd geheissen ein engel des grossen rathes. Singet got dem
> herren ein neues lied; dan er hat wundersam ding gemachet. Ehre sei dem vater und dem etc.

Introit: Unto us a child is born, and unto us a son is given, whose government is upon his
shoulder; and his name shall be called the angel of great counsel. Sing unto God the Lord a new
song, for he hath done marvellous things. Glory be to the Father and to the, etc.

**Wittgenstein 1555.** Wittgenstein keeps the Latin festal introits, *Puer natus*, *Resurrexi*
and *Spiritus Domini*. It adds that these "may also be learned and sung in German in the
villages", or else replaced by the festal hymn. **Wittgenstein, *Kirchenordnung*, 1555**
(Sehling 22, p. 102):

<!-- doc 1493 -->
> nach dem Veni sancte den gewönlichen introitum singen, als da sind: Puer natus est nobis etc.,
> Resurrexi et adhuc tecum sum etc., Spiritus Domini replevit orbem terrarum etc., welche man
> auch auff den dörffern deutsch lernen und singen kan oder an stadt derselbigen brauchen: Der
> tag, der ist so freudenreich etc., Christ lag in todes banden etc., Es ist das heyl uns kommen
> her etc.

[…] after the *Veni sancte* sing the customary introit, such as are: *Puer natus est nobis*
etc., *Resurrexi et adhuc tecum sum* etc., *Spiritus Domini replevit orbem terrarum* etc.; which
one may also learn and sing in German in the villages, or use in their stead: "Der Tag, der ist
so freudenreich" etc., "Christ lag in Todesbanden" etc., "Es ist das Heil uns kommen her" etc.

**Hof 1592.** Hof's weekly table (§10.3) gives German prose introits for ordinary Sundays:
"Bistu, der da kommen soll?" (Advent III), "Ein kindlein ist uns geboren" (Epiphany I), "Ich bin
die auferstehung" (Cantate) (Sehling 11, pp. 433–440). The festal introits are kept in Latin, in
polyphony.

**Hymns in the introit's place.** These are treated in the hymn-practice guide
(`HYMN_PRACTICE_GUIDE.md`, §5): "a German psalm" (Ps 67, 51, 130, 12, 124 or 14), "Komm heiliger
Geist", or the feast's own *Leise*.

### 4.5 Organ, polyphony and alternation

**Organ.** In the larger churches the introit was shared between organ and choir, or set in
polyphony:
- In **Regensburg 1553** the organist, if there is one, "plays the introit together with the
  Kyrie, *Et in terra*, *Patrem*, Sanctus and Agnus Dei on the organ" (Sehling 13, p. 421).
- In **Merseburg 1545**, at an ordination Mass, *Benedicta sit sancta Trinitas*, the Kyrie and
  the Gloria were sung "on the organ and choir", in alternation (Sehling 2, p. 7).
- In **Nördlingen 1579**, on the high feasts, "the introit of the season is first struck by the
  organist, and sung by the scholars *figuraliter*" (Sehling 12, p. 365).

**Hof 1592** describes a three-choir alternation of the introit with the organ. The parts are
the whole choir, a second choir of the older boys, and a **choir of girls**. **Hof, *Ordo
ecclesiasticus*, 1592** (Sehling 11, p. 424):

<!-- doc 294 -->
> I. Organicen introitum modulatur usque ad versum, chorus vero eundem gubernante ludirectore
> canit et quidem primam partem chorus totus, alteram seu repetitionem chorus secundus ex
> adulterioribus conflatus versiculum chorus puellarum, qui in ordine est tertius. His peractis
> organicen versiculum seu Gloria Patri praecinit; chorus totus Gloria Patri, secundus chorus
> denuo incipit introitum usque ad repetitionem, chorus puellarum repetitionem absolvit usque ad
> versiculum. […] Nota. Figuraliter eodem modo unaque vice canitur introitus praeside cantore
> usque ad versiculum; post organa audita versiculus additur solus nihil amplius repetito.

I. The organist playeth the introit as far as the verse; and the choir, the schoolmaster
governing, singeth the same: the first part the whole choir, the second or repetition the second
choir, made up of the older [boys], the versicle the choir of girls, which is the third in
order. These done, the organist preludeth the versicle or *Gloria Patri*; the whole choir
[sings] *Gloria Patri*; the second choir beginneth the introit again as far as the repetition;
the girls' choir finisheth the repetition as far as the versicle. […] Note. In figural music the
introit is sung in the same manner and once only, the cantor presiding, as far as the versicle;
after the organ hath been heard, the versicle alone is added, and nothing more repeated.

Hof's festal table assigns polyphonic introits by name. For Christmas it has "*Puer natus est
nobis*, a 4, by Senfl", and for the Ascension "*Viri Galilaei*, a 4" (Sehling 11, pp. 457, 462).
See §10.

---

## 5. The lessons: prophecy, epistle and gospel

### 5.1 The Old Testament "prophecy"

**At the Mass.** None of the orders in the corpus adds a regular **Old Testament lesson**
(*prophetia*, *lectio*) before the epistle. The lessons from the prophets that survive are of
two kinds:
- **The historic epistles taken from a prophet.** Hof 1592 instructs its readers how to announce
  them: "Lectio ex propheta Esaia …", and the like (Sehling 11, p. 409). These are the lessons
  of the Christmas Masses, Epiphany and the Ember days in the Missal.
- **Festal chapters in place of the epistle.** Pfalz-Neuburg 1543 has "the chapters out of the
  Bible" read on the feasts "wherein the history of the feast is described" (Sehling 13, p. 71).
  Mecklenburg 1545 reads Isaiah 40 for St John the Baptist's day, because "it is written of John
  the Baptist" (Sehling 5, p. 152).

**At Matins and Vespers.** The Old Testament lessons were read at the office, not the Mass.
Their **tone** was the tone of the prophecies. Hamburg 1529 has the lessons read "in the tone in
which one is wont to read at Matins; but the ending as one was wont to end when one read a
prophecy, thus: *sol sol sol la sol fa fa*" (Sehling 5, p. 522). Pomerania 1535 prescribes the
same cadence (Sehling 4, p. 349). Wittenberg 1533 has the boys end each lesson "as one was wont
to read or sing the prophecies, *in fine*: *sol sol mi fa sol sol*" (Sehling 1, p. 703). This is
one of the few places where an order writes down a melodic formula of the old chant.

### 5.2 The epistle and gospel: kept, and read toward the people

**Kept everywhere.** Every Lutheran order in the corpus keeps the **epistle and gospel of the
day** (*de dominica*, *de festo*), with these exceptions:
- **Müntzer** (Radical Reformation) reads "always a whole chapter instead of the epistle and
  gospel" (§3.2).
- **Nürnberg 1524** and **Brandenburg-Nürnberg 1533** read the New Testament continuously
  (*lectio continua*). In the Nürnberg parish Mass of 1524 the minister sings a whole chapter of
  Romans, and the deacon a chapter of Matthew, in German, each with a fixed announcement: "Ir
  aller liebsten, vernemet das N. capitel …" (Sehling 11, p. 46).

**Toward the people.** The reader turns **toward the people** ("gegen dem volk", "tom volke
gekeret"). That is what made the reading a reading. The **priest** reads the epistle and gospel
in most orders. Where there were deacons or chaplains, they read: in Pfalz-Neuburg and
Regensburg the subdeacon and deacon (see `MINOR_ORDERS_DEACONS_ELDERS_GUIDE.md`, §4.2). Some
orders read the epistle **from the pulpit**:
- Schweinfurt 1543: "the chaplain shall not read the epistle over the altar, but from the
  pulpit" (Sehling 11, p. 641);
- Pomerania 1535: "as one is wont to do on the pulpit" (Sehling 4, p. 341).

### 5.3 Sung or read, Latin or German

**Luther's tones.** Luther's *Deutsche Messe* sets the **epistle in the eighth tone**, "that it
remain at the same pitch as the collect", and the **gospel in the fifth tone**, both "with the
face turned to the people". **Luther, *Deutsche Messe und ordnung gottis diensts*, 1526**
(Sehling 1, p. 14):

<!-- doc 3 -->
> Darnach die epistel in octavo tono, das er im unisono der collecten gleich hoch bleibe, cuius
> regulae sunt istae. […] Er sol aber die epistel lesen mit dem angesicht zum volk gekert, aber
> die collecten mit dem angesicht zum altar gekeret. […] Darnach lieset er das evangelion in
> quinto tono, auch mit dem angesicht zum volk gekeret.

Thereafter the epistle in the eighth tone, that he remain at the same pitch, in unison with the
collect; whose rules are these: […] But he shall read the epistle with his face turned to the
people, but the collects with his face turned to the altar. […] Thereafter he readeth the gospel
in the fifth tone, also with his face turned to the people.

**Saxony copies Wittenberg.** The Saxon orders refer the pastors to the larger towns for the
melody. The visitation instruction of 1539 says: "the melody for singing the gospels and
epistles in German the pastors may seek and copy at the churches of the greater towns, as
Dresden, Leipzig, Weißenfels, Salza" (Sehling 1, p. 281). Wurzen (1542) and the Saxon town
orders want the epistle read "in German, in the tone and accent customary at Wittenberg, Torgau,
Dresden or Leipzig" (Sehling 2, p. 98; 1, p. 564).

**Read without notes.** Other orders had the lessons read **without notes**, for
intelligibility:
- Mecklenburg 1545: "with a loud voice, without notes, that the church may understand the words"
  (Sehling 5, p. 152);
- Mecklenburg 1552 repeats it (5, p. 202);
- Pomerania 1535: "if the priest cannot sing, he may read loud and understandable" (4, p. 341).

**Latin first, then German.** A third group kept the **Latin chant first**, for the school, and
then read the lesson again in German:
- **Schwäbisch Hall** (1526): the deacon sings the gospel "in the choir in this tone, as it hath
  hitherto been sung", and it is then read to the people in German (Sehling 17/1, p. 40).
- **Hamburg 1556**: two scholars read the Latin gospel "in the customary tone", and a third
  repeats it in German "in the same tone" (Sehling 5, p. 552).
- **Brieg 1592**: the pastor sings the epistle and the gospel in Latin before the altar, but "in
  little towns it may remain in German" (Sehling 3, p. 445).
- **Brandenburg 1573**: the electoral visitors went furthest. They required the epistles and
  gospels to be sung "**not in German, but in the old customary melody in Latin**", then read in
  German "for the simple folk's sake, that they may understand it, which cannot happen in
  singing". **Brandenburg, *Visitations- und Consistorialordnung*, 1573** (Sehling 3, p. 129):

<!-- doc 1748 -->
> Sie sollen auch darauf sehen, das die pfarrer und caplene die episteln und evangelia vor dem
> altare nicht deutsch, sondern in der alten, gewohnlichen melodei lateinisch singen, und dann
> hernach, um der einfeltigen willen, deutsch vorlesen, das sie es verstehen können, welches im
> singen nicht geschehen kan

They shall also see to it that the pastors and chaplains sing the epistles and gospels before
the altar not in German, but in the old customary melody in Latin, and then afterward, for the
simple folk's sake, read them in German, that they may understand it, which in singing cannot be
done […]

**Wittenberg's German tones.** Halle's order of 1543 takes the opposite view. It lets the
epistles and gospels be sung in Latin "for the youth's sake", "yet it shall also be free to have
them sung in German, as at Wittenberg, and especially when one hath a good melody"
(Sehling 2, p. 436). **Calenberg-Göttingen 1542** prints its German gospels with notes, to be
sung "in German toward the people with a loud voice" (Sehling 6/2, p. 813).

---

## 6. Gradual, alleluia and tract

### 6.1 Luther: two verses, and the alleluia always

The *Formula missae* keeps "the gradual of two verses together with the alleluia, or either".
The long Lenten graduals and tracts are to be sung "by whoever will, in his own house". The
alleluia is not to be dropped in Lent, for "**the alleluia is the perpetual voice of the
church**". **Luther, *Formula missae et communionis*, 1523** (Sehling 1, p. 5):

<!-- doc 2 -->
> Quarto, graduale duorum versuum simul cum alleluia, vel utrum, iuxta arbitrium episcopi
> cantetur. Porro gradualia quadragesimalia et similia, quae duos versus excedunt, cantet
> quisquis velit in domo sua. In ecclesia nolumus tedio extingui spiritum fidelium. […] Alleluia
> enim vox perpetua est ecclesiae, sicut perpetua est memoria passionis et victoriae eius.

Fourthly, let the gradual of two verses, together with the alleluia, or either of them, be sung
at the bishop's discretion. But the Lenten graduals and the like, which exceed two verses, let
whoso will sing in his own house. In the church we will not have the spirit of the faithful
quenched with tedium. […] For the alleluia is the perpetual voice of the church, as the memory
of his passion and victory is perpetual.

**Schleswig-Holstein and Hildesheim.** Bugenhagen's orders for Schleswig-Holstein (1542) and
Hildesheim (1544) take this over. They also **shorten the melody**: the children sing the
alleluia with its verse, "**but leaving out the many notes which one was wont to hang on at the
end**", that is, the jubilus. Before the gradual "a German psalm, taken from Scripture, or else
a gradual that hath two verses". **Schleswig-Holstein, *Kirchenordnung*, 1542**
(Sehling 23, p. 90):

<!-- doc 1576 -->
> Alleluia, welcker ein ewich stemme der Kercken ys, singen de kinder mit dem verse, doch
> uthgelaten de vele noten, de men plach hinden anthohengende, darna vor dat Gradual einen
> düdesschen Psalm, uth der Schrifft genamen, edder ock ein Gradual, dat men twe verse hefft.

The alleluia, which is a perpetual voice of the church, the children sing with the verse, yet
leaving out the many notes which one was wont to hang on behind; thereafter, for the gradual, a
German psalm taken out of Scripture, or else a gradual that hath two verses.

The Hildesheim text is word for word the same (Sehling 7/2.1, p. 853).

### 6.2 Kept where pure, by the school, or exchanged for a German psalm

**The pattern.** The gradual and alleluia survived as a **choir piece in Latin**, sung by the
school between the epistle and gospel. In the parishes and villages they were exchanged for a
German psalm or hymn:
- **Brandenburg 1540**: "the gradual, or in the parishes a German psalm in place of the gradual;
  then the alleluia and sequence, or as occasion serveth a tract, in Latin" (Sehling 3, p. 71).
- **Pfalz-Neuburg 1543**: the choir "sings again in Latin a gradual or a tract or an alleluia
  with a sequence, as the order of the season giveth". "Where there is no choir, the priest may
  sing or say it himself, and the people meanwhile a good German spiritual song"
  (Sehling 13, p. 71).
- **Brandenburg-Nürnberg 1533**: the priest "may read an alleluia with its verse in Latin, or a
  gradual taken from holy Scripture; the same the scholars may also sing in Latin"
  (Sehling 11, p. 195).
- **Weißenburg 1528**: "the schoolmaster sings a short alleluia or gradual"
  (Sehling 11, p. 659).

**Where the gradual was not pure.** The Ansbach *Auctuarium* of 1548, an Interim order, lists
German psalms to be sung where the gradual or alleluia "were not pure, as commonly *de
sanctis*". **Brandenburg-Ansbach-Kulmbach, *Auctuarium*, 1548**
(Interim order; Sehling 11, p. 329):

<!-- doc 278 -->
> An den andern feirtagen und festen, die nit raine oder keine sequenz haben, sol man das
> gradual oder Alleluia singen. Wo aber die nit rain weren, als gemainlich de sanctis, an dero
> stat sing man dieser psalm einen: Ein feste burg ist unser Gott etc. Wer Gott nit mit uns
> diese zeit etc. Wol dem, der in Gottes forcht steht etc. Aus tiefer not etc.

On the other holy days and feasts which have no sequence, or none pure, one shall sing the
gradual or alleluia. But where these were not pure, as commonly *de sanctis*, let one of these
psalms be sung in their stead: "Ein feste Burg ist unser Gott" etc., "Wär Gott nicht mit uns
diese Zeit" etc., "Wohl dem, der in Gottes Furcht steht" etc., "Aus tiefer Not" etc.

**The tract.** The tract, the Lenten substitute for the alleluia, appears in Brandenburg 1540,
Pfalz-Neuburg 1543, Pomerania 1569 and Hof 1592. Luther's ruling notwithstanding, these orders
kept the Lenten change.

### 6.3 German graduals

**Müntzer and Erfurt.** These (Müntzer's Radical Reformation offices and Erfurt's Lutheran
reprint) have German prose graduals and alleluias. Erfurt's Passion gradual is an example.
**Erfurt, *Deutsches Kirchenamt*, 1525, office of the Passion** (Sehling 2, p. 380):

<!-- doc 1251 -->
> Gradual: Christus ist worden für uns gehorsam bis zum tode, zum tode des creuzes. Darumb hat
> in gott auch erhöhet und hat im einen namen gegeben, der uber alle namen ist. Alleluia :
> Alleluia. Christus ist gehorsam worden seinem vater bis in tod, und in tod des kreuzes.

Gradual: Christ became for us obedient unto death, even the death of the cross. Wherefore God
also hath exalted him, and given him a name which is above every name. Alleluia: Alleluia.
Christ became obedient to his Father unto death, even the death of the cross.

This is *Christus factus est*, the gradual of Maundy Thursday and Palm Sunday, in German.

**Nürnberg's new tone.** In Nürnberg, by the report sent to Goslar in 1528, "the gradual is
sung, that is again a verse or two from the Psalter or another book of the Old Testament, **in a
tone made for it**". The tone was new, not the old melisma (Sehling 7/2.2, p. 230).

**Calenberg-Göttingen.** The German alleluias of Calenberg-Göttingen 1542 are printed with
notes. For the Purification it puts the *Nunc dimittis* hymn "Mit fried und freud ich far dahin"
"for the gradual and alleluia" (Sehling 6/2, pp. 813, 823).

### 6.4 The sequence

The sequence, the hymn after the alleluia, was cut back to a few "pure" texts for the chief
feasts and farced with German stanzas. This is treated in `HYMN_PRACTICE_GUIDE.md`, §8.2–8.3.

---

## 7. The offertory

### 7.1 Rejected with the offertory prayers

For Luther the offertory chant belonged to "that whole abomination" that begins at the
offertory, where "almost everything soundeth and smelleth of oblation" (Sehling 1, p. 5). Most
orders dropped the chant together with the offertory prayers (the *canon minor*):
- **Volprecht's Nürnberg Mass (1524)**: "The offertory is never said, **because Christ was once
  offered for our sins**" (Sehling 11, p. 39).
- **The Nürnberg parish Mass (1524)**: it is left out with the *canon minor*
  (Sehling 11, p. 47).
- **Prussia 1525**: "the offertory, secret, *canon minor* and *maior* are necessarily left out"
  (Sehling 4, p. 32).

**Nürnberg, *Deutsche Messe* of Prior Volprecht, 1524** (Sehling 11, p. 39):

<!-- doc 247 -->
> Credo s[em]p[er] dicit[ur]. Interim praeparatur calix. Offertorium nunquam d[ici]tur, quia
> Christus semel pro peccatis nostris oblatus est.

The Creed is always said. Meanwhile the chalice is prepared. The offertory is never said,
because Christ was once offered for our sins.

### 7.2 Kept as a sung text from Scripture

**The Latin offertory kept.** A few orders kept the **Latin offertory chant** as a text from
Scripture, sung by the choir while the bread and wine were prepared:
- **Wittenberg 1525** lists it among the parts sung (§3.1).
- **Brandenburg 1540** has "the offertory of the Sunday or feast" after the sermon, "but in the
  villages one may sing a German psalm for it" (Sehling 3, p. 71).
- **Amberg 1550**: "Chorus: Offertorium de tempore" (Sehling 13, p. 286).
- **The Ansbach *Auctuarium* (1548)**, an Interim order, has the schoolmaster sing "the Latin
  offertory **noted in the same Mass, since they are all taken from holy Scripture**", or a
  Latin responsory. **Brandenburg-Ansbach-Kulmbach, *Auctuarium*, 1548**
  (Interim order; Sehling 11, p. 330):

<!-- doc 278 -->
> Sobald die predig ir end hat, soll der schulmaister das lateinisch offertorium, so in
> derselben meß verzaichnet, singen (dann sie alle aus der hailig schrift genommen) oder aber
> ein responsorium lateinisch

As soon as the sermon hath its end, the schoolmaster shall sing the Latin offertory that is
noted in the same Mass (for they are all taken out of holy scripture), or else a Latin
responsory […]

**German offertories.** Müntzer (Radical Reformation) and the Erfurt *Kirchenamt* translate the
offertory into German. Erfurt has an offertory for Easter ("Die erde hat erbidmet und geruget,
do got wolt zum urteil auferstehn. Alleluia", *Terra tremuit*) and for Pentecost (*Confirma hoc,
Deus*). In the Trinity office it has "a psalm or else a spiritual hymn of praise" "for the
offertory" (Sehling 2, pp. 376–378).

### 7.3 A German psalm, or the Creed, in its place

**The usual Lutheran solution.** The usual Lutheran solution was a German psalm or hymn "an stat
des offertorii", sung while the elements were prepared and the communicants came forward:
- **Naumburg 1527**: "Aus tiefer Not" (Sehling 2, p. 60).
- **Calenberg-Göttingen 1542**: "In place of the offertory one shall sing with the congregation
  a German psalm", and at Christmas "Ein kindelein so löbelich" (Sehling 6/2, pp. 814, 821).
- **Dortmund 1554**: "a fitting hymn of praise for the offertory" (Sehling 21, p. 209).
- **Lippe 1525**: "for the offertory one singeth a spiritual song, that is a psalm"
  (Sehling 22, p. 568).
- **In Bugenhagen's orders** the creed hymn "Wir glauben all" after the sermon served as the
  offertory (`HYMN_PRACTICE_GUIDE.md`, §9.2, §11.3).

---

## 8. The Proper Preface

The full texts of every Proper Preface in the corpus are in Appendix A. This section deals with
three questions:
- whether the Preface was kept at all;
- on which days a proper Preface was used, and which;
- who sang it, in which language and to which tune.

### 8.1 Kept, shortened or dropped

**Luther, 1523.** The *Formula missae* keeps the dialogue and the common Preface but **cuts it
off at *per Christum Dominum nostrum*** and joins the Words of Institution to it. The Words are
sung "in the same tone of voice" as the Preface. Volprecht and the Nürnberg parish Mass of 1524
follow (see the Canon guide, §3.2, §7.1). The Nürnberg Mass marks the cut with the rubric "Hic
finitur prefatio" (Sehling 11, p. 47).

**Luther, 1526.** The *Deutsche Messe* drops the Preface and puts a paraphrase of the Our Father
and an exhortation in its place. Orders that followed the *Deutsche Messe* closely did the same:
- The Prussian order of 1544 says plainly "In place of the preface, **which shall be abolished
  and left out**", the paraphrase follows. **Prussia, *Kirchenordnung*, 1544**
  (Sehling 4, p. 65):

<!-- doc 1833 -->
> An stat der prefation, welche abgethan und ausbleiben sölle, volgt balde ein offentliche
> vermanung und paraphrasis des vater unsers, die der priester conceptis ader prescriptis verbis
> thun sölle, wol laut und vernemblich

In place of the preface, which shall be done away and left out, there followeth straightway a
public exhortation and paraphrase of the Our Father, which the priest shall make in conceived or
in prescribed words, right loud and audibly […]

- The Prussian order of 1568 repeats it (Sehling 4, p. 81).
- The Strasbourg agendas after 1525 (mediating) have no Preface or Sanctus
  (Sehling 20/1, p. 63, editor's introduction).
- The Engerhafe liturgy in East Frisia (1583) replaces the Preface with Psalm 111
  (Sehling 7/1, p. 677, n. 20).

**The compromise of 1539.** Duke Henry's Saxon order allowed the exhortation and paraphrase to
be dropped "sometimes, especially on the feasts", and the Latin Preface sung instead.
**Albertine Saxony, *Kirchenordnunge zum anfang* (Duke Henry's *Agende*), 1539**
(Sehling 1, p. 271):

<!-- doc 30 -->
> Auch mag man zuzeiten, sonderlich auf die festa, die paraphrasim und vermanung dem volk
> furzulesen, nachlassen, und dafur die latinische prefation singen, darauf das latinische
> sanctus

One may also at times, especially on the feasts, forgo reading the paraphrase and exhortation to
the people, and instead thereof sing the Latin preface, and thereupon the Latin Sanctus […]

**The usual Lutheran rule.** This became the usual Lutheran rule: **Preface on feasts,
exhortation on ordinary Sundays**, or Preface "if time allows". Examples:
- Hatzkerode about 1534: "on the great feasts the *praefatio de festo* shall be sung in its
  stead, with the customary Latin Sanctus" (Sehling 2, p. 587).
- Halberstadt: "On the high feasts the pastor singeth the preface" (Sehling 2, p. 484).
- Pomerania 1535 and 1542: "not always, but when one will, especially at the high feasts"
  (Sehling 4, pp. 341, 357).
- Mecklenburg 1552: "if the time allows" (Sehling 5, p. 199).
- Lüneburg 1564: "in feasts, in the towns" (Sehling 6/1, p. 546).
- Stralsund 1555: "which may also at times be left out, as the time requireth"
  (Sehling 4, p. 551).

**Shortened at the cantor's discretion.** Hamburg 1556 allows the Preface to be shortened, "but
so that the cantor and the priest have agreed on it beforehand". **Hamburg, *Kirchenordnung*,
1556** (Sehling 5, p. 552):

<!-- doc 1963 -->
> darna de prefation latine singen na dem altar gewendet. Idt mag ock wol underwilen de
> prefation vorkortet werden, averst doch dat de cantor und prester des falles eines geworden
> vorhenne. Dat sanctus schall stedes naher gesungen werden, pro ratione festorum et
> dominicarum, underwilen düdesch, Jesaia dem propheten etc.

[…] thereafter sing the preface in Latin, turned to the altar. The preface may also well at
times be shortened, but so that the cantor and the priest be agreed beforehand of the case. The
Sanctus shall always be sung after it, according to the feasts and Sundays, sometimes in German,
"Isaiah the prophet", etc.

### 8.2 Which days: the temporal cycle

**The core set.** Where a proper Preface was kept, the core set was the *de tempore* Prefaces of
the feasts of Christ: Christmas, Epiphany, Easter, Ascension, Pentecost and Trinity, with the
common Preface for other days. The second Saxon visitation instruction of 1539 names exactly
this set, to be taken "out of the Latin missals". **Albertine Saxony, *Instruktion zur zweiten
Visitation*, 1539** (Sehling 1, p. 281):

<!-- doc 31 -->
> Prefation in der messe, oder communion, prefatio in natali domini, prefatio in epiphania
> domini, prefatio in festo paschali, prefatio in festo ascensionis domini, prefatio in festo
> pentecostes, prefatio de s. trinitate. Item prefationem communem, mögen die pfarherr aus den
> latinischen missaln nemen

The preface in the mass, or communion: the preface on the Lord's Nativity, the preface on the
Lord's Epiphany, the preface on the feast of Easter, the preface on the feast of the Lord's
Ascension, the preface on the feast of Pentecost, the preface of the Holy Trinity. Item the
common preface, the pastors may take out of the Latin missals […]

**Shorter sets.** Some orders used fewer:
- **Lippe 1571** prints only Christmas, Easter, Pentecost and Michaelmas, for "the high
  four-times feasts" (*Viergezeiten*) (Sehling 21, p. 410).
- **Grubenhagen 1581** has Christmas, Easter, Pentecost and Trinity, "where there are schools
  and boys" (Sehling 6/2, p. 1073).
- **Osnabrück 1618** has Michaelmas, Christmas, Easter and Pentecost (Sehling 7/1, pp. 268–269).
- **Kurland 1570** has German Prefaces for Christmas, Easter and Pentecost, sung "for variation"
  on the high feasts instead of the daily one (§A.14).

**Two forms for each feast.** The Pfalz-Neuburg order (in its 1547 form) says that each high
feast has two Prefaces, "**a *solemnis* and a *dominicalis***". These are the solemn and the
Sunday tones of the Missal. It tells the priest to write them out with their notes and keep them
on the desk. **Pfalz-Neuburg, *Kirchenordnung* of Ottheinrich, [1547]** (Sehling 14, p. 109):

<!-- doc 473 -->
> und die prefation gantz oder ein stuck darauß nach der gelegenheyt singen oder lesen. Es seind
> aber auf etliche hohe fest, Osterfest, Auffart, Pfingsten, Trinitatis etc., besondere
> prefation, von idem fest zwo, ein solemnis und eine dominicalis, die mag ein priester
> außnotiren oder außschreiben und auf dem pult alwegen neben der kirchenordnung haben

[…] and sing or read the preface, whole or a piece thereof, as occasion serveth. But for certain
high feasts, Easter, Ascension, Pentecost, Trinity etc., there are special prefaces, of each
feast two, a solemn and a Sunday one, which a priest may note out or write out and have always
on the desk beside the church order […]

**Trinity on ordinary Sundays.** For ordinary Sundays the northern Bugenhagen orders chose the
**Trinity Preface**, because it "was made against the Arians", "as the Nicene Creed also was".
**Hamburg, *Hamburger Kirchenordnung*, 1529** (Sehling 5, p. 528):

<!-- doc 1960 -->
> und in den groten festen, de sunderge prefation hebben, und sus wen he wil up etlike sondage
> mit der prefatien trinitatis, de wedder de Arrianer, alse ock das Symbolum Nicenum gemaket is,
> schal he anheven latinisch de prefatie dominus vobiscum und singen se bet an dat ende. Darup
> singe dat chor ein latinsch sanctus.

[…] and on the great feasts which have a special preface, and otherwise when he will on certain
Sundays with the preface of the Trinity, which was made against the Arians, as was also the
Nicene Creed, he shall begin in Latin the preface *Dominus vobiscum*, and sing it unto the end.
Thereupon let the choir sing a Latin Sanctus.

**Wolfenbüttel 1543** gives the same reason, and goes further. It allows Latin Prefaces in the
towns at Christmas, Easter and Pentecost, and on other feasts the Trinity Preface. Every other
Preface, **the common one included**, is to be "simply let lie as unneeded". **Wolfenbüttel,
*Christlike kerken-ordeninge im lande Brunschwig*, 1543** (Sehling 6/1, p. 59):

<!-- doc 1972 -->
> de prester mach denne ock dar wol singen de latinische praefatio vam Wynachten-, vam Paschen-
> und Pinxten-feste und up andere feste de prefatio de sancta trinitate, wenn man wil, welcke
> praefatio gemaket is wedder de Arrianer, andere praefation, ock de quotidiana, lasse men
> slichtes ligen alse unnödich etc. Up de latinische praefatio mach de ganze kercke frölick dat
> düdesch Sanctus singen.

[…] the priest may then also well sing there the Latin preface of the feast of Christmas, of
Easter and of Pentecost, and on other feasts the preface of the Holy Trinity, if one will, which
preface was made against the Arians; other prefaces, the *quotidiana* too, let them simply lie
as needless, etc. Upon the Latin preface the whole church may joyfully sing the German Sanctus.

**Herford** (1532) has the rule that a feast takes its own Preface, and a Sunday, if any, the
Trinity: "wil me ock up de sondage Prefatien holden, so schal me singen de Prefatien de
Trinitate" (Sehling 21, p. 176). So does Wittenberg's own town order of 1533: "on the feasts …
with the preface of the feast, or else on the Sunday with the preface *de sancta trinitate*, if
one will" (Sehling 1, p. 704).

**Calenberg-Göttingen 1542** gives its model Sunday Mass a shortened German **Easter** Preface
instead (§A.6, German 5).

**The seasons are almost absent.** No order in the corpus prescribes a Preface for **Advent**
apart from Müntzer's tradition (Müntzer himself belongs to the Radical Reformation). That
tradition uses the reworded Marian Preface (§A.10). Lent and Passiontide have a Preface only in
Dortmund and in the Müntzer tradition (§A.4–A.5). Grubenhagen added a new German Passion Preface
from Isaiah 53 for Maundy Thursday (§A.12).

### 8.3 Saints' days: Michaelmas, the Virgin and the Apostles

**The purity rule.** Saints' Prefaces were generally excluded under the rule that only "pure"
texts may be sung:
- Halle 1543: "at great feasts the Latin prefaces remain, **which are Christian and agreeable to
  Scripture**" (Sehling 2, p. 436).
- Corvinus's order for Lippe (1542): "the prefaces **that are pure**" (Sehling 21, p. 345).

The exceptions are few:
- **Michaelmas.** The common Preface is the festal Preface for Michaelmas in Hoya 1581,
  Osnabrück 1618 and Lippe 1571. Lippe's German version for the villages replaces the choirs of
  angels with the forgiveness of sins (§A.1, §A.13). Osnabrück sings it "on Michaelmas **and
  other high feasts**".
- **The Virgin and the Apostles.** Dortmund 1554 alone translates the Marian Preface, for five
  feasts including the Assumption, and the Preface of the Apostles. It turns the Apostles'
  protection into the Apostles' "doctrine" (§A.10–A.11).
- **Müntzer's tradition** (Müntzer himself Radical Reformation) keeps the Marian Preface's text
  but strikes Mary's feast from it, and uses it for Advent and Trinity (§A.10).

### 8.4 Who sang it, in what language, to which tune

**The celebrant sings, the choir answers.** Everywhere the Preface belongs to the **priest at
the altar**, turned to the altar (Hamburg 1556). The **choir** (the school) answers the dialogue
and sings the Sanctus. Kurland 1570 and Osnabrück 1618 mark the parts "Der diener" / "Das chor"
and "Minister" / "Chorus" (§A.14; Sehling 7/1, p. 268). In Osnabrück the Sanctus that follows
"is sung or played on the organ" (Sehling 7/1, p. 269). In Wolfenbüttel 1543 "the whole church"
sings a German Sanctus to the Latin Preface (above).

**Latin in the towns, German in the villages.** Language followed the school:
- Mecklenburg's Mass order of 1545 has the pastor sing the Preface in Latin or German in the
  towns, "in the villages German".
- It also insists on one tune: "these notes and no other", against "the useless motley singing
  that every man maketh after his own head". **Mecklenburg, *Ordeninge der misse*, 1545**
  (Sehling 5, p. 154):

<!-- doc 1922 -->
> mach de kerckhere singen in den steden to tiden latin edder düdesch de prefation, wo hir na
> folget. Up den dörperen schal men düdesch singen, unde sündergen in den festen nicht laten
> anstan. De trinitate ock under tiden düdesch. […] De kerckheren willen ock düsse noten so
> leren, wo hirna geschreven. Unde de prefationes ock de verba consecrationis, mit duessen und
> neuen anderen noten singen. Dat unnutte bunte singent, dat ein ider na sinem koppe maket,
> buwet nicht in der gemene.

[…] the pastor may in the towns at times sing the preface, in Latin or in German, as here
followeth. In the villages one shall sing it in German, and especially on the feasts not let it
stand over. [The preface] of the Trinity also at times in German. […] The pastors will also
learn these notes, as hereafter written; and sing the prefaces and also the words of
consecration with these and no other notes. The useless motley singing which every man maketh
after his own head edifieth not in the congregation.

- **Lippe 1571** prints each Latin Preface with a German one beside it "for the villages" (§A.2,
  §A.6, §A.8, §A.13).
- **Grubenhagen 1581** keeps the Latin Prefaces only "where there are schools and boys", and
  gives its new German Isaiah Preface "for the simple layman" (§A.12).
- **Kurland 1570** begins the communion "with the customary noted German preface", "since the
  Latin Mass is abolished" (Sehling 5, p. 89).

**The tunes.** The Latin Prefaces kept their **Missal tones**:
- Duke Henry's order of 1539 refers the pastors to "the notes of the Latin Missal". Sehling's
  editor gives this from the first edition (Sehling 1, p. 89).
- The 1539 instruction tells pastors to take the Prefaces "out of the Latin missals" (above).
- Amberg 1555/57 wants them sung "German or Latin, as they are in use in other evangelical
  places and set to the customary notes" (Sehling 13, p. 291).
- The Pfalz-Neuburg order distinguishes the solemn tone from the Sunday tone (above).
- Hof 1592 has the Preface sung on the chief feasts "from Lossius's book", that is the
  *Psalmodia* of Lucas Lossius (Sehling 11, p. 473).
- Sehling's editors identify the notated Prefaces of Calenberg-Göttingen, Grubenhagen and the
  other Lower Saxon orders with the standard melodies in the *Handbuch der deutschen
  evangelischen Kirchenmusik*.

The German Prefaces were sung to the same **Preface tone** adapted to German. So were the Words
of Institution. Prussia 1544 has them sung "*in nota prefationis*, as they were also sung with
us before in that way" (Sehling 4, p. 65).

---

## 9. The communion chant (*communio*)

### 9.1 Optional, and soon replaced

**Luther.** The *Formula missae* leaves the communion chant free: "**if one will sing the
communion, let it be sung**". The Agnus Dei is sung during the communion itself
(Sehling 1, p. 6). **Luther, *Formula missae et communionis*, 1523** (Sehling 1, p. 6):

<!-- doc 2 -->
> VI. Deinde communicet tum sese, tum populum, interim cantetur Agnus dei. […] VII. Si
> communionem cantare libet, cantetur.

VI. Then let him communicate both himself and the people; meanwhile let the Agnus Dei be sung.
[…] VII. If it please to sing the communion, let it be sung.

**Orders that kept the Latin communio.**
- **Volprecht** (1524): "*Communio de quo sit missa*", the communion of whatever Mass is being
  said (Sehling 11, p. 39).
- **The Ansbach visitation order of 1536**: "where there are Latin schools", "the introit,
  Kyrie, Gloria, *Et in terra*, *Patrem*, Sanctus, Agnus Dei **and communion** in Latin"
  (Sehling 11, p. 326).
- **Brandenburg 1540**: "the Latin preface, the Sanctus, the communion, and further the
  conclusion" (Sehling 3, p. 71).

**German communio.** Müntzer (Radical Reformation) and the Erfurt *Kirchenamt* have a German
communio for each office. For Easter it is "Unser osterlamp Christus ist geopfert fur uns.
Alleluia" (*Pascha nostrum*). For Christmas it is "Alle grenze der erden haben gesehn den
heiland unsers gottes" (*Viderunt omnes*) (Sehling 2, pp. 376, 379). In the Advent office "a
psalm or other spiritual hymn of praise" is sung "for the communion" (Sehling 2, p. 379).

**Replaced by hymns.** Elsewhere the slot was filled by the **communion hymns** and the **Agnus
Dei**, often several in turn "according as the communicants be many or few". These are treated
in `HYMN_PRACTICE_GUIDE.md`, §14–15.

### 9.2 Polyphonic communions and festal motets

**Motets "sub communione".** In the larger town churches the communion was covered by
**motets**, Latin and German, often chosen to fit the feast:
- **Wittenberg 1533**: "*Pange lingua* in Latin and the like, and also German songs of the
  feast, until the communion is over" (Sehling 1, p. 705).
- **Nördlingen 1555**: on Maundy Thursday "*sub communione*, *Pange lingua* in mensural music".
  At Pentecost the *Sanctus paschale* may be sung "in place of 'Jesaia' and 'Jesus Christus'"
  (Sehling 12, pp. 321, 325).
- **Hof 1592**: the fullest list. For each Sunday and feast it names a motet "*sub communione*".
  For the Sunday after Easter (*Quasimodogeniti*) it gives "*Pascha nostrum immolatus est
  Christus*, a 5, Clemens non Papa", which is the text of the Easter communio, in polyphony. "If
  these do not suffice, as also at other times whenever the number of communicants requireth
  it", it adds "Schaff in mir, Gott, ein reines Herz", a 6, by Leonhard Schröter, or *O sacrum
  convivium*, a 6, by Victoria. **Hof, *Ordo ecclesiasticus*, 1592, Dominica Quasimodogeniti**
  (Sehling 11, pp. 461–462):

<!-- doc 294 -->
> Sub communione: Pascha nostrum immolatus est Christus, A 5. Clemens Non Papa, item: Dum
> transisset sabbatum. Vaet. A 6. His non sufficientibus, (sicut etiam alias, quotiescunque
> multitudo communicantium requirit), additur Schaff in mir Gott ein reines herz. A 6. Leonhardi
> Schroteri, vel: O sacrum convivium. A 6. L. de Victoria.

During the communion: *Pascha nostrum immolatus est Christus*, for five voices, by Clemens non
Papa; also *Dum transisset sabbatum*, by Vaet, for six voices. If these suffice not (as also at
other times, as often as the number of the communicants requireth it), there is added "Schaff in
mir, Gott, ein reines Herz", for six voices, by Leonhard Schröter, or *O sacrum convivium*, for
six voices, by L. de Victoria.

**The organ.** Several orders let the **organ** play during the communion, or alternate with the
hymns:
- Regensburg 1553 (Sehling 13, p. 421);
- the Schönburg lordships (1542), "only on the high feasts" (Sehling 2, p. 171);
- Engerhafe 1583 (Sehling 7/1, p. 681).

---

## 10. The music: old chant, cut chant, new tones, polyphony and organ

### 10.1 The old melodies kept

**Latin propers.** Where the Latin propers were kept, they were sung to the **plainchant of the
old books**:
- the introits, graduals and alleluias of the Gradual;
- the Prefaces in the Missal tones (§8.4).

The orders seldom say so outright, because it went without saying. They speak of "the customary
notes", "as hitherto", "as was customary". Two late orders insist on the old melody against
innovation:
- **Brandenburg 1573** requires the epistles and gospels "in the old customary melody in Latin"
  (§5.3).
- **Mecklenburg 1545** requires the Prefaces and Verba "with these and no other notes" (§8.4).

**The Lossius standard.** From mid-century the Latin chant was standardized for Lutheran use in
**Lucas Lossius's *Psalmodia*** (1553). The Rostock order of about 1560 makes it the norm for
all the city's churches. **Rostock, *Conformitas ceremoniarum in singulis templis ecclesiae
Rostochiensis*, 1560–1576** (Sehling 5, p. 288):

<!-- doc 1936 -->
> Es wird für gut angesehen und notig eracht, das man in allen kirchen halten sol Lucae Lossii
> psalmodia und sol sich das chor darnach richten. Nach dem introitum sol das kyrie gesungen und
> geschlahen werden.

It is held good and deemed needful that in all churches Lucas Lossius's *Psalmodia* be kept, and
that the choir order itself thereafter. After the introit the Kyrie shall be sung and played.

**Other references to Lossius.** Hof 1592 sings the gradual and sequence "from the great Missal
or from Lossius's book", and the festal Prefaces "from Lossius's book" (Sehling 11, p. 473). On
the authorized cantionals of Spangenberg and Lossius see `HYMN_PRACTICE_GUIDE.md`, §18.6.

### 10.2 The old melodies cut

The orders also trimmed the chant:
- **Graduals:** Luther's rule of **two verses** for the gradual, with the long Lenten graduals
  sent home (§6.1).
- **The alleluia's jubilus:** Bugenhagen's **removal of the long melisma** at the end of the
  alleluia, "the many notes that one was wont to hang on behind" (§6.1).
- **Introit psalm:** Müntzer's (Radical Reformation) **whole psalm** for the introit, against
  the single verse of the medieval introit (§3.2).
- **Pace:** Calenberg-Göttingen's warning that the choir sing "right slowly, that it become not
  an ass's braying" (§4.2).

### 10.3 New tones for German texts

**The new tones.** German texts needed new tones, or adaptations of the old:
- Luther's epistle tone (eighth mode) and gospel tone (fifth mode) in the *Deutsche Messe*
  (§5.3).
- The Nürnberg gradual "in a tone made for it" (§6.3).
- Müntzer's notated German offices (Radical Reformation), sung "with the customary singing, in
  their own tongue" (§3.2).
- The German Prefaces of Calenberg-Göttingen, Grubenhagen and Lippe, set to the Preface tone
  (Appendix A).

**Copying the melodies.** The Saxon visitors told pastors to copy the melodies for the German
epistles and gospels "at the churches of the greater towns" (§5.3). Halle 1543 allows the German
lessons "especially when one hath a good melody" (Sehling 2, p. 436).

### 10.4 Polyphony

**Feasts in mensural music.** From the 1530s the propers of the feasts were often sung **in
figural (mensural) music** by the school choir. At Naumburg (1537/38) the cantor may "on the
high feasts, when one singeth mensural music", sing "a good Latin motet" for the *Et in terra*
or after the epistle, "and sometimes, when there is a goodly introit, the same before the 'Komm
heiliger Geist'". **Naumburg, *Kirchen-Ordnung für die St. Wenzelskirche*, 1537/1538**
(Sehling 2, p. 71):

<!-- doc 1219 -->
> an den hohen festen, wenn man mensur singet, mag der cantor wol bisweilen vor das et in terra
> etc. item für dem psalm, so man nach der epistel singet, eine gute lateinische muteten und
> bisweilen, wan ein schöner introitus ist, denselben vor das Kom heiliger geist singen.

[…] on the high feasts, when one singeth in measure, the cantor may well at times, instead of
the *Et in terra* etc., and also instead of the psalm which one singeth after the epistle, sing
a good Latin motet; and at times, when there is a goodly introit, the same instead of "Komm,
heiliger Geist".

**"Choraliter or figuraliter".** The formula "choraliter or figuraliter" is common in the later
orders:
- Gottleuba 1567: "one singeth plainchant and sometimes figural" (Sehling 1, p. 567).
- Penig 1575: "the introit, the Kyries etc., *Et in terra pax* etc. *choraliter*, oftener also
  *figuraliter*" (Sehling 1, p. 634).
- Schwäbisch Hall 1543/1615: "an introit of the season, the Kyrie eleison, *Gloria in excelsis
  Deo* etc. sung in Latin, *vel choraliter, vel figuraliter*, as the season giveth occasion"
  (Sehling 17/1, p. 162).
- Nördlingen 1579: on the high feasts the introit is "sung by the scholars *figuraliter*"
  (Sehling 12, p. 365).
- Schweinfurt 1576: after the epistle the choir, "if it hath adjutants", sings "something in
  four or five voices" (Sehling 11, p. 648).

**Hof 1592.** Hof's *Ordo ecclesiasticus* gives the fullest repertory. For each Sunday and feast
it names the polyphonic introit, Mass setting, motets after the epistle and the gospel, a motet
"in place of 'Nun bitten wir'", and the motets "*sub communione*". The composers are Senfl,
Lassus ("Orlandus"), Clemens non Papa, Vaet, Victoria, Johann Walter, Isaac, Josquin,
Galliculus, Dressler, Meiland and others. **Hof, *Ordo ecclesiasticus*, 1592, Christmas Day**
(Sehling 11, p. 457):

<!-- doc 294 -->
> In die Nativitatis Jesu Christi. Introitus: Puer natus est nobis A 4. Senffelii. Missa super
> Praeter rerum seriem. A 6. Ludovici Daser. Post epistolam: Quem vidistis pastores. A 6. L. de
> Victoria. Post evangelium: Resonet in laudibus. A 5. Orlandi. Loco Nun bitten wir: Exultet
> coelum. Orlandus. A 5. Sub communione: Sanctus prioris missae.

On the day of the Nativity of Jesus Christ. Introit: *Puer natus est nobis*, for four voices, by
Senfl. The Mass upon *Praeter rerum seriem*, for six voices, by Ludwig Daser. After the epistle:
*Quem vidistis pastores*, for six voices, by L. de Victoria. After the gospel: *Resonet in
laudibus*, for five voices, by Orlando. In place of "Nun bitten wir": *Exultet coelum*, by
Orlando, for five voices. During the communion: the Sanctus of the foregoing Mass.

**The plain Sundays at Hof.** Beside this, Hof's ordinary Sunday table uses **German** introits
and chorale Kyries (§4.4). The festal Latin polyphony and the German chorale service stand side
by side in the same order.

**Rhau's collections.** Sehling's editors note that Georg Rhau's printed collections of
1539–1545 supplied Lutheran choirs with polyphonic introits, alleluias and sequences
(Sehling 7/2.1, p. 1085).

### 10.5 The organ

**Organ and choir.** The organ entered the propers in alternation with the choir:
- **Heilbronn 1543**: "every Sunday hath its own introit, which shall be sung **to the organ**"
  (Sehling 17/1, p. 322).
- **Regensburg 1553**: the organist "plays the introit" with the ordinary (Sehling 13, p. 421).
- **Schweinfurt 1576**: the organist begins the introit "which the choir singeth after"
  (Sehling 11, p. 648).
- **Hof 1592**: the organ plays the introit "as far as the verse" in alternation with three
  choirs (§4.5).
- **Osnabrück 1618**: the Sanctus after the Preface "is sung or played on the organ"
  (Sehling 7/1, p. 269).

**Silent seasons.** Hof stops the organ from Advent II until Christmas Eve (Sehling 11, p. 432).

---

## 11. Table by order

**Key.**
- **L**: Latin, sung by the school or choir.
- **G**: German prose proper.
- **H**: German hymn or psalm in its place.
- **—**: dropped.
- **?**: not stated.
- "town / village": the order sets different practice.

| Order | Vol. | Introit | Epistle and gospel | Gradual, alleluia | Offertory | Preface | Communio | Music |
|---|---|---|---|---|---|---|---|---|
| Luther, *Formula missae*, 1523 | 1 | L (Sunday and festal, from Scripture) | L | L (two verses); alleluia always | — | Common, cut at *per Christum* | L "if one will" | Plainchant |
| Müntzer, Allstedt, 1524 (Radical Reformation) | 1 | G (whole psalm) | G, whole chapters | G | G | G (Advent, Christmas, Passion, Easter, Pentecost) | G | Notated; "customary singing in own tongue" |
| Nürnberg parish Mass, 1524 | 11 | L | G, chapters in sequence | L | — | Common, cut | ? | Plainchant |
| Volprecht, Nürnberg, 1524 | 11 | L | ? | L | — ("never said") | Common, cut | L (*de quo sit missa*) | — |
| Wittenberg report, 1525 | 1 | L | L | L (no sequence) | L | L | ? | — |
| Erfurt *Deutsches Kirchenamt*, 1525 | 2 | G | G | G | G (Easter, Pentecost); H (Trinity) | G (Müntzer's, plus Trinity) | G; H (Advent) | Notated |
| Strasbourg *Teutsche Meß*, 1524 (mediating) | 20/1 | ? | G | ? | ? | G (Christmas, Epiphany, Easter, Ascension, Pentecost; Cross in Schwarz) | ? | — |
| Luther, *Deutsche Messe*, 1526 | 1 | H | G (8th and 5th tones) | H | — | — | H | New tones |
| Nürnberg report for Goslar, 1528 | 7/2.2 | L | G (levites) | gradual "in a tone made for it" | — | Common, cut | ? | New tone |
| Hamburg, 1529 | 5 | ? | ? | ? | ? | L on feasts; Trinity on Sundays | ? | Prophecy cadence written out |
| Herford, 1532 | 21 | ? | ? | ? | ? | L on feasts; Trinity on Sundays | ? | — |
| Brandenburg-Nürnberg, 1533 | 11 | L by school / H in villages | G, chapters in sequence | L | — | — | ? | — |
| Wittenberg town order, 1533 | 1 | ? | ? | L alleluia, at times gradual | ? | Feast Preface; Trinity on Sundays | Motets (*Pange lingua*) | Prophecy cadence |
| Hatzkerode, 1534(?) | 2 | L; Trinity as fallback | G | ? | ? | L on great feasts | ? | Organ in Kyrie and Gloria |
| Pomerania, 1535/1542/1569 | 4 | L / H | Epistle tone or read | L where schools; tract | ? | L or G on feasts (16 Prefaces, 1542, not printed) | ? | Prophecy cadence |
| Naumburg St Wenzel, 1537/38 | 2 | L "goodly introit" on feasts | ? | H | H ("Aus tiefer Not", 1527) | ? | ? | Mensural motets on high feasts |
| Albertine Saxony (Duke Henry), 1539 | 1 | L by scholars | G toward the people | H or sequence | — | L on feasts instead of exhortation | ? | Missal notes; Wittenberg tones |
| Brandenburg, 1540 | 3 | L | L in foundations / G in parishes | L / H in parishes; tract | L / H in villages | L (common) | L | — |
| Schleswig-Holstein, 1542; Hildesheim, 1544 | 23; 7/2.1 | ? | G | Alleluia with verse, jubilus cut; gradual of two verses / H | Creed hymn | L Prefaces at feasts | H | Melisma cut |
| Calenberg-Göttingen, 1542 | 6/2 | L ("slowly") | G sung, notated | G alleluia, notated | H | G (Müntzer's; Sunday Easter form) | H | Notated |
| Pfalz-Neuburg, 1543 (1547 edn.) | 13; 14 | L / priest in villages | G; festal chapters | L / priest | Offertory prayer (Osiander) | Solemn and Sunday forms for each feast | ? | Two Preface tones |
| Wolfenbüttel, 1543 | 6/1 | L on feasts of Christ | ? | ? | Creed hymn | L Christmas, Easter, Pentecost; Trinity; not the common | H | German Sanctus by the whole church |
| Heilbronn song order, 1543 | 17/1 | L to the organ; reduced cycle | ? | L alleluia or gradual | ? | ? | ? | Organ alternation |
| Mecklenburg, 1545/1552 | 5 | L in towns, listed by feast / H in villages | G read "without notes" | H | ? | L or G in towns / G in villages (not printed) | ? | "These notes and no other" |
| Nürnberg, Veit Dietrich, 1545 | 11 | L where schools / H | ? | L or H | — | — | ? | Latin "exercised" for the schools |
| Ansbach visitation, 1536; *Auctuarium*, 1548 | 11 | L | ? | L where pure / H | L (from Scripture) | ? | L | — |
| Amberg, 1550/1555 | 13 | L | Customary tone | ? | L *de tempore* | L or G on feasts, "customary notes" | ? | — |
| Regensburg, 1553 | 13 | L / organ | G | L or Latin text from the gradual | — | — | Organ with hymns | Organ |
| Dortmund, 1554 | 21 | ? | Read or sung, "after old custom" | H | H | Full Roman set in Low German | ? | — |
| Wittgenstein, 1555 | 22 | L festal / G in villages | ? | ? | ? | ? | ? | — |
| Hamburg, 1556 | 5 | L on feasts; Trinity or Holy Ghost on Sundays | L read by scholars, then G | ? | ? | L, may be shortened by agreement with the cantor | ? | — |
| Lüneburg, 1564 | 6/1 | ? | ? | ? | ? | L set (7) on high feasts, in towns | ? | Notated |
| Wolfenbüttel, 1569 | 6/1 | ? | ? | ? | ? | L set (7) | ? | Notated |
| Kurland, 1570 | 5 | ? | ? | ? | ? | G "customary noted" daily; G festal (3) | ? | Notated |
| Lippe, 1571 | 21 | L on feasts of Christ | ? | ? | ? | L in towns / G in villages: Christmas, Easter, Pentecost, Michaelmas | ? | Notated |
| Brandenburg visitation, 1573 | 3 | ? | **L "old melody", then G read** | ? | ? | ? | ? | Old melody required |
| Hesse *Agende*, 1574 (mediating) | 8 | L only before the people gather; H | ? | ? | ? | ? | ? | — |
| Nördlingen, 1579 | 12 | Organ plus scholars *figuraliter* on feasts; H on Sundays | ? | ? | ? | ? | ? | Polyphony, organ |
| Grubenhagen, 1581; Hoya, 1581 | 6/2 | L (Hoya: pastor) | ? | ? | ? | L where schools; Michaelmas (Hoya); German Isaiah 53 Preface (Grubenhagen) | ? | Notated |
| Hof, 1592 | 11 | L figural on feasts / G on Sundays; organ and three choirs | L then G | L from the Missal or Lossius; tract | ? | L from Lossius on chief feasts | Motets | Senfl, Lassus, Clemens, Victoria |
| Brieg, 1592 | 3 | L | L sung / G in small towns | L | ? | ? | ? | — |
| Verden, 1606 | 7/1 | ? | ? | ? | ? | L set (7) | ? | Notated |
| Osnabrück, (1588) 1618 | 7/1 | ? | ? | ? | ? | L: Michaelmas, Christmas, Easter, Pentecost | ? | Sanctus by organ |
| Schwäbisch Hall, 1543/1615 | 17/1 | L *choraliter vel figuraliter* | G (1526: L sung, then G) | L | ? | ? | ? | Polyphony |

---

## 12. Concordance of the orders quoted

Every order quoted or cited in this guide is listed below by region. The table gives:
- **Sehling**: the volume and pages in Sehling's edition.
- **Doc**: the `eko.db` document that holds the text, for full-text lookup. A single database
  record may hold several orders.
- **§**: the sections where the order is quoted or cited ("A" = Appendix A).

**Saxony, Thuringia and central Germany**

| Order | Sehling | Doc | § |
|---|---|---|---|
| Luther, *Formula missae et communionis*, 1523 | 1, pp. 4–6 | 2 | 3.1, 4.1, 6.1, 7.1, 8.1, 9.1, A.1 |
| Allstedt, Thomas Müntzer, *Deutsch evangelisch Messe*, 1524 (Radical Reformation) | 1, pp. 500–504 | 51, 52 | 3.2, A.2, A.5, A.6, A.8, A.10 |
| Allstedt, Thomas Müntzer, *Ordnung und berechnunge des teutschen ampts*, 1523/24 (Radical Reformation) | 1, pp. 504–505 | 52 | 3.2, 5.2 |
| Wittenberg, *Wie es einer zeit mit den ceremonien der messe gehalten*, 1525 | 1, p. 698 | 147 | 3.1, 7.2 |
| Luther, *Deutsche Messe und ordnung gottis diensts*, 1526 | 1, p. 14 | 3 | 3.3, 5.3 |
| Wittenberg, *Kirchen-Ordnung für die Stadt Wittenberg*, 1533 | 1, pp. 703–705 | 148 | 5.1, 8.2, 9.2 |
| Albertine Saxony, *Kirchenordnunge zum anfang* (Duke Henry's *Agende*), 1539 | 1, pp. 89 (editor), 271 | 7, 30 | 3.3, 4.2, 8.1, 8.4 |
| Albertine Saxony, *Instruktion zur zweiten Visitation*, 1539 | 1, p. 281 | 31 | 5.3, 8.2, 8.4 |
| Gnandstein, visitation articles, 1539 | 1, p. 564 | 85 | 5.3 |
| Wurzen, *Gemeine Artikel*, 1542 | 2, p. 98 | 1223 | 5.3 |
| Gottleuba, *Verzeichnus der kirchenordnung*, 1567–1577 | 1, p. 567 | 87 | 10.4 |
| Penig, *Kirchenordnung*, 1575 | 1, p. 634 | 116 | 10.4 |
| Electoral Saxony, *Kirchenordnung* of Elector August, 1580 | 1, p. 368 | 44 | 4.2 |
| Erfurt, *Deutsches Kirchenamt*, 1525 | 2, pp. 376–380 | 1251 | 3.2, 4.4, 6.3, 7.2, 9.1, A.2, A.5, A.6, A.8, A.10 |
| Naumburg, *Kirchen-Ordnung für die St. Wenzelskirche*, 1527, 1537/1538 | 2, pp. 60, 71 | 1218, 1219 | 7.3, 10.4 |
| Merseburg, ordination Mass, 1545 | 2, p. 7 | 1210 | 4.5 |
| Halle, *Kirchen-Ordnung der christlichen Gemein zu Halle*, 1543 | 2, p. 436 | 1257 | 5.3, 8.3, 10.3 |
| Halberstadt, town order | 2, p. 484 | 1260 | 8.1 |
| Hatzkerode (Anhalt), *Kirchenordnunge*, 1534(?) | 2, pp. 586–587 | 1263 | 4.3, 8.1 |
| Schönburg lordships, *Kirchen-Ordnung* of Johann Pfeffinger, 1542 | 2, p. 171 | 1235 | 9.2 |
| Henneberg, Meiningen, 1566 | 2, p. 339 | 1248 | 4.1 |

**Brandenburg, Pomerania, Prussia and the Baltic**

| Order | Sehling | Doc | § |
|---|---|---|---|
| Brandenburg, *Kirchenordnung* of Joachim II, 1540 | 3, p. 71 | 1746 | 3.1, 6.2, 7.2, 9.1 |
| Brandenburg, *Visitations- und Consistorialordnung*, 1573 | 3, p. 129 | 1748 | 5.3, 10.1 |
| Brieg, *Kirchenordnung*, 1592 | 3, p. 445 | 1809 | 5.3 |
| Teschen, *Kirchenordnung*, 1584 | 3, p. 462 | 1815 | 4.1 |
| Prussia, *Artikel der ceremonien*, 1525 | 4, p. 32 | 1832 | 7.1 |
| Prussia, *Kirchenordnung*, 1544; *Kirchenordnung und ceremonien*, 1568 | 4, pp. 65, 81 | 1833 | 8.1, 8.4 |
| Pomerania, *Kirchenordnung*, 1535; *Pia ordinatio caeremoniarum*, 1535 | 4, pp. 341, 349 | 1856, 1857 | 5.1, 5.2, 5.3, 8.1 |
| Pomerania, *Kirchenordnung*, 1542 | 4, pp. 357, 370 | 1859 | 8.1, A |
| Pomerania, *Agenda*, 1569 | 4, p. 438 | 1865 | 6.2 |
| Stralsund, *Entwurf einer Kirchenordnung*, 1555 | 4, p. 551 | 1889 | 8.1 |
| Kurland, *Kurländische Kirchenordnung*, 1570 | 5, pp. 89–90 | 1907 | 8.2, 8.4, A.6, A.14, A.15 |
| Mecklenburg, *Ordeninge der misse*, 1545 | 5, pp. 151–154 | 1922 | 4.1, 4.2, 5.1, 5.3, 8.4, 10.1 |
| Mecklenburg, *Kirchenordnung*, 1552 | 5, pp. 199, 202 | 1922 | 5.3, 8.1, A |
| Rostock, *Conformitas ceremoniarum*, 1560–1576 | 5, p. 288 | 1936 | 10.1 |
| Hamburg, *Hamburger Kirchenordnung*, 1529 | 5, pp. 522, 528 | 1960 | 5.1, 8.2 |
| Hamburg, *Kirchenordnung*, 1556 | 5, p. 552 | 1963 | 4.3, 5.3, 8.1, 8.4 |

**Lower Saxony, Westphalia and the north**

| Order | Sehling | Doc | § |
|---|---|---|---|
| Wolfenbüttel, *Christlike kerken-ordeninge*, 1543 | 6/1, p. 59 | 1972 | 8.2, 8.4 |
| Wolfenbüttel, *Kirchenordnung* of Duke Julius, 1569 | 6/1, pp. 180–181 | 1974 | A.1–A.9 |
| Lüneburg, *Kirchenordnung*, 1564 | 6/1, pp. 546, 574–575 | 2003, 2005 | 8.1, A.1–A.9 |
| Calenberg-Göttingen, *Kirchenordnung*, 1542 | 6/2, pp. 793–833 | 2036, 2037 | 3.2, 4.2, 5.3, 6.3, 7.3, 8.2, A.2, A.5–A.8, A.10 |
| Grubenhagen, *Kirchenordnung*, 1581 | 6/2, pp. 1073–1074 | 2058 | 8.2, 8.4, A.2, A.6, A.8, A.9, A.12 |
| Hoya, *Kirchenordnung*, 1581 | 6/2, pp. 1154–1155 | 2065 | 8.3, A.1–A.2, A.6–A.9 |
| Verden, *Kirchenordnung*, 1606 | 7/1, pp. 206–207 | 2092 | A.1–A.9 |
| Osnabrück, *Agende* (1588) 1618 | 7/1, pp. 268–269 | 2100 | 8.2, 8.3, 8.4, 10.5, A.1, A.2, A.6, A.8 |
| Engerhafe (East Frisia), *Liturgie*, 1583 | 7/1, pp. 677, 681 | 2119 | 8.1, 9.2 |
| Nürnberg, *Bericht für den Goslarer Rat*, 1528 | 7/2.2, p. 230 | 2186 | 6.3, 10.3 |
| Hildesheim, *Kirchenordnung*, 1544 | 7/2.1, pp. 853, 855 | 2136 | 6.1, A |
| Oldenburg, *Kirchenordnung*, 1573 (editors' notes) | 7/2.1, p. 1085 | 2149 | 10.4 |
| Herford, *Kirchenordnung*, 1532 | 21, p. 176 | 1442 | 8.2 |
| Dortmund, *Gottesdienstordnung*, 1554 | 21, pp. 209–211 | 1446 | 7.3, 8.3, A.1–A.11 |
| Lippe, *Kirchenordnung* of Antonius Corvinus, 1542 | 21, p. 345 | 1460 | 8.3 |
| Lippe, *Kirchenordnung*, 1571 | 21, pp. 410–411 | 1462 | 8.2, 8.3, 8.4, A.1, A.2, A.6, A.8, A.13 |
| Lippe, *Deutsche Messe*, [1525–1538] | 22, p. 568 | 1549 | 7.3, A.9 |
| Wittgenstein, *Kirchenordnung*, 1555 | 22, p. 102 | 1493 | 3.2, 4.4 |
| Schleswig-Holstein, *Kirchenordnung*, 1542 | 23, p. 90 | 1576 | 6.1 |
| Kiel, Low German Mass, [after 1526] | 23, p. 56 | 1576 | A.6 |

**Hesse**

| Order | Sehling | Doc | § |
|---|---|---|---|
| Hesse, *Agende*, 1574 (mediating) | 8, p. 411 | 2272 | 4.2 |

**Franconia, Bavaria, the Palatinates and Swabia**

| Order | Sehling | Doc | § |
|---|---|---|---|
| Nürnberg, *Deutsche Messe* of Prior Volprecht, 1524 | 11, p. 39 | 247 | 7.1, 9.1 |
| Nürnberg, *Gottesdienstordnung der Pfarrkirchen*, 1524 | 11, pp. 46–47 | 249 | 5.2, 7.1, 8.1 |
| Weißenburg, *Kirchenordnung*, 1528 | 11, p. 659 | 308 | 4.1, 6.2 |
| Brandenburg-Nürnberg, *Kirchenordnung*, 1533 | 11, pp. 188, 195 | 270 | 4.1, 4.2, 6.2 |
| Brandenburg-Ansbach, *Kirchenvisitation*, 1536 | 11, p. 326 | 277 | 9.1 |
| Brandenburg-Ansbach-Kulmbach, *Auctuarium*, 1548 (Interim order) | 11, pp. 329–330 | 278 | 6.2, 7.2 |
| Nürnberg, *Agendbüchlein* of Veit Dietrich, 1545 | 11, p. 495 | 297 | 3.1 |
| Schweinfurt, *Kirchenordnung*, 1543; *Gottesdienstordnung*, 1576 | 11, pp. 641, 648 | 304, 305 | 5.2, 10.4, 10.5 |
| Hof, *Ordo ecclesiasticus*, 1592 | 11, pp. 409, 424, 432–473 | 294 | 4.4, 4.5, 5.1, 6.2, 8.4, 9.2, 10.1, 10.4, 10.5 |
| Nördlingen, *Ordnung der ceremonien*, 1555 | 12, pp. 321, 325 | 373 | 9.2 |
| Nördlingen, *Kirchenordnung*, 1579 | 12, p. 365 | 375 | 4.5, 10.4 |
| Pfalz-Neuburg, *Kirchenordnung*, 1543 | 13, pp. 70–71 | 386 | 4.2, 5.1, 6.2 |
| Amberg, *Kirchenordnung*, 1550; 1555/1557 | 13, pp. 286, 291 | 411, 412 | 7.2, 8.4 |
| Regensburg, *Kirchenordnung unter Justus Jonas*, 1553 | 13, p. 421 | 440 | 4.5, 9.2, 10.5 |
| Kurpfalz, *Gemaine maß*, 1546 | 14, p. 96 | 472 | 4.3 |
| Pfalz-Neuburg, *Kirchenordnung* of Ottheinrich, [1547] | 14, p. 109 | 473 | 8.2, 8.4 |
| Hohenlohe, *Kirchenordnung*, 1553 | 15, p. 68 | 539 | 4.1 |
| Schwäbisch Hall, *Frühmessordnung*, 1526 | 17/1, p. 40 | 754 | 5.3 |
| Schwäbisch Hall, *Kirchenordnung* 1543/1615 | 17/1, p. 162 | 762 | 10.4 |
| Heilbronn, *Ordnung des Kirchengesangs*, 1543 | 17/1, p. 322 | 782 | 4.3, 10.5 |

**Alsace**

| Order | Sehling | Doc | § |
|---|---|---|---|
| Strasbourg, Mass of Diebold Schwarz, and *Teutsche Meß und Tauff*, 1524 (mediating) | 20/1, pp. 121, 133–135 | 1279 | 3.2, 8.1, A.2, A.3, A.5–A.8 |

---

## Appendix A. The Proper Prefaces: texts and translations

This appendix gives every Proper Preface printed in the corpus, once for each distinct text, and
lists the orders that carry it.

**How the entries are laid out.**
- **The Latin, where the corpus has it.** The Latin text is given first, from one witness, with
  the other witnesses listed and their variants noted. The English is translated from the Latin.
- **The German translations.** Each distinct German or Low German translation follows, with
  notes on where it shortens, adds to or changes the Latin.
- **German where the Latin is not in the corpus.** Some prefaces survive only in German: Lent,
  the Cross, the Blessed Virgin and the Apostles. The Latin of these is not printed anywhere in
  the corpus, so the English is made from the German. The note names the Latin preface of the
  Roman Missal that the German renders.
- **New German compositions.** Prefaces that are new German texts, not translations, are given
  last (§A.13–A.16).

**Where the Latin set comes from.** The Latin texts all belong to one Lower Saxon and
Westphalian chain of orders:
- Lüneburg 1564;
- Wolfenbüttel 1569;
- Grubenhagen and Hoya 1581;
- Verden 1606;
- Osnabrück (1588) 1618;
- Lippe 1571.

These orders print the prefaces "with notes" at the end of the order or of the Mass. Sehling's
editors refer them to the Roman Missal (*Röm. Meßbuch*) and to the *Missale Hildensemense* of
1511 (Sehling 7/2.1, p. 855, n. 33).

**Prefaces mentioned but not printed.** Several orders printed prefaces that Sehling's edition
does not reproduce:
- Mecklenburg 1540/45 ("Folgen Präfationes, 35 Seiten, mit Noten");
- Mecklenburg 1552;
- Pomerania 1542 ("Folgen 16 praefationes mit Noten");
- Mansfeld 1580 ("eine Reihe von Präfationes");
- Buxtehude 1565, which has Christmas, Epiphany, Easter, Ascension, Pentecost, Trinity and the
  *Quotidiana*;
- Oldenburg 1573.

Their texts are not in the corpus. Where their headings are given, they match the Lower Saxon
set.

**Already in the Canon guide.** The *common* Preface in German is also rendered in
[`CANON_IN_GERMAN_MASSES.md`](CANON_IN_GERMAN_MASSES.md), for Kantz, Worms (mediating),
Volprecht, Döber and Bremen. Those renderings are not repeated here.

### A.1 The dialogue and the common Preface (*Quotidiana*, *Praefatio communis*)

The common Preface frames every proper one. After *Vere dignum … aeterne Deus* the proper text
is inserted, and it ends with its own *Et ideo* or *Per quem* clause. In the Lower Saxon orders
the common Preface is also the festal Preface of **Michaelmas** (29 September) in Hoya 1581,
Osnabrück 1618 and Lippe 1571. This is the only sanctoral use of a Latin Preface in the corpus
(§8.3).

**Latin witnesses:**
- Lüneburg 1564 (Sehling 6/1, p. 574);
- Wolfenbüttel 1569 (6/1, p. 180);
- Verden 1606 (7/1, p. 206);
- Hoya 1581, "In die Michaelis" (6/2, p. 1155);
- Osnabrück (1588) 1618, "In die Michaelis" (7/1, pp. 268–269);
- Lippe 1571, "In die Michaelis" (21, p. 411).

Luther's *Formula missae* (1523) and the Nürnberg parish Mass of 1524 keep only the opening, cut
off at *per Christum Dominum nostrum* (§8.1).

**Wolfenbüttel, *Kirchenordnung* of Duke Julius, 1569, "Quotidiana"** (Sehling 6/1, p. 180):

<!-- doc 1974 -->
> Dominus vobiscum. Et cum spiritu tuo. Sursum corda. Habemus ad Dominum. Gratias agamus Domino
> Deo nostro. Dignum et iustum est. Vere dignum et iustum est, aequum et salutare, nos tibi
> semper et ubique gratias agere, Domine sancte Pater omnipotens, aeterne Deus, per Christum
> Dominum nostrum, per quem maiestatem tuam laudant angeli, adorant dominationes, tremunt
> potestates, coeli coelorumque virtutes ac beata seraphin socia exultatione concelebrant. Cum
> quibus et nostras voces ut admitti iubeas te precamur supplici confessione dicentes:

The Lord be with you. And with thy spirit. Lift up your hearts. We lift them up unto the Lord.
Let us give thanks unto the Lord our God. It is meet and right. It is very meet and right, just
and wholesome, that we should at all times and in all places give thanks unto thee, O holy Lord,
Father almighty, everlasting God, through Christ our Lord; through whom the Angels praise thy
majesty, the Dominions adore, the Powers tremble, the heavens and the Virtues of the heavens and
the blessed Seraphim with one accord celebrate it with exultation. With whom we beseech thee
that thou wouldest bid our voices also to be admitted, saying with lowly confession:

The German versions of the common Preface follow the Latin closely. The Low German of **Dortmund
1554** is a fair example. **Dortmund, *Gottesdienstordnung*, 1554, "Gemen edder Dechlike
Prefatio"** (Sehling 21, p. 211):

<!-- doc 1446 -->
> Ja frylick (warlick) isset recht unde billick, behörlick unde ock heilsam, Dat wy dy, Here, O
> hilge Vader, Almechtige, ewige Godt, tho allen tyden unde steden dancken Dorch Christum, unsen
> Heren, Dorch welcken dyne Herlicheit de Engele laven, de herschopen anbeden, de Mechte
> fruchten. Dartho ock de Hemmele unde der hemmelen Krefften unde de hilligen Seraphim mit
> groter froude tho samen hochlick eeren unde prysen, Mit welcken wy bidden, du willest
> tholaten, unse stemme demötlick loffsingende (loffsegende).

*Notes on the German.*
- The Low German doubles some terms: "recht unde billick, behörlick unde ock heilsam" for
  *dignum et iustum, aequum et salutare*.
- *Supplici confessione* becomes "humbly singing praise" (or "speaking praise"). The printed
  alternatives in brackets are the order's own.

Dortmund also gives the short form that Luther had made. It runs "through Christ our Lord, who
in the night when he was betrayed took the bread" straight into the Words of Institution
(Sehling 21, pp. 209–210).

### A.2 Christmas (*Quia per incarnati Verbi mysterium*)

**Latin witnesses:**
- Lüneburg 1564 (6/1, p. 574);
- Wolfenbüttel 1569 (6/1, p. 180);
- Grubenhagen 1581 (6/2, p. 1073; reads *infulsit*, the Missal's reading, for *effulsit*);
- Hoya 1581 (6/2, p. 1154; *agnoscimus* for *cognoscimus*);
- Verden 1606 (7/1, p. 206);
- Osnabrück (1588) 1618 (7/1, p. 269; *caritatis* for *claritatis*);
- Lippe 1571 (21, p. 410).

**Lüneburg, *Kirchenordnung*, 1564, "In die nativitatis Christi"** (Sehling 6/1, p. 574):

<!-- doc 2005 -->
> Vere dignum et etc. Aeterne Deus, quia per incarnati verbi mysterium nova mentis nostrae
> oculis lux tuae claritatis effulsit, ut dum visibiliter Deum cognoscimus, per hunc in
> invisibilium amorem rapiamur. Et ideo cum angelis et archangelis, cum thronis et
> dominationibus, cumque omni militia coelestis exercitus hymnum gloriae tuae canimus, sine fine
> dicentes.

It is very meet, etc. … everlasting God: for by the mystery of the Word made flesh the new light
of thy brightness hath shone upon the eyes of our mind; that while we know God visibly, we may
by him be caught up into the love of things invisible. And therefore with Angels and Archangels,
with Thrones and Dominions, and with all the company of the heavenly host, we sing the hymn of
thy glory, evermore saying:

**German (1): Müntzer's translation** (Radical Reformation). Müntzer's *Deutsch evangelisch
Messe* (1524) has this translation. So do the Erfurt *Deutsches Kirchenamt*
(1525; Sehling 2, p. 379), Calenberg-Göttingen (1542; 6/2, p. 821) and Lippe 1571, "auff den
Dörffern an Weihenachten" (21, p. 410). **Allstedt, Thomas Müntzer, *Deutsch evangelisch Messe*,
1524, Christmas office** (Sehling 1, pp. 501–502):

<!-- doc 51 -->
> Dann durch das geheimnis des vormenschten wortes ist das neue licht deiner klarheit den augen
> unsers gemüthes erschinen. Auf das so wir got sichtbarlich erkennen, mügen kummen zu dem
> erkentnis der unsichbaren gotheit. Dorumb singen wir mit allen engeln und erzengein, und mit
> den, do got innen hirschet, dozu mit aller himlischer geselschaft, singen wir eine leisen
> deinem preise one ende sagende.

*Notes on Müntzer's German.*
- **Opening.** It begins at *quia*. The opening is "as in the Mass of Advent" (§A.11).
- ***Per hunc in invisibilium amorem rapiamur*** ("may by him be caught up into the love of
  things invisible") becomes "may come to the knowledge of the invisible Godhead". The words "by
  him" are dropped, and love becomes knowledge.
- ***Cum thronis et dominationibus*** becomes "with them in whom God reigneth": the Thrones are
  read as the seat of God.
- ***Omni militia coelestis exercitus*** becomes "all the heavenly company".
- ***Hymnum gloriae tuae canimus*** becomes "sing we a *Leise* to thy praise". A *Leise* is a
  vernacular hymn ending *Kyrieleis*.
- **Lippe 1571** substitutes "Lobgesang deines preyses", "a song of praise of thy glory", for
  *eine leisen*.

**German (2): Strasbourg** (mediating). **Strasbourg, *Teutsche Meß und Tauff*, 1524, "Etliche
vorreden"** (mediating; Sehling 20/1, p. 133):

<!-- doc 1279 -->
> So du in der oben angezeigten Prefation gelesen hast das wörtlin Ewiger Gott, so folget: Dann
> durch die geheymnuß des worts, so fleysch worden, ist ein neüwes liecht deiner klarheit den
> augen unsers gemüts erschinen, auff das, so wir Gott sichtbarlichen erkennen, das wir durch in
> zuor liebe unsichtbarer dingen gezogen werden, Deßhalb wir mit den Engeln und allen
> hymmlischen härscharen dir singen on underlaß den preyß deiner ere und sagent:

When thou hast read in the Preface shewn above the little word "everlasting God", there
followeth: For by the mystery of the Word which was made flesh a new light of thy brightness
hath appeared to the eyes of our mind; that, as we know God visibly, we may by him be drawn to
the love of invisible things. Wherefore we with the Angels and all the heavenly hosts sing unto
thee without ceasing the praise of thine honour, and say:

*Notes on the Strasbourg German.*
- This is a close translation, and it keeps *per hunc* ("durch in") and *amorem* ("liebe").
- It drops the Archangels, Thrones and Dominions.
- It renders *sine fine* "without ceasing".
- The rubric shows that the proper text was spliced into the common Preface after *aeterne
  Deus*, as in the Missal.

**German (3): Dortmund (Low German).** **Dortmund, *Gottesdienstordnung*, 1554, "Vorrede tho
Wynachten edder Midtwynter"** (Sehling 21, p. 210):

<!-- doc 1446 -->
> Wente dorch de geheimniss des fleschgewordenen Wordes (edder: went dorch de minschwerdinge
> dynes leven Söns) ys unses herten ogen ein nye licht dyner klarheit erschenen, Up dat, als wy
> Godt sichtlick erkennen, dorch em thor leve der unsichtliken dinge getagen werden, Darumme mit
> den Engelen unde Ertzengelen, mit den Thronen unde den Herschopen Unde ock mit aller
> Ridderschop des Hemmelschen heres singen wy loff dyner herlicheit, sunder ende seggende:
> Hillich etc.

*Notes on the Dortmund Low German.*
- This is a full and faithful translation, with every rank of angel kept.
- It offers an alternative, "by the incarnation of thy dear Son", for "the mystery of the Word
  made flesh".
- It renders *mentis* as "heart".

### A.3 Epiphany (*Quia cum Unigenitus tuus*)

**Latin witnesses:** Lüneburg 1564 (6/1, p. 574), Wolfenbüttel 1569 (6/1, pp. 180–181) and
Verden 1606 (7/1, pp. 206–207). Grubenhagen, Hoya, Osnabrück and Lippe have no Epiphany Preface.

**Lüneburg, *Kirchenordnung*, 1564, "In die epiphanias"** (Sehling 6/1, p. 574):

<!-- doc 2005 -->
> Vere dignum et iustum etc. Aeterne Deus, qui cum unigenitus tuus in substantia nostrae
> mortalitatis apparuit, nova nos immortalitatis suae luce reparavit, et ideo cum angelis et
> archangelis, cum thronis et dominationibus, cumque omni militia coelestis exercitus hymnum
> gloriae tuae canimus, sine fine dicentes.

It is very meet and right, etc. … everlasting God: for when thine Only-begotten appeared in the
substance of our mortality, he restored us by the new light of his immortality. And therefore
with Angels and Archangels, with Thrones and Dominions, and with all the company of the heavenly
host, we sing the hymn of thy glory, evermore saying:

*Note.* The Lower Saxon orders print *qui cum* where the Missal has *quia cum*.

**German: Strasbourg** (mediating). **Strasbourg, *Teutsche Meß und Tauff*, 1524, "Ein ander
Vorred"** (mediating; Sehling 20/1, p. 133):

<!-- doc 1279 -->
> Ewiger Gott, So dein eingeborner sun in dem wesen unser tödtlicheit erschinen ist, hat er uns
> mit dem neüwen liecht seiner untödtlichheyt widerbracht etc., Deshalb wir etc., wie oben
> steet.

Everlasting God, when thine only-begotten Son appeared in the being of our mortality, he
restored us with the new light of his immortality, etc.; wherefore we, etc., as standeth above.

*Note.* The translation is exact; *substantia* becomes "wesen", "being".

**German: Dortmund (Low German).** **Dortmund, *Gottesdienstordnung*, 1554, "Inn der Apenbaringe
Christi edder der Köninge dach"** (Sehling 21, p. 210):

<!-- doc 1446 -->
> Wente do dyn eingebaren Söne yn gestalt (edder: yn der Substantien efft wesende) unser
> sterfflicheit ys erschennen, hefft he uns mit dem nyen lichte syner unsterfflicheit wedder
> maket. Darumme etc., wo baven.

For when thine only-begotten Son appeared in the form (or: in the substance or being) of our
mortality, he made us anew with the new light of his immortality. Therefore, etc., as above.

### A.4 Lent (*Qui corporali ieiunio*)

**Witness:** Dortmund 1554 only. No Latin Lenten Preface is printed in the corpus. The Low
German renders the Missal's *Qui corporali ieiunio vitia comprimis, mentem elevas, virtutem
largiris et praemia*, faithfully. **Dortmund, *Gottesdienstordnung*, 1554, "Inn der Vasten"**
(Sehling 21, p. 210):

<!-- doc 1446 -->
> De du dorch dat lyfflike vastent de gebrecke vordrückest, dat herte erhevest, dogede unde lon
> uns gevest Dorch Christum, unsen Heren, Dorch welcken etc., wo nedden yn der gemenen vorrede.

[It is very meet … everlasting God:] Who by bodily fasting dost suppress our faults, lift up the
heart, and give us virtue and reward; through Christ our Lord, through whom, etc., as below in
the common Preface.

### A.5 Passiontide and the Holy Cross (*Qui salutem humani generis in ligno crucis*)

**Witnesses:** Müntzer 1524 (Radical Reformation; 1, p. 502), Erfurt 1525 (2, p. 380),
Calenberg-Göttingen 1542 (6/2, p. 826), Strasbourg 1524 (mediating; 20/1, p. 121) and Dortmund
1554 (21, p. 210).
- Müntzer, Erfurt and Calenberg use it in the Mass "of the suffering of Christ".
- Strasbourg puts it in its ordinary Sunday Mass.
- Dortmund uses it "of the Cross and Passion of Christ".

No Latin text of this Preface is printed in the corpus. The German renders the Missal's *Qui
salutem humani generis in ligno crucis constituisti, ut unde mors oriebatur, inde vita
resurgeret, et qui in ligno vincebat, in ligno quoque vinceretur*.

**German (1): Müntzer** (Radical Reformation). Müntzer's translation is also in Erfurt and
Calenberg. **Allstedt, Thomas Müntzer, *Deutsch evangelisch Messe*, 1524, office of the
Passion** (Radical Reformation; Sehling 1, p. 502):

<!-- doc 51 -->
> Warlich es ist wirdig und recht billich und ist heilsam, das wir dir herr almechtiger ewiger
> got allzeit danksagen. Der du das heil des menschlichen geschlechtes am holz des kreuzes
> dargestelt hast, auf das do der tod her entsprossen war, solt wider erstehn das leben, durch
> Christum unseren herren, durch wilchen loben die engel dein herligk. etc.

Verily it is worthy and right, meet and wholesome, that we should at all times give thanks unto
thee, O Lord, almighty everlasting God: who hast set forth the salvation of mankind on the wood
of the cross, that whence death had sprung, thence life might rise again; through Christ our
Lord, through whom the Angels praise thy glory, etc.

*Note.* Müntzer **omits the last clause** of the Latin, *et qui in ligno vincebat, in ligno
quoque vinceretur*, "and that he who by a tree overcame might also by a tree be overcome".
Erfurt and Calenberg follow him. Calenberg completes the ending with the full German common
Preface, "durch welchen loben die engel … ohne ende sagende".

**German (2): Strasbourg, Schwarz** (mediating). Diebold Schwarz's Strasbourg Mass expands that
last clause with a reference to Adam and to the obedience shown on the tree. **Strasbourg, Mass
of Diebold Schwarz, 1524** (mediating; Sehling 20/1, p. 121):

<!-- doc 1279 -->
> Es geburt sich furwor und ist billich, recht und heilsam, das wir dir alweg an allen orten
> danck sagen. O herr, heiliger, almechtiger vatter, ewiger Gott, der du unser heil durch das
> holtz des creutzs verschafft hast, uff das das leben von solchem keme, von welchem der todt
> uffgangen ist, und uff das der feyndt, so durch das holtz übertrettung uns alle in Adam
> überwunden hatt, wider uß gehorsam, so am holtz geleistet ist, bestritten wurde, durch
> Christum Jesum, unsern hern, durch welches maiestat und herlichkeyt dich die engel und alle
> hymmelsche ritterschafft loben, mit glichem frolocken samenthafft ryemen und preysen, zu
> welchen du auch unsere stymmen annemen wöllest, bitten wir mit undertheniger bekantnuß und
> sagen:

It is fitting in truth, and meet, right and wholesome, that we should always and in all places
give thanks unto thee, O Lord, holy, almighty Father, everlasting God, who hast wrought our
salvation by the wood of the cross, that life might come from that from which death had arisen;
and that the enemy, who through the transgression at the tree had overcome us all in Adam, might
be overcome again through the obedience rendered on the tree; through Christ Jesus our Lord,
through whose majesty and glory the angels and all the heavenly chivalry praise thee, and with
like exultation together extol and laud thee; with whom we pray thee to accept our voices also,
with humble confession, and we say:

*Notes on Schwarz's German.*
- The Latin's "he who overcame by a tree" is glossed as **the devil**, who conquered "through
  the transgression at the tree" "in Adam".
- The Latin's "might be overcome by a tree" becomes **"through obedience rendered on the
  tree"**. Christ's obedience is set against Adam's disobedience (Rom 5:19).
- The angelic orders of the common Preface are reduced to "the angels and all the heavenly
  chivalry".

**German (3): Dortmund (Low German).** Dortmund renders the whole Latin, the last clause
included. **Dortmund, *Gottesdienstordnung*, 1554, "Vam Crütze unde Lyden Christi"**
(Sehling 21, p. 210):

<!-- doc 1446 -->
> De du des minschliken geslechts salicheit am holte des Crützes heffst gewercket, up dat, dar
> de dodt van her was gekamen, dar hen dat leevent wedder uth erstönde unde de dar im holte
> averwunnen hadde, wedderumme ock am holte averwunnen worde, Dorch Christum, unsen Heren, dorch
> welcken etc., nedden yn der gemenen vorrede.

[It is very meet … everlasting God:] Who hast wrought the salvation of mankind on the wood of
the Cross, that whence death had come, thence life might rise again; and that he who had
overcome by the tree might in turn be overcome on the tree; through Christ our Lord, through
whom, etc., below in the common Preface.

### A.6 Easter (*Te quidem, Domine, omni tempore*)

**Latin witnesses:**
- Lüneburg 1564 (6/1, p. 574);
- Wolfenbüttel 1569 (6/1, p. 181);
- Grubenhagen 1581 (6/2, p. 1074);
- Hoya 1581 (6/2, p. 1154). It prints *verus est Deus* for *verus est agnus*, which Sehling's
  editor takes for a misprint;
- Verden 1606 (7/1, p. 207);
- Osnabrück (1588) 1618 (7/1, p. 269);
- Lippe 1571 (21, p. 410).

**Lüneburg, *Kirchenordnung*, 1564, "In die Paschae"** (Sehling 6/1, p. 574):

<!-- doc 2005 -->
> Vere dignum et iustum est, aequum et salutare, te quidem Domine, omni tempore, sed in hac
> potissimum die gloriosius praedicare, cum pascha nostrum immolatus est Christus. Ipse enim
> verus est agnus, qui abstulit peccata mundi, qui mortem nostram moriendo destruxit et vitam
> resurgendo reparavit, et ideo cum angelis et archangelis, cum thronis et dominationibus,
> cumque omni militia coelestis exercitus hymnum gloriae tuae canimus, sine fine dicentes.

It is very meet and right, just and wholesome, at all times indeed to praise thee, O Lord, but
chiefly on this day more gloriously, when Christ our Passover was sacrificed. For he is the very
Lamb, which hath taken away the sins of the world; who by dying hath destroyed our death, and by
rising again hath restored life. And therefore with Angels and Archangels, with Thrones and
Dominions, and with all the company of the heavenly host, we sing the hymn of thy glory,
evermore saying:

**German (1): Müntzer** (Radical Reformation). This translation is in Müntzer 1524 and Erfurt
1525 (2, p. 376). It is also in Calenberg-Göttingen 1542 (6/2, p. 829) and Lippe 1571, "auff den
Dörffern" (21, p. 410). The Low German Mass from Kiel has it too
(Sehling 23, p. 56; rendered in the Canon guide, §11.2). **Allstedt, Thomas Müntzer, *Deutsch
evangelisch Messe*, 1524, office of the Resurrection** (Sehling 1, p. 503):

<!-- doc 51 -->
> Warlich es ist wirdig und recht billich und gleich und ist heilsam, das wir herr almechtiger
> got dir allenthalben danksagen. Und sonderlich in dieser zeit höcher preisen, dann Christus
> unser osterlamp ist vor uns geopfert. Er ist das ware lamp gotes, wilchs do weg genommen hat
> die sunde der werlet. Der do durch seinen tod unsern ewigen tod vorstöret hat und als er
> auferstanden ist, hat er herwiderbracht das leben. Dorumb singen wir mit allen engeln der
> himlischen scharen ein leisen deines preises one ende sagende.

*Notes on Müntzer's German.*
- **The opening is the common Preface's.** *Te quidem, Domine, omni tempore … praedicare* is
  replaced by "that we give thanks unto thee in all places, and specially at this time praise
  thee more highly". The Latin's own "at all times indeed to praise thee" disappears into the
  common formula.
- ***In hac potissimum die*** ("chiefly on this day") becomes **"at this time"**, so the Preface
  serves the whole Easter season.
- ***Mortem nostram*** becomes "our **eternal** death".
- **The *Et ideo* is reduced** to "with all the angels of the heavenly hosts", and "the hymn"
  becomes "a *Leise*".
- **The Kiel Mass** adds that Christ died "by his **temporal** death" ("synen tytliken dot").
  Lippe 1571 reads "einen lobgesang" for "ein leisen".

**German (2): Kurland.** Kurland 1570 has its own translation. **Kurland, *Kurländische
Kirchenordnung*, 1570, "Auf ostern"** (Sehling 5, p. 90):

<!-- doc 1907 -->
> Warlich, es ist billich und gerecht, dazu gleich und ganz heilsam, das wir dir alzeit und an
> allen enden danksagen, und sonderlich zu dieser zeit höher preisen, dieweil Christus, unser
> osterlam, für uns am creuze ist geopfert, welch ist das wahre lam gottes, das dar weggenommen
> hat der welt sünde, der durch sein sterben den tod uberwunden hat, und durch sein auferstehung
> das leben herwider gebracht, darum wir mit allen engeln und mit der ganzen himlischen
> herscharen singen einen lobgesang deines preises ohne ende sagende.

*Notes on Kurland's German.* It follows Müntzer's shape. It adds "**on the cross**" to
"sacrificed for us", and it says that Christ by his death "overcame death" instead of "destroyed
our death".

**German (3): Strasbourg** (mediating). **Strasbourg, *Teutsche Meß und Tauff*, 1524, "Ein ander
Vorred"** (mediating; Sehling 20/1, p. 133):

<!-- doc 1279 -->
> Recht und heylsam, das man dich allweg herrlich rüm und preyße, Dann unser osterlamb Christus
> ist geschlachtet. Er ist das wor lamb, das hyn nympt der welt sünde, der unsern tod durchs
> sterben zerstöret und das leben durch aufferstehung widerbracht hat, Deßhalb wir etc.

[It is] right and wholesome that thou be always gloriously extolled and praised; for Christ our
Passover is slain. He is the true Lamb, that taketh away the sin of the world; who by dying hath
destroyed our death, and by rising again hath restored life. Wherefore we, etc.

*Note.* Strasbourg keeps the Latin's own opening ("always … gloriously praised"). But it **drops
*sed in hac potissimum die***: there is no "chiefly on this day".

**German (4): Dortmund (Low German).** **Dortmund, *Gottesdienstordnung*, 1554, "Tho Paschen"**
(Sehling 21, p. 210):

<!-- doc 1446 -->
> Dy twarn, O Here, tho allen tyden, besunder överst up dessem dage (edder: desse tydt)
> hochtydtliker tho prysen, dar yn unse Paschen Christus ys geoffert, De sülve ys dat ware Lam,
> dat dar hen genomen hefft der werlt sünde. De unsen dodt dorch syn stervent hefft tho braken
> unde dat leevent dorch syn upstaent weddermaket. Darumme etc., wo baven tho Wynachten.

[It is very meet … wholesome,] to praise thee indeed, O Lord, at all times, but chiefly upon
this day (or: this time) more festally, wherein Christ our Passover is offered. The same is the
true Lamb, that hath taken away the sin of the world; who by his dying hath broken our death,
and by his rising hath made life anew. Therefore, etc., as above at Christmas.

*Note.* This is complete and faithful. "Chiefly upon this day" is kept, with "this time" offered
as an alternative, as in Müntzer.

**German (5): the Easter text as Calenberg's Sunday Preface.** Calenberg-Göttingen 1542 prints a
shorter form of the Easter Preface in its model Mass for an ordinary Sunday. That Mass has the
Trinity propers: the Alleluia *Benedictus es, Domine, Deus patrum nostrorum* and the Gospel John
3. **Calenberg-Göttingen, *Kirchenordnung*, 1542** (Sehling 6/2, p. 815):

<!-- doc 2036 -->
> Warlich ist das billich und recht und heilsam, das wir dir danken, heiliger Herr, almechtiger
> Vater, ewiger Gott, durch Christum, unsern Herren, der das ware osterlamb ist, der ist warlich
> das lamb, das der welt sünde tregt, der unsern todt mit seinem sterben verstöret hat und das
> leben mit seiner auferstehunge erworben hat. Darumb singen wir mit seinen engeln und erzengeln
> deiner ehr ein lobgesang, ohn end sprechende

Verily it is meet and right and wholesome that we give thanks unto thee, holy Lord, almighty
Father, everlasting God, through Christ our Lord, who is the true Passover lamb; he is verily
the Lamb that beareth the sin of the world, who by his dying hath destroyed our death, and by
his resurrection hath won life. Therefore we sing with his angels and archangels a song of
praise to thine honour, without end saying:

*Note.* All reference to the day and the season is gone. The Easter Preface becomes a **Sunday
Preface**: every Sunday is a feast of the resurrection.

### A.7 Ascension (*Qui post resurrectionem suam*)

**Latin witnesses:**
- Lüneburg 1564 (6/1, p. 574);
- Wolfenbüttel 1569 (6/1, p. 181);
- Hoya 1581 (6/2, p. 1155; *faceret* for *tribueret*);
- Verden 1606 (7/1, p. 207).

**Lüneburg, *Kirchenordnung*, 1564, "Ascensionis"** (Sehling 6/1, p. 574):

<!-- doc 2005 -->
> Vere dignum et etc. Per Christum Dominum nostrum, qui post resurrectionem suam omnibus
> discipulis suis manifestus apparuit et ipsis cernentibus est elevatus in coelum, ut nos
> divinitatis suae tribueret esse participes, et ideo cum angelis et archangelis, cum thronis et
> dominationibus, cumque omni militia coelestis exercitus, hymnum gloriae tuae canimus, sine
> fine dicentes.

It is very meet, etc. … through Christ our Lord: who after his resurrection appeared openly unto
all his disciples, and in their sight was lifted up into heaven, that he might grant us to be
partakers of his Godhead. And therefore with Angels and Archangels, with Thrones and Dominions,
and with all the company of the heavenly host, we sing the hymn of thy glory, evermore saying:

**German (1): Strasbourg** (mediating). **Strasbourg, *Teutsche Meß und Tauff*, 1524, "Ein ander
Vorred"** (mediating; Sehling 20/1, p. 134):

<!-- doc 1279 -->
> Ewiger Gott, durch Christum, unnsern herrn, Der nach seiner aufferstendtnuß seinen jüngern
> offentlich erschinen und in irem gesicht erhebt ist in hymmel, auff das er unß seiner gotheit
> teilhaftig macht, Deshalb wir etc.

Everlasting God, through Christ our Lord, who after his resurrection appeared openly to his
disciples, and in their sight was lifted up into heaven, that he might make us partakers of his
Godhead; wherefore we, etc.

*Note.* The translation is exact, but it leaves out "all" (*omnibus*).

**German (2): Calenberg-Göttingen.** **Calenberg-Göttingen, *Kirchenordnung*, 1542, Ascension**
(Sehling 6/2, p. 831):

<!-- doc 2037 -->
> Warlich, es ist billich und recht und ist heilsam, das wir dir, Herr, almechtiger Gott,
> allenthalben danksagen durch Christum, unseren Herren, welcher nach seiner auferstehung allen
> seinen jüngern offenbarlich erschinen ist und fur ihren augen aufgenomen ist in himel, auf das
> er uns geb, das wir seiner gottheit teilhaftig würden. Darumb singen wir mit den engeln und
> erzengeln, herschenden und gewaltigen engeln, auch mit der herschaft der himlischen herscharen
> ein lobgesang deiner herrligkeit, ohn ende sagende

*Notes on Calenberg's German.*
- This is a full and faithful translation.
- *Cum thronis et dominationibus* becomes "ruling and mighty angels", and *omni militia
  coelestis exercitus* becomes "the lordship of the heavenly hosts".
- Sehling's editor notes that the text is close to the Erfurt *Kirchenamt* of 1526.

**German (3): Dortmund (Low German).** **Dortmund, *Gottesdienstordnung*, 1554, "Hemmelfart
Christi"** (Sehling 21, p. 210):

<!-- doc 1446 -->
> Dorch Christum, unsen Heren, De na syner upstandinge alle synen Jungeren sick klarlick hefft
> apenbaret unde ys hüdden ansehens vor eren ogen tho hemmel gefaren, dat he uns syner Godtheit
> deelhafftich makede. Darumme etc., tho Wynachten.

[It is very meet …] through Christ our Lord, who after his resurrection shewed himself clearly
to all his disciples, and this day, in sight before their eyes, went up into heaven, that he
might make us partakers of his Godhead. Therefore, etc., [as] at Christmas.

*Note.* Dortmund adds "**this day**" ("hüdden").

### A.8 Pentecost (*Qui ascendens super omnes caelos*)

**Latin witnesses:**
- Lüneburg 1564 (6/1, pp. 574–575);
- Wolfenbüttel 1569 (6/1, p. 181);
- Grubenhagen 1581 (6/2, p. 1074);
- Hoya 1581 (6/2, p. 1155);
- Verden 1606 (7/1, p. 207);
- Osnabrück (1588) 1618 (7/1, p. 269);
- Lippe 1571 (21, p. 411).

**The *canimus* variant.** Lüneburg, Wolfenbüttel and Hoya read ***canimus*** ("we sing") where
the Missal has *concinunt* ("[the Powers] sing together"). Sehling's editor marks it "[!]" in
Hoya. The grammar is broken, but the sense is that the congregation joins the angels. The others
read *concinunt*. In Grubenhagen the editor has restored *concinunt* against a print reading
*canimus*.

**Lüneburg, *Kirchenordnung*, 1564, "Pentecostes"** (Sehling 6/1, pp. 574–575):

<!-- doc 2005 -->
> Vere dignum et iustum etc. Per Christum Dominum nostrum, qui ascendens super omnes coelos,
> sedensque ad dexteram tuam, promissum Spiritum sanctum hodierna die in filios adoptionis
> effudit. Quapropter profusis gaudiis totus in orbe terrarum mundus exultat, sed et supernae
> virtutes atque angelicae potestates hymnum gloriae tuae canimus, sine fine dicentes.

It is very meet and right, etc. … through Christ our Lord: who, ascending above all the heavens,
and sitting at thy right hand, did on this day pour forth the promised Holy Ghost upon the
children of adoption. Wherefore with overflowing joy the whole world throughout all the earth
doth exult; and the Virtues on high and the angelic Powers also [with them] we sing the hymn of
thy glory, evermore saying:

**German (1): Müntzer** (Radical Reformation). Müntzer's translation is also in Erfurt 1525 (2,
p. 377), Calenberg-Göttingen 1542 (6/2, p. 833) and Lippe 1571, "auff den Dörffern" (21, p.
411). In Sehling's edition Müntzer's Pentecost office is printed at the head of the following
document (*eko.db* doc 52). **Allstedt, Thomas Müntzer, *Deutsch evangelisch Messe*, 1524,
office of the Holy Ghost** (Sehling 1, p. 504):

<!-- doc 52 -->
> Warlich es ist wirdig und recht billich und ist heilsam, das wir dir almechtiger ewiger got
> allzeit und allenthalben danksagen durch Christum unseren herren. Der do aufgestigen ist in
> himmel und sitzt zu der rechten des vaters, und hat heut den heilgen geist, den er vorheissen
> hatte, ergossen in die auserwelten kinder. Dorumb ist die ganze welt voll freuden, im ganzen
> umkreis der erden. Dozu singet alle himlische schaer ein leisen deinem preise one ende
> sagende.

*Notes on Müntzer's German.*
- ***Super omnes caelos*** ("above all the heavens") becomes "into heaven".
- ***In filios adoptionis*** ("upon the children of adoption") becomes **"upon the elect
  children"**.
- ***Profusis gaudiis*** is dropped.
- ***Supernae virtutes atque angelicae potestates*** becomes "all the heavenly host", who "sing
  a *Leise*".

**German (2): Strasbourg** (mediating). **Strasbourg, *Teutsche Meß und Tauff*, 1524, "Ein ander
Vorred"** (mediating; Sehling 20/1, p. 134):

<!-- doc 1279 -->
> Ewiger Gott, durch Christum, unnsern hern, Der, auffgestigen über alle hymmel und sitzend zuo
> deiner gerechten, außgossen hat den verheyssen geist über dein an kindes statt angenommene
> kinder, Deßhalb mit außtringenden freüden in allem erdtrich die welt sich freüwet, auch die
> Engel dein lob singen und sprechen: Sanctus, Heyliger etc.

Everlasting God, through Christ our Lord, who, ascended above all heavens and sitting at thy
right hand, hath poured out the promised Spirit upon thy children taken in the stead of
children; wherefore with overflowing joys in all the earth the world rejoiceth, and the Angels
also sing thy praise and say: Sanctus, Holy, etc.

*Note.* This is close, and it keeps "above all heavens" and "adoption" ("an kindes statt
angenommene"). It drops ***hodierna die***, "on this day".

**German (3): Dortmund (Low German).** **Dortmund, *Gottesdienstordnung*, 1554, "Pingesten"**
(Sehling 21, pp. 210–211):

<!-- doc 1446 -->
> Dorch Christum, unsen Heren. De upfarende baven alle hemmele unde sittende tho dyner rechtern
> handt, hefft (hüden tho dage) den belaveden hilligen Geist yn de utherwelden Kyndere
> gestörtet, Des sick de gantze werlt avermaten seer hochlick vorblidet, Ja, ock de Oversten
> Kreffte unde Engelschen mechte singen loff dyner herlicheit, sunder ende seggende: Hillich
> etc.

[It is very meet …] through Christ our Lord, who, ascending above all heavens and sitting at thy
right hand, hath (on this day) poured out the promised Holy Ghost upon the chosen children;
whereof the whole world rejoiceth exceedingly; yea, the highest Virtues also and the angelic
Powers sing the praise of thy glory, without end saying: Holy, etc.

*Notes on Dortmund's German.* Dortmund agrees with Müntzer's "**chosen children**" against the
Latin's "children of adoption". It puts "today" in brackets as optional, and it has *concinunt*,
not *canimus*.

### A.9 Trinity (*Qui cum unigenito Filio tuo*)

**Latin witnesses:**
- Lüneburg 1564 (6/1, p. 575);
- Wolfenbüttel 1569 (6/1, p. 181);
- Grubenhagen 1581 (6/2, p. 1074);
- Hoya 1581 (6/2, p. 1155; *essentiae* for *substantiae*);
- Verden 1606 (7/1, p. 207).

Several orders also prescribe it for **ordinary Sundays** (§8.2): Wolfenbüttel 1543, Hamburg
1529, Herford 1532 and Wittenberg 1533. The reason they give is that the Preface "was made
against the Arians".

**Lüneburg, *Kirchenordnung*, 1564, "Trinitatis"** (Sehling 6/1, p. 575):

<!-- doc 2005 -->
> Vere dignum et iustum est, aequum et salutare, nos tibi semper et ubique gratias agere, Domine
> sancte Pater omnipotens, aeterne Deus, qui cum unigenito Filio tuo et Spiritu sancto unus es
> Deus, unus es Dominus, non in unius singularitate personae, sed in unius trinitate
> substantiae. Quod enim de tua gloria revelante te credimus, hoc de Filio tuo, hoc de Spiritu
> sancto sine differentia discretionis sentimus, ut in confessione verae sempiternaeque deitatis
> et in personis proprietas et in essentia unitas et in maiestate adoretur aequalitas, quam
> laudant angeli, adorant dominationes, tremunt potestates, coeli coelorumque virtutes ac beata
> seraphin socia exultatione concelebrant. Cum quibus et nostras voces, ut admitti iubeas te
> precamur supplici confessione dicentes.

It is very meet and right, just and wholesome, that we should at all times and in all places
give thanks unto thee, O holy Lord, Father almighty, everlasting God: who with thine
only-begotten Son and the Holy Ghost art one God, one Lord; not in the singleness of one Person,
but in the Trinity of one substance. For that which by thy revelation we believe of thy glory,
the same we believe of thy Son, the same of the Holy Ghost, without any difference or
separation; that in the confession of the true and everlasting Godhead there may be adored in
the Persons propriety, in the essence unity, and in the majesty equality: which the Angels
praise, the Dominions adore, the Powers tremble at, the heavens and the Virtues of the heavens
and the blessed Seraphim with one accord celebrate with exultation. With whom we beseech thee
that thou wouldest bid our voices also to be admitted, saying with lowly confession:

*Note.* The ending is that of the common Preface: *quam laudant angeli, adorant dominationes …*.
It is not the *Cherubim quoque ac Seraphim, qui non cessant clamare* of the later Roman form.

**German (1): Lippe, Low German.** **Lippe, *Deutsche Messe*, [1525–1538], Trinity Sunday**
(Sehling 22, p. 568):

<!-- doc 1549 -->
> Warlyck, edt is byllick unde recht, dartho ock yst seer heilsam, dat wy dy altydt und yn allen
> enden danck seggen. Here, heillyge vader, almechtige, ewyge Godt, welcker du myt dynem
> eyngebornen soen und dem hilligen geiste eyn enyge Godt bist, eyn enyger here bist. Nicht yn
> eynycheit der personen, sonder yn der enycheit eynes sunderliken wesens. Den dat wy durch dyn
> sulvest apenbarynge von dyner herlicheit gheloven, even dat sulffte holden wy underscheiden
> van dynem sone und dem hilligen geiste, up dat yn der bekentnysse der waren und ewyghen
> godtheit de eghenschop yn den personen und enyccheit [!] yn dem wesen und de ghelicheit yn der
> majestat recht werde anghebetet, welke de engel laven, erwerdigen de ertzeengel, dartho
> Cherubin und Seraphin, de ane unterladt myt eyndrechtiger stemmen syngen:

*Notes on the Lippe Low German.*
- ***Sed in unius trinitate substantiae*** ("but in the Trinity of one substance") becomes "but
  in the **unity** of one peculiar being". The word "Trinity" is lost.
- ***Sine differentia discretionis*** ("without difference or separation") becomes "**that same
  we hold distinctly** of thy Son and the Holy Ghost". The negative is lost, and the clause
  seems to say the opposite of the Latin.
- **The angelic ending** follows the other Roman form: "the angels praise, the archangels
  worship, and Cherubim and Seraphim … sing without ceasing with one voice". Compare *Angeli
  atque Archangeli, Cherubim quoque ac Seraphim, qui non cessant clamare*.

**German (2): Dortmund (Low German).** **Dortmund, *Gottesdienstordnung*, 1554, "Van der
Hilligen Drevoldicheit"** (Sehling 21, p. 211):

<!-- doc 1446 -->
> De mit dynem eingebaren Söne unde dem hilligen Geiste bist ein Godt, ein Here, nicht yn einer
> personen enicheit, sunder ynn eines wesendes drevoldicheit. Wente dat wy van dyner herlicheit
> dorch dyn apenbarent gelöven, dat völe wy ock van dynem Söne unde van dem Hilligen Geiste,
> sunder jenich underscheides, voranderinge, Also dat ynn der bekenninge der warachtigen, ewigen
> Godtheit ein underscheit yn den personen, ein enicheit yn dem wesende unde doch gelickheit yn
> der herlichen angebedet werde. De dar de Engelen laven etc., als yn der gemenen Prefation.

[It is very meet … everlasting God:] Who with thine only-begotten Son and the Holy Ghost art one
God, one Lord; not in the oneness of a person, but in the trinity of one being. For what we
believe of thy glory through thy revealing, that we feel also of thy Son and of the Holy Ghost,
without any difference [or] change; so that in the confession of the true, everlasting Godhead a
distinction in the Persons, a unity in the being, and yet an equality in the glory be adored.
Which the Angels praise, etc., as in the common Preface.

*Note.* This is faithful. *Proprietas* becomes "a distinction", and *discretionis* becomes
"change".

### A.10 The Blessed Virgin (*Et te in … beatae Mariae*), and Müntzer's Advent rewording

**Witnesses:**
- **Dortmund 1554:** the Marian Preface itself, for the Purification, Annunciation, Visitation,
  Assumption and Nativity of Mary.
- **Müntzer 1524 (Advent; Radical Reformation), Erfurt 1525 (Trinity, also used in Advent) and
  Calenberg-Göttingen 1542 (Advent):** a reworded form, which turns the praise of Mary's feast
  into thanksgiving for the Incarnation.

No Latin text is printed in the corpus. The German renders the Missal's *Et te in [festivitate]
beatae Mariae semper Virginis collaudare, benedicere et praedicare. Quae et Unigenitum tuum
Sancti Spiritus obumbratione concepit: et virginitatis gloria permanente, lumen aeternum mundo
effudit, Iesum Christum Dominum nostrum.*

**German (1): Dortmund (Low German), the Marian feasts.** **Dortmund, *Gottesdienstordnung*,
1554, "Inn Marien Festen"** (Sehling 21, p. 211):

<!-- doc 1446 -->
> Unde dynem dage (der reyningen, der Bodtschop, der Heymsökinge edder des Berchganges, der
> hemmelfart, der Gebort etc.) Marien, der hilligen steden Junckfrouwen, mit fröliken herten
> thosamen laven, benedyen unde hochlick prysen, De dynen eingebaren Söne yn averschemminge des
> hilligen Geistes hefft entfangen unde beholdener eeren der junckfrouwschop desser werlt dat
> ewige licht geberet, Jhesum Christum, unsen Heren, Dorch welcken etc., yn der gemenen
> prefation.

[It is very meet … to give thanks unto thee,] and on thy day (of the Purification, of the
Annunciation, of the Visitation or Going over the Mountain, of the Assumption, of the Nativity,
etc.) of Mary, the holy, ever Virgin, with joyful hearts together to praise, bless and highly
extol; who conceived thine only-begotten Son by the overshadowing of the Holy Ghost, and, the
honour of her virginity remaining, brought forth to this world the everlasting light, Jesus
Christ our Lord; through whom, etc., in the common Preface.

*Notes on Dortmund's German.*
- **"Thy day … of Mary".** The Missal's "in the festival of blessed Mary" becomes "on **thy**
  day … of Mary". The feast is God's, and the Virgin is its occasion.
- **The Assumption is still listed** ("der hemmelfart", 15 August).
- *Effudit* ("poured forth") becomes "brought forth".

**German (2): Müntzer's rewording for Advent** (Radical Reformation). Müntzer's form is also in
Erfurt 1525 (2, p. 378) and Calenberg-Göttingen 1542 (6/2, p. 818). **Allstedt, Thomas Müntzer,
*Deutsch evangelisch Messe*, 1524, office of Advent** (Sehling 1, p. 500):

<!-- doc 51 -->
> Warlich, es ist billich und recht und ist heilsam, das wir dir, herr, o heiliger vater,
> almechtiger, ewiger got, allzeit und allenthalben danksagen. Dann du dein heilige menscheit
> von der junkfrauen Maria hast empfangen durch die umbschetigung des heilgen geistes, das sie
> mit unvorruckter keuscheit das ewige licht zur welt gebracht hat, Jesum Christum, unseren
> herren. Durch wilchen loben die engel dein herligkeit und ehr erbieten die engel, do du innen
> hirschest; es entsetzten sich die gewaltigen engel; dozu die himmel und der himmel krefte und
> die heiligen seraphin preisen dich on unterlass mit einmütiger freuden. Drumb bitten wir dich,
> o herr, das du woltest unsere stimmen mit in zu lassen, das wir dich mit warem bekentnis mügen
> loben one ende, sagende:

Verily it is meet and right and wholesome that we should at all times and in all places give
thanks unto thee, O Lord, holy Father, almighty, everlasting God. For thou hast received thy
holy manhood of the Virgin Mary by the overshadowing of the Holy Ghost, so that she with
unblemished chastity brought the everlasting light into the world, Jesus Christ our Lord:
through whom the angels praise thy glory, and the angels in whom thou reignest do thee honour;
the mighty angels tremble; and the heavens and the powers of the heavens and the holy Seraphim
praise thee without ceasing with one accord of joy. Therefore we pray thee, O Lord, that thou
wouldest admit our voices with them, that we may praise thee with true confession, without end
saying:

*Notes on Müntzer's rewording.*
- **Mary's feast is gone.** The clause "and on the festival of blessed Mary to praise, bless and
  proclaim thee" is struck out.
- **The subject changes.** It is no longer Mary who "conceived thine Only-begotten". It is God
  who "received thy holy manhood of the Virgin Mary". The Preface becomes a thanksgiving for the
  Incarnation, fit for Advent.
- **The common ending is translated**, with *dominationes* as "the angels in whom thou
  reignest".
- **Erfurt 1525** prints the same text in its Trinity office. Its Advent office takes the whole
  Preface from there, and its Passion office takes "the beginning together with the conclusion"
  (Sehling 2, pp. 379–380).

### A.11 The Apostles (*Et te, Domine, suppliciter exorare*)

**Witness:** Dortmund 1554 only. No Latin is printed in the corpus. The Low German renders the
Missal's *Et te, Domine, suppliciter exorare, ut gregem tuum, pastor aeterne, non deseras: sed
per beatos Apostolos tuos continua protectione custodias. Ut iisdem rectoribus gubernetur, quos
operis tui vicarios eidem contulisti praeesse pastores.* **Dortmund, *Gottesdienstordnung*,
1554, "Van den Apostolen"** (Sehling 21, p. 211):

<!-- doc 1446 -->
> Dy Here, demötlick tho bidden, dat du, O ewige Herde, dyne Schape nicht vorlatest, sunder
> dorch dyner hilligen Apostolen lere vor allem erdom ynn stedeliker höde bewarest, dat se dorch
> der sülven regenten lere geleidet werden, de du en dynes werckes, plegers an dyner stede ym
> worde vor tho syn tho Herden heffst gegeven, Derhalven mit den Engelen unde Ertzengelen etc.,
> baven, tho Wynachten.

[It is very meet … wholesome,] humbly to beseech thee, O Lord, that thou, O everlasting
Shepherd, forsake not thy sheep, but through the doctrine of thy holy Apostles keep them in
continual guard from all error; that they may be led by the doctrine of the same rulers, whom
thou hast given them for shepherds, stewards of thy work, to be over them in thy stead in the
word. Therefore with the Angels and Archangels, etc., above, at Christmas.

*Notes on Dortmund's German.*
- **"Through thy blessed Apostles" becomes "through the doctrine of thy holy Apostles … from all
  error".** The Apostles keep the flock by their teaching, not by their intercession.
- **"By the same rulers" becomes "by the doctrine of the same rulers"**, again teaching, not
  rule.
- ***Vicarios*** becomes "stewards … in thy stead **in the word**".

### A.12 Passiontide and Maundy Thursday: Grubenhagen's Isaiah 53 Preface (new German text)

**Witness:** Grubenhagen 1581. "So that the simple layman may be awakened more devoutly to the
contemplation of the sufferings and death of Christ", the order adds "a German preface taken
from the 53rd chapter of Isaiah". It is to be sung "on Maundy Thursday, or else at any time when
there are many communicants". It is a new composition with notes, built on the frame of the
German common Preface. **Grubenhagen, *Kirchenordnung*, 1581** (Sehling 6/2, p. 1074):

<!-- doc 2058 -->
> Warlich, es ist billich und recht, löblich und auch heilsam, das wir dir immer und ewiglich,
> Gott Vater, danksagen, das du uns deinen lieben Son geschenket hast, der mit seinem bittern
> leiden bezahlet hat, was Adam und wir verschuldet han, wie Esaias sagt: Fürwar, er trug unser
> krankheit und lud auf sich unser schmerzen. Er ist umb unser missethat willen verwundet und
> umb unser sünde willen so zuschlagen; die straffe ligt auf ihm, auf das wir friede hetten, und
> durch seine wunden sind wir geheilet. Wir gingen alle irr, gleich wie die schafe, die keinen
> hirten haben. Ein jeglicher sah auf seinen weg. Aber der Herr warf unser aller sünd auf ihn,
> ein untregliche last, darunter er blutigen schweis geschwitzet hat und am stam des kreuzes
> geschrieen hat: Mein Gott, mein Gott, warumb hastu mich verlassen?, auf das wir nicht ewig
> würden verlassen. Darumb wir dir mit den engeln und erzengeln, mit den thronen und den
> herschaften und mit allem himlischem heer den lobgesang deiner ehre singen, immer und ewig
> sagende

Verily it is meet and right, laudable and also wholesome, that we should give thanks unto thee,
God the Father, evermore and everlastingly, for that thou hast given us thy dear Son, who by his
bitter suffering hath paid what Adam and we had deserved; as Isaiah saith: Surely he hath borne
our griefs and carried our sorrows. He was wounded for our transgressions, he was bruised for
our iniquities; the chastisement is upon him, that we might have peace, and with his stripes we
are healed. All we like sheep have gone astray, as sheep that have no shepherd; we have turned
every one to his own way. But the Lord laid on him the sin of us all, an unbearable burden,
under which he sweat bloody sweat, and on the stem of the cross cried: My God, my God, why hast
thou forsaken me? that we might not be forsaken for ever. Therefore with the angels and
archangels, with the thrones and the dominions, and with all the heavenly host, we sing unto
thee the hymn of thine honour, evermore and ever saying:

### A.13 Michaelmas: Lippe's German Preface for the villages (new German text)

**Witness:** Lippe 1571. For the towns, Lippe sets the Latin common Preface "In die Michaelis"
(§A.1). For the villages it gives a German Preface of its own. This keeps the opening of the
common Preface but replaces the choirs of angels with the forgiveness of sins. On the feast of
St Michael and All Angels, the angels are named only in the Sanctus. **Lippe, *Kirchenordnung*,
1571, "Am tage Michaelis auff den Dörffern"** (Sehling 21, p. 411):

<!-- doc 1462 -->
> Warlich, es ist billich und recht und ist heilsam, das wir dich, Herre, O Heiliger Vater,
> Allmechtiger, Ewiger Gott, allzeit und allenthalben dancksagen durch Christum unsern Herren.
> Umb welches willen du uns verschonest, vergibst uns unsere sünden und verheischest die Ewige
> wolfart. Des wir danckbarlich singen einen Lobgesang deiner Herrligkeit one ende sagende:
> Sanctus.

Verily it is meet and right and wholesome that we should at all times and in all places give
thanks unto thee, O Lord, holy Father, almighty, everlasting God, through Christ our Lord: for
whose sake thou sparest us, forgivest us our sins, and promisest everlasting welfare. Wherefore
we thankfully sing a song of praise of thy glory, without end saying: Holy.

### A.14 Christmas in Kurland: the Easter Preface with the Nativity prefixed (new German text)

**Witness:** Kurland 1570. "On the high feasts, for variation (as is done at the princely
court)", the minister may sing "these prefaces noted below, in place of the *quotidiana*". The
**Christmas** Preface is not the Roman Christmas text. It is the German Easter Preface, with the
Virgin Birth set in front of the Lamb. The minister and choir sing the dialogue in alternation.
The Easter Preface follows (§A.6, German 2), then a Pentecost Preface, which is the Easter text
again with the Ascension and the sending of the Spirit added (§A.15). **Kurland, *Kurländische
Kirchenordnung*, 1570, "Auf Nativitatis"** (Sehling 5, pp. 89–90):

<!-- doc 1907 -->
> Der diener: Der herre sei mit euch. Das chor: Und mit deinem geist. Der diener: Erhebet eure
> herzen. Das chor: Wir heben sie zum herren. Der diener: Last uns dank sagen gotte, unserem
> herren. Das chor: Es ist billich und gerecht. Der diener: Warlich, es ist billich und gerecht,
> Da zugleich ganz und heilsam, Das wir dir alzeit Und an allen enden dank sagen, Und sonderlich
> zu dieser zeit höher preisen, Dieweil uns ein jungfreulein zart Den sohne gottes geboren hat,
> Welch ist das wahre lam gottes, Das da weggenommen hat der welt sünde, Der durch sein sterben
> Den tod uberwunden hat, Und durch sein auferstehung Das leben her wider gebracht, Darum wir
> mit allen englen Und mit der ganzen himlischen herscharen Singen einen lobgesang deines
> preises Ohne ende sagende.

The minister: The Lord be with you. The choir: And with thy spirit. The minister: Lift up your
hearts. The choir: We lift them up unto the Lord. The minister: Let us give thanks unto God our
Lord. The choir: It is meet and right. The minister: Verily it is meet and right, and withal
wholly wholesome, that we should at all times and in all places give thanks unto thee, and
especially at this time praise thee more highly, because a tender little maiden hath borne unto
us the Son of God, who is the true Lamb of God that hath taken away the sin of the world; who by
his dying hath overcome death, and by his resurrection hath brought life again. Therefore with
all the angels and with all the heavenly hosts we sing a song of praise of thy glory, without
end saying:

### A.15 Pentecost in Kurland: the Easter Preface with the Ascension and Pentecost added (new German text)

**Witness:** Kurland 1570. This is the Easter Preface of §A.6 (German 2), extended. Before the
Sanctus it adds that Christ, "when he was taken visibly into heaven", sent down the Comforter.
**Kurland, *Kurländische Kirchenordnung*, 1570, "Auf pfingsten"** (Sehling 5, p. 90):

<!-- doc 1907 -->
> Warlich, es ist billich und gerecht, dazu gleich und ganz heilsam, das wir dir alzeit und an
> allen enden danksagen, und sonderlich zu dieser zeit höher preisen, dieweil Christus, unser
> osterlam für uns am creuze ist geopfert, welch ist das ware lam gottes, das dar weggenommen
> hat der welt sünde, der durch sein sterben den tod uberwunden hat und durch sein auferstehung
> das leben her widergebracht, und als er sichtlich zu himel genommen ist, hat er den tröster,
> den heiligen geist, seinen gleubigen hernieder gesant, darum wir mit allen engeln und mit der
> ganzen himlischen herscharen singen einen lobgesang deines preises ohne ende sagende.

Verily it is meet and right, and withal wholly wholesome, that we should at all times and in all
places give thanks unto thee, and especially at this time praise thee more highly, because
Christ our Passover lamb is sacrificed for us upon the cross, who is the true Lamb of God that
hath taken away the sin of the world; who by his dying hath overcome death and by his
resurrection hath brought life again; and when he was taken up visibly into heaven, he sent down
the Comforter, the Holy Ghost, upon his faithful. Therefore with all the angels and with all the
heavenly hosts we sing a song of praise of thy glory, without end saying:

### A.16 Summary: which Prefaces each order has

| Preface | Latin in the corpus | German or Low German in the corpus |
|---|---|---|
| Common (*Quotidiana*) | Lüneburg 1564, Wolfenbüttel 1569, Verden 1606; for Michaelmas: Hoya 1581, Osnabrück 1618, Lippe 1571; cut short: Luther 1523, Nürnberg 1524 | Dortmund 1554; Kantz, Worms (mediating), Volprecht, Döber, Bremen (see the Canon guide) |
| Christmas | Lüneburg, Wolfenbüttel, Grubenhagen, Hoya, Verden, Osnabrück, Lippe 1571 | Müntzer 1524 (Radical Reformation), Erfurt 1525, Calenberg 1542, Lippe 1571; Strasbourg 1524 (mediating); Dortmund 1554; Kurland 1570 (new text, §A.14) |
| Epiphany | Lüneburg, Wolfenbüttel, Verden | Strasbourg 1524 (mediating); Dortmund 1554 |
| Lent | — | Dortmund 1554 |
| Passion and Cross | — | Müntzer (Radical Reformation), Erfurt, Calenberg; Strasbourg (Schwarz) 1524 (mediating); Dortmund 1554; Grubenhagen 1581 (new Isaiah 53 text, §A.12) |
| Easter | Lüneburg, Wolfenbüttel, Grubenhagen, Hoya, Verden, Osnabrück, Lippe 1571 | Müntzer (Radical Reformation), Erfurt, Calenberg, Lippe 1571, Kiel; Kurland 1570; Strasbourg 1524 (mediating); Dortmund 1554; Calenberg's Sunday form |
| Ascension | Lüneburg, Wolfenbüttel, Hoya, Verden | Strasbourg 1524 (mediating); Calenberg 1542; Dortmund 1554 |
| Pentecost | Lüneburg, Wolfenbüttel, Grubenhagen, Hoya, Verden, Osnabrück, Lippe 1571 | Müntzer (Radical Reformation), Erfurt, Calenberg, Lippe 1571; Strasbourg 1524 (mediating); Dortmund 1554; Kurland 1570 (§A.15) |
| Trinity | Lüneburg, Wolfenbüttel, Grubenhagen, Hoya, Verden | Lippe 1525; Dortmund 1554 |
| Blessed Virgin | — | Dortmund 1554; Müntzer (Radical Reformation), Erfurt, Calenberg (reworded for Advent and Trinity) |
| Apostles | — | Dortmund 1554 |
| Michaelmas (new German text) | (common Preface) | Lippe 1571 (§A.13) |
