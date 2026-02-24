# Function to find sum of digits
def sum_digits(n):
    total = 0
    
    # Loop until number becomes 0
    while n > 0:
        digit = n % 10
        total += digit
        n //= 10
    
    return total


# Input
num = int(input("Enter number: "))


print("Sum of digits =", sum_digits(num))
#OUTPUT
#Enter number: 34
#Sum of digits = 7
