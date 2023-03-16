import random

# zvol si kamen, noznice alebo papier
user = int(input("Zvol si: 0 - kamen, 1 - papier, 2 - noznice\n"))
computer = random.randint(0, 2)

# ASCII art https://www.asciiart.eu/people/body-parts/hand-gestures
rock = """
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)

        """

paper = """
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)

         """

scissor = """
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)

           """

asci_list = [rock, paper, scissor]
pick_list = ["kamen", "papier", "noznice"]

# vykreslenie obrazkov pre uzivatela
user_asci = asci_list[user]
user_pick = pick_list[user]
print(f"Zvolil si {user_pick}:\n{user_asci}")

# vykreslenie obrazkov pre pocitac
computer_asci = asci_list[computer]
computer_pick = pick_list[computer]
print(f"Pocitac zvolil {computer_pick}:\n{computer_asci}")

# Podmienka kto vyhral
if user == computer:
    print("Remiza")
elif user == 0 and computer == 1:
    print("Prehral si")
elif user == 0 and computer == 2:
    print("Vyhral si")
elif user == 1 and computer == 0:
    print("Vyhral si")
elif user == 1 and computer == 2:
    print("Prehral si")
elif user == 2 and computer == 0:
    print("Prehral si")
elif user == 2 and computer == 1:
    print("Vyhral si")

# iny zapis
# if user == 0:
#     if computer == 1:
#         print("Prehral si")
#     elif computer == 2:
#         print("Vyhral si")
#     else:
#         print("Remiza")
# elif user == 1:
#     if computer == 0:
#         print("Vyhral si")
#     elif computer == 2:
#         print("Prehral si")
#     else:
#         print("Remiza")
# else:
#     if computer == 0:
#         print("Prehral si")
#     elif computer == 1:
#         print("Vyhral si")
#     else:
#         print("Remiza")
