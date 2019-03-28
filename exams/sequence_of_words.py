def sequence_of_words():
    list_array=[]
    user_input = input("Given a input comma separated of words")
    print(user_input)
    for word in user_input.split(","):
        list_array.append(word)
    print(",".join(sorted(list_array)))


sequence_of_words()
