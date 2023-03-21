class Robot:
    # constructor
    # funkcia, ktora sa inicializuje hned pri vytvoreni objektu pomoc class
    def __init__(self, batery, arm_lenght):
        self.batery = batery
        self.arm_lenght = arm_lenght
        # atribut, ktory je rovnaky pre kazdy objekt
        # zadam rovno ako cislo/hodnotu
        self.ukony_do_kontroly = 1000

    def krok_vpred(self):
        print("Robot urobil krok vpred")
        # odpocitam jeden ukon
        self.ukony_do_kontroly -= 1
        print(f"Zostavajuci pocet ukonov do kontroly: {self.ukony_do_kontroly}")

    def krok_vzad(self):
        print("Robot urobil krok vzad")
        # odpocitam jeden ukon
        self.ukony_do_kontroly -= 1
        print(f"Zostavajuci pocet ukonov do kontroly: {self.ukony_do_kontroly}")


# vytvorenie objektu robot_1 podla class/triedy Robot
robot_1 = Robot(48, 0.5)

robot_1.krok_vpred()
robot_1.krok_vpred()
robot_1.krok_vpred()
robot_1.krok_vzad()
