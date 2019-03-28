def migration_bird(birds_count):
    array = []
    dict = {}
    array_values = []
    for i in range(0, len(birds_count)):
        array.append(birds_count.count(birds_count[i]))
        dict[birds_count[i]] = array[i]

    max_value = max(dict.values())
    for key, values in dict.items():
        if values == max_value:
            array_values.append(key)

    print(min(array_values))


birds_count = [1,3,6,7]
migration_bird(birds_count)
