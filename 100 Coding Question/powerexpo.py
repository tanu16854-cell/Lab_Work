# Program to calculate power without using **

base = int(input("Enter base: "))
power = int(input("Enter exponent: "))

result = 1

for i in range(power):
    result *= base

print("Result:", result)

#Output
#Enter base: 2
#Enter exponent: 3
#Result: 8
