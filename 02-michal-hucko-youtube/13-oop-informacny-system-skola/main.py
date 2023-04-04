from information_system import InformationSystem
from personal import Teacher


def print_menu():
    print("\n****************************************************")
    print("Vitajte v systeme")
    print("Stlacte prosim:")
    print("\t[0] Pre pridanie kurzu")
    print("\t[1] Pre pridanie ucitela")
    print("\t[2] Pre pridanie studenta")
    print("\t[3] Pre ukoncenie prace so systemom")
    print("\t[4] Pre zoznam kurzov")
    print("\t[5] Pre zoznam ucitelov")
    print("\t[6] Pre zoznam studentov")


# vytvorenie objektu Informacneho Systemu
# len kvoli funkcnosti zacinam s nacitanim 2 ucitelov
info_system = InformationSystem(
    teachers=[
        Teacher("Petr", "Petrov", "ing"),
        Teacher("Jan", "Janov", "ing"),
    ]
)

while True:
    print_menu()
    try:
        menu_choice = int(input("Menu choice: "))
        if menu_choice < 0 or menu_choice >= 7:
            raise Exception("Wrong menu choice")
    except Exception as e:
        print(e)
        print("Please choose valid menu choice")
        continue
    if menu_choice == 3:
        print("Good Bye")
        break
    elif menu_choice == 0:
        info_system.create_courses()
    elif menu_choice == 1:
        info_system.create_teachers()
    elif menu_choice == 2:
        info_system.create_students()
    elif menu_choice == 4:
        print("Courses are:")
        for course in info_system.courses:
            print(course)
    elif menu_choice == 5:
        print("Teachers are:")
        for teacher in info_system.teachers:
            print(teacher)
    elif menu_choice == 6:
        print("Students are:")
        for student in info_system.students:
            print(student)
