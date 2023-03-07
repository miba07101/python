import random

# zadam mena
names = input("Zadaj mena platiacich [oddel ich ciarkou a medzerou]\n")

# nacitam mena do listu oddelenych ciarkou a medzerou - split()
names_list = names.split(", ")

# vygenerujem nahodne cislo
# v rozsahu 0 az dlzka (pocet elementov) listu
# pozor! dlzka listu sa rata od 1 a nie 0
# pomocou tohto cisla priradim element z listu
number = random.randint(0, len(names_list) - 1)

# vypisem kto bude dnes platit
print(f"Dnes bude plati: {names_list[number]}")
