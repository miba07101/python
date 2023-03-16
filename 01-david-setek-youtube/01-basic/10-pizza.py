# lower() mi zmeni zadane pismeno na male
pizza = input("Vyber si velkost pizze [S/M/L]:\n").lower()
feferony = input("Chcete feferony naviac [ano/nie]?\n").lower()
cheese = input("Chcete extra syr [ano/nie]?\n").lower()

bill = 0

if pizza == "s":
    bill = 100
    if feferony == "ano":
        bill += 20
    else:
        bill += 0
    if cheese == "ano":
        bill += 15
    else:
        bill += 0
elif pizza == "m":
    bill = 150
    if feferony == "ano":
        bill += 30
    else:
        bill += 0
    if cheese == "ano":
        bill += 15
    else:
        bill += 0
else:
    bill = 200
    if feferony == "ano":
        bill += 30
    else:
        bill += 0
    if cheese == "ano":
        bill += 15
    else:
        bill += 0

print(f"Celkova suma je {bill}")
