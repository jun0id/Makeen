class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def say_hi(self):
        print("Hello {} from Person class.".format(self.name))

class Student(Person):
    def __init__(self, name, age = 23):
        super().__init__(name, age)
    def say_hi(self):
        print("Hello {} from Student class.".format(self.name))

p1 = Person("A", 22)
s1 = Student("B", 22)
s1.say_hi()
p1.say_hi()