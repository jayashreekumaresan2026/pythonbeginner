# def repeated_string(user_string, number_of_times):
#     string_count = number_of_times - len(user_string)
#     print(string_count)
#     for i in range(len(user_string), string_count):
#         print(user_string[:], end="")
#
#
# user_string = 'aba'
# number_of_times = 10
# repeated_string(user_string, number_of_times)
import math


def repeatedString(s, n):
    if len(s) == 1:
        return 0
    else:
        l = s.count('a')
        c = math.floor(n / len(s))
        sum = l * c
        sum += s[:(n % len(s))].count('a')
    return sum


s = "a"
n = 10000000000
print(repeatedString(s, n))
