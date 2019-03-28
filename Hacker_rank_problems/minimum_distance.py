def minimum_distance(array):
    array_list = []
    for i in range(0, len(array)):
        for j in range(i + 1, len(array)):
            if array[i] == array[j]:
                array_list.append(abs(i - j))
    if len(array_list) == 0:
        print(-1)
    else:
        print(min(array_list))


array = [7, 1, 3, 4, 1, 7]
minimum_distance(array)
