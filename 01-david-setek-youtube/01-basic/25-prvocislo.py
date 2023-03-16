# zisti ci zadane cislo je prvocislo
# prvocislo je delitelne iba 1 a samym sebou
# number = int(input("Zadaj cislo\n"))
#
#
# def prime_number(number):
#     if number > 2 and number % 2 == 0:
#         print(f"Cislo {number} nie je prvocislo")
#     else:
#         print(f"Cislo {number} je prvocislo")
#
#
# prime_number(number)

# sposob podla videa
# zistujem ci zvolene cislo je delitelne akymkolvek cislom v rozsahu
# od 1 az po zvolene cislo


def prime_number_checker(number):
    result = "Je to prvocislo"
    # zistim ci zvolene cislo je delitelne v danom rozsahu
    for one_number in range(2, number):
        # ak je cislo delitelne bez zvysku
        if number % one_number == 0:
            result = "Nie je to prvocislo"
    print(result)


n = int(input("Zadaj cislo\n"))
prime_number_checker(n)
