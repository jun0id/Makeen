from random import randint

x = randint(0,10)
n1=0

while (n1 !=''):
    n1= int(input("->"))
    if (n1<x):
        print("Go up")
            
    elif (n1 > x):
        print("Go down")
        continue
    else:
        print ("you win")
        break
    