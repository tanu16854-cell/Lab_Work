# Replace vowels

s = input("Enter string: ")

vowels = "aeiouAEIOU"
result = ""

for ch in s:
    if ch in vowels:
        result += "*"
    else:
        result += ch

print("Result:", result)


#output
#Enter string: Tanu
#Result: T*n*
