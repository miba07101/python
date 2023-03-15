# GUESS GAME - hadacia hra
import random
import os


def random_num():
    random_number = random.randint(1, 100)
    return random_number


def guess_num(guess_number, user_number):
    if user_number not in range(1, 101):
        return "Tipujes mimo rozsah cisel :("
    elif user_number < guess_number:
        return "Nizke cislo"
    elif user_number > guess_number:
        return "Vysoke cislo"
    elif user_number == guess_number:
        return "Hura uhadol si cislo :)"


def difficulty_lvl(difficulty):
    difficulty_dic = {"easy": 10, "hard": 5}
    return difficulty_dic[difficulty]


def guess_game():
    print("Vitajte v hre Guess secret number.")
    print("Myslim si cislo od 1 do 100. Skus uhadnut ake :)")

    user_difficulty = input("Vyber si obtiaznost. [easy / hard]: ")
    life = difficulty_lvl(user_difficulty)
    print(f"Pocet pokusov je: {life}")
    result_random_num = random_num()
    # print(result_random_num)
    lets_continue = ""

    while life != 0:
        user_num = int(input("Tipni si cislo: "))
        result_guess = guess_num(result_random_num, user_num)
        print(result_guess)
        if result_guess != "Hura uhadol si cislo :)":
            life -= 1
            print(f"Pocet zostavajucich pokusov je: {life}")
        else:
            break
    if life == 0:
        print("Skoda neuhadol si cislo :(")
        print(f"Hadane cislo bolo: {result_random_num}")

    lets_continue = input("Chces pokracovat? [yes / no]: ")

    if lets_continue == "yes":
        os.system("clear")
        guess_game()

    elif lets_continue == "no":
        os.system("clear")


guess_game()
