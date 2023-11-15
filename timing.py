from sys import exit

time = int(input('Enter Time(1) 00:00 '))
t= input('PM or AM: ')
time2 = int(input('Time(2) 00:00 '))
t2= input('PM or AM: ')

if len(t) != 2:
    exit("the time must be PM or AM")

if t.lower() =="am" and t2.lower() == "pm":
    print(time, "", t)
elif t.lower() =="pm" and t2.lower() == "am":
    print(time2, "", t2)
else:
    if time > time2:
        print(time2, t2)        
    elif time2 > time:
        print(time, t)