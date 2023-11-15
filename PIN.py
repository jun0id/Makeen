pin = int(input('Enter your PIN number '))
balance=1500

if pin == 1234:
    signed= int(input('Select:\n1- Check Balance \n2- Withdeaw \n3- Deposite '))
    if signed == 1:
        print("Your balance: "x)
    elif signed == 2:
        withdraw = int(input('Amount Withdraw '))
        print(balance - withdraw)
    elif signed == 3:
        deposite = float(input('Amount Deposite '))
        print(balance + deposite)
else:
    print("The PIN not correct")
            