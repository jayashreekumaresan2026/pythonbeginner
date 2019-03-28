def patterns(rows):
    k = 1
    for i in range(0, rows + 1):
        for j in range(0, i):
            print(chr(96 + k), end='')
            k = k + 1
        print()
    for i in range(0, rows):
        for j in range(0, rows - i - 1):
            print(chr(99 - i), end='')
        print()


rows = 4
patterns(rows)
