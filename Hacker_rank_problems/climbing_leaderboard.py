def leader_board(array):
    dictionary = {}
    for key in range(0, len(array)):
        dictionary[key + 1] = array[key]

    print(dictionary)


array = [100, 50, 50, 20, 10]

leader_board(array)
