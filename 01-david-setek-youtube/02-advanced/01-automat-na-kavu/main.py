from source_data import MENU
from source_data import resources

# === zakladne nastavenie ===
espresso_price = MENU["espresso"]["cost"]
latte_price = MENU["latte"]["cost"]
cappuccino_price = MENU["cappuccino"]["cost"]


# === funkcie ===
def coins():
    print("Prosim zvolte mince 1, 2, 5, 10, 20, 50")
    kc1 = int(input("kolko 1 KC chcete zvolit?: ")) * 1
    kc2 = int(input("kolko 2 KC chcete zvolit?: ")) * 2
    kc5 = int(input("kolko 5 KC chcete zvolit?: ")) * 5
    kc10 = int(input("kolko 10 KC chcete zvolit?: ")) * 10
    kc20 = int(input("kolko 20 KC chcete zvolit?: ")) * 20
    kc50 = int(input("kolko 50 KC chcete zvolit?: ")) * 50
    suma = kc1 + kc2 + kc5 + kc10 + kc20 + kc50
    print(f"Celkom ste vhodili: {suma} KC")
    return suma


def refund(price, user_sum_coins):
    vydaj = user_sum_coins - price
    if vydaj >= 0:
        print("Vas napoj sa pripravuje")
        if vydaj > 0:
            print(f"Vraciam: {vydaj} KC")
    else:
        print(
            f"Nevhodili ste dostatok penazi. Este je potrebne vhodit {price - user_sum_coins} KC"
        )


# === hlavny program ===
user_choice = input("Co by ste si dal? (esspresso, latte, cappuccino): ")

# mozem zadat a "report" pre vypis zostatku ingrediencii
if user_choice == "report":
    print(resources)
    sum = coins()
    refund()
