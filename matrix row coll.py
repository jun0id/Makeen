matrix1 = [[0,4,5],
          [1,6,0],
          [0,9,0]]

matrix2 = [[0,4,5],
          [1,6,0],
          [0,9,0]]

def adding(matrix1, matrix2):
    new_matrix=[]
    for i in range(len(matrix1)):
        for j in range(len(matrix2)):
            add_ = matrix1[i][j] + matrix2[i][j]
            print(add_ , end =' ')
        print()

def main():
    adding(matrix1, matrix2)
    
main()
