class Robot:
    # constructor
    # funkcia, ktora sa inicializuje hned pri vytvoreni objektu pomoc class
    def __init__(self, batery, arm_lenght):
        self.batery = batery
        self.arm_lenght = arm_lenght
        # atribut, ktory je rovnaky pre kazdy objekt
        # zadam rovno ako cislo/hodnotu
        self.ukony_do_kontroly = 1000


# vytvorenie objektu robot_1 podla class/triedy Robot
robot_1 = Robot(48, 0.5)

print(robot_1.batery)
print(robot_1.dni_do_opravy)
