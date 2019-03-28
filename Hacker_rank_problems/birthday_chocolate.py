def birthday(s, d, m):
    if len(s) != 1:
        count = 0

        # get the index starting and ending with birthday_month
        starting_index = 0
        ending_index = m - 1
        while (len(s) != ending_index):
            sums = 0
            for i in range(starting_index, ending_index):
                sums += s[i]
            starting_index += 1
            ending_index += 1
            # add the index value continuously one by one and check the sum is equal to the birthday_day
            if sums == d:
                count = count + 1
        return count
    else:
        return m


s = [1, 2, 1, 3, 2]
d = 3
m = 2

print(birthday(s, d, m))
