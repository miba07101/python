# vytvorte 3 objekty (instance) podla class
# napiste funkciu na urcenie najstarsieho psa
# vypiste vyslednu vetu "Vek najstarsieho psa je: "
class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age


# def oldest_dog(all_dogs):
#     max_age = 0
#     for one_dog in all_dogs:
#         dog_age = int(one_dog.age)
#         if max_age < dog_age:
#             max_age = dog_age
#     # print(f"Vek najstarsieho psa je: {max_age}")
#     return max_age


# iny sposob zapisu oldest_dog funkcie s vyuzitim f-cie max
def oldest_dog(all_dogs_age):
    return max(all_dogs_age)


dog_list = []
for index in range(3):
    index += 1
    dog_name = input(f"Zadaj meno psa c.{index}: ")
    dog_age = input(f"Zadaj vek psa c.{index}: ")
    dog = Dog(dog_name, dog_age)
    # dog_list.append(dog)
    # list pre funkciu oldest_dog s f-ciou max
    # list obsahujuci iba vek psa
    dog_list.append(int(dog.age))

print(f"Vek najstarsieho psa je: {oldest_dog(dog_list)}")
