sum = 0
result = [[0, 0], [0, 0]]
# get the matrix1 and matrix2
matrix1 = [[1, 2], [4, 5]]
matrix2 = [[6, 7], [5, 6]]
# process the matrix1
for i in range(0, len(matrix1)):
    # process the matrix2
    for j in range(0, len(matrix2)):
        # process the matrix2
        for k in range(0, len(matrix1)):
            result[i][j] += matrix1[i][k] * matrix2[k][j]
# get the resultant matrix one by one and print the matrix
for k in result:
    print(k)
