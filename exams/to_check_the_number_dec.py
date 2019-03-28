def checking_the_number(number2):
    user_input = list(map(int, str(number2)))
    print(user_input)
    user_input1 = list(map(int, str(number2)))
    print(user_input1)
    user_input.sort()
    print(user_input)

    if user_input == user_input1:
        print("yes")
    else:
        print("no")


number1 = 1234
number2 = 1243
checking_the_number(number1)
checking_the_number(number2)
