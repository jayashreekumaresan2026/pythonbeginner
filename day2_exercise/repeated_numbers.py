n = int(input("enter the number of element to be present"))
my_array = []

for i in range(1, n + 1):
    elements = int(input("enter the elements to be present"))
    my_array.append(int(elements))
print(my_array)


def repeated_number(my_array):
    repeated_numbers = {}
    numbers = {}
    for i in range(1, set(my_array)):
        if repeated_numbers.count(i) > 0:
            numbers[i] = repeated_numbers.count(i)
    for i in range(1, numbers):
        print('{}{}'.format(i, numbers[i]))


repeated_number(my_array)
