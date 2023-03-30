# LAMBDA funkcia
# nema return - aj tak vracia vysledok
# nema nazov
# lambda x:print(x)
# ------------------------------------------------------------------------------

# vstup pre vsetky ukazky
numbers = [2, 3, 4, 5, 6]

# ------------------------------------------------------------------------------
# MAP funkcia
# map funkcia vracia pozmeneny prvok vstupe
# prvy argument map funkcie je funkcia, ktoru aplikujeme na kazdy prvok zoskupenia, napr. listu
# map(funkcia, zoskupenie)


# pr. sprav druhu mocninu cisel
def return_power(number, power=2):
    return number**power


# pouzitie MAP
# musim zmenit na list pomocou "list konstruktoru""
print(list(map(return_power, numbers)))

# vyuzitie LAMBDA namiesto return_power()
print(list(map(lambda number: number**2, numbers)))

# ------------------------------------------------------------------------------
# FILTER funkcia
# pouziva sa na vyfiltrovanie elemntov
# funkcia vracia True alebo False pre prvok na vstupe (alternativou True je 1 a False je 0)
# filter(funkcia, zoskupenie)


# pr. vyfiltruj parne cisla
def is_even(number):
    return number % 2 == 0


print(list(filter(is_even, numbers)))
# pomocou lambda funkcie
print(list(filter(lambda number: number % 2 == 0, numbers)))

# ------------------------------------------------------------------------------
# REDUCE funkcia
# funkcia specifikuje ako sa ma zredukovat zoskupenie
# je zvacsa tvorena medzivysledkovou premennou a prvkom
# !!! musim ju importovat
from functools import reduce


# pr. sucet
def reduce_sum(a, b):
    return a + b


# iterativne zrata jednotlive polozky v liste numbers a vyhodi vysledok ako sucet vsetkych poloziek
print(reduce(reduce_sum, numbers))
# pomocou lambda funkcie
print(reduce(lambda a, b: a + b, numbers))

# ------------------------------------------------------------------------------
# pr. pole faktorialovych prvkov pomocou map, reduce
numbers = range(1, 11)

# potrebujem pre kazde cislo vytvorit zoskupenie od 1 po dane cislo
# lambda number: range(1, number)
print(list(map(lambda number: range(1, number + 1), numbers)))

# aplikujem REDUCE funkciu, ktora na znasobi kazdy prvok vytvoreneho rozsahu (pomocou lambda)
# a - 1 prvok z vytvoreneho rozshau (range)
# b - 2 prvok z vytvoreneho rozshau (range)
print(
    list(map(lambda number: reduce(lambda a, b: a * b, range(1, number + 1)), numbers))
)
