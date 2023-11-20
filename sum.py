n= int(input("->"))
sum_=0
i=0
while(i<=n):
    n= n%10
    sum_= i+n
    i =i//10
print(sum_)