## Brezposelnost in Prosta Delovna Mesta v Sloveniji (2008-2024)

### 1. Opis problema
Raziskava analizira ključne trende na trgu dela v Sloveniji v obdobju 2008-2024,
ki zajema dve večji gospodarski krizi: finančno krizo (2008-2013) in pandemijo COVID-19 (2020-2022).<br/>
Glavni cilji so bili:
1. Analizirati razlike v brezposelnosti
    • Med spoloma
    • Med regijama (vhodna in zahodna Slovenija)
2. Proučiti povezavo med brezposelnostjo in razpoložljivostjo delovnih mest

### 2. Podatki
Podatkovna osnova raziskave temelji na četrtletnih podatkih Statističnega urada Republike Slovenije (SURS), ki zagotavljajo visoko kakovost, transparentnost in primerljivost na nacionalni in mednarodni ravni. Podatki so v formatu PC-Axis (PC-AXIS), ki omogoča strukturirano hranjenje in analizo statističnih in besedilnih podatkov. Za vsak podatkovni nabor so na voljo tudi metapodatki in metodološka pojasnila, kar omogoča natančno razumevanje izvorov in omejitev podatkov.

Glavni podatkovni nabori

1. brezposelneCetrtletno.PX :  
    • Ključne spremenljivke: regija (vzhodna/zahodna Slovenija), spol (moški/ženske), število brezposelnih (v 1000), delež brezposelnosti v %, četrtletje.
    • Opis: Podatki zajemajo obdobje od 2008Q1 do 2024Q4. Vključujejo tudi podatke o trajanju brezposelnosti in omogočajo analizo razlik med regijami in spoloma skozi čas.

2. delovnaMestaCetrtletno.PX :<br/>
    • Ključne spremenljivke: število prostih delovnih mest, število zasedenih delovnih mest, stopnja prostih delovnih mest (%) po SKD dejavnostih (od B do S),             četrtletje.
    • Opis: Podatki pokrivajo vse glavne sektorje gospodarstva (npr. predelovalne dejavnosti, gradbeništvo, trgovina, gostinstvo, zdravstvo) in omogočajo analizo                povpraševanja po delovni sili po sektorjih.
3. vsi.PX :<br/>
    • Ključne spremenljivke: delovno aktivni (v 1000), četrtletje.
    • Opis: Podatki zajemajo skupno število delovno aktivnih oseb v Sloveniji, kar omogoča analizo trga dela in primerjavo s številom brezposelnih in zasedenih delovnih mest.
   

