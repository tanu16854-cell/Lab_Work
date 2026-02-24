# Function to find maximum
def find_max(a, b, c):
    
    # Compare values
    if a > b and a > c:
        return a
    elif b > c:
        return b
    else:
        return c


# Input
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
c = int(input("Enter third number: "))

print("Maximum =", find_max(a, b, c))

#OUTPUT
#Enter first number: 3
#Enter second number: 4
#Enter third number: 5
#Maximum = 5
