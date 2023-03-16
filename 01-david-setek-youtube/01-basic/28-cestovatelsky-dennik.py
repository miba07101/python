# ulohou je vytvorit funkciu, ktora mi prida dalsie udaje do existujucich udajov
# existujuci list
travel_diary = [
    {
        "country": "Spain",
        "visited_cities": ["Madrid", "Leon", "Valencia"],
        "visits": 2,
    },
    {
        "country": "France",
        "visited_cities": ["Paris", "Nice", "Rennes"],
        "visits": 5,
    },
]


# funkcia na pridanie udajov o navstivenej krajine
def add_to_travel_diary(add_country, add_cities, add_visits):
    add_cities_list = add_cities.split(", ")
    new_dict = {}
    new_dict["country"] = add_country
    new_dict["visited_cities"] = add_cities_list
    new_dict["visits"] = add_visits

    travel_diary.append(new_dict)


country = input("Napis krajinu, ktoru si navstivil:\n")
cities = input("Napis mesta, ktore si navstivil [oddel ich ciarkou a medzerou]:\n")
no_visits = int(input("Napis pocet navstev]:\n"))

add_to_travel_diary(add_country=country, add_cities=cities, add_visits=no_visits)
print(travel_diary)
