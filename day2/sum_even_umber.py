array = []
total = int(input("enter the value"))


def create_list():
    for i in range(0, total):
        n = int(input("collect the number"))
        array.append(n)


def find_even(array):
    sum = 0
    for i in range(0, len(array)):
        if array[i] % 2 == 0:
            sum = sum + array[i]
    return sum


create_list()
print(find_even(array))
