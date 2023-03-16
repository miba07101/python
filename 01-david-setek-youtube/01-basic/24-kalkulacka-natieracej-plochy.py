# urcte pocet plechoviek farby potrebnych na natretie steny
# 1 plechovka je na 5 m2
import math


def paint_calculator(height, width, cover):
    area = height * width
    pocet_plechoviek = math.ceil(area / cover)
    print(f"Na vymalovanie budes potrebovat {pocet_plechoviek} ks plechoviek s farbou")


wall_height = float(input("Zadaj vysku steny [m]: "))
wall_width = float(input("Zadaj sirku steny [m]: "))
plechovka = 5

# volanie fcie s keyword argumentmi
paint_calculator(cover=plechovka, height=wall_height, width=wall_width)
