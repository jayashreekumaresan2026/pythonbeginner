
def Check_Vow(string, vowels):
    array=[]
    for each in string:
        if each in vowels:
            array.append(each)
    print(array)
    print(len(array))



string = "Geeks for Geeks"
vowels = "AeEeIiOoUu"
Check_Vow(string, vowels)
