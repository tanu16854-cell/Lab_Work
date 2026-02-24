# Program to remove duplicate elements

numbers = list(map(int, input("Enter numbers: ").split()))
unique_list = []

for num in numbers:
    if num not in unique_list:
        unique_list.append(num)

print("List after removing duplicates:", unique_list)


#Output
#Enter numbers: 1 2 2 3 4 4
#List after removing duplicates: [1, 2, 3, 4]
