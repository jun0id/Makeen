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
print()
print(Math.add_numbers(3,4))
    