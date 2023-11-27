x = [[1,2,3],
     [6,7,8]]

y = [[6,1],
     [2,10],
     [0,2]]

c =[[0,0],
    [0,0]]
def mula_matrix(x, y):
    for i in range(len(x)):
        for j in range(len(y[i])):
            for k in range(len(y)):
                c[i][j] += x[i][k] * y[k][j]
    print(c)


def main():
    mula_matrix(x , y)
main()