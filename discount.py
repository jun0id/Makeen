amount = int(input('Enter the Amount: '))

if amount > 100:
    discount = amount * 0.9
else:
    discount = amount * 0.95

print ("Discount $",discount)
