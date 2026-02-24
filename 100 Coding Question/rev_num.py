# Program to reverse a number

# Taking input
num = int(input("Enter a number: "))

# Store original for display
original = num

reverse = 0

# Loop to reverse digits
while num != 0:
    digit = num % 10              # Extract last digit
    reverse = reverse * 10 + digit  # Build reversed number
    num = num // 10               # Remove last digit

# Display result
print("Reverse of", original, "is:", reverse)

#OUTPUT
#Enter a number: 234
#Reverse of 234 is: 432
