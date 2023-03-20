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


def ingrediences():
    return resources


def gen_allow_ing(name, ing):
    ing["water"] = ing["water"] - MENU[name]["ingredients"]["water"]
    ing["milk"] = ing["milk"] - MENU[name]["ingredients"]["milk"]
    ing["coffee"] = ing["coffee"] - MENU[name]["ingredients"]["coffee"]
    print(f"Zvysok surovin je: {ing}")
    # return ing


def allowable_ingrediences(choice):
    if choice == "espresso":
        gen_allow_ing(choice, allowable_ing)
    if choice == "latte":
        gen_allow_ing(choice, allowable_ing)
    if choice == "cappuccino":
        gen_allow_ing(choice, allowable_ing)


def rest_ingrediences(rest_ing):
    if rest_ing["water"] < 0:
        print("Zial nemame dostatok surovin na pripravu vasho napoja")
        return False
    elif rest_ing["milk"] < 0:
        print("Zial nemame dostatok surovin na pripravu vasho napoja")
        return False
    elif rest_ing["coffee"] < 0:
        print("Zial nemame dostatok surovin na pripravu vasho napoja")
        return False
    else:
        print("Mame dostatok surovin na pripravu vasho napoja")
        return True


# === hlavny program ===
# nacitam zostatok / mnozstvo dostupnych surovin
allowable_ing = ingrediences()

lets_continue = True
while lets_continue:
    user_choice = input("Co by ste si dal? (espresso, latte, cappuccino): ")

    # vypocet zostatku surovin
    allowable_ingrediences(user_choice)

    # kontrola dostatku surovin
    if user_choice != "report":
        lets_continue = rest_ingrediences(allowable_ing)

        # kontrola pokracovania cyklu while
        if lets_continue is not True:
            break

    # mozem zadat aj "report" pre vypis zostatku surovin
    if user_choice == "report":
        print(allowable_ing)

    # volba napoja - hlavny program
    if user_choice == "espresso":
        sum = coins()
        print(f"Cena espressa je: {espresso_price} KC")
        refund(espresso_price, sum)
    elif user_choice == "latte":
        sum = coins()
        print(f"Cena latte je: {espresso_price} KC")
        refund(latte_price, sum)
    elif user_choice == "cappuccino":
        sum = coins()
        print(f"Cena cappuccina je: {espresso_price} KC")
        refund(cappuccino_price, sum)
