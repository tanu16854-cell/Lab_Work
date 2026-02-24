# Check anagram

s1 = input("Enter first string: ")
s2 = input("Enter second string: ")

if sorted(s1) == sorted(s2):
    print("Anagram")
else:
    print("Not Anagram")
#output
#Enter first string: Abhinav
#Enter second string: Tanu
#Not Anagram
