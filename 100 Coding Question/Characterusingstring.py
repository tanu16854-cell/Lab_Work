# Count character frequency in string

text = input("Enter string: ")

freq = {}

# Counting logic
for ch in text:
    if ch in freq:
        freq[ch] += 1
    else:
        freq[ch] = 1

print("Character frequency:", freq)

#output
#Enter string: tanu
#Character frequency: {'t': 1, 'a': 1, 'n': 1, 'u': 1}
