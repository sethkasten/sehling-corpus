"""Family H -- Bugenhagen's pulpit exhortation after the sermon (Low German):
Creed, open confession ("Got sy gnedich my arme sunder"), then biddings for
the magistrates, the preachers, peace and all in need, closed with the Our
Father.  Braunschweig 1528 is the model for Hamburg 1529, Lübeck 1531 and
other Bugenhagen orders."""
from gp import P

W = []

W.append(dict(
    key='braunschweig_1528', doc=1983, year=1528,
    order='Braunschweig, Der erbarn stadt Brunswig christlike ordeninge (Bugenhagen)',
    territory='Braunschweig (city)',
    citation='Sehling 6/1, I/1, p. 443',
    family='H. Bugenhagen pulpit exhortation', form='exhortation: Creed + confession + biddings + Lord’s Prayer',
    tradition='Lutheran',
    position='From the pulpit after the sermon (“Exhortatio edder vormaninge up dem predickstole na der predige”); the exhortation to communicants before the altar follows.',
    heading='Exhortatio edder vormaninge up dem predickstole na der predige',
    heading_en='Exhortation or admonition from the pulpit after the sermon',
    notes='Low German. Special common needs (corn, hops, fruits, weather, murrain, pestilence) may be brought in.',
    petitions=[
        P('creed', sub='exhortation',
          r='Exhortatio edder vormaninge up dem predickstole na der predige:', r_en='Exhortation or admonition from the pulpit after the sermon:',
          b='Leven frunde in Christo, spreket mit my den loven. Ick love in Got den Vader, almechtigen etc.',
          b_en='Dear friends in Christ, say with me the Creed. I believe in God the Father Almighty, etc.'),
        P('confession',
          b='Spreket de bicht mit my unde bekennet Gade jue sunde, dat uns Got gnedich sy.',
          b_en='Say the confession with me, and confess your sins unto God, that God may be gracious unto us.',
          p='Got sy gnedich my arme sunder. Id feylet my an deme loven, dat ick Got mynen Heren nicht van ganzeme herten leve, my nicht ganzlick up em vorlate in anvechtingen unde aller nöt lives unde der selen. Ick scholde alleyne Got fruchten unde in allen dingen vor ogene hebben, nu fruchte ick my vor de lüde, de my umme der gerechticheit willen konen bose dohn. Ick fruchte vor myn gut, ere, fruntschop unde lyff to vorlesende. Ick sorge vor de neringe unchristlick unde söke in allen dingen dat myne unde nicht, wat Gades is. Ock stelle ick nicht ganz myne salicheit in Jesum Christum, synen eyngebarn Sone, vor uns gegeven. Id feylet my ock an der leve, dat ick mynen negesten nicht leve alse my sulvest, sonder handele wedder en mit bosen vordechtnissen, mit achterkosen, mit worden, mit werken unde kan nicht eyn wort van em wedder mick liden. Ick swige denne mehr unde kan em nicht van herten vorgeven unde bun doch sulcks schuldich to dohn. Besundergen hebbe ick eyne beswerde conscientie in disser anvechtinge: N., in disser sunden: N. (Eyn jewelick klage Gade syne heymelike beswerlike sunde tor beteringe). Darumme, almechtige Got, leve Vader, vorgiff my alle myne sunde unde erlüchte myn herte mit dyner warheit, dat ick dick mach holden vor mynen gnedigen Vader unde mynen negesten vor mynen broder ane alle ergernisse nach dyneme worde dorch unsen Heren Jesum Christum. (spreket:) Amen. Jesus Christus is unse salicheit ewichlick. (spreket:) Amen.',
          p_en='God be merciful to me a poor sinner. I fail in faith, in that I love not God my Lord with my whole heart, nor trust wholly in him in temptations and in all need of body and soul. I ought to fear God alone and have him before mine eyes in all things; but now I fear the people that can do me evil for righteousness’ sake. I fear to lose my goods, honour, friendship and life. I care for my living in unchristian wise, and seek in all things mine own, and not the things that are God’s. Neither do I set my salvation wholly in Jesus Christ, his only-begotten Son, given for us. I fail also in love, in that I love not my neighbour as myself, but deal against him with evil suspicions, with backbiting, with words, with works, and can bear no word from him against me. I keep silence then the more, and cannot forgive him from the heart, and yet am bound to do so. Especially I have a burdened conscience in this temptation: N., in this sin: N. (Let every one bewail unto God his secret, grievous sin, unto amendment.) Therefore, almighty God, dear Father, forgive me all my sins, and enlighten my heart with thy truth, that I may hold thee for my gracious Father, and my neighbour for my brother, without all offence, according to thy word; through our Lord Jesus Christ. (Say:) Amen. Jesus Christ is our salvation for ever. (Say:) Amen.'),
        P('civil-authority',
          b='So lat uns nu vlitich bidden vor keyserlike majestat, vor konnige, vor heren, fursten, furstenrede unde stadrede, eddele lüde, borgermeystere unde richtere unde allen, den dat werlike swert bevalen is, besundergen vor unsen landesfursten unde vor den radt disser stadt, dat Got mit syner gnaden stedes by en sy unde geve en, dat se unstrafflick mogen regeren in den werliken dingen, de en bevalen synt, dat wy under en mögen eyn rowelick unde stille leven vohren mit aller gotsalicheit unde redelicheit.',
          b_en='Let us now pray diligently for the Imperial Majesty, for kings, for lords, princes, princes’ counsellors and town councillors, noblemen, burgomasters and judges, and all to whom the temporal sword is committed, especially for our prince of the land and for the council of this city, that God may be always with them with his grace, and grant them that they may rule unblameably in the temporal things that are committed unto them, that we under them may lead a quiet and still life in all godliness and honesty.',
          note='“mistrafflick” (print) read “unstrafflick”.'),
        P('ministers', sub='word',
          b='Biddet ock vor de prestere, de uns armen schapen weyden mit deme wörde unde evangelio Christi, dat se uns mit vulstendigeme herten dat reyne wort Gades vordregen to unser beteringe unde werden behödet vor allen erdöm unde gesterket to alleme besten wedder den düvel unde alle weddersagere, dat jo dat evangelion Christi by uns reyne blive.',
          b_en='Pray ye also for the priests that feed us poor sheep with the word and Gospel of Christ, that they may set forth unto us the pure word of God with a steadfast heart to our amendment, and be kept from all error and strengthened unto all good against the devil and all gainsayers, that the Gospel of Christ may ever remain pure among us.'),
        P('peace', sub='afflicted; childbirth; enemies; conclusion',
          b='Biddet ock umme eynen tidliken frede, vor kranke, swake, elende, anvechtede lüde, vor swangere frauen, vor unse vyende, vor alle nöt lives unde der selen. Amen. Lattet uns bidden den eynen vor den anderen, dat wy alle salich werden. Amen.',
          b_en='Pray ye also for temporal peace; for the sick, the weak, the wretched and tempted folk; for women with child; for our enemies; for all need of body and soul. Amen. Let us pray one for another, that we may all be saved. Amen.'),
        P('lords-prayer', b='Spreket eyn Vader unse etc.', b_en='Say an Our Father, etc.'),
        P('special', sub='fruits-of-earth; calamities',
          r='So etlike sunderge gemeyne nöde vohrvallen, alse to bidden vor dat körne, hoppen, früchte, vor eyn tidlick weder, wedder böse tucht unde pestilentie etc., dat kan me wol mit inbringen.',
          r_en='If any special common needs befall, as to pray for the corn, hops, fruits, for seasonable weather, against evil murrain and pestilence, etc., that may well be brought in therewith.',
          note='“tucht” (sic; Lietzmann: “sucht”).'),
    ]))

