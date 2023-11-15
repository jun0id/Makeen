A = int(input('Enter Number for A: '))
B = int(input('Enter Number for B: '))
C = int(input('Enter Number for C: '))

if A > B and A> C:
    print("A is greater than B and C")
elif B > A and B > C:
        print("B is greater than A and C")
elif C > A and C> B:
        print("C is greater than A and B")
else:
    print("equals")
    