# importujem "abstraktnu" triedu ABC
from abc import ABC, abstractmethod


# vytvorim "abstraktnu" triedu Person od ktroej budu dedit (inheritance) ostatne triedy
class Person(ABC):
    # def konkretny konstruktor
    def __init__(self, name, surname):
        # instancne atributy
        self.name = name
        self.surname = surname

    # def abstraktnu methodu (ta v podstate nerobi nic len ju budu potom dedit)
    # def ju pomocou "dekoratora"
    @abstractmethod
    def introduce_yourself(self):
        pass  # to znamena ze nerobi nic ale python ju aj tak vezme


# vytvorim triedu Student (bude dedit od person)
class Student(Person):
    # konstruktor bude mat navyse od Person triedy este argument "grade"
    def __init__(self, name, surname, grade):
        # methoda pomocou ktorej "overwrite" - zdedim konstruktor triedy Person
        super().__init__(name, surname)
        # instancny atribut
        self.grade = grade

    def introduce_yourself(self):
        print(f"Hi my name is {self.name} and surname is {self.surname}")

    # methoda __str__() mi definuje co sa ma vypisat ak budem chciet vypisat
    # objekt/instanciu daneho studenta
    def __str__(self):
        return f"Student, name: {self.name} surname: {self.surname} grade: {self.grade}"


# vytvorim triedu Teacher (bude dedit od person)
class Teacher(Person):
    # konstruktor bude mat navyse od Person triedy este argument "degree"
    def __init__(self, name, surname, degree):
        # methoda pomocou ktorej "overwrite" - zdedim konstruktor triedy Person
        super().__init__(name, surname)
        # instancny atribut
        self.degree = degree

    def introduce_yourself(self):
        print(f"Hi my name is {self.name} and surname is {self.surname}")

    # methoda __str__() mi definuje co sa ma vypisat ak budem chciet vypisat
    # objekt/instanciu daneho ucitela
    def __str__(self):
        return (
            f"Teacher, name: {self.name} surname: {self.surname} degree: {self.degree}"
        )
