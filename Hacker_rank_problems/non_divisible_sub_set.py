def non_divisible_subset(divisible_number, array_list):
    new_count_array = {}
    new_array = []
    count = 0
    dulication_removed_array_list = list(set(array_list))
    # print(dulication_removed_array_list)
    for i in range(0, len(dulication_removed_array_list)):
        new_array.append(dulication_removed_array_list[i] % divisible_number)
    new_array.sort()
    # print(new_array)
    for i in range(0, divisible_number):
        new_count_array[i] = (new_array.count(i))
    print(new_count_array)

    for key in range(0, (divisible_number // 2) + 1):
        if key in new_count_array:

            if key == 0 or divisible_number == (key * 2):
                if new_count_array[key] >= 1:
                    count = count + 1

            else:
                key_pair = divisible_number - key
                if key_pair in new_count_array:

                    if new_count_array[key_pair] > new_count_array[key]:
                        count = count + new_count_array[key_pair]

                    else:
                        count = count + new_count_array[key]

    return count


array_list = [278 ,576, 496, 727, 410 ,124, 338, 149, 209, 702, 282, 718, 771 ,575 ,436]
divisible_number = 7
print(non_divisible_subset(divisible_number, array_list))
