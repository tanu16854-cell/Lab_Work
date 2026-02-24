# Program to find factorial

n = int(input("Enter a number: "))
fact = 1

for i in range(1, n + 1):
    fact *= i

print("Factorial:", fact)
#output
#Enter a number: 5
#Factorial: 120
