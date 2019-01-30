user_string = input("enter the string")
len_string = len(user_string)


def non_repeating():
    for i in range(0, len_string + 1):
        if i == 0:
            if user_string[i] != user_string[i + 1]:
                print(user_string[i])
                break
        elif i == len_string + 1:
             if user_string[i] != user_string[i - 1]:
                print(user_string[i])
                break
             else:
                if user_string[i] != user_string[i + 1] and user_string[i] != user_string[i - 1]:
                  print(user_string[i])
                  break
non_repeating()