W.append(dict(
    key='hamburg_1529', doc=1960, year=1529,
    order='Hamburg, Kirchenordnung (Bugenhagen)',
    territory='Hamburg (city)',
    citation='Sehling 5, Hamburg mit Landgebiet, pp. 530–531',
    family='H. Bugenhagen pulpit exhortation', form='exhortation: Creed + confession + biddings + Lord’s Prayer',
    tradition='Lutheran',
    position='From the pulpit after the sermon; the exhortation to communicants before the altar follows.',
    heading='Exhortatio edder vormaninge up dem predickstole na der predige',
    heading_en='Exhortation or admonition from the pulpit after the sermon',
    notes='Verbatim from Braunschweig 1528, in Hamburg spelling (“lyff” omitted in the list of things feared; “ganz” omitted before “myne salicheit”).',
    petitions=[
        P('creed', sub='exhortation', tr_from=('braunschweig_1528', 1),
          r='Exhortatio edder vormaninge up dem predickstole na der predige.',
          b='Leven frunde in Christo, spreket mit mi den loven: Ick love in den vader almechtigen etc.',
          tr_sub=[('I believe in God the Father Almighty', 'I believe in the Father Almighty')]),
        P('confession', tr_from=('braunschweig_1528', 2),
          b='Spreket ock de bicht mit mi und bekennet gade juwe sunde, dat uns god gnedich si.',
          p='Godt si gnedich mi arme sundere, id feilet mi am loven, dat ick godt minen heren nicht van ganzem herten leve, mi nicht genslick up ene vorlate, in anvechtingen und aller nodt lives und der selen. Ick scholde allene godt fruchten und in allen dingen vor ogene hebben, nu fruchte ick mi vor de lude, de mi umme der gerechticheit willen konen bose doen. Ick fruchte vor min gudt, ehre, fruntschup to vorlesende. Ick sorge vor de neringe unchristlick und soke in allen dingen dat mine, und nicht wat gades is. Ock stelle ick nicht mine salicheit in Jesum Christum sinen eingebaren sone vor uns gegeven. Id feilet mi ock an der leve, dat ick minen negesten nicht leve alse mi sulvest, sunder handele wedder en mit bosen vordechtnissen, mit achter kosen, mit worden, mit werken, und kan nicht ein wordt van em wedder mi liden. Ick schwige denne mer, und kan em nicht van herten vorgeven, und bin doch sulckes schuldich to donde. Besundergen hebbe ick eine beswerede conscientie in dusser anvechtinge N., in dusser sunde N. (ein juwelick klage gade sine hemelike beswerlike sunde tor beteringe). Darumme, almechtige godt, leve vader, vorgiff mi alle mine sunde und erluchte min herte mit diner warheit, dat ick di mach holden vor minen gnedigen vader und minen negesten vor minen broder, ane alle ergernisse, nach dinem worde, dorch unsen heren Jesum Christum, (spreket) Amen. Jesus Christus ist unse salicheit ewichlick, (spreket) Amen.',
          tr_sub=[('Say the confession with me', 'Say also the confession with me'), ('to lose my goods, honour, friendship and life', 'to lose my goods, honour, friendship'),
                  ('Neither do I set my salvation wholly in Jesus Christ', 'Neither do I set my salvation in Jesus Christ')]),
        P('civil-authority', tr_from=('braunschweig_1528', 3),
          b='So lat uns nu vlitich bidden vor keiserlike majestat, vor koninge, vor heren, fursten, fursten rede und stad rede, eddel lude, borgermeister und richter, und allen den dat wertlicke swerdt bevalen is, besundergen vor unsen landesfursten und vor den radt dusser stadt, dat godt mit siner gnade stedes bi en si und geve en, dat se unstraflick mogen regeren in den wertliken dingen, de en bevalen sint, dat wi under en mogen ein rouwelick und stille levent vorent mit aller godsalicheit und redelicheit.'),
        P('ministers', sub='word', tr_from=('braunschweig_1528', 4),
          b='Biddet ock vor de prestere, de uns armen schape weiden mit dem worde und evangelio Christi, dat se uns mit vulstendigen herten dat reine wort gades vordregen to unser beteringe, und werden behodet vor allem erdom, und gesterket to allem besten wedder den duvel und alle weddersagere, dat jo dat evangelion Christi bi uns reine blive.'),
        P('peace', sub='afflicted; childbirth; enemies; conclusion', tr_from=('braunschweig_1528', 5),
          b='Biddet ock umme einen tidliken frede, vor kranke, swake, elende, anvechtede lude, vor swanger frouwen, vor unse viande, vor alle nod lives und der selen, amen. Latet uns bidden de eine vor den anderen, dat wi alle salich werden, amen.'),
        P('lords-prayer', tr_from=('braunschweig_1528', 6), b='Spreket ein vader unse etc.'),
        P('special', sub='fruits-of-earth; calamities', tr_from=('braunschweig_1528', 7),
          r='So etlike sunderge gemene node vorvallen, alse to biddende vor dat korne, hoppen, fruchte etc. vor ein tidtlick wedder, jegen bose sucht edder pestilentie etc., de kanme wol mit inbringen.',
          tr_sub=[('against evil murrain and pestilence', 'against evil sickness or pestilence')]),
    ]))

