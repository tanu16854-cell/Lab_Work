# Function to return unique elements
def unique_list(lst):
    return list(set(lst))


# Input
lst = list(map(int, input("Enter elements: ").split()))

print("Unique elements:", unique_list(lst))
#OUTPUT
#Enter elements: 2
#Unique elements: [2]
