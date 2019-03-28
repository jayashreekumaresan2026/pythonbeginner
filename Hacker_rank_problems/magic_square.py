def magic_square():
    sum_list = []
    sum_list_item = []

    # declare a matrix to process
    matrix = [[5, 3, 4],
              [1, 5, 8],
              [6, 4, 2]]
    index = len(matrix[0])
    # declare a even list
    even_list = [2, 4, 6, 8]
    # declare_a_odd_list
    odd_list = [1, 3, 5, 7, 9]
    matrix[0][0] = 8
    print((matrix))

    # check_sum_of_vertical
    for row in matrix:
        sum_list.extend([sum(row)])
    print(sum_list)
    # check_sum_of_horizontal
    for col in range(index):
        sum_list.append(sum(row[col] for row in matrix))
    print(sum_list)

    # for i in range(, len(matrix)):
    #     for j in range(, len(matrix)):
    #         if matrix[i][j] == even:
    # #check_sum_of_diagonals
    # result1 = 0
    # for i in range(0, index):
    #  result1 += matrix[i][i]
    # sum_list.append(result1)
    # print(sum_list)
    # result2 = 0
    # for i in range(index - 1):
    #  result2 += matrix[i][i]
    # sum_list.append(result2)
    # print(sum_list)


magic_square()
