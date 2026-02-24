# Program to generate Fibonacci series

n = int(input("Enter number of terms: "))

a, b = 0, 1
count = 0

while count < n:
    print(a, end=" ")
    c = a + b
    a = b
    b = c
    count += 1
#OUTPUT
#Enter number of terms: 5
#0 1 1 2 3
