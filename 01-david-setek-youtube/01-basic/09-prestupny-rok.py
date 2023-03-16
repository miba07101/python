# prestupny rok
# je delitelny 4
# nesmie byt delitelny 100
# ak je delitelny 4 a 100 (mal by byt neprestupny) ale ak je zaroven
# delitelny 400 tak je tiez prestupny

year = int(input("Zadaj rok:\n"))

if year % 4 == 0 or year % 400 == 0:
    print("Prestupny rok")
else:
    print("Neprestupny rok")
