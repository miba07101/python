# Hangman hra

import random

# hangman obrazky
hangman_stages = [
    """
    +---+
        |
        |
        |
       ===""",
    """
    +---+
    O   |
        |
        |
       ===""",
    """
    +---+
    O   |
    |   |
        |
       ===""",
    """
    +---+
    O   |
   /|   |
        |
       ===""",
    """
    +---+
    O   |
   /|\  |
        |
       ===""",
    """
    +---+
    O   |
   /|\  |
   /    |
       ===""",
    """
    +---+
    O   |
   /|\  |
   / \  |
       ===""",
]

# pocet zivotov / pokusov
# hodnota 6 podla poctu obrazkov hangman_stages
lives = 7

# vytvorenie zoznamu slov zo suboru 21-Hangman-words.txt
with open("21-Hangman-words.txt") as f:
    words_list = f.read().splitlines()

# vyber nahodneho slova zo zoznamu
word_ran = words_list[random.randint(0, len(words_list) - 1)]
print(word_ran)

# vytvorenie skryteho slova z podtrzitok
word_hidden = ""
for one_letter in word_ran:
    word_hidden += "_"

# musim vytvorit list pre moznost zmeny pismen
word_hidden_list = list(word_hidden)

# Uvodne uvitanie
print("Vitaj v hre HANGMAN")
print(f"{hangman_stages[6]}")
print(f"Tvoje slovo ma {len(word_ran)} pismen")
print(f"{word_hidden}\n")

# hadaj slovo
while "_" in word_hidden_list:
    guess_letter = input("Zadaj pismeno: ").lower()
    for index in range(0, len(word_ran)):
        one_letter = word_ran[index]
        if guess_letter == one_letter:
            word_hidden_list[index] = guess_letter

    # zmena listu na string
    # je to opat premena toho co uz bolo zmenene, ale este neboli vysvetlene
    # funkcie, preto to je v kode napisane 2 krat
    word_hidden = ""
    for item in word_hidden_list:
        word_hidden += item

    # kontrola zivotov
    if guess_letter not in word_ran:
        lives -= 1
        # musel som dat abs(lives-6) pretoze inac by som musel prehodit obrazky
        print(hangman_stages[(7 - lives) - 1])
        print(f"Zostavajuci pocet zivotov je {lives}")

    if lives == 0:
        print("Skoda, prehral si :(")
        # break ukonci cyklus while
        break

    # print(word_hidden_list)
    print(f"\n{word_hidden}\n")

if "_" not in word_hidden_list:
    print("HURAAAA! VYHRAL SI :)")
