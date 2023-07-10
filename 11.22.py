# Joshua Soto
# 1553869

# Assigns inputs to words
words = input()

# Splits inputs by the space between them then adds them to a list
words_list = words.split(" ")

# Prints words and how often they occur
for words in words_list:
    print(words, words_list.count(words))
