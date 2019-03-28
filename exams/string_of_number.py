def string_of_number(number):
    number1 = list(map(int, str(number)))
    number2 = list(map(int, str(number)))
    number2.sort()
    if number1 == number2:
        print("ascending")
    elif number1 == sorted(number1, reverse=True):
        print("descending")
    else:
        print("mixed")


number_in_asc = 469
number_in_desc = 9551
number_in_mixed = 1212
string_of_number(number_in_asc)
string_of_number(number_in_desc)
string_of_number(number_in_mixed)
