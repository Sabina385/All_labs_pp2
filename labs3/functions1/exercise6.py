def reverse_words_in_sentence(sentence):
    return ' '.join(sentence.split()[::-1])
user_input = input("Enter sentence: ")
print(reverse_words_in_sentence(user_input))