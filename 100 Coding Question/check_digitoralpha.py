# Program to check digit or alphabet

# Taking input
ch = input("Enter a character: ")

# Using built-in functions
if ch.isdigit():
    print("It is a Digit")
elif ch.isalpha():
    print("It is an Alphabet")
else:
    print("Special Character")
#OUTPUT
#Enter a character: 5
#It is a Digit
