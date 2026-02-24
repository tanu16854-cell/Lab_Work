# Count uppercase and lowercase

s = input("Enter string: ")

upper = 0
lower = 0

for ch in s:
    if ch.isupper():
        upper += 1
    elif ch.islower():
        lower += 1

print("Uppercase:", upper)
print("Lowercase:", lower)

#OUTPUT
#Enter string: taNu
#Uppercase: 1
#Lowercase: 3
