# def insertion_sort():
array = []
key_element = []
element_range = int(input("Enter the range of the values"))
for i in range(1, element_range):
    values = int(input("the numbers are:"))
    array.append(values)
    print(array)
    key_element = array[i]
    array_element = i - 1
    while array_element > 0 and key_element < array_element[i]:
        array[array_element + 1] = array[array_element]
        array_element -= 1
    array[array_element] = key_element
# print(insertion_sort())
