# Remove duplicate characters

s = input("Enter string: ")

result = ""

for ch in s:
    if ch not in result:
        result += ch

print("Without duplicates:", result)
#Output
#Enter string: Abhinav
#Without duplicates: Abhinav
