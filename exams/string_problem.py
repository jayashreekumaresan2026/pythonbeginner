def string_problem(list_string):
    list_string = list_string.lower()
    print(list_string)
    _string = {}
    # list_string = list_string.split(",")
    list_string=list(list_string)
    print(list_string)
    for i in range(0, len(list_string)):
        _string[list_string[i]] = list_string.count(list_string[i])
        print(_string)
    for key in _string:
        if _string[key] == value:
            print(key)


value = 2
list_string = "Abcabbdc"
string_problem(list_string)
