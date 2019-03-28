def solveMeFirst(a, b):
    number1 = int(input())
    number2 = int(input())
    result = solveMeFirst(number1, number2)
    return result


a = 1
b = 2
print(solveMeFirst(a, b))
