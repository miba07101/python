numbers = [3, 4, 1, 2, 5]
print(numbers)

for i in range(0, len(numbers)):
    # print(numbers[i])
    swapped = False
    for j in range(0, len(numbers) - i - 1):
        # print(numbers)
        if numbers[j] > numbers[j + 1]:
            numbers[j], numbers[j + 1] = numbers[j + 1], numbers[j]
            # print(numbers[i], numbers[j])
            # print(numbers)
            swapped = True

    if swapped == False:  # if not swapped: - to iste len iny zapis
        break

print(numbers)

items = [3, 4, 1, 2, 5]
items.sort()
print(items)
