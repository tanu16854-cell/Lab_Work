# Find longest word

s = input("Enter sentence: ")

words = s.split()

longest = words[0]

for word in words:
    if len(word) > len(longest):
        longest = word

print("Longest word:", longest)

#OUTPUT
#Enter sentence: Abhinav is very intelligent boy
#Longest word: intelligent
