def item():
    count = 0
    for x in dict.values():
        if x == random.random():
            count += len(dict[x])
    return count
print(item({1:"a"}))