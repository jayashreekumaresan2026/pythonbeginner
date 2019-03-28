# # get the number of rows
# row = 2
# # get the number of columns
# columns = 3
# matrix = [[0] * 3] * 2
# print(matrix)
# matrix[1][1] = 5
# print(matrix)
# create a list of matrix
sums = 0
result = [[0, 0], [0, 0]]
# get the matrix1 and matrix2
matrix1 = [[1, 2], [4, 5]]
matrix2 = [[6, 7], [5, 6]]
# process the matrix1
for i in range(0, len(matrix1)):
    # process the matrix2
    for j in range(0, len(matrix2)):
        # add the matrix value and stored into the another matrix
        result[i][j] = matrix1[i][j] + matrix2[i][j]
# get the resultant matrix one by one and print the matrix
for k in result:
    print(k)
