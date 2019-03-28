def Check_Vow(string, vowels):


    string=string.casefold()
    print(string)
    array = {}.fromkeys(vowels, 0)
    for each in string:
        if each in vowels:
            array[each] += 1
    print(array)
    print(len(array))


string = "geeks FOR Geeks"
vowels = "aeiou"
Check_Vow(string, vowels)
