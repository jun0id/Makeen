class Shape:
    def __init__(self, color, name):
        self.color = color
        self.name = name
    def __str__(self):
        print("My color is {} and the name {}".format(self.color, self.name))
        

class Circule(Shape):
    def __init__(self, color, name, radius):
        super().__init__(color, name)
        self.radius = radius
        area= 3.14 * radius ** 2
        print(area)
class Square(Shape):
    def __init__(self, color, name, side):
        super().__init__(color, name)
        self.side = side
        area = side ** 2
        print (area)
        
cr = Circule("Red", "Circule", 4)
cr.__str__()

cr = Square("Blue", "Square", 4)
cr.__str__()