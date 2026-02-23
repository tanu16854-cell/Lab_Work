# Palindrome Checker
# This program checks whether a string is palindrome or not
# (same forward and backward)

text = input("Enter text: ")

# reverse string using slicing
reverse_text = text[::-1]

if text == reverse_text:
    print("Palindrome")
else:
    print("Not Palindrome")
