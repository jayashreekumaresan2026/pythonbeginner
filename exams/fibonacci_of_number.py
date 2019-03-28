def fibo_of_number(number):
    fibo = []
    first_number = 0
    second_number = 1
    fibo.append(second_number)
    for i in range(2, number + 1):
        third_number = first_number + second_number
        fibo.append(third_number ** 3)
        first_number = second_number
        second_number = third_number
    print(sum(fibo))


number = 4
fibo_of_number(number)
