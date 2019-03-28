def pairs(list_of_element, number):
    count = 0
    for i in range(0, len(list_of_element)):
        for j in range(i + 1, len(list_of_element)):
            new_array = []
            if abs(list_of_element[i] - list_of_element[j]) == number:
                new_array.append(list_of_element[i])
                new_array.append(list_of_element[j])
                count += 1
    print(count)


list_of_element = [1, 5, 3, 4, 2]
number = 2
pairs(list_of_element, number)