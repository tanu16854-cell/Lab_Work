# Program to count vowels in a string

text = input("Enter a string: ")

count = 0

# Convert to lowercase for easy checking
text = text.lower()

# Loop through each character
for ch in text:
    if ch in "aeiou":
        count += 1

print("Total vowels =", count)


#OUTPUT
#Enter a string: tanurana
#Total vowels = 4

