#list with factors

ls =[]
value= []
f = int(input("factor>"))
def readFloats():
    while(True):
        num= input(">")
        if(num == 'stop'):
            break
        else:
            ls.append(float(num))
            continue
    return ls

def mult(ls):
    for i in range(len(ls)):
        res= ls[i] * f
        value.append(res)
    return value

def print_reverse(value):
    value.reverse()
    print(value)

def main():
    readFloats()
    mult(ls)
    print_reverse(value)
    
main()