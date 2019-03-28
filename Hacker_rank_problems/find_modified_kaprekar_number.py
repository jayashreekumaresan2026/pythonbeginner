def kaprekar_number(number):
    square_of_number = number * number
    array = list(map(int, str(square_of_number)))
    print(array)
    length_of_array = len(array)
    divide_the_length_of_array = length_of_array // 2
    split_the_number = array[:divide_the_length_of_array]
    split_the_last_digit = array[divide_the_length_of_array:]
    print(split_the_number)
    for i in split_the_number:
        print(i, end="")
    print()
    for i in split_the_last_digit:
         print(i, end="")


number = 45
kaprekar_number(number)
