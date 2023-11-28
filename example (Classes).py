#examples about classes
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def __str__(self):
        return "Hello {} you are {} years old.".format(self.name, self.age)

person1 = Person('Ahmed', 24)
print(person1)

print("-------------------------------------------------")

#defualt value if you did not mention line number 15
class Person:
    def __init__(self, name, age = 19):
        self.name = name
        self.age = age
    def __str__(self):
        return "Hello {} you are {} years old.".format(self.name, self.age)

person1 = Person('Ali')
print(person1)

print("-------------------------------------------------")

#count Number of object
class Person:
    num_of_object = 0
    def __init__(self, name, age):
        self.name = name
        self.age = age
        Person.num_of_object +=1
    def __str__(self):
        return "Hello {} you are {} years old.".format(self.name, self.age)

person1 = Person('Ahmed', 24)
person2 = Person('Ali', 24)
print(person2.num_of_object)

print("-------------------------------------------------")

class Person:
    num_of_object = 0
    def __init__(self, name, age):
        self.name = name
        self.age = age
        Person.num_of_object +=1
    def __str__(self):
        return "Hello {} you are {} years old.".format(self.name, self.age)

person1 = Person('Ahmed', 24)
person2 = Person('Ali', 24)
print(person2.num_of_object)
        
