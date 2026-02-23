# Word Counter
# This program counts number of words in a sentence

text = input("Enter a sentence: ")

words = text.split()     # split sentence into words
word_count = len(words)

print("Number of words:", word_count)
