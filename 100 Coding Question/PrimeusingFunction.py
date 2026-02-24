# Function to check prime number
def is_prime(n):
    
    # Numbers less than 2 are not prime
    if n <= 1:
        return False
    
    # Check divisibility
    for i in range(2, n):
        if n % i == 0:
            return False
    
    return True


# Taking input
num = int(input("Enter a number: "))

# Calling function
if is_prime(num):
    print("Prime Number")
else:
    print("Not a Prime Number")

#OUTPUT
#Enter a number: 2
#Prime Number
