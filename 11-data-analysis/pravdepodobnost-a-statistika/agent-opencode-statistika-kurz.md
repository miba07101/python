# Kurz: Základy štatistiky pre energetiku
**5 dní × 2-3 h** | **Nástroj:** Excel | **Úroveň:** Začiatočník

---

## Zdroje

### Všeobecná štatistika
- CMU OLI – Probability & Statistics (zadarmo): https://oli.cmu.edu/courses/probability-statistics-open-free/
- UPJŠ Košice – Základy pravdepodobnosti a štatistiky: https://umv.science.upjs.sk/zezula/stgjax/
- TU Delft – Statistics for Engineers: https://tudelft-citg.github.io/learn-probability/intro.html
- LithoGuru – Online Statistics Review: https://www.lithoguru.com/scientist/statistics/review.html
- E-learning VŠCHT – Statistická analýza dat: https://e-learning.vscht.cz/course/view.php?id=2088

### Štatistika v energetike
- IEA – Energy Efficiency Indicators: https://elearning.iea.org/courses/course-v1:InternationalEnergyAgency+FS1+Open/about
- UN SDG:Learn – Energy Statistics: https://www.unsdglearn.org/courses/e-learning-course-on-energy-statistics/
- IEA – Energy Statistics Course: https://www.iea.org/events/30th-energy-statistics-course
- UN SIAP – Energy Statistics and Balances: https://siap-elearning.org/mod/page/view.php?id=2993
- Building Energy Statistical Modelling: https://buildingenergygeeks.org/

### Slovenské/české zdroje
- VITA – Kurzy Štatistika: https://www.vita.sk/online-kurzy-statistika/
- Kurzy.sk – Excel štatistické analýzy: https://www.kurzy.sk/
- Školenia.sk – Základy štatistiky: https://www.skolenia.sk/kurzy/110000180/

---

## Plán kurzu

| Deň | Téma | Kľúčové pojmy |
|-----|------|---------------|
| 1 | Čo je štatistika + typy dát | populácia, vzorka, premenné, úroveň merania |
| 2 | Popisná štatistika | priemer, medián, modus, rozptyl, štandardná odchýlka, kvartily |
| 3 | Grafické zobrazenie dát | histogram, boxplot, stĺpcový graf, interpretácia |
| 4 | Pravdepodobnosť a rozdelenia | pravdepodobnosť, normálne, binomické, Poissonovo rozdelenie |
| 5 | Záverečná aplikácia | interval spoľahlivosti, korelácia, súhrnná analýza energetických dát |

### Navrhované ďalšie kurzy
- Testovanie hypotéz (t-test, ANOVA, chi-kvadrát)
- Lineárna regresia (modelovanie spotreby)
- Časové rady (predpoveď spotreby)
- Energetické bilancie (IEA metodológia)

---

## Metodológia výučby

**Prístup:** Interaktívna výučba – najprv teória → príklad → úloha pre študenta → výpočet → vysvetlenie krokov → zápis poznatkov do MD súboru.

**Postup pre každý deň:**
1. Vysvetli teóriu (krátko, jasne)
2. Ukáž príklad na energetických dátach
3. Daj študentovi úlohu (vypočítať/analyzovať)
4. Over výsledok, vysvetli prípadné chyby
5. Pokračuj ďalšou úlohou
6. Na konci dňa vytvor MD súbor so zhrnutím všetkých poznatkov

**Dáta:** Dataset `1.den/energeticky_dataset.csv` (50 domácností) sa používa od Dňa 1.

---

## TO DO list (pre AI – každý deň)

### Deň 1 ✅ ABSOLVOVANÝ
- [x] Teória: Čo je štatistika (deskriptívna vs. inferenčná), základné pojmy
- [x] Teória: Typy premenných (kvantitatívne/kvalitatívne, spojité/diskrétne), úrovne merania
- [x] Príklad: Dataset 10 domácností – interpretácia
- [x] Úloha: Výpočet priemeru (3805 kWh)
- [x] Úloha: Výpočet mediánu (3450 kWh), porovnanie s priemerom
- [x] Úloha: Odchýlky, rozptyl, štandardná odchýlka
- [x] Práca s Excelom: Data Analysis nástroj, vysvetlenie rozdielu populačná vs. vzorková (n vs. n-1)
- [x] Výstup: `1.den/den1_zaklady_statistiky.md`
- [ ] Študent: Absolvovať online cvičenie (CMU OLI alebo UPJŠ)

### Deň 2 – MIERY CENTRÁLNEJ TENDENCIE A VARIABILITY (detailný plán)
- [ ] Teória: Kvartily (Q1, Q2, Q3), kvartilový rozsah IQR
- [ ] Teória: Kedy použiť priemer vs. medián (zhrnutie z Dňa 1)
- [ ] Príklad: Výpočet kvartilov na datasete 10 domácností
- [ ] Úloha: Študent v Exceli (QUARTILE.EXC) vypočíta Q1, Q2, Q3 pre spotrebu
- [ ] Úloha: Vypočíta IQR = Q3 - Q1
- [ ] Príklad: Identifikácia outlierov pomocou 1.5 × IQR pravidla
- [ ] Úloha: Študent nájde outliery v datasete
- [ ] Excel: Použiť Data Analysis pre všetkých 50 domácností z datasetu
- [ ] Výstup: Vytvoriť `2.den/den2_popisna_statistika.md`

### Deň 3 – GRAFICKÉ ZOBRAZENIE DÁT
- [ ] Teória: Histogram (ako čítať, kedy použiť)
- [ ] Teória: Boxplot (čo zobrazuje, ako identifikovať outliery)
- [ ] Teória: Stĺpcový graf vs. koláčový
- [ ] Príklad: Vytvorenie histogramu v Exceli z nášho datasetu
- [ ] Príklad: Vytvorenie boxplotu v Exceli
- [ ] Úloha: Študent vytvorí 3-4 grafy a interpretuje ich
- [ ] Výstup: Vytvoriť `3.den/den3_grafy.md`

### Deň 4 – PRAVDEPODOBNOSŤ A ROZDELENIA
- [ ] Teória: Základy pravdepodobnosti (P(A), doplnková, sčítacie, násobné pravidlo)
- [ ] Teória: Normálne rozdelenie (68-95-99.7 pravidlo)
- [ ] Teória: Binomické a Poissonovo rozdelenie
- [ ] Príklad: Výpočty pravdepodobností v Exceli na energetických dátach
- [ ] Úloha: Študent rieši 3 úlohy na pravdepodobnosť
- [ ] Výstup: Vytvoriť `4.den/den4_pravdepodobnost.md`

### Deň 5 – ZÁVEREČNÁ APLIKÁCIA
- [ ] Teória: Interval spoľahlivosti (vzorec, interpretácia)
- [ ] Teória: Korelácia (coefficient r, interpretácia)
- [ ] Príklad: Výpočet 95% CI a korelácie na energetických dátach
- [ ] Úloha: Záverečná komplexná úloha – celá analýza datasetu
- [ ] Zhodnotenie: Čo sa študent naučil, čo ďalej
- [ ] Výstup: Vytvoriť `5.den/den5_zaverecna_aplikacia.md`

### Navrhované ďalšie kurzy
- Testovanie hypotéz (t-test, ANOVA, chi-kvadrát)
- Lineárna regresia (modelovanie spotreby)
- Časové rady (predpoveď spotreby)
- Energetické bilancie (IEA metodológia)
