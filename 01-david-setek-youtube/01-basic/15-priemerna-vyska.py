# poziadam o zadanie udajov
heights = input("Zadaj vysky osob v cm [oddel ich ciarkou a medzerou]\n")
# udaje nacitam do listu
heights_list = heights.split(", ")
# zistim pocet prvkov v liste
heights_list_len = len(heights_list)

# vytvorim cyklus, ktory scita vsetky prvky v liste
# zacinam s 0 hodnotou
heights_sum = 0

for item in heights_list:
    heights_sum += int(item)

# vypocet priemernej vysky
avg_heights = heights_sum / heights_list_len

# vypisem vysledok
print(f"Priemerna vyska je: {avg_heights} cm.")
