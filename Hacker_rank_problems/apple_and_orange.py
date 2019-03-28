def countApplesAndOranges(s, t, a, b, apples, oranges):
    count_apple = 0
    count_orange = 0
    for position in apples:
        if s <= position + a <= t:
            count_apple += 1
    for position in oranges:
        if s <= position + b <= t:
            count_orange += 1

    print(count_apple, count_orange)


countApplesAndOranges(7, 11, 5, 15, [-2, 2, 1], [5, -6])
