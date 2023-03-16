# funkcia s jednym parametrom
# definujem si vlastnu funkciu, napr. na oslovenie
def grreting(name):
    print(f"Ahoj ja som {name}")
    if name == "Milan":
        print("... a som KRAL :)")
    elif name == "Vierka" or name == "Viera":
        print("... a som ZOPKACIK :)")


name = input("Zadaj svoje meno: ")
grreting(name)

# pozn:
# 1) definujem funkciu
#     def greeting(name)
#     name - je parameter funkcie, v podstate premenna
# 2) definujem premennu (variable)
#     name = ...
#     name - je premenna (variable)
# 3) volam funkciu
#     greeting(name)
#     name - je argument funkcie, v podstate to co zadam do premennej
