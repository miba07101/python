import random

letters = [
    "a",
    "b",
    "c",
    "d",
    "e",
    "f",
    "g",
    "h",
    "i",
    "j",
    "k",
    "l",
    "m",
    "n",
    "o",
    "p",
    "q",
    "r",
    "s",
    "t",
    "u",
    "v",
    "w",
    "x",
    "y",
    "z",
    "A",
    "B",
    "C",
    "D",
    "E",
    "F",
    "G",
    "H",
    "I",
    "J",
    "K",
    "L",
    "M",
    "N",
    "O",
    "P",
    "Q",
    "R",
    "S",
    "T",
    "U",
    "V",
    "W",
    "X",
    "Y",
    "Z",
]
numbers = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
special_char = ["%", "#", "$", "!", "&", "(", ")", "*", "+", "?"]

print("Generator hesiel!")
num_letters = int(input("Kolko pismien chcete v hesle?\n"))
num_numbers = int(input("Kolko cisel chcete v hesle?\n"))
num_char = int(input("Kolko znakov chcete v hesle?\n"))

# nahodny vyber pismen, cislic, znakov
password_list = []
for index in range(1, num_letters):
    ran_index = random.randint(0, len(letters) - 1)
    password_list.append(letters[ran_index])

for index in range(1, num_numbers):
    ran_index = random.randint(0, len(numbers) - 1)
    password_list.append(numbers[ran_index])

for index in range(1, num_char):
    ran_index = random.randint(0, len(special_char) - 1)
    password_list.append(special_char[ran_index])

print(password_list)

# iny sposob predchadzajuceho
# # nahodny vyber znakov pomocou funkcie random.choices()
# letters_ran_list = random.choices(letters, k=num_letters)
# numbers_ran_list = random.choices(numbers, k=num_numbers)
# char_ran_list = random.choices(special_char, k=num_char)

# # vytvorenie jedneho listu z 3 listov
# # to je len pomocne, pretoze to vypisuje vysledok ako list v liste
# # potrebujem potom cyklus pre vytvorenie len jedneho listu
# all_list = [letters_ran_list, numbers_ran_list, char_ran_list]
#
# # cyklus pre vytvorenie jedneho listu
# # polozky z 3 listov v podstate prepisem do jedneho listu
# password_list = []
# for item in all_list:
#     password_list += item
# print(password_list)

# funkcia random.shuffle pre nahodne rozhodenie poloziek v liste
random.shuffle(password_list)
print(password_list)

# prevod listu na string
password = ""
for item in password_list:
    password += item

# vypisanie vysledku
print(f"Heslo je: {password}")
