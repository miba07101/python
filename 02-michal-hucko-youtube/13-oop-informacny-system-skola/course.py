# trieda Course
class Course:
    # trieda Course vie v zasade fungovat aj bez udajov o ziakoch a uciteloch
    # preto argumenty nastavim "teacher=None" a "students=[] (prazdny list)"
    def __init__(self, name, teacher=None, students=[]):
        self.name = name
        self.teacher = teacher
        self.students = students

    # funkcia pre pridanie studenta do kurzu
    def add_student(self, student):
        # do listu students priradim objekt studenta
        self.students.append(student)

    # methoda __str__() mi definuje co sa ma vypisat ak budem chciet vypisat
    # objekt/instanciu daneho kurzu
    def __str__(self):
        # pomocny parameter aby som vo funkcii join() pri vypise mohol pouzit
        # \n - cize novy riadok
        delimeter = "\n\t"
        # !!! zaujimavy sposob vypisu
        # !!! pouzivam pri studentoch list comprehension
        return f"Course {self.name}\n\t{self.teacher}\n\t{delimeter.join([student.__str__() for student in self.students])}"
