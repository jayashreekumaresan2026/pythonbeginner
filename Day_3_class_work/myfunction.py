def get_input():
    list_ = []
    size_ = int(input("Enter the size of the list"))
    for i in range(0, size_):
        number = int(input())
        list_.append(number)
    return list_


def find_occurrence(list_):
    occurrence = {}
    for number in set(list_):
        if list_.count(number) > 1:
            occurrence[number] = list_.count(number)

    for key in occurrence:
        print("{}: {} times".format(key, occurrence[key]))


find_occurrence(get_input())