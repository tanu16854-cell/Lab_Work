# Program to replace negative numbers with 0

numbers = list(map(int, input("Enter numbers: ").split()))

for i in range(len(numbers)):
    if numbers[i] < 0:
        numbers[i] = 0

print("Updated list:", numbers)


#Output
#Enter numbers: -1 2 -3 4
#Updated list: [0, 2, 0, 4]
