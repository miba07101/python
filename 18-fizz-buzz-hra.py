# cislo delitelne 3 = fizz
# cislo delitelne 5 = buzz
# cislo delitelne 3 a 5 = fizzbuzz
# inac vypisat bezne cislo

# vytvorim range 1 az 100
for item in range(1, 101):
    # overim ci cislo je delitelne 3 a 5 zaroven
    if item % 3 == 0 and item % 5 == 0:
        print("FizzBuzz")
    # ci je cislo delitelne 3
    elif item % 3 == 0:
        print("Fizz")
    # ci je cislo delitelne 5
    elif item % 5 == 0:
        print("Buzz")
    else:
        print(item)
