weight = input("Zadaj svoju vahu [kg]\n")
height = input("Zadaj svoju vysku [m]\n")

# BMI zaokruhli na 3 desatinne
bmi = round(int(weight) / float(height) ** 2, 3)

print("Vas BMI je: " + str(bmi))