<br> celotna koda je napisana v [Jupyter Notebook](https://github.com/KekecD/PR255/blob/main/projekt.ipynb)
### 3. Splošni trendi brezposelnosti in napovedi v kriznih obdobjih

Analiza splošnih trendov brezposelnosti v Sloveniji med letoma 2008 in 2024 jasno izpostavlja dve ključni krizni obdobji, kar je razvidno iz spodnjih grafov.

1. Finančna kriza (2008-2013)
V obdobju finančne krize je stopnja brezposelnosti vztrajno naraščala in dosegla vrhunec v letih 2013–2014, ko je dosegla 11,1 % v letu 2013 in 10,8 % v letu 2014. Sledilo je počasno okrevanje, ki je trajalo vse do leta 2019. Ta trend je lepo prikazan na grafu, kjer je obdobje krize posebej označeno, krivulja pa jasno izpostavlja dolgotrajno visoko brezposelnost in počasno zniževanje po letu 2014

2. Pandemija COVID-19 (2020-2022)
Pandemija je povzročila krajši, a izrazito manjši šok na trgu dela v primerjavi s finančno krizo. Najvišja stopnja brezposelnosti je bila dosežena leta 2021 (5,6 %), okrevanje pa je bilo bistveno hitrejše, saj se je stopnja brezposelnosti že do leta 2024 vrnila na predkrizno raven

3. Napovedi in primerjava z dejanskimi podatki:
Napovedne modele smo trenirali na širši množici podatkov, vključno s povprečno plačo, inflacijo, rastjo BDP, aktivnim prebivalstvom in prostimi delovnimi mesti. V obdobjih stabilnosti so bile napovedi precej natančne, medtem ko so v kriznih obdobjih, zlasti ob nenadnih šokih, modeli pogosto precenjevali dejansko stopnjo brezposelnosti. To potrjuje, da so napovedni modeli uporabni za oceno trendov, a njihova natančnost upade v času izjemnih gospodarskih sprememb, kot sta bila finančna kriza ali pandemija COVID-19

![Graf brezposelnosti v Sloveniji](slike%2FBrezposelnostSkupaj.png) graf 1


![Napoved brezposelnosti](slike%2FForecast20082013.png) graf 2

![Napoved brezposelnosti](slike%2FForecast20132019.png) graf 3

### 4. Razlike med spoloma (Slika 2) in trendi skozi krize
Analiza stopnje brezposelnosti po spolu v Sloveniji med letoma 2008 in 2024 razkriva izrazite razlike, ki so se še posebej pokazale v kriznih obdobjih.<br/>

1. Finančna kriza (2008–2013):
V času finančne krize so bile ženske nesorazmerno bolj prizadete. Leta 2013 je stopnja brezposelnosti pri ženskah dosegla vrh pri 11,7 %, pri moških pa 10,7 %, kar pomeni 1 odstotno točko razlike v škodo žensk. Ta razlika je bila posledica večje izpostavljenosti žensk v sektorjih, ki so jih kriza najmočneje prizadela, ter večje zastopanosti v negotovih oblikah zaposlitve.

2. Obdobje po krizi in pandemija COVID-19 (2020–2022):
Po letu 2014 se je brezposelnost postopno zmanjševala pri obeh spolih, vendar so ženske še naprej imele nekoliko višje stopnje brezposelnosti. Med pandemijo COVID-19 je razlika še narasla – v prvem četrtletju 2021 je bila brezposelnost pri ženskah 6,9 %, pri moških pa 4,6 %, kar je 2,3 odstotne točke razlike v škodo žensk. Razlogi za to so bili predvsem v večji zastopanosti žensk v storitvenih dejavnostih in na delovnih mestih, ki so bila v času pandemije bolj ogrožena.

3. Najnovejši trendi:
Po letu 2021 se razlike med spoloma nekoliko zmanjšujejo, v posameznih četrtletjih pa so moški tudi presegli ženske v stopnji brezposelnosti, kar kaže na spreminjajočo se strukturo trga dela in prilagajanje gospodarstva novim razmeram. Do konca leta 2024 je stopnja brezposelnosti pri ženskah padla na okoli 4 %, kar je najnižja vrednost v zadnjem desetletju

![Graf brezposelnosti za spola v Sloveniji](slike%2FBrezposelniSpoli.png)
    
### 5. Regionalne razlike (Slika 3) – trendi brezposelnosti po regijah
Izrazite in trajne razlike v brezposelnosti med vzhodno in zahodno Slovenijo v obdobju 2008–2024 so bile jasno vidne. V vseh obdobjih, še posebej med gospodarskimi krizami, je bila stopnja brezposelnosti v vzhodni Sloveniji bistveno višja kot v zahodni.

1. Finančna kriza (2008–2013):
V času finančne krize se je razlika med regijama še povečala. Največja razlika je bila dosežena leta 2013, ko je bila brezposelnost v vzhodni Sloveniji 12,6 %, v zahodni pa 9,5 %. To pomeni razliko 3,1 odstotne točke v škodo vzhodne Slovenije. Na grafu je to obdobje jasno označeno s sivo barvo, pri čemer modra krivulja (vzhod) vztrajno vodi nad oranžno (zahod).

2. Pandemija COVID-19 (2020–2022):
Tudi v času pandemije COVID-19 (označeno z modro barvo) je vzhodna Slovenija ohranila višjo stopnjo brezposelnosti, čeprav sta se obe regiji po letu 2022 začeli približevati zgodovinsko nizkim vrednostim.

3. Strukturni vzroki:
Glavni razlogi za trajno slabše rezultate vzhodne Slovenije so manj razvita industrijska struktura, nižja raven investicij in manj priložnosti za zaposlitev v primerjavi z bolj gospodarsko razvitim zahodom države.

Najbolj izpostavljene točke:

 • Vzhodna Slovenija je v obeh kriznih obdobjih beležila izrazite skoke brezposelnosti, medtem ko je bila zahodna regija bolj odporna na gospodarske šoke.

 • Po letu 2016 se razlika nekoliko zmanjšuje, vendar vzhodna Slovenija tudi v najnovejšem obdobju ostaja bolj ranljiva na trgu dela.

![Graf brezposelnosti za regije v Sloveniji](slike%2FBrezposelniRegije.png)

### 6. Prosta delovna mesta po dejavnosti (Slika 4)
Gibanje števila prostih delovnih mest v petih ključnih sektorjih slovenskega gospodarstva med letoma 2008 in 2024. Največ prostih mest so v tem obdobju beležile predelovalne dejavnosti, gradbeništvo, trgovina, raznovrstne poslovne dejavnosti in gostinstvo, pri čemer so sektorji izkazovali močno nihanje v času kriz in hitrejše okrevanje po njihovem koncu

C Predelovalne dejavnosti

F Gradbeništvo

G Trgovina, vzdrževanje in popravila motornih vozil

N Druge raznovrstne poslovne dejavnosti

I Gostinstvo

Glavni trendi in ugotovitve
1. Predelovalne dejavnosti in gradbeništvo vodita po številu prostih mest:
Oba sektorja sta v zadnjem desetletju beležila največ prostih delovnih mest. Predelovalne dejavnosti so še posebej izstopale v obdobju po letu 2016, z izrazitim vrhom okoli leta 2022, ko je število prostih mest preseglo 6.000. Gradbeništvo je prav tako doseglo rekordne vrednosti, pri čemer je opazna značilna volatilnost zaradi sezonskih in gospodarskih vplivov.

2. Trgovina, poslovne dejavnosti in gostinstvo:
Trgovina, vzdrževanje in popravila motornih vozil ter druge raznovrstne poslovne dejavnosti sta stabilno prispevali k povpraševanju po delovni sili. Gostinstvo pa je po pandemiji COVID-19 doživelo izrazit porast prostih delovnih mest, kar je povezano z odpravo omejitev in ponovnim zagonom turizma ter storitvenih dejavnosti.

3. Vpliv kriznih obdobij:

Finančna kriza (2008–2013): Vsi sektorji so v tem obdobju beležili nizko število prostih delovnih mest, kar je razvidno iz znižanih vrednosti na grafu v označenem sivem območju.

Pandemija COVID-19 (2020–2022): Kljub začetnemu padcu so se nekateri sektorji (predvsem gostinstvo in gradbeništvo) hitro pobrali, kar je razvidno iz strmega porasta prostih mest v obdobju po letu 2021 (modro označeno obdobje).

4. Sektorske posebnosti in izzivi:

 - Gradbeništvo in gostinstvo izstopata po izraziti volatilnosti, ki je posledica sezonskih vplivov, začasnih zaposlitev in občutljivosti na gospodarske cikle.

 - Predelovalne dejavnosti so ključni motor povpraševanja po delovni sili, a se soočajo z izzivi pri iskanju ustrezno usposobljenih kadrov.

 - Povpraševanje po delavcih v trgovini in poslovnih dejavnostih ostaja stabilno, vendar se spreminja glede na gospodarske razmere in tehnološki razvoj.

![graf z top 5 sektorjev z največ prostih mest](slike%2FProstaDelovnaMestaO.png)


### 7. Korelacija med brezposelnostjo in številom delovnih mest po sektorjih (Slika 5)
Na grafu so prikazane normalizirane vrednosti zaposlenosti v štirih ključnih sektorjih (predelovalne dejavnosti, promet in skladiščenje, trgovina ter gostinstvo) v primerjavi s stopnjo brezposelnosti (črtkana črna črta) v obdobju 2008–2024. Označena so tudi krizna obdobja: finančna kriza (sivo) in pandemija COVID-19 (modro).

Glavne ugotovitve:
Močna negativna korelacija:
Vsi analizirani sektorji izkazujejo izrazito obratno gibanje glede na brezposelnost. Ko stopnja brezposelnosti narašča (črtkana črta gre navzgor), število zaposlenih v teh sektorjih upada – najbolj izrazito v času finančne krize 2008–2013, ko so predelovalne dejavnosti, promet, trgovina in gostinstvo dosegli najnižje vrednosti zaposlenosti.

Obdobje okrevanja:
Po koncu gospodarske krize (po letu 2014) se v vseh sektorjih začne postopno okrevanje – število zaposlenih ponovno raste, medtem ko stopnja brezposelnosti vztrajno pada. Ta trend je viden vse do izbruha pandemije COVID-19.

Poseben primer gostinstva med COVID-19:
Med pandemijo COVID-19 (2020–2022) je gostinstvo doživelo izjemno strm upad zaposlenosti, kar je neposredna posledica zaprtja gostinskih lokalov in omejitev javnega življenja. Že pred koncem pandemije pa se število zaposlenih v gostinstvu hitro pobere, kar kaže na občutljivost sektorja na sproščanje ukrepov in povratek povpraševanja.

Sektorske posebnosti:
Predelovalne dejavnosti, promet in skladiščenje ter trgovina so ključni sektorji, ki najbolj obratno sledijo trendom brezposelnosti. Njihova zaposlenost je zelo odvisna od splošnega gospodarskega cikla in povpraševanja, kar potrjuje tako domača kot evropska literatura

![korelacija.png](slike%2Fkorelacija.png)

### 7. Zaključki
Analiza podatkov o brezposelnosti in zaposlenosti v Sloveniji med letoma 2008 in 2024 je razkrila več ključnih vzorcev, ki so pomembni za razumevanje dinamike trga dela, zlasti v času gospodarskih šokov.

Neposredni vpliv gospodarskih šokov na brezposelnost:
V vsaki večji krizi – finančni krizi (2008–2013) in pandemiji COVID-19 (2020–2022) – je stopnja brezposelnosti v Sloveniji močno narasla. To potrjuje, da so gospodarski šoki ključni dejavniki za spremembe na trgu dela in da imajo neposredne posledice za zaposlenost in socialno varnost.

• Spolne razlike:
  Ženske so v povprečju imele višjo stopnjo brezposelnosti kot moški. Med pandemijo COVID-19 je bila razlika še bolj izrazita, saj so bile ženske zaradi večje        zastopanosti v ogroženih sektorjih (npr. storitve, gostinstvo) znatno bolj prizadete.

• Regionalne razlike:
  Vzhodna Slovenija je v vseh analiziranih obdobjih imela po absolutnem številu več brezposelnih kot zahodna Slovenija. To kaže na trajne strukturne razlike med      regijama, povezane z manj razvito industrijo, nižjo stopnjo investicij in manj priložnosti za zaposlitev.

• Sektorski vplivi:
  Ko brezposelnost narašča, so najbolj na udaru predelovalne dejavnosti, promet in skladiščenje, trgovina, vzdrževanje in popravila motornih vozil ter gostinstvo.    Ti sektorji so bistveno občutljivi na gospodarske cikle in hitro reagirajo na spremembe povpraševanja.

• Gostinstvo kot najbolj ranljiv sektor med pandemijo:
  Gostinstvo je med epidemijo COVID-19 doživelo največji šok. Zaprtje lokalov in omejitve javnega življenja so povzročile izjemen upad zaposlenosti, vendar se je     sektor po odpravi ukrepov hitro opomogel, kar kaže na njegovo prilagodljivost in pomen turizma za slovensko gospodarstvo.
