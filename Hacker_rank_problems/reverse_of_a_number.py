def reverse_of_number():
    starting = 20
    ending = 23
    reverse = 0
    for i in range(starting, ending + 1):
        if (i - int(str(i)[::-1])) % 6 == 0:
            reverse = reverse + 1
    print(reverse)


reverse_of_number()
