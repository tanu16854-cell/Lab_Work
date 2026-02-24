# Program to find maximum value in tuple

t = tuple(map(int, input("Enter tuple values: ").split()))

maximum = t[0]

for num in t:
    if num > maximum:
        maximum = num

print("Maximum value:", maximum)


# Output
#Enter tuple values: 3 7 1 9
#Maximum value: 9
