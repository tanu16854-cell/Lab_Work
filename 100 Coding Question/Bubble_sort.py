# Bubble sort algorithm

lst = list(map(int, input("Enter elements: ").split()))

# Sorting logic
for i in range(len(lst)):
    for j in range(len(lst) - i - 1):
        
        # Swap if elements are in wrong order
        if lst[j] > lst[j + 1]:
            lst[j], lst[j + 1] = lst[j + 1], lst[j]

print("Sorted list:", lst)
#Output
#Enter elements: 34
#Sorted list: [34]
