# scitaj vsetky sude(parne) cisla od 1 do 100

# vytvorim si prazdny list kde ulozim parne cisla
parne_cisla_list = []

# range neberie posledne cislo, preto ho treba dat vzdy o jedno viac
# ako je pozadovana hodnota
for item in range(1, 101):
    # modulo operator, zistim ci zvysok po deleni 2 je nula,
    # cize cislo je parne
    if item % 2 == 0:
        # kazde parne cislo vlozim do listu
        parne_cisla_list.append(item)

# scitam vsetky cisla v liste parnych cisel
suma = 0
for item in parne_cisla_list:
    suma += item

# vypisem vysledok
print(f"Suma vsetkych parnych cisel od 1 do 100 je: {suma}")
