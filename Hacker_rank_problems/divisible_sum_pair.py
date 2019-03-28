def divisible_sum_pair(k, array):
    count = 0
    for num in range(0, len(array)):
        for nums in range(num + 1, len(array)):
            value = array[num] + array[nums]
            if value % k == 0:
                count = count + 1
    print(count)


divisible_sum_pair(3, [1, 3, 2, 6, 1, 2])
