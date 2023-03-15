# prestupny rok
# je delitelny 4
# nesmie byt delitelny 100
# ak je delitelny 4 a 100 (mal by byt neprestupny) ale ak je zaroven
# delitelny 400 tak je tiez prestupny

# ulohou je vypisat aj dni v mesiaci
# ak je prestupny rok tak februar bude mat 29 dni

days_in_month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

rok = int(input("Zadaj rok:\n"))
mesiac = int(input("Zadaj mesiac:\n"))


def prestupny_rok(year, month):
    if year % 4 == 0 or year % 400 == 0:
        days_in_month[1] = 29
        return f"Rok {year} je prestupny.\
                {month} mesiac ma {days_in_month[month-1]} dni"
    else:
        return f"Rok {year} je neprestupny.\
                {month} mesiac ma {days_in_month[month-1]} dni"


result = prestupny_rok(rok, mesiac)
print(result)
