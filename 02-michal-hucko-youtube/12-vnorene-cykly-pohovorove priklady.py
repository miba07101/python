# kod, ktory na zaklade 2 premennych vyska a sirka vyplni pole *
rows = 8
columns = 3

for one_row in range(0, rows):
    for one_column in range(0, columns):
        # end je optional parameter
        # defaultne je nastaveny aby sa vypisal kazdy print do noveho riadku "\n"
        # ak dam iba end="" tak bude vypisovat kazdu iteraciu v tom istom riadku
        print("*", end="")
    # skoci do noveho riadku
    print()


# pyramida :)
count = 1
while True:
    if count <= rows:
        stars = count * ("*")
        print(stars)
        count += 1
    else:
        break

count = rows - 1
while True:
    if count > 0:
        stars = count * ("*")
        print(stars)
        count -= 1
    else:
        break

# pyramida - iny zapis
for row_value in range(1, rows + 1):
    for star in range(0, row_value):
        print("*", end="")
    print()
for row_value in range(rows - 1, 0, -1):
    for star in range(0, row_value):
        print("*", end="")
    print()


# pyramida s cislami :)
# zapis skrz for podmienku
for row_value in range(1, rows + 1):
    for number in range(1, row_value + 1):
        print(number, end="")
        # prida medzeru medzi cisla
        print(" ", end="")
    print()
for row_value in range(rows - 1, 0, -1):
    for number in range(1, row_value + 1):
        print(number, end="")
        # prida medzeru medzi cisla
        print(" ", end="")
    print()
