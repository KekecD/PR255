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
Podatkovna osnova vključuje četrtletne podatke Statističnega urada RS (OPSI), podatki so v formatu pcaxis, kjer imamo besedilne in statistične tipe podatkov, predvsem:
1. brezposelneCetrtletno.PX :  
    • Ključne spremenljivke: regija, spol, število brezposelnih (v 1000) in delež v %, četrtletje.
2. delovnaMestaCetrtletno.PX :<br/>
    • Ključne spremenljivke: število prostih/zasedenih mest po SKD dejavnostih.
3. vsi.PX :<br/>
    • Ključne spremenljivke: Delovno aktivni (v 1000) .

   

<br> celotna koda je napisana v [Jupyter Notebook](https://github.com/KekecD/PR255/blob/main/projekt.ipynb)
### 3. Splošni trendi brezposelnosti (Slika 1)
Podatki kažejo dve kritični obdobji:
1. Finančna kriza (2008-2013)
    • vrhunec brezposelnosti v letih 2013-2014 (11.1% v letu 2013, 10.8% za 2014)
    • Počasno okrevanje do leta 2019
2. Pandemija COVID-19 (2020-2022)
    • Manjši šok kot leta 2008 (5.6% maksimalna brezposelnost v 2021)
    • Hitrejše okrevanje do leta 2024

![Graf brezposelnosti v Sloveniji](slike%2FBrezposelnostSkupaj.png)

### 4. Razlike med spoloma (Slika 2)
Ženske so bile ne-sorazmerno prizadete:<br/>
    • Med krizo 2008: ženske imajo v 2013Q1 11.7%, moški pa 10.7% (1% razlike)<br/>
    • Po letu 2020: v letu 2021Q1 ženske so imele 6.9% medtem moški 4.6% (2.3% razlike)<br>
Vidi se torej, da po krizi 2008 imajo ženske večjo brezposelnost. Od 2021 naprej pa so tudi moški kdaj imeli večjo.
![Graf brezposelnosti za spola v Sloveniji](slike%2FBrezposelniSpoli.png)
    
### 5. Regionalne razlike (Slika 3)
Vzhodna Slovenija kaže trajno slabše rezultate:
- V kriznih obdobjih največja razlika med vzhodom in zahodom je 3.1% leta 2013 (vzhodna 12.6%, zahodna 9.5%)
- Glavni vzroki:<br/>
    • Manj industrije<br/>
    • Manj investicij<br/>
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
Zanimalo nas je tudi kakšne so korelacije med brezposelnostjo in številom delovnih mest po sektorjih. Sektorji, kateri najbolj obratno sledijo brezposelnosti(ko brezposelnost raste delovna mesta padajo) so:
1. Predelovalne dejavnosti
2. Promet in skladiščenje
3. Trgovina, vzdrževanje in popravila motornih vozil
4. Gostinstvo

Iz grafa se vidi, da ko brezposelnost raste, delovna mesta v zgornjih sektorjih upadajo. Po koncu gospodarkse krize začnejo ponovno rasti. Zelo zanimiv je podatek za gostinstvo med COVID-19 krizo. Na grafu se vidi kako strmo vpade število delovnih mest v gostinstvu med karaneteno, kot posledica nezmožnosti obratovanja gostilen in restevracij. Že pred koncem krize pa hitro število delovnih mest skoči nazaj. 

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
