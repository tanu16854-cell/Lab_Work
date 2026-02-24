# Sum all values in dictionary

d = eval(input("Enter dictionary: "))

total = 0

for value in d.values():
    total += value

print("Sum of values:", total)

#OUTPUT
#Enter dictionary: {'a': 10, 'b': 20, 'c': 30}
#Sum of values: 60
