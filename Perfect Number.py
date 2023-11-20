num = int(input(">"))
for x in range (1, num):
    sum_=0
    for i in range(1, x):      
        if (x % i == 0):
            sum_+=i
    if (sum_ == x):
        print(x)
