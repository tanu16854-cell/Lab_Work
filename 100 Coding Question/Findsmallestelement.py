# Program to find smallest element

numbers = list(map(int, input("Enter numbers: ").split()))

smallest = numbers[0]

for num in numbers:
    if num < smallest:
        smallest = num

print("Smallest element:", smallest)



# Output
#Enter numbers: 3 7 2 9 5
#Smallest element: 2
