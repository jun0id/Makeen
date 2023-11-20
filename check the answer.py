answer="abaacb"
q= input("Enter you answers: ")
m=0

for i in range(len(answer)):
    if(answer[i] == q[i]):
        m +=1
    else:
        print(i+1,  end = " ")
print()
print(m, " Out of " , len(answer))