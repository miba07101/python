print("Vitajte v kalkulacke na vypocet platieb")
platba = int(input("Kolko mate zaplatit? "))
sprepitne = int(input("Vyska sprepitneho [v %] "))
pocet_ludi = int(input("Medzi kolkych ludi rozdelit platbu? "))

suma = (platba + (platba * sprepitne / 100)) / pocet_ludi

# formatovanie na 2 desatinne
suma_format = "{:.2f}".format(suma)
print(f"Kazdy clovek by mal zaplatit: {suma_format} eur")
