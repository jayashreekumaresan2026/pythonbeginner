n = int(input("enter the number of element to be present"))
my_array = []
repe_numbers = []

for i in range(1, n + 1):
    elements = int(input("enter the elements to be present"))
    my_array.append(int(elements))
return my_array
print("list of elements:", my_array)



def repeated_number(my_array):
    repe_numbers = {}
    numbers = {}
    for i in range(1, set(my_array)):
        if repe_numbers.count(i) > 0:
            numbers[i] = repe_number.count(i)
    for i in range(1, numbers):
        print('{}{}'.format(i, numbers[i])
repeated_number(my_array)
