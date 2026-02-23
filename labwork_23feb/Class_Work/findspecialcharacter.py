# Program to count number of special characters in a sentence

# Take input from user
text = input("Enter a sentence: ")
print("------------------------------------")
count = 0   # variable to count special characters
# Loop through each character
for ch in text:
    # Check if character is NOT letter and NOT digit and NOT space
    if not ch.isalnum() and ch != " ":
        count += 1
# Display result
print("Number of special characters:", count)
