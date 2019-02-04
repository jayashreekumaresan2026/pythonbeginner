# user_input=input("Hypen separate words")
# sequence_words=[word for word in user_input.split("-")]
# print("-".join(sorted(list(sequence_words))))


def sort_words(hyphenated_string):
    split_words = hyphenated_string.split("-")
    sorted_words = sorted(split_words)
    joined_string = "-".join(sorted_words)
    return joined_string


print(sort_words("green-red-yellow-black-white"))
