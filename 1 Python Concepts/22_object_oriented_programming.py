class Students:
    def __init__(self, name, contact):
        self.name = name
        self.contact = contact

    def get_data(self):
        print('My name is ' + self.name + '\nMy contact no: ' + str(self.contact))


stud = Students('John', 123456)
stud.get_data()
print()


# Inheritance
class ScienceStudent(Students):
    def __init__(self, name, contact, age):
        super().__init__(name, contact)
        self.age = age

    def science(self):
        print('I am a science student.\nMy age is: ' + str(self.age))


stud = ScienceStudent('Rob', 123456789, 22)
stud.get_data()
stud.science()
print()


# Data hiding
class MyClass:
    __x = 0

    def add(self, increment):
        self.__x += increment
        print(self.__x)


obj = MyClass()
obj.add(5)
