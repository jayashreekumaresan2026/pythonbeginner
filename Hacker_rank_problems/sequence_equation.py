p = []
# get the  number of list
number_element = 5
# get each and every element in the list
list_array = [2, 3, 1]
# iterate the item using the loop
for i in range(len(list_array)):
    k = i + 1
    first = list_array.index(k)
    second = list_array.index(first + 1)
    result = second + 1
    p.append(result)
print(p)
