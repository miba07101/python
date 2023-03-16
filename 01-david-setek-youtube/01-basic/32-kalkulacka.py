# kalkulacka

import os


# funkcie matematickych operacii
def sum(num1, num2):
    """sucet 2 cisel"""
    return num1 + num2


def sub(num1, num2):
    """odcitanie 2 cisel"""
    return num1 - num2


def mult(num1, num2):
    """nasobenie 2 cisel"""
    return num1 * num2


def div(num1, num2):
    """delenie 2 cisel"""
    return num1 / num2


# vytvorenie dictionary symbolov matematickych operacii
# key = symbol value = funkcia mat operacii
math_symbols = {"+": sum, "-": sub, "*": mult, "/": div}


def calculator():
    # zadam vstupne udaje
    user_num1 = float(input("Zadaj 1 cislo: "))

    # vytvorenie cyklu pre pokracovanie v matematickych operaciach
    lets_continue = "yes"

    while lets_continue == "yes":
        # vstupne udaje
        user_operation = input("Zadaj matematicku operaciu [+, -, *, /]: ")
        user_num2 = float(input("Zadaj 2 cislo: "))

        # podla zvoleneho symbolu mat operacie vyhladam pozadovanu operaciu v
        # dic math_symbol a priradim jej funkciu mat operacie
        math_operation = math_symbols[user_operation]

        # vysledok s priradenim vstupnych udajov
        result = math_operation(num1=user_num1, num2=user_num2)
        print(f"Vysledok: {user_num1} {user_operation} {user_num2} = {result}")

        # otazka ci chcem pokracovat alebo zacat odznova
        lets_continue = input("Chces pokracovat 'yes' alebo zacat znova 'no': ")
        # podmienka
        # ak pokracujem tak do 1 cisla vlozi vysledok z predchadzajucej operacie
        # ak nepokracujem tak vycisti obrazovku
        if lets_continue == "yes":
            user_num1 = result
        else:
            os.system("clear")
            # !!! RECURSION - RECURSIVE FUNCTION !!!
            # rekurzia funkcie - cize znova vyvolanie seba samej funkcie
            calculator()


# zavolanie funkcie
calculator()
