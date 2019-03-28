import collections


# def cut_the_strick(array):
#     # count_list = 0
#
# print(array)
# count = collections.Counter(array)
# dictionary = dict(count)
# print(dictionary)
# minimum_value = min(dictionary.keys())
# print(minimum_value)
# for i in range(0, (len(array) - count_list)-1):
#     print(len(array))
#     if array[i] == minimum_value:
#         array.remove(array[i])
#         count_list = count_list + 1
# print(array)
# print(count_list)
# for j in range(i + 1, len(array)):
#     if array[i] == array[j]:
#         count_of_each_element.append(array[i])

#     count_of_each_element[array[i]] = array.count(array[i])
# print(count_of_each_element)


def cut_the_stick(array):
    result = []
    while len(array) > 0:
        minimum_value = min(array)
        new_array_element = []
        array.sort()
        result.append(len(array))
        for i in array:
            new_array_element.append(i - minimum_value)
            if 0 in new_array_element:
                new_array_element.remove(0)
            array = new_array_element
    return result


array = [5, 4, 4, 2, 2, 8]
result = cut_the_stick(array)
print(result)
