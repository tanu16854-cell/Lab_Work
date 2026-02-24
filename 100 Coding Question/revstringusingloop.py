# Program to reverse a string using for loop

text = input("Enter a string: ")
reverse = ""

# Loop from end to start
for i in range(len(text) - 1, -1, -1):
    reverse += text[i]

print("Reversed string:", reverse)


#Output
#Enter a string: hello
#Reversed string: olleh
