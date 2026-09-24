"""Other Lutheran general prayers: biddings addressed to the people (the
"Vermahnung zum Gebet" type, closing with the Our Father) and continuous
prayers that do not descend from the Brenz or Württemberg forms."""
from gp import P

W = []

# ---------------------------------------------------------------------------
W.append(dict(
    key='hanau_lichtenberg_1573', doc=1364, year=1573,
    order='Hanau-Lichtenberg, Kirchenordnung (Graf Philipp IV.)',
    territory='County of Hanau-Lichtenberg (Alsace)',
    citation='Sehling 20/2, Hanau-Lichtenberg Nr. 6, pp. 52–53',
    family='C. Bidding exhortation (Strasbourg type)', form='bidding exhortation + Lord’s Prayer',
    tradition='Lutheran',
    position='After the sermon; then a psalm is sung by school and congregation, followed by a collect and the blessing. The pastor is to refer to the sermon just preached and to present needs (war, plague, dearth) in the common prayer.',
    heading='Nach der Predig geschehe das gemein Gebet auff folgende weiß',
    heading_en='After the sermon let the common prayer be made on this wise',
    notes='The Württemberg 1553 collects printed later in the order (XII. Collecten oder Gebet, pp. 72–78, without their biddings) are a collect bank and are not entered here.',
    petitions=[
        P('exhortation',
          r='Nach der Predig geschehe das gemein Gebet auff folgende weiß:',
          r_en='After the sermon let the common prayer be made on this wise:',
          b='Lieben freund, Dieweil wir beyeinander versamlet sein und Gottes wort gehöret haben, so wöllen wir alle not der gantzen Christenheit unserm Herrgott fürtragen, ihne bitten, er wöll uns gnedig und barmhertzig sein, alles geben, was uns nutz und not ist, zur leibes notturfft und zur seelen seligkeit:',
          b_en='Dear friends, forasmuch as we are gathered together and have heard God’s word, we will lay all the need of the whole of Christendom before our Lord God, and pray him that he would be gracious and merciful unto us, and give all that is profitable and needful for us, for the necessity of the body and for the salvation of the soul:'),
        P('word', sub='persecuted; errant; church',
          b='Am ersten so bittet für das Geistlich, das unser lieber Herrgott uns sein heiligs wort wölle lassen predigen und gnad verleihen, das wir solches gerne hören, mit dem hertzen glauben und unser leben darnach richten, auch alle die jenigen, so von solchs Worts wegen in jamer, elend und widerwertigkeit stecken, trösten, stercken und auß allem jamer und elend erretten. Er wölle auch alle, so noch in finsternuß, irrthumb und abgötterey stecken, gnediglich durch sein Wort und Heiligen Geist erleuchten und zu erkantnuß der warheit bringen, auff daß sie mit uns und wir mit ihnen mögen selig werden.',
          b_en='First, pray ye for the spiritual estate: that our dear Lord God would let his holy word be preached unto us, and vouchsafe grace that we may gladly hear the same, believe it with the heart, and order our life thereafter; and that he would comfort, strengthen, and deliver out of all misery and woe all those that for the sake of this Word are in misery, woe and adversity. That he would also graciously enlighten by his Word and Holy Spirit all that are yet in darkness, error and idolatry, and bring them to the knowledge of the truth, that they with us and we with them may be saved.'),
        P('civil-authority', sub='peace',
          b='Zum andern bittet für das Weltlich Regiment: Erstlich für das Haupt, die Römische Kayserliche Majestat, unsern aller gnedigsten Herren, Darnach für die Glieder, alß Churfürsten, Fürsten und Herren der gantzen Christenheit, In sonderheit aber für unsere gnedige Herren, Frawe und Frewlein von Hanaw, für irer Gnaden Räthe, Amptleut, Diener und die gantze Herrschafft, für ein ersam Gericht und Gemeine alhie, auch die umbligende Nachpaurschafft. Der Allmechtige Gott verleihe der Oberkeit seinen Heiligen Geist und weißheit, das sie Christlich und wol regieren, die Unterthanen in gemeinem friden erhalten und bewaren.',
          b_en='Secondly, pray ye for the temporal government: first for the head, his Roman Imperial Majesty, our most gracious lord; then for the members, as the Electors, princes and lords of all Christendom; but especially for our gracious lords, lady and damsels of Hanau, for their Graces’ counsellors, officers, servants and the whole lordship, for a worshipful court and commune here, and also the neighbourhood round about. Almighty God vouchsafe unto the magistrates his Holy Spirit and wisdom, that they may rule in Christian wise and well, and keep and preserve the subjects in common peace.'),
        P('estates', sub='marriage',
          b='Letzlich bittet auch für den Ehelichen stand, der Allmechtige Gott verleihe allen Eheleuten seinen Heiligen Geist, das sie Christlich, fridlich und eintrechtiglich beieinander leben, ihre Kinder und Gesind zu Gottes forcht, auch ehr und tugent mögen aufferziehen.',
          b_en='Lastly, pray ye also for the estate of matrimony: Almighty God vouchsafe unto all married folk his Holy Spirit, that they may live together in Christian wise, peaceably and in concord, and may bring up their children and household in the fear of God, and also in honour and virtue.'),
        P('fruits-of-earth',
          b='Bittet für die frucht des Feldes, umb ein seliges Wetter und umb alles, so uns von nöten ist.',
          b_en='Pray ye for the fruit of the field, for seasonable weather, and for all that is needful unto us.'),
        P('afflicted', sub='childbirth',
          b='Kinder und Krancken wölle unser Herrgott pflegen und warten, Schwangern und Seugerin fröliche frucht und gedeien geben, die gefangnen loß und ledig machen.',
          b_en='May our Lord God tend and keep children and the sick, give unto women with child and them that give suck joyful fruit and increase, and loose and set free the captives.'),
        P('special',
          b='Und ein jeglicher bedenck sein eigene not und kom mit ir für Gott, den himlischen Vater, und zweiffel nicht, er werde uns gnediglich durch Christum erhören. Und sprecht von gantzem hertzen also:',
          b_en='And let every man consider his own need and come with it before God, the heavenly Father, and doubt not that he will graciously hear us through Christ. And say with your whole heart thus:'),
        P('lords-prayer',
          p='Unser Vater, der du bist im Himel, Geheiliget werde dein Nam. Zukom dein Reich. Dein will geschehe auff Erden wie im Himel. Unser täglich Brot gib uns heut. Und vergib uns unser Schuld, alß wir vergeben unseren Schuldigern. Füre uns nit in versuchung, Sondern erlöse uns von dem bösen. Dann dein ist das Reich und die Krafft und die Herrligkeit von ewigkeit zu ewigkeit, Amen.',
          p_en='Our Father, which art in heaven, Hallowed be thy name. Thy kingdom come. Thy will be done in earth, as it is in heaven. Give us this day our daily bread. And forgive us our debts, as we forgive our debtors. And lead us not into temptation, but deliver us from evil: For thine is the kingdom, and the power, and the glory, from everlasting to everlasting. Amen.',
          note='With the doxology (Strasbourg use).'),
    ]))
