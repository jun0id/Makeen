from math import tan, pi


def area_(x,y):
    n, s = x, y
    area= (n * s**2)/ (4 * tan(pi / n))
    rounded = format(area,".2f")
    print(rounded)

area_(5, 6.5)