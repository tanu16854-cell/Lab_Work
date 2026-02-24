# Program to find largest element

numbers = list(map(int, input("Enter numbers: ").split()))

largest = numbers[0]

for num in numbers:
    if num > largest:
        largest = num

print("Largest element:", largest)


#Output
#Enter numbers: 3 7 2 9 5
#Largest element: 9
