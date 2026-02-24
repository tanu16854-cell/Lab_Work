# Program to merge two dictionaries manually

dict1 = eval(input("Enter first dictionary: "))
dict2 = eval(input("Enter second dictionary: "))

merged = {}

# Add elements from dict1
for key in dict1:
    merged[key] = dict1[key]

# Add elements from dict2
for key in dict2:
    merged[key] = dict2[key]

print("Merged dictionary:", merged)

#Output
#Enter first dictionary: {'a': 1, 'b': 2}
#Enter second dictionary: {'b': 3, 'c': 4}
#Merged dictionary: {'a': 1, 'b': 3, 'c': 4}
