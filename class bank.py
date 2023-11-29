class NegativeValueException(Exception):
    def __init__(self, value):
        self.value = value
        super().__init__("Negative value not allowed")

class BankAccount(Exception):
    def __init__(self, name, balance, account_number):
        self.name = name
        self.__balance = balance
        self.__account_number = account_number

    def deposit(self):
        amount = float(input("Enter amount to be deposited: "))
        self.__balance += amount
        print(amount)
        
    def withdraw(self, value):   
        if value < 0:
            raise NegativeValueException(value)
        self.__balance -= value
    
    def display(self):
        print(self.__balance)


t = BankAccount("Junaid", 1000, 183265)

try:
    value = float(input("Enter the withdraw amount: "))
    t.withdraw(value)
except NegativeValueException as e:
    print(e)

t.withdraw(0)
t.display()
