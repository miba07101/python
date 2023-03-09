# funkcie s viacerymi parametrami
def meno_mesto(name, location):
    print(f"Ahoj, som {name} a pochadzam z mesta {location}")


# positional arguments
# !!! zalezi na poradi argumentov
# spravne priradenie argumentov
meno_mesto("Milan", "Michalovce")
# nespravne priradenie
meno_mesto("Michalovce", "Milan")

# keyword arguments
# !!! nezalezi na poradi
# vzdy sa argumenty priradia spravne
meno_mesto(location="Michalovce", name="Milan")
