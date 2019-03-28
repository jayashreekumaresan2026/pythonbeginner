def find_list_pairs(user_input1, number):
    # user_input=input("enter the number seperated by space")
    # number=int(input("enter the number to check"))
    # user_input1=user_input.split()
    # print(user_input1)
    for i in range(0, len(user_input1)):
        for j in range(i + 1, len(user_input1)):
            if (user_input1[i] + user_input1[j]) == number:
                array_sum = []
                array_sum.append(user_input1[i])
                array_sum.append(user_input1[j])
                print(array_sum)


array = [1, 3, 7, 4, 5, 6, 5, 8, 9]
number = 10
find_list_pairs(array, number)
