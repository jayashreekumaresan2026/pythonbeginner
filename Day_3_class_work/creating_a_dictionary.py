def dictionaries(array_list):
    dict = {}
    for key in range(0, len(array_list)):
        dict[key + 1] = array_list[key]
    print(dict)
    print(dict.keys())
    print(dict.values())
    print(len(dict))
    print((dict)[1])
    print(type(dict.values()))
    # print((dict.values())[2])
    print(dict.items())


array_list = ['apple', 'orange', 'banana']
dictionaries(array_list)


def key_values(dictionaries):
    for key, values in dictionaries.items():
        print(sorted((key, values)))


dictionaries = {7: 5, 2: 1, 3: 1}
key_values(dictionaries)
