sum=0
stu = int(input("number of students: " ))

for i in range(1, stu+1):
    grade = float(input("Student of grade: "))
    sum +=grade
avg = sum/stu
print(avg)