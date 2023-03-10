# 26 pismen - mala abeceda
alphabet = [
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
]


# funkcia na sifrovanie
# def encryption(sentence, shift):
#     sentence_encryption = ""
#     for one_letter in sentence:
#         for index in range(0, len(alphabet)):
#             if one_letter == alphabet[index]:
#                 position = (index + shift) % len(alphabet)
#                 sentence_encryption += alphabet[position]
#     print("____________________________________________\n")
#     print(f"Sifrovana sprava: {sentence_encryption}\n")


# sposob podla videa
def encryption(sentence, shift):
    shifted_text = ""
    for one_letter in sentence:
        # aby to vyriesilo medzery
        if one_letter != " ":
            # priradim index pismena z listu alphabet
            # cize nepotrebujem podmienku na zistovanie
            # ci sa pismeno nachadza v liste/zozname ako som to robil ja
            index = alphabet.index(one_letter)
            # novy index posunuty o shift
            new_index = (index + shift) % len(alphabet)
            # priradim pismeno do "posunuteho" textu
            shifted_text += alphabet[new_index]
        else:
            # pridaj do sifrovaneho textu medzeru
            shifted_text += one_letter
    print("____________________________________________\n")
    print(f"Sifrovana sprava: {shifted_text}\n")


# funkcia na desifrovanie
# def decryption(sentence, shift):
#     sentence_decryption = ""
#     for one_letter in sentence:
#         for index in range(0, len(alphabet)):
#             if one_letter == alphabet[index]:
#                 position = (index - shift) % len(alphabet)
#                 sentence_decryption += alphabet[position]
#     print("____________________________________________\n")
#     print(f"Desifrovana sprava: {sentence_decryption}\n")


# sposob podla videa
def decryption(sentence, shift):
    shifted_text = ""
    for one_letter in sentence:
        if one_letter != " ":
            index = alphabet.index(one_letter)
            new_index = (index - shift) % len(alphabet)
            shifted_text += alphabet[new_index]
        else:
            shifted_text += one_letter
    print("____________________________________________\n")
    print(f"Desifrovana sprava: {shifted_text}\n")


# vytvorenie cyklu na pokracovanie
# vytvorim premennu do ktorej na zaciatok vlozim "natvrdo" hodnotu, napr. y (yes)
# to mi spusti cyklus while, ktory bude bezat dovtedy kym je podmienka splnena
pokracovat = "y"

while pokracovat == "y":
    # vyber ci chces encrypt alebo decrypt
    choose = input("Chces sifrovat alebo desifrovat spravu [s/d]?\n")
    # zadaj text
    text = input("Zadaj text:\n").lower()
    # zadaj posun
    posun = int(input("Zadaj posun sifrovania [1-10]:\n"))

    if choose == "s":
        encryption(sentence=text, shift=posun)
        pokracovat = input("Chces pokracovat [y/n]?\n")
    # !!! elif dam namiesto else preto, pretoze, keby niekto urobil preklep,
    # tak sa nic nespusti
    # ak by bolo else, tak pri preklepe by sa spustilo f-cia decryption
    elif choose == "d":
        decryption(sentence=text, shift=posun)
        pokracovat = input("Chces pokracovat [y/n]?\n")

    if pokracovat == "n":
        break
