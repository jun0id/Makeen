shape= int(input("Choose the shape: \n1.triangle\n2.square\n3.circule\n4.cylinder\n5.quit\n> "))

def triangle(base, height):
    area = base * height / 2
    print("area = ", area)

def cylinder(height, radian):
    pi= 22/7
    volume = pi * radian * radian * height
    print("Volume is: ", volume)

def circule(r):
    pi= 22/7
    area = pi * r ** 2
    print("Area is: ", area)
    
def square(n):
    sqaure = n ** 2
    print ("Sqaure is: ",sqaure)


if (shape == 1):
    base = int(input("Base: "))
    height = int(input("Height: "))
    triangle(base, height)
        
elif (shape == 2):
    n = int(input(">"))
    square(n)
    
elif (shape == 3):
    r = int(input(">"))
    circule(r)
    
elif (shape == 4):
    height= int(input("Height: "))
    radian = int(input("Radian: "))
    cylinder(height, radian)
    
elif (shape == 5):
    exit("You have quit")
    
else:
    print("Choose the correct Number for the shape")