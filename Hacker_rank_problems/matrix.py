matrix1 = [[1, 2],[6,7]]
matrix2 = [[8, 9],[10,11]]
cols = [matrix1, matrix2]

result = []
if len(matrix1) != len(matrix2):
    print("multiplication is not possible ")
else:
    for i in range(0, len(matrix1)):
        for j in range(0, len(matrix2)):
            for k in range(0, len(matrix1)):
                result[i][j] = result[i][j] + (matrix1[i][k] * matrix2[k][j])


    for multiply in result:

        print(multiply)
