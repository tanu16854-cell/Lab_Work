# Function to count vowels
def count_vowels(text):
    count = 0
    
    # Convert to lowercase
    text = text.lower()
    
    for ch in text:
        if ch in "aeiou":
            count += 1
    
    return count


# Input
text = input("Enter string: ")

print("Vowels =", count_vowels(text))

#OUTPUT
#Enter string: tanu
#Vowels = 2
