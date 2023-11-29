try:
    x = 4/6
    w = 4/1
    print(y)
    print(w)
except ZeroDivisionError:
    print("Can not divid by zero")
except NameError:
    print("somthing going wrong")
 
print("----------------------")

try:
    x = 4/6
    print(y)
except Exception as exc:
    print(exc)

print("----------------------")

try:
    x = 4/6
    print(y)
except Exception as exc:
    print(type(exc))
finally:
    print("Done")

print("----------------------")

try:
    gender = int(input('Enter gender M or F: '))

    if gender.lower() =="m":
        age = int(input('Enter the age: '))
        if 24 <= age <= 30:
            print("Accpeted")
        else:
            print ("Not Accepted")
    else:
        print("your are Female")
except Exception as exc:
    print(type(exc),"\n", str(exc))
finally:
    print("Done")

print("----------------------")

x=1
while x<=5:
    print(x)
    x +=1
print()    
for i in range(1,6):
    print(i)