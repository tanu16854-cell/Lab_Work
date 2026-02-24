# Program to merge two lists and remove duplicates

list1 = list(map(int, input("Enter list1: ").split()))
list2 = list(map(int, input("Enter list2: ").split()))

merged = list1 + list2
result = []

for num in merged:
    if num not in result:
        result.append(num)

print("Merged unique list:", result)


# Output
#Enter list1: 1 2 3
#Enter list2: 2 3 4
#Merged unique list: [1, 2, 3, 4]
