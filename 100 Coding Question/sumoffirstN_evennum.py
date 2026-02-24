# Program to find sum of even numbers up to N

n = int(input("Enter value of N: "))
i = 1
sum_even = 0

while i <= n:
    if i % 2 == 0:
        sum_even += i
    i += 1

print("Sum of even numbers:", sum_even)
#OUTPUT
#Enter value of N: 10
#Sum of even numbers: 30
