# Remove spaces

s = input("Enter string: ")

result = ""

for ch in s:
    if ch != " ":
        result += ch

print("Without spaces:", result)

#OUtput
#Enter string: tanu Abhinav
#Without spaces: tanuAbhinav
