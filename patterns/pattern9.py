def pattern8(row):
    space = row - 1
    star = 1
    for i in range(0, row):
        for j in range(0, space - i):
            print("-", end='')
        for k in range(0, star):
            print("*", end='-')

        star += 1
        print()


row = 4
pattern8(4)
