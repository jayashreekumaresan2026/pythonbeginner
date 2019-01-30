def multiple_of_numbers():
    for i in range(1, 51):
        if i % 5 == 0 and i % 3 == 0:
            print("FizzBuzz")
        elif i % 5 == 0:
            print("Fizz")
        elif i % 3 == 0:
            print("Buzz")
        else:
            print(i)
multiple_of_numbers()
