def equal_elements(array):
    count_list = []
    for i in range(0, len(array)):
        count_list.append(array.count(array[i]))
    maximum = max(count_list)
    result = len(array) - maximum
    print(result)


array = [3, 3, 2, 1, 3]
equal_elements(array)
