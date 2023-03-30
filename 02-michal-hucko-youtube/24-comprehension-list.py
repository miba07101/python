# vynasobte 10 kazde parne cislo v intervale (1,20)

# klasicke riesenie
result = []
# cyklus for
for number in range(1, 20):
    # podmienkova cast
    # kazde parne cislo je delitelne 2 bezo zvysku
    if number % 2 == 0:
        # navratova cast
        # do result priradim kazde parne cislo vynasobene 10-timi
        result.append(number * 10)


print(result)


# LIST COMPREHENSION riesenie
# umoznuje jednoduchsi zapis predchadzajuceho riesenia
# result = [ navratova_cast cyklus_for podmienkova_cast (bez else: podmienky)]
result = [number * 10 for number in range(1, 20) if number % 2 == 0]
print(result)

# ak chcem pouzit else: podmienku, tak musim podmienkovu_cast presunut pred cyklus_for
# pr. nasobenie neparnych cisel 30-tkou
result = [number * 10 if number % 2 == 0 else number * 30 for number in range(1, 20)]
print(result)

# pr. vypis dlzku kazdeho slova vo vete:
veta = "Milan sa uci python"
# zmena string na pole(list)
# veta.split()
result = [len(word) for word in veta.split()]
print(result)

# uloha:
# napis funkciu list_of_list, ktora na vstupe dostanecez parameter pole celych cisel
# vacsich ako ), napr. [0,2,3,2] a nasledne vrati pole cisel ktore bude obsahovat pre
# kazde cislo pole s cislami od 0 po dane cislo

# vstup [0,2,3,2]
# vystup [[0], [0,1,2], [0,1,2,3], [0,1,2]]
vstup = [0, 2, 3, 2]


# klasicky zapis
def list_of_list(flist):
    result = []
    for number in flist:
        temp_list = []
        for one_num in range(0, number + 1):
            temp_list.append(one_num)
        result.append(temp_list)
    return result


print(list_of_list(vstup))


# zapis pomocou comprehension list
def list_of_list_comp(flist):
    return [[one_num for one_num in range(0, number + 1)] for number in flist]
    # tiez zaujimava forma zapisu
    # return [list(range(0, number + 1)) for number in flist]


print(list_of_list_comp(vstup))
