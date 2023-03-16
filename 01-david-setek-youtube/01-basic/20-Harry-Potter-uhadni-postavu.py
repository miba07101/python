# uhadni postavu z filmu Harry Potter
import random

# zoznam postav - list
characters_list = [
    "Harry",
    "Ron",
    "Hermiona",
    "Draco",
    "Brumbal",
    "Snake",
    "Voldemort",
]

print(f"Uhadni postavu z filmu Harry Potter. Moznosti su:\n{characters_list}")

# vygeneruje nahodne meno postavy
character_ran = characters_list[random.randint(0, len(characters_list) - 1)]

# vytvorenie prazdnej premennej pre hadane meno
character_guess = ""

# vytvorenie premennej pre pocet pokusov hadania
guess_count = 3
print(f"Pozor! Na uhadnutie mas {guess_count} pokusy(ov).")

# while - cyklus bezi pokial je vysledok podmienky true,
# resp pokial nenastane false
# cize pokial bude hadane meno postavy odlizne od nahodne vybraneho mena postavy
while character_guess != character_ran:
    # pokial pocet pokusov je rozny od nuly
    if guess_count != 0:
        character_guess = input("Zadaj meno postavy: ")
        # odpocitam 1 pokus
        guess_count -= 1
    else:
        print(
            f"Neuhadol si!\nVycerpal si pocet pokusov.\nHladane meno bolo: {character_ran}"
        )
        # kedze som vycerpal pocet pokusov, ale while cyklus stale bezi
        # (nenasiel som zhodu, cize moja while podmienka je true)
        # preto pre ukoncenie while cyklu:
        break

    # podmienka, ze som uhadol meno
    if character_guess == character_ran:
        print("Uhadol si! Gratulujem :)")
    else:
        print("Hadaj znova.")
