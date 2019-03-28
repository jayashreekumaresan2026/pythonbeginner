def sum_factorial(number):
    fact = 1
    for i in range(1, number + 1):
        fact = fact * i
    list_of_number = list(map(int, str(fact)))
    print("The sum of digits in the factorial is:", sum(list_of_number))


number = 5
sum_factorial(number)
