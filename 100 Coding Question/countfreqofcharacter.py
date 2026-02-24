# Count frequency of characters

s = input("Enter string: ")

freq = {}

for ch in s:
    freq[ch] = freq.get(ch, 0) + 1

print("Frequency:", freq)

#OUTPUT
#Enter string: tanuRAna
#Frequency: {'t': 1, 'a': 2, 'n': 2, 'u': 1, 'R': 1, 'A': 1}

