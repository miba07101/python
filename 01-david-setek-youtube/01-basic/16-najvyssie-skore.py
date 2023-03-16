# zadaj hodnoty
score = input("Zadaj skore studentov [oddelene ciarkou a medzerou]\n")

# vloz zadane hodnoty do listu
score_list = score.split(", ")

# cyklus zmena str na int zadanych hodnot
score_list_int = []
for item in score_list:
    score_list_int.append(int(item))
# iny sposob
# for index in range(0, len(score_list)):
#     score_list_int.append(int(score_list[index]))

# cyklus na urcenie maximalnej hodnoty
max_score = 0
for item in score_list_int:
    if max_score < item:
        max_score = item

# vypisanie vysledku
print(f"Najvyssie skore je: {max_score}")
