# Compress string using counts

s = input("Enter string: ")

result = ""
count = 1

for i in range(len(s) - 1):
    if s[i] == s[i + 1]:
        count += 1
    else:
        result += s[i] + str(count)
        count = 1

# last character
result += s[-1] + str(count)

print("Compressed string:", result)

#OUTPUT
#Enter string: tanu
#Compressed string: t1a1n1u1
