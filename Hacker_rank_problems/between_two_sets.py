def between_two_sets():
    flag = 0
    count = 0
    array_list = []
    # get the first list from the user
    user_input_list1 = [3, 4]
    # get the second list from the user
    user_input_list2 = [24, 48]
    # find max_number in the first list
    list1_max = max(user_input_list1)

    # find the minimum number in the second list
    list2_min = min(user_input_list2)

    for i in range(list1_max, list2_min + 1, list1_max):
        # find the factors of the list
        array_list.append(i)
    print(array_list)
    for i in range(0, len(array_list)):
        flag = 0
        for j in range(0, len(user_input_list1)):
            # check the list is divisible by array_list
            if array_list[i] % user_input_list1[j] != 0:
                flag = 1
        if flag == 1:
            continue
        for k in range(0, len(user_input_list2)):
            # check the list is divisible by array_list
            if user_input_list2[k] % array_list[i] != 0:
                print(i)
                flag = 1
        if flag == 1:
            continue
        count = count + 1
    print(count)


between_two_sets()