W.append(dict(
    key='osnabrueck_1543', doc=2096, year=1543,
    order='Stift Osnabrück, Kirchenordnung (Hermann Bonnus): Ordenunge der evangelischen missen',
    territory='Prince-Bishopric (Stift) and city of Osnabrück',
    citation='Sehling 7/1, III/Stift Osnabrück, pp. 224–225',
    family='H. Bugenhagen pulpit exhortation', form='prescription of contents (indirect speech)',
    tradition='Lutheran',
    position='In the Mass after the exposition of the Gospel from the pulpit and the recitation of the catechism: an exhortation to prayer, then “Verleih uns Frieden gnädiglich” is sung; after the sermon the Credo, Preface and Sanctus follow.',
    heading='Ordenunge der evangelischen missen, de to Osenbrugge in den kerspelskercken geholden werd',
    heading_en='Order of the evangelical Mass that is held at Osnabrück in the parish churches',
    notes='Low German. The corresponding chapter of the Osnabrück city order of 1543 (Sehling 7/1, p. 258) is almost word for word the same. Sehling compares Tecklenburg 1543 and Minden 1530.',
    petitions=[
        P('word', sub='exhortation',
          b='Nach der uhtlegginge des evangelii schal de pastor de worde des catechismi affseggen umb des gemeinen volkes willen und darnach vermanen to bidden, ersten vor de sake des hilligen evangelii,',
          b_en='After the exposition of the Gospel the pastor shall say over the words of the catechism for the sake of the common people, and thereafter exhort them to pray: first, for the cause of the holy Gospel;'),
        P('civil-authority', sub='peace',
          b='tom andern vor de weltliche overicheit und gemeinen frede, sonderlich aver vor unsen gnadigen forsten und herr des landes, vor dat werdige capittel und einen ehrsamen rat der stadt,',
          b_en='secondly, for the temporal magistrates and common peace, but especially for our gracious prince and lord of the land, for the worthy chapter and an honourable council of the city;'),
        P('congregation', sub='special',
          b='tom drudden vor de ganzen gemeine und vor alle andere not lives und der sehlen, dar men des vor begeren iß und Gade bekant. Darnach sall werden gesungen: Verlehne uns frede gnädiglich.',
          b_en='thirdly, for the whole congregation and for all other need of body and soul, wherefor it is desired and is known to God. Thereafter shall be sung: Grant us peace graciously.'),
    ]))
