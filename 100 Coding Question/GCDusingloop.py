# Program to find GCD

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

# Euclidean Algorithm
while b != 0:
    temp = b
    b = a % b
    a = temp

print("GCD is:", a)
#OUTPUT
#Enter first number: 12
#Enter second number: 18
#GCD is: 6
