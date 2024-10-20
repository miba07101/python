numbers = [3, 5, 2, -1, 4]
print(numbers)

for i in range(0, len(numbers)):
    print(numbers[i])
    for j in range(i, len(numbers)):
        # print(numbers[i], numbers[j])
        if numbers[i] > numbers[j]:
            numbers[i], numbers[j] = numbers[j], numbers[i]
            # print(numbers[i], numbers[j])
            print(numbers)

print(numbers)
