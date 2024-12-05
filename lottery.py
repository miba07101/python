import random


# definujem metodu na zadanie 6 cisel od uzivatela
def get_user_numbers():
    user_input = input("Zadaj 6 cisel (1-20), oddelenych ciarkou: ")
    # vytvorim list zadanych cisel oddelenych ciarkou - split metoda
    user_input_list = user_input.split(",")
    # konvertujem list data na set data
    # konvertujem string na integer - pomocou comprehesion set
    user_input_set_int = {int(input_number) for input_number in user_input_list}
    return user_input_set_int


# definujem metodu na vytvorenie 6 nahodnych cisel
def create_lottery_numbers():
    # vytvorim prazdny set
    values = set()
    # naplnim prazdny set 6 cislami{values} pomocou WHILE
    while len(values) < 6:
        # prida jednotlive cislo do setu
        values.add(random.randint(1, 20))
    return values


# porovnam zhodu medzi user a lottery - set.intersection
user_numbers = get_user_numbers()
lottery_numbers = create_lottery_numbers()
print(user_numbers)
print(lottery_numbers)
# porovnanie
matched_numbers = user_numbers.intersection(lottery_numbers)
print(
    "Trafil si cisla {}. Celkova vyhra je {}".format(
        matched_numbers, 100 ** len(matched_numbers)
    )
)
