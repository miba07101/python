numbers = [5, 2, 3, 1, 4]

for i in range(0, len(numbers)):
    for j in range(i + 1, len(numbers)):
        # od najmensieho po najvacsie ">"
        # od najvecieho po najmensie "<"
        if numbers[i] > numbers[j]:
            temp = numbers[i]
            numbers[i] = numbers[j]
            numbers[j] = temp

print(numbers)

# pr.2 spojenie dvoch listov a usporiadanie cisel od najmensieho po najvacsie
num1 = [1, 2, 4, 22, -10, -5]
num2 = [2, 3, 6, 0]

# naplnim vysledne pole poliami num1 num2
num = []
for i in range(0, len(num1)):
    num.append(num1[i])
for i in range(0, len(num2)):
    num.append(num2[i])

# triedenie cisel
for i in range(0, len(num)):
    for j in range(i + 1, len(num)):
        if num[i] > num[j]:
            # efektivnejsi zapis, nemusim pouzit "temp" premennu
            num[i], num[j] = num[j], num[i]
print(num)


# iny sposob riesenia - podla videa
# !!!! FUNGUJE IBA PRE KLADNE CISLA !!!!
def merge(n1, n2):
    # vytvorim 2 indexy,ktore budu v prvom kroku cyklu ukazovat na zaciatocny
    # element kazdeho z danych poli/listov n1 a n2
    i1 = 0
    i2 = 0
    # vysledne pole/listov
    res = []
    # iterujem dovtedy pokial cislo indexu i1,i2 nebude mensie ako pocet elementov
    # daneho pola n1,n2
    while i1 < len(n1) and i2 < len(n2):
        # ponam hodnoty cisla z pola n1 na indexe i1 s hodnotou cisla n2 na i2
        if n1[i1] < n2[i2]:
            # ak je to pravda, tak do vysledneho pola vlozim cislo n1 na i1
            res.append(n1[i1])
            # musim zvysit cislo indexu, preunut ho na dalsie cislo
            i1 += 1
        else:
            res.append(n2[i2])
            i2 += 1
    # podmienka pre kontrolu dlzky poli n1,n2
    if i1 < len(n1):
        # priradim vsetky zvysne hodnoty pola n1 do vysledneho pola
        # robim to skr +=
        res += n1[i1:]
        # ak pouzijem append tak priradi cislo ako list
        # res.append(n1[i1:])
    if i2 < len(n2):
        res += n2[i2:]
    return res


if __name__ == "__main__":
    num1 = [1, 2, 4, 22]
    num2 = [2, 3, 6, 10]
    print(merge(num1, num2))
