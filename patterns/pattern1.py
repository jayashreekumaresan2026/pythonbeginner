def patterns(pattern_rows):
    for i in range(0, pattern_rows):
        for j in range(0, i+1):
            print("*", end='')
        print()


pattern_rows = 4
patterns(pattern_rows)
