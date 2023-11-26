matrix = [[2,4,5],
          [1,6,6],
          [1,9,3]]
print(matrix[1])
print(matrix[1][2])

print("---------------")

for i in range(len(matrix)):
    for j in range(len(matrix)):
        print(matrix[i][j] * 2, end=' ')
    print()
    
print("---------------")

#to count zeros in matrix (table)
matrix = [[0,4,5],
          [1,6,0],
          [0,9,0]]
zero_ = 0
for i in range(len(matrix)):
    for j in range(len(matrix)):
        if(matrix[j][i] == 0):
             zero_ +=1
print(zero_)