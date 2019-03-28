def hurdel_race(k, height):
    array = 0
    maximum_height = max(height)
    if maximum_height < k:
        return array
    else:
        value = maximum_height - k
        return value


array_list = [1, 6, 3, 5, 2]
maximum_jumps = 4
array_list1 = [2, 5, 4, 5, 2]
maximum_jumps2 = 7
print(hurdel_race(maximum_jumps, array_list))
print(hurdel_race(maximum_jumps2, array_list1))
