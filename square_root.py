def square_root(x, list_):
    high = len(list_)-1
    low = 0
    while(low <= high):
        mid = int((high + low) / 2)
        if(list_[mid]*list_[mid] == x):
            return mid
        elif (list_[mid]*list_[mid] < x):
            low = mid + 1
        else:
            high = mid - 1
    return -1


list_ =[]
x = int(input("Enter the key: "))
for i in range(x):
    list_.append(i)
print(list_)
result= print(square_root(x, list_))

print("------------------------------------------------------")

def square_root(x):
    high = x
    low = 1
    if(x == 1 or x ==0):
        print(x)
    while(low <= high):
        mid = int((high + low) / 2)
        if(mid*mid == x):
            print(mid)
            break
        elif (mid*mid < x):
            low = mid + 1
        else:
            high = mid - 1
    else:
        print(-1)
square_root(1)
