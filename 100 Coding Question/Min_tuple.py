# Program to find minimum value in tuple

t = tuple(map(int, input("Enter tuple values: ").split()))

minimum = t[0]

for num in t:
    if num < minimum:
        minimum = num

print("Minimum value:", minimum)

#Output
#Enter tuple values: 3 7 1 9
#Minimum value: 1
