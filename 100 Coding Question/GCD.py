# Function to find GCD using loop
def gcd(a, b):
    
    while b != 0:
        a, b = b, a % b   # Euclidean algorithm
    
    return a


# Input
x = int(input("Enter first number: "))
y = int(input("Enter second number: "))

print("GCD =", gcd(x, y))


#OUTPUT
#Enter first number: 456
#Enter second number: 567
#GCD = 3
