v = "aoeui"
m= input(">")
counter=0

for chr1 in m:
    if(chr1.lower() in v):
        counter+=1
print(counter)