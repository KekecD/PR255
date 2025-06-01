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
Drugi graf prikazuje, kako so napovedni modeli napovedovali stopnjo brezposelnosti v naslednjem četrtletju v primerjavi z dejanskimi vrednostmi. Med pandemijo COVID-19 so napovedi pogosto precenjevale dejansko stopnjo brezposelnosti, kar je razvidno iz izrazitega odstopanja napovedi navzgor v letu 2020. V obdobjih stabilnosti pa so bile napovedi precej bolj usklajene z dejanskimi podatki, kar kaže na večjo zanesljivost modelov v mirnejših gospodarskih razmerah

![Graf brezposelnosti v Sloveniji](slike%2FBrezposelnostSkupaj.png)
![Napoved brezposelnosti](slike%NapovedBrezposelnosti.png)
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
Graf prikazuje izrazite in trajne razlike v brezposelnosti med vzhodno in zahodno Slovenijo v obdobju 2008–2024. V vseh obdobjih, še posebej pa med gospodarskimi krizami, je bila stopnja brezposelnosti v vzhodni Sloveniji bistveno višja kot v zahodni.

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
Top 5 sektorjev z največ prostih mest:
1. Predelovalne dejavnosti
2. Gradbeništvo
3. Trgovina, vzdrževanje in popravila motornih vozil
4. Druge raznovrstne poslovne dejavnosti
5. Gostinstvo

![graf z top 5 sektorjev z največ prostih mest](slike%2FProstaDelovnaMestaO.png)

Posebej zanimivi vzorci:
- Dejavnosti, ki imajo največ prostih mest so gradbeništvo in predelovanje dejavnosti.
- Gradbeništvo ima izrazito volatilnost. Opažamo periodične skoke in padce, kar je verjetno posledica začasne zaposlitve, sezonskih vplivov in odvisnost od gospodarskih ciklov.
- Gostinstvo ima tudi visok skok v letu 2022 do 2023, po odpravi COVID-19 ukrepov

### 7. Korelacija med brezposelnostjo in številom delovnih mest po sektorjih (Slika 5)
Na grafu so prikazane normalizirane vrednosti zaposlenosti v štirih ključnih sektorjih (predelovalne dejavnosti, promet in skladiščenje, trgovina ter gostinstvo) v primerjavi s stopnjo brezposelnosti (črtkana črna črta) v obdobju 2008–2024. Označena so tudi krizna obdobja: finančna kriza (sivo) in pandemija COVID-19 (modro).
1. Predelovalne dejavnosti
2. Promet in skladiščenje
3. Trgovina, vzdrževanje in popravila motornih vozil
4. Gostinstvo

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
Glavni vzorci kažejo:

[//]: # (1. Močno povezanost med gospodarskimi šoki in brezposelnostjo)

[//]: # (2. Trajne regionalne neenakosti)

[//]: # (3. Sektorske posebnosti)
1. Gospodarski šoki in krize imajo neposredne posledice pri brezposelnosti. V vsaki krizi nivo brezposelnosti naraste.
2. Ženske imajo v povprečju večjo brezposelnost. Kovid kriza je bolj povečala število brezposelnih žensk kot moških.
3. Vzhodna Slovenija ima po absolutnem številu več brezposelnih kot zahodna Slovenija
4. Ko raste brezposelnost so najbolj na udaru predelovalne dejavnosti, promet in skladiščenje, trgovina, vzdrževanje in popravila motornih vozil in gostinstno.
5. Gostinstvo je občtutilo največji šok med Kovid epidemijo.
