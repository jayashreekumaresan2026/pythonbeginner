def remove_the_element(list):
    for i in range(0, len(list)):
        if 'apple' in list:
            list.remove('apple')

    print(list)


list = ['apple', 'panana', 'apple']
remove_the_element(list)
