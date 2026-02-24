# Program to sort dictionary by values

d = eval(input("Enter dictionary: "))

sorted_items = sorted(d.items(), key=lambda x: x[1])

sorted_dict = {}

for key, value in sorted_items:
    sorted_dict[key] = value

print("Sorted by values:", sorted_dict)


#Output
#Enter dictionary: {'a': 3, 'b': 1, 'c': 2}
#Sorted by values: {'b': 1, 'c': 2, 'a': 3}
