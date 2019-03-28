def patterns(rows):
    for i in range(0, rows):
        for j in range(0, i + 1):
            print("*", end='')
        print()
    for i in range(0, rows):
        for j in range(0, rows - i-1):
            print("*", end='')
        print()


rows = 4
patterns(rows)
