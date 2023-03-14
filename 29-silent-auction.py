# riesenie podla videa aj s vycistenim terminalu
import os

# vytvorenie prazdneho dictionary pre prihadzujucich
bidders = {}

# cyklus pre naplnenie dictionary prihadzujucimi
lets_continue = "yes"
while lets_continue == "yes":
    au_name = input("Zadajte Vase meno:\n")
    au_bid = int(input("Zadajte ponukanu sumu:\n"))
    bidders[au_name] = au_bid
    lets_continue = input("Je dalsi zaujemca? [yes/no]:\n")
    if lets_continue == "no":
        os.system("clear")
# print(bidders)


# funkcia pre najdenie najvyssej ponuky
def highest_bid(bidders_dic):
    highest_bid = 0
    winner = ""
    for key in bidders_dic:
        # vypise mi z value podla key z dictionary
        # cize vypise mi hodnotu ponuky podla mena
        if bidders_dic[key] > highest_bid:
            highest_bid = bidders_dic[key]
            winner = key
    print(f"Najvyssia ponuka je od: {winner} v hodnote {highest_bid} eur")


highest_bid(bidders)

# MOJE RIESENIE - komplikovanejsie :)
# # vytvorenie listu s prvotnym dictionary
# # k nemu pomocou funkcie add_auctioner budem pridavat prihadzujucich v aukcii
# au_list = [{"name": "0", "value": 0}]
#
#
# # funkcia na naplnenie prihadzujucich v aukcii
# def add_auctioner(name, value):
#     new_au_dic = {}
#     new_au_dic["name"] = name
#     new_au_dic["value"] = value
#     au_list.append(new_au_dic)
#
#
# # cyklus pre zadfavanie prihadzujucich v aukcii
# next_au = "yes"
# while next_au == "yes":
#     au_name = input("Zadajte Vase meno:\n")
#     au_value = int(input("Zadajte ponukanu sumu:\n"))
#     add_auctioner(name=au_name, value=au_value)
#     next_au = input("Je dalsi zaujemca? [yes/no]:\n")
#
#     if next_au == "no":
#         break
# # print(au_list)
#
# # hladanie najvyssej ponuky
# highest_bind = 0
# for index in range(0, len(au_list)):
#     index_bind = au_list[index]["value"]
#     if highest_bind < index_bind:
#         highest_bind = index_bind
#         highest_bind_index = index
#
# print(au_list[highest_bind_index]["name"])
