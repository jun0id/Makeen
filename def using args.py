def sum_(*args):
    sum1=0
    for n in args:
        sum1+=n
    return sum1

r= sum_(2,2)
print(r)