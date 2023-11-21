x= [-1, 2 , 3 , -5, 6]
c=0
cP=0
for i in x:
    if(i < 0 ):
        c +=1
    else:
        cP +=1
print("Negative elemnts: ",c)
print("Postive or zero elemnts: ",cP)