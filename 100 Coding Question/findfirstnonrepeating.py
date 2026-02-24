# Find first non-repeating character

s = input("Enter string: ")

for ch in s:
    if s.count(ch) == 1:
        print("First non-repeating:", ch)
        break
#OUTPUT
#Enter string: tannu
#First non-repeating: t
