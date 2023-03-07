# vytvorim si 3 listy
set1 = ["▤", "▤", "▤"]
set2 = ["▤", "▤", "▤"]
set3 = ["▤", "▤", "▤"]

# vytvorim z 3 listov 1 list
# nested list
all_sets = [set1, set2, set3]

# vypisem vsetky sety v samostatnych riadkoch
print(f"{set1}\n{set2}\n{set3}")

# uzivatel zada poziciu a podla nej zmenime symbol stvorca na X
position = int(input("Zadaj poziciu [1 az 9]\n"))

if position == 1:
    position_tran = "00"
elif position == 2:
    position_tran = "01"
elif position == 3:
    position_tran = "02"
elif position == 4:
    position_tran = "10"
elif position == 5:
    position_tran = "11"
elif position == 6:
    position_tran = "12"
elif position == 7:
    position_tran = "20"
elif position == 8:
    position_tran = "21"
else:
    position_tran = "22"

# rozdelim position_trans na 2 samostatne cisla
# position_tran je string takze musim previest na integer
position_1 = int(position_tran[0])
position_2 = int(position_tran[1])

# v all_set liste nahradim stvorec za X podla zvolenej pozicie
all_sets[position_1][position_2] = "X"
# zjednoduseny zapis / oneliner
# all_sets[int(position_tran[0])][int(position_tran[1])] = "X"

# vypisem vysledok - all_sets[0] je set1, all_sets[1] je set2 ..
# print(f"{all_sets[0]}\n{all_sets[1]}\n{all_sets[2]}")
# alebo
print(f"{set1}\n{set2}\n{set3}")
