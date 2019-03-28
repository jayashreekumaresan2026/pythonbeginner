def taum_and_birthday(black, white, black_cost, white_cost, z):
    if ((black_cost + z) < white_cost):
        cost = (black_cost * black + white * (black_cost + z))
    elif ((white_cost + z) < (black_cost)):
        cost = (white_cost * white + black * (white_cost + z))
    else:
        cost = black_cost * black + white_cost * white
    return cost


print(taum_and_birthday(10, 10, 1, 1, 1))
print(taum_and_birthday(5, 9, 2, 3, 4))
print(taum_and_birthday(3, 6, 9, 1, 1))
print(taum_and_birthday(7, 7, 4, 2, 1))
print(taum_and_birthday(3, 3, 1, 9, 2))
