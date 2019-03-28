def split_the_array():
    array = [12, 10, 5, 6, 52, 36]
    print("The list before rotation ", array)
    first_array = []
    second_array = []
    position = 2
    for i in array[:position]:
        first_array.append(i)
    for j in array[position:]:
        second_array.append(j)
    print("the list after rotation", second_array + first_array)

split_the_array()
