from personal import Student, Teacher
from course import Course


# vytvorim triedu InformationSystem
class InformationSystem:
    def __init__(self, courses=[], students=[], teachers=[]):
        self.courses = courses
        self.students = students
        self.teachers = teachers

    # funkcia pre vytvorenie objektov studentov
    def create_students(self):
        print("Student details: ")
        # cyklus na osetrenie chybnych vstupov
        while True:
            try:
                name = input("Name: ")
                surname = input("Surname: ")
                grade = int(input("Grade: "))
                # chcem aby mi informacny system vypisal vsetky moznosti kurzov
                # a ja si budem moct vybrat ktory kurz chcem
                # najpr sa to riesilo pri funkci def create_courses(), tu je to v podstate
                # skopirovane ale iny sposob zapisu je pouzity
                # namiesto counter pouzijem "enumerate"
                # enumerate / pre kazdy prvok pola mi vytvori tuple, cize kazdemu
                # prvku pola priradi jeho index
                print("Choose your course")
                for counter, course in enumerate(self.courses):
                    print(f"{counter} {course}")
                course_id = int(input("Course id: "))
                # osetrenie ak niekto zada nespravne cislo, cize zadana ine cislo ako je v ponuke
                if course_id < 0 or course_id >= len(self.courses):
                    # vyvolaj chybu
                    raise Exception("Please choose course from above")
            # Exception - zachytavanie akejkolvek chyby - nie velmi dobry zvyk
            except Exception as e:
                print(e)
                print("Error during student creation. Reenter details")
                # pomocou continue spustim while este raz cize opat mozem zadat udaje
                continue
            break
        # vytvorim objekt/instanciu studenta
        student = Student(name, surname, grade)
        # priradenie studenta do kurzu
        # ??? nie prilis tomu rozumiem
        self.courses[course_id].add_student(student)
        # pridanie objektu studenta do informacneho systemu
        self.students.append(student)

    # funkcia pre vytvorenie objektov ucitelov
    def create_teachers(self):
        print("Teacher details: ")
        while True:
            try:
                name = input("Name: ")
                surname = input("Surname: ")
                degree = input("Degree: ")
            except Exception as e:
                print(e)
                print("Error during teacher creation. Reenter details")
                continue
            break
        teacher = Teacher(name, surname, degree)
        self.teachers.append(teacher)

    # funkcia pre vytvorenie objektov kurzov
    def create_courses(self):
        print("Course details: ")
        while True:
            try:
                name = input("Name: ")
                # chcem aby mi informacny system vypisal vsetky moznosti uzitelov
                # a ja si budem moct vybrat ktoreho ucitela pre dany kurz chcem
                counter = 0
                print("Choose your teacher")
                for teacher in self.teachers:
                    print(f"{counter} {teacher}")
                    counter += 1
                teacher_id = int(input("Teacher id: "))
                # osetrenie ak niekto zada nespravne cislo, cize zadana ine cislo ako je v ponuke
                if teacher_id < 0 or teacher_id >= len(self.teachers):
                    # vyvolaj chybu
                    raise Exception("Please choose teacher from above")
            except Exception as e:
                print(e)
                print("Error during teacher creation. Reenter details")
                continue
            break
        # vytvorim objekt/instanciu kurz
        course = Course(name, self.teachers[teacher_id])
        # pridanie objektu ucitela do informacneho systemu
        self.courses.append(course)
