# Create dictionary from two lists

keys = input("Enter keys: ").split()
values = list(map(int, input("Enter values: ").split()))

d = {}

for i in range(len(keys)):
    d[keys[i]] = values[i]

print("Dictionary:", d)

#OUTPUT
#Enter keys: a b c
#Enter values: 10 20 30
#Dictionary: {'a': 10, 'b': 20, 'c': 30}
