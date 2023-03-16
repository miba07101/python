import random

data = [
    {
        "name": "Instagram",
        "follower_count": 501,
        "description": "Sociální platforma",
        "country": "USA",
    },
    {
        "name": "Facebook",
        "follower_count": 4,
        "description": "Sociální platforma",
        "country": "USA",
    },
    {
        "name": "Cristiano Ronaldo",
        "follower_count": 436,
        "description": "Fotbalový hráč",
        "country": "Portugal",
    },
    {
        "name": "Dwayne Johnson",
        "follower_count": 161,
        "description": "Herec a wrestler",
        "country": "USA",
    },
    {
        "name": "Harry Potter film",
        "follower_count": 8,
        "description": "Film",
        "country": "USA",
    },
    {
        "name": "Kim Kardashian",
        "follower_count": 307,
        "description": "Podnikatelka",
        "country": "USA",
    },
    {
        "name": "Lionel Messi",
        "follower_count": 324,
        "description": "Fotbalista",
        "country": "Argentina",
    },
    {
        "name": "Neymar",
        "follower_count": 158,
        "description": "Fotbalista",
        "country": "Brazilie",
    },
    {
        "name": "Eminem",
        "follower_count": 40,
        "description": "Hudebník",
        "country": "USA",
    },
    {
        "name": "Justin Bieber",
        "follower_count": 193,
        "description": "Hudebník",
        "country": "Canada",
    },
    {
        "name": "Emma Watson",
        "follower_count": 111,
        "description": "Herečka",
        "country": "Francie",
    },
]


def subject_generator(subject_data):
    index = random.randint(0, len(subject_data) - 1)
    subject = subject_data[index]
    return subject


def printing_options(sub_a, sub_b):
    print(f"Porovnajte A: {sub_a['name']}, {sub_a['description']}")
    print(f"Porovnajte B: {sub_b['name']}, {sub_b['description']}")
    # len testovaci vypis poctu followerov
    # print(f"test A followers: {sub_a['follower_count']}")
    # print(f"test B followers: {sub_b['follower_count']}")


def game():
    subject_a = subject_generator(data)
    subject_b = subject_generator(data)

    right_answer = ""
    score = 0
    lets_continue = True
    # pokial je lets_continue = True tak bezi cyklus
    # nie je nutne pisat True v podmienke,
    # pretoze ju spusti len ked je vysledok True
    while lets_continue:
        printing_options(sub_a=subject_a, sub_b=subject_b)
        user_guess = input("Tipni kto ma viac followerov? [A / B]: ").lower()

        if subject_a["follower_count"] > subject_b["follower_count"]:
            right_answer = "a"
        else:
            right_answer = "b"

        # do subjectu_a zadam hodnoty subjectu_b
        subject_a = subject_b

        if user_guess == right_answer:
            score += 1
            subject_b = subject_generator(data)
            print(f"Hura, uhadol si. Tvoje score je: {score}")
        else:
            print(f"Neuhadol si. Tvoje konecne skore je: {score}")
            # neuhadol si
            # nastavim lets_continue = false
            # ukonci cyklus while
            lets_continue = False


# spustim funkciu game
game()
