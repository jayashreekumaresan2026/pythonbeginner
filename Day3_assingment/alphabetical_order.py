def alpha(word):
    my_array=sorted(word)
    my_list=''.join(my_array)
    if my_list == word:
         return True
    else:
        return False

print(alpha('acbd'))
print(alpha('abcd'))

