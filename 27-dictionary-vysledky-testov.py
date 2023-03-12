students_results = {
    "Harry": 85,
    "Ron": 71,
    "Hermiona": 98,
    "Draco": 69,
}

# student = input("Zadaj meno studenta [Harry, Ron, Hermiona, Draco]:\n")
#
# for key in students_results:
#     if key == student:
#         result = students_results[key]
#         if result < 71:
#             print("Nesplnene")
#         elif result < 80:
#             print("Splnene")
#         elif result < 90:
#             print("Vynikajuce")
#         elif result <= 100:
#             print("Excelentne")

# vytvorenie dictioanry s vysledkami
# inajprv vytvorim prazdny dict, do ktoreho budem vkladat vysledky
description_results = {}

for key in students_results:
    result = students_results[key]
    if result < 71:
        description_results[key] = "Nesplnene"
    elif result < 80:
        description_results[key] = "Splnene"
    elif result < 90:
        description_results[key] = "Vynikajuce"
    elif result <= 100:
        description_results[key] = "Excelentne"

print(description_results)
