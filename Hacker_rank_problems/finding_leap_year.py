def is_leap(year):
    leap_year= False
    if (year % 4) == 0:
        if (year % 100) == 0:
            if (year % 400) == 0:
                return True
            else:
                return False
        else:
            return True
    else:
        return False

    return leap_year
year = int(input())
print(is_leap(year))