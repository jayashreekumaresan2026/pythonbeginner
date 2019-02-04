def item(my_array):
    count = 0
    for values in my_array.values():
        if type(values) == list:
            count +=1
    return count
print(item({1:"a",2:[1,2,3,]}))