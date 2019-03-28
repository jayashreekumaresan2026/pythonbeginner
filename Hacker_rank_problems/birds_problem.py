def bird_migration(array):
    count = 0
    for i in range(0, len(array)):
        for j in range(i + 1, len(array)):
            if array[i] == array[j]:
                count = count + 1
    print(count)
    # print(count.index(result))


array = [1, 4, 4, 4, 5, 3]
bird_migration(array)
