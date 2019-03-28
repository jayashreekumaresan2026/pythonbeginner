def find_the_legs_and_chick(number_of_legs, number_of_heads):
    for number_of_chicks in range(0, number_of_heads + 1):
        number_of_rabbit = number_of_heads - number_of_chicks
        total = 4 * number_of_rabbit + 2 * number_of_chicks
        if total == number_of_legs:
            return [number_of_rabbit, number_of_chicks]
    return 0


heads = 35
legs = 94
print(find_the_legs_and_chick(legs, heads))
