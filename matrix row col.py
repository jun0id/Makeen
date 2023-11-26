matrix1 = [[0,4,5],
          [1,6,0],
          [0,9,0]]

matrix2 = [[0,4,5],
          [1,6,0],
          [0,9,0]]

def adding(matrix1, matrix2):
    new_matrix=[]
    for row in range(len(matrix1)):
        rows = []
        for coluumn in range(len(matrix1)):
            rows.append(matrix1[row][coluumn] * matrix2[row][coluumn])
        new_matrix.append(rows)
    print(new_matrix)

def main():
    adding(matrix1, matrix2)
    
main()