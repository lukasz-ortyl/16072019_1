class Person:
    def __init__(self, name):
        self.name = name

    @property
    def description(self):
        return "I am person. My name is {}.".format(self.name)

class Student(Person):
    def __init__(self, name):
        super().__init__(name)

class Doctor(Person):
    def __init__(self, name, salary):
        super(). __init__(name)
        self.salary = salary

    @property
    def description(self):
        return "I am doctor. My name is {}. I have {} zl salary.".format(self.name, self.salary)


class Professor:
    def __init__(self, students):
        self.students = students


#def f(person):
#    person.name = "Marcin"

def f(person):
    new_person = person
    person = Student("Ignacy")
    new_person.name = "Marcin"


def g(person):
    new_person = person
    person = None
    person = Student("Kamil")
    person.name = "Wojciech"
    new_person.name = ("Natalia")





if __name__ == '__main__':
    p1 = Student("Piotr")
    p2 = Doctor("Ewa", 5000)
    p3 = Student("Marysia")

    p3 = p2
    p2 = p1
    p3 = p2
    g(p3)

    print(p2.name)
    print(p3.name)


#    p2 = p1 #Piotr
#    f(p1) #Marcin dla p1
#    print(p1.name) #Marcin
#    print(p2.name) #Marcin


#    student_list = [Student("Piotr"), Student("Ewa")]
#    professor = Professor(student_list)

#    student_list = [1, 2, 3]

#    print(student_list)
#    print(professor.students)


#    person_1 = Person("Piotr")
#    person_2 = Student("Ewa")
#    person_3 = Doctor("Maciej", 2000)

#    person_2 = person_3
#    f(person_3)

#    ZAD1
#    person_2 = person_3

#    person_3.name = "Piotr"
#    person_3 = Doctor("Tomasz", 5000)

#    print(person_2.name)
#    print(person_3.name)





#    print()
#    print(person_1.name)
#    print()
#    print(person_1.description)
#    print()
#    print(person_2.name)
#    print()
#    print(person_2.description)
#    print()
#    print(person_3.name)
#    print()
#    print(person_3.description)
#    print()

#    person_list = [person_1, person_2, person_3]
#    for person in person_list:
#        print(person.description)

#    person_1 = person_3
#    print(person_1.description)


