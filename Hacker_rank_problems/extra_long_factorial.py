def extra_long_factorial(factorial_number):
    fact = 1
    if factorial_number>0:
       for i in range(1, factorial_number+1):
         fact = fact * i
       print(fact)
    else:
        print("please enter the  valid number ")

factorial_number = 25
extra_long_factorial(factorial_number)
