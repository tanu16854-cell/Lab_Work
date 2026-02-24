# Reverse string manually

s = input("Enter string: ")

rev = ""

for ch in s:
    rev = ch + rev

print("Reversed string:", rev)

#OUTPUT
#Enter string: tanu
#Reversed string: unat
