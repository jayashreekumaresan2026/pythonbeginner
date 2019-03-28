def check_anagram(s1, s2):
    s1 = s1.replace(" ", "")
    s2 = s2.replace(" ", "")
    print(s1)
    print(s2)
    if (sorted(s1) == sorted(s2)):
        print(sorted(s1))
        print(sorted(s2))
        print("True")
    else:
        print("false")


string_1 = "astronomer"
string_2 = "moon starer"
check_anagram(string_1, string_2)
