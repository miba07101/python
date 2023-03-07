height = int(input("Aka je tvoja vyska? [cm]\n"))
bill = 0

if height > 100:
    age = int(input("Aky je tvoj vek?\n"))
    if age <= 12:
        bill = 50
        print(f"Cena listku je {bill} eur")
    elif age <= 18:
        bill = 100
        print(f"Cena listku je {bill} eur")
    else:
        bill = 150
        print(f"Cena listku je {bill} eur")
    photo = input("Chces sa vyfotit? [ano-nie]\n")
    if photo == "ano":
        photo_price = 50
        # pripocita k uctu este cenu fotky
        bill += photo_price
        print(f"Cena za fotku je {photo_price} eur. Celkova cena je {bill} eur")
    else:
        print(f"Celkova cena je {bill} eur")
else:
    print("Zial, nemozes ist na horskej drahe")
