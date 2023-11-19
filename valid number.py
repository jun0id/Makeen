num = "+968 9621-1932"
#True or False#
valid = len(num)== 14
po=0

while valid and po < len(num):
    valid = ( num[0:5]=="+968 " and num[5:9].isdigit() and num[9]=="-" and num[10:15].isdigit())
    po+=1
    
if (valid):
    print("The number is correct")
    
else:
    print("the number is wrong")
