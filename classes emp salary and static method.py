#count the salary of employee (Overtime)
class Employee:
    def __init__(self, emp_id, emp_name, emp_salary, emp_department):
        self.emp_id= emp_id
        self.emp_name = emp_name
        self.emp_salary = emp_salary
        self.emp_department = emp_department

    
    def calculate_emp_salary(self, hours_worked):
        self.hours_worked= hours_worked
        if (hours_worked > 50):
            self.overtime = hours_worked - 50
            self.overtime_amount = (self.overtime * (self.emp_salary / 50))
            self.emp_salary += self.overtime_amount
    def emp_assign_department(self, emp_department):
        self.emp_department = emp_department
            
    def print_employee_details(self):
        print("Name: {}, ID: {} , salary: {}, Department: {}".format(self.emp_name, self.emp_id, self.emp_salary, self.emp_department))
        
data = Employee("Adams", "E7333", 5000, "Sales")
data.calculate_emp_salary(60)
data.print_employee_details()

print("--------------------------------------------------------------------")
print("--------------------------------------------------------------------")

#Class of staticmethod

class Employee:
    def __init__(self, name, age):
        self.__name = name
        self.__age= age
    def __str__(self):
        return f"{self.__name}, {self.__age}"
    def set_name(self, new_name):
        self.__name = new_name
    @classmethod
    def c_emplyee(cls, name, date_of_birth):
        age = 2023 - date_of_birth
        return cls(name, age)
        
e1 = Employee("Ali", 23)
e1.set_name("Ahmed")
print(e1)

e2 = Employee.c_emplyee("JU", 1955)
print(e2)

print("--------------------------------------------------------------------")
print("--------------------------------------------------------------------")

#Class of staticmethod

class Math:
    @staticmethod
    def add_numbers(x, y):
        return x+y
    @staticmethod
    def pi():
        return 3.14
class Shape:
    def __init__(self, name, color, r):
        self.name = name
        self.color = color
        self.r = r
    def area(self):
        return 2*Math.pi()*self.r

sh1= Shape("T", "Blue", 5)
print(sh1.area())
print(Math.add_numbers(3,4))
    
