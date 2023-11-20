n = int(input(">"))
sum_=0

for i in range(1, n+1):
    s= '2' * i
    if (i != n): 
        print(s, end=" + ")
    else:
        print(s)
    sum_ += int('2' * i)
print(sum_)
