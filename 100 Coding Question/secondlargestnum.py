# Program to find second largest number

numbers = list(map(int, input("Enter numbers: ").split()))

largest = second = float('-inf')

for num in numbers:
    if num > largest:
        second = largest
        largest = num
    elif num > second and num != largest:
        second = num

print("Second largest:", second)

#Output
#Enter numbers: 10 20 30 40
#Second largest: 30
