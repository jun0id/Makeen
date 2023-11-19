x = int(input(">"))
for x in range (1, x):
    sum_=0
    for i in range(1, x):      
        if (x % i == 0 and x!=i):
            sum_+=i
    if (sum_ == x):
        print(x)
