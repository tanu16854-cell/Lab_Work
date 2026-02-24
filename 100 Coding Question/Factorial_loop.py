# Program to find factorial using while loop

n = int(input("Enter a number: "))

fact = 1
i = 1

# Loop to calculate factorial
while i <= n:
    fact *= i
    i += 1

print("Factorial =", fact)


#Output
#Enter a number: 24
#Factorial = 620448401733239439360000
