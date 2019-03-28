def pattern3(rows):
    for i in range(0, rows):
        for j in range(0, rows - 1 - i):
            print(' ', end='')

        for k in range(0, i + 1):
            print("*", end='')

        print()


rows = 4
pattern3(rows)
