# Deň 1: Základy štatistiky

## 1. Čo je štatistika?

**Štatistika** je veda o pozorovaní javov, zbieraní dát a ich analyzovaní a interpretovaní.

### Dve vetvy štatistiky

| Vetva | Čo robí | Príklad |
|-------|---------|---------|
| **Deskriptívna** | Opisuje dáta, ktoré už máme | „Priemerná spotreba našich zákazníkov je 3200 kWh" |
| **Inferenčná** | Robí závery o celej populácii zo vzorky | „Na základe 200 meraní odhadujeme, že celé Slovensko spotrebuje X GWh" |

### Základné pojmy

- **Populácia** – celá skupina, ktorá nás zaujíma (všetky domácnosti na SR)
- **Vzorka** – časť, z ktorej reálne zbierame dáta (200 domácností)
- **Premenná** – čo meriame (spotreba, typ paliva, plocha...)

---

## 2. Typy premenných

```
Premenné
├── KVALITATÍVNE (kategorické)
│   ├── Nominálne (bez poradia): typ paliva, kraj
│   └── Ordinálne (s poradím): trieda účinnosti A>B>C
│
└── KVANTITATÍVNE (číselné)
    ├── Spojité (akákoľvek hodnota): spotreba kWh, plocha m²
    └── Diskrétne (celočíselné): počet osôb, počet izieb
```

### Úrovne merania

| Úroveň | Zoradenie | Rozdiely | Pomer | Príklad |
|--------|-----------|----------|-------|---------|
| Nominálna | ✗ | ✗ | ✗ | typ paliva |
| Ordinálna | ✓ | ✗ | ✗ | trieda účinnosti |
| Intervalová | ✓ | ✓ | ✗ | teplota °C |
| Pomerová | ✓ | ✓ | ✓ | spotreba kWh |

---

## 3. Praktický príklad – Energetické dáta

Dataset 10 domácností:

| ID | Spotreba (kWh) | Typ paliva | Plocha (m²) |
|----|----------------|------------|-------------|
| 1 | 2400 | elektrina | 65 |
| 2 | 4800 | plyn | 120 |
| 3 | 1200 | elektrina | 35 |
| 4 | 6200 | uhlie | 95 |
| 5 | 3100 | plyn | 80 |
| 6 | 1850 | elektrina | 50 |
| 7 | 5400 | plyn | 140 |
| 8 | 2100 | elektrina | 55 |
| 9 | 3800 | uhlie | 90 |
| 10 | 7200 | uhlie | 180 |

---

## 4. Miery centrálnej tendencie

### Priemer (Mean)
```
Priemer = Σx / n = 38050 / 10 = 3805 kWh
```
- Jednoduchý výpočet
- **Nevýhoda:** Citlivý na extrémne hodnoty (7200 kWh ťahá priemer nahor)

### Medián (Median)
```
Zoradené: 1200, 1850, 2100, 2400, 3100, 3800, 4800, 5400, 6200, 7200
Medián = (3100 + 3800) / 2 = 3450 kWh
```
- Hodnota uprostred
- **Výhoda:** Neovplyvňujú ho extrémy → lepšie vystihuje "typickú" hodnotu

### Modus
- Najčastejšie sa vyskytujúca hodnota
- V našich dátach: každá hodnota sa vyskytuje len raz → nemáme modus

### Porovnanie

| Miera | Hodnota | Charakteristika |
|-------|---------|-----------------|
| Priemer | 3805 kWh | Ťahaný nahor extrémami |
| Medián | 3450 kWh | Skutočne typická hodnota |

---

## 5. Miery variability

### Odchýlka od priemeru
Pre každú hodnotu: x - x̄

| ID | Hodnota | Odchýlka |
|----|---------|----------|
| 1 | 2400 | -1405 |
| 2 | 4800 | +995 |
| 3 | 1200 | -2605 |
| 4 | 6200 | +2395 |
| 5 | 3100 | -705 |
| 6 | 1850 | -1955 |
| 7 | 5400 | +1595 |
| 8 | 2100 | -1705 |
| 9 | 3800 | -5 |
| 10 | 7200 | +3395 |

### Rozptyl (Variance)
```
Rozptyl = Σ(x - x̄)² / (n-1) = 36 782 250 / 9 = 4 086 917
```
- Číslo je veľké a v jednotkách kWh² → nepohodlné na interpretáciu

### Štandardná odchýlka (Standard Deviation)
```
s = √Rozptyl = √4 086 917 = 2021.61 kWh
```
- V tej istej jednotke ako dáta (kWh)
- **Interpretácia:** Domácnosti sa v priemere líšia o ±2021 kWh od priemeru

### Populačná vs. Vzorková

| Typ | Vzorec | Použitie |
|-----|--------|----------|
| Populačná σ | √(Σ(x-x̄)² / **n**) | Keď poznáme celú populáciu |
| Vzorková s | √(Σ(x-x̄)² / **n-1**) | Keď máme len vzorku (štandardné) |

**Prečo n-1?** Besselova korekcia – keď máme len vzorku, priemer nie je presný odhad skutočného priemeru. Delenie n-1 koriguje túto neistotu.

---

## 6. Výsledky z Excelu (Data Analysis)

| Ukazovateľ | Hodnota | Význam |
|------------|---------|--------|
| Mean | 3805 | Priemer |
| Standard Error | 639.29 | Chyba priemeru (s/√n) |
| Median | 3450 | Medián |
| Mode | #N/A | Nemáme modus |
| Standard Deviation | 2021.61 | Štandardná odchýlka (vzorková) |
| Sample Variance | 4 086 917 | Rozptyl (vzorkový) |
| Kurtosis | -1.12 | Ploché rozdelenie (málo extrémov) |
| Skewness | 0.41 | Mierne naklonené doprava |
| Range | 6000 | Rozsah (7200 - 1200) |
| Minimum | 1200 | Minimálna hodnota |
| Maximum | 7200 | Maximálna hodnota |
| Sum | 38050 | Sumár |
| Count | 10 | Počet pozorovaní |

---

## 7. Kľúčové poznatky

1. **Priemer nie je vždy najlepší** – extrémy ho skresľujú
2. **Medián** lepšie vystihuje "typickú" hodnotu
3. **Štandardná odchýlka** ukazuje variabilitu – čím väčšia, tým viac sa dáta líšia
4. **Vzorková št. odchýlka (n-1)** sa používa takmer vždy, lebo pracujeme so vzorkami
5. **Kurtosis a Skewness** hovoria o tvare rozdelenia (ploché/naklonené)

---

## Ďalšie kroky

- **Deň 2:** Kvartily, IQR, boxplot, ďalšie miery variability
- **Deň 3:** Grafické zobrazenie dát
- **Deň 4:** Pravdepodobnosť a rozdelenia
- **Deň 5:** Interval spoľahlivosti a korelácia
