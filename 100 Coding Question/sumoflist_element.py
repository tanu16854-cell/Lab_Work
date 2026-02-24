# Program to find sum of list elements

numbers = list(map(int, input("Enter numbers: ").split()))

total = 0

for num in numbers:
    total += num

print("Sum:", total)


#Output
#Enter numbers: 1 2 3 4
#Sum: 10
