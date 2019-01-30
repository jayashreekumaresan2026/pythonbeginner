user_input=input("Hypen separate words")
sequence_words=[word for word in user_input.split("-")]
print("-".join(sorted(list(sequence_words))))