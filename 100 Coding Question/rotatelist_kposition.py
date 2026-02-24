# Program to rotate a list by K positions (left rotation)

numbers = list(map(int, input("Enter list: ").split()))
k = int(input("Enter K: "))

n = len(numbers)

# Handle large K values
k = k % n

# Rotate list
rotated = numbers[k:] + numbers[:k]

print("Rotated list:", rotated)


#Output
#Enter list: 1 2 3 4 5
#Enter K: 2
#Rotated list: [3, 4, 5, 1, 2]
