height = float(input("Zadaj svoju vysku [m]\n"))
weight = int(input("Zadaj svoju vahu [kg]\n"))

# BMI zaokruhli na 1 desatinne
bmi = round(weight / height**2, 1)

if bmi < 18.5:
    print(f"Vas BMI je {bmi}. Je to PODVAHA")
elif bmi < 24.9:
    print(f"Vas BMI je {bmi}. Je to NORMAL")
elif bmi < 29.9:
    print(f"Vas BMI je {bmi}. Je to NADVAHA")
elif bmi < 34.9:
    print(f"Vas BMI je {bmi}. Je to OBEZITA")
else:
    print(f"Vas BMI je {bmi}. Je to EXTREMNA OBEZITA")
