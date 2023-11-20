def sum_digits(n):
    total = 0
    for i in n:
        total += int(i)
    return total


num = input("Enter an integer: ")
result = sum_digits(num)
print(f"The sum of the digits in {num} is: {result}")