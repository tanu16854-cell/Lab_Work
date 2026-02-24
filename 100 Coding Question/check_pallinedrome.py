# Check palindrome

s = input("Enter string: ")

rev = ""

for ch in s:
    rev = ch + rev

if s == rev:
    print("Palindrome")
else:
    print("Not palindrome")

#OUTPUT
#Enter string: tanu
#Not palindrome
