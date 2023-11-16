n= int(input("->"))

while (n !=""):
    n1= int(input("->"))
    if (n1<n):
        print("Go up")
            
    elif (n1 > n):
        print("Go down")
        continue
    else:
        print ("you win")
        break