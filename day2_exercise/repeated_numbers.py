n = int(input("enter the number of element to be present"))
my_array = []


def repeated_number():
    for i in range(1, n + 1):
        elements = int(input("enter the elements to be present"))
        my_array.append(int(elements))
        print("list of elements:", my_array)
    my_array.sort()
    print("sorted elements:", my_array)

    for i in range(len(my_array) - 1):
       if my_array[i] == my_array[i + 1]:
         print(my_array[i])
         print(my_array.count(my_array[i]))
print(repeated_number())
