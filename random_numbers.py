import random

magic_number = [random.randint(0,9)]

def ask_user_and_check_number():
    user_number = int(input("Zadaj svoje cislo: "))
    if user_number in magic_number:
        return "Uhadol si cislo, GRATULUJEM :)"
    if user_number not in magic_number:
        return "Neuhadol si cislo, skus stastie znova"

def run_program_x_times(pokusy):
    for pokus in range(pokusy):
        print("Toto je tvoj {} pokus".format(pokus))
        print(ask_user_and_check_number())

user_pokusy = int(input("Zadaj pocet pokusov: "))
run_program_x_times(user_pokusy)
print("Hladane cislo je {}".format(magic_number))
