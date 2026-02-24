# Convert to title case manually

s = input("Enter sentence: ")

words = s.split()
result = ""

for word in words:
    result += word[0].upper() + word[1:].lower() + " "

print("Title case:", result.strip())

#OUTPUT
#Enter sentence: Abhinav is very intelligent boy
#Title case: Abhinav Is Very Intelligent Boy

