# Dockstring
# sluzi na popisanie funkcie


def sum(num1, num2):
    # dockstring:
    """Sucet dvoch cisel"""
    return num1 + num2


result = sum(1, 2)
# ine formy zapisu
# result = sum(float(input("prve cislo: ")), float(input("druhe cislo ")))
# result = sum(num1=float(input("prve cislo: ")), num2=float(input("druhe cislo ")))
print(result)
