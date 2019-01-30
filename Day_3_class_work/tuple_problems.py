def immutable(my_string):
    print(hex(id(my_string)))
    my_string = my_string.replace('st', 'ST')
    print(hex(id(my_string)))


def mutable(number):
    print(hex(id(number)))
    number += 1
    print(hex(id(number)))
    print()


def mutable_test_list(my_list):
    print(hex(id(my_list)))
    my_list = my_list.append()
    print(hex(id(my_list)))
    print()


immutable("string")
mutable(50)
mutable_test_list(30)
