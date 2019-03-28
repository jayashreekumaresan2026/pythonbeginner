def replace_string(string):
    string.replace("%20", '===')
    print(string)


string = "we%20use%20%%20to%20find%20remainder"
replace_string(string)
