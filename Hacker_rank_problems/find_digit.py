get_the_list_digit = []
# get the count of the number
number_count = 2
# get the number from the user
number = 1012
# split the number into a single digit and replace the O with empty space
for i in str(number).replace('0', ''):
    get_the_list_digit.append(int(i))
count=0
# check collect each and every  item from the list
for j in range(0, len(get_the_list_digit)):
    # if the number  is divisible by digit
    if number % get_the_list_digit[j] == 0:
        # count the number of digit which is divisible by the number
        count = count + 1
print(count)

# # check the list if any zeros in the list
#
#     if get_the_list_digit[i] == 0:
#         get_the_list_digit.remove(0)
#         count = 0
#         # after split the number check the number is divisible by the digit
#         for i in (0, len(get_the_list_digit) - 1):
#             # if the number  is divisible by digit
#             if number % get_the_list_digit[i] == 0:
#                 # count the number of digit which is divisible by the number
#                 count = count + 1
#         print(count)
#     else:
#         count = 0
#         # after split the number check the number is divisible by the digit
#
