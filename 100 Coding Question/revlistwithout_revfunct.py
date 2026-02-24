# Program to reverse a list without using reverse()

numbers = list(map(int, input("Enter numbers: ").split()))
reversed_list = []

for i in range(len(numbers) - 1, -1, -1):
    reversed_list.append(numbers[i])

print("Reversed list:", reversed_list)


#Output
#Enter numbers: 1 2 3 4
#Reversed list: [4, 3, 2, 1]
