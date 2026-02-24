# Recursive function to calculate power
def power(base, exp):
    
    # Base case
    if exp == 0:
        return 1
    
    # Recursive call
    return base * power(base, exp - 1)


# Input
b = int(input("Enter base: "))
e = int(input("Enter exponent: "))

print("Result =", power(b, e))

#OUTPUT
#Enter base: 3
#Enter exponent: 5
#Result = 243
