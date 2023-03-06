# zadaj svoj vek
age = int(input("Zadaj svoj vek:\n"))
# priemerna dlzka zivota
average = 90

zivot = 90 - age
mesiace = zivot * 12
tyzdne = mesiace * 4
dni = zivot * 365

print(
    f"Vas vek je {age}.\n\
Priemer je {average} rokov,\n\
Zostava Ti este {zivot} rokov,\n\
{mesiace} mesiacov,\n\
{tyzdne} tyzdnov alebo\n\
{dni} dni."
)
