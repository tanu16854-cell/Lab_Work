# Function to check palindrome
def is_palindrome(text):
    # Compare string with its reverse
    return text == text[::-1]


# Input
text = input("Enter string: ")

# Output
if is_palindrome(text):
    print("Palindrome")
else:
    print("Not Palindrome")



#OUTPUT
#Enter string: ama
#Palindrome
