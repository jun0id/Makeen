gender = input('Enter gender M or F: ')

if gender.lower() =="m":
    age = int(input('Enter the age: '))
    if 24 <= age <= 30:
        print("Accpeted")
    else:
        print ("Not Accepted")
else:
    print("your are Female")