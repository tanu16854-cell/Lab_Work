# Program to find sum of digits

# Taking input
num = int(input("Enter a number: "))

# Convert number to positive (for safety)
num = abs(num)

sum_digits = 0

# Loop until number becomes 0
while num > 0:
    digit = num % 10        # Get last digit
    sum_digits += digit     # Add digit
    num = num // 10         # Remove last digit

# Display result
print("Sum of digits:", sum_digits)
#output
#Enter a number: 23
#Sum of digits: 5
