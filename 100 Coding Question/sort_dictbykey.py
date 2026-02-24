# Program to sort dictionary by keys

d = eval(input("Enter dictionary: "))

sorted_dict = {}

for key in sorted(d.keys()):
    sorted_dict[key] = d[key]

print("Sorted by keys:", sorted_dict)

#Output
#Enter dictionary: {'b': 2, 'a': 1, 'c': 3}
#Sorted by keys: {'a': 1, 'b': 2, 'c': 3}
