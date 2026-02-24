# Safely remove a key

d = eval(input("Enter dictionary: "))
key = input("Enter key to remove: ")

# pop with default avoids error
removed = d.pop(key, None)

if removed is None:
    print("Key not found")
else:
    print("Updated dictionary:", d)

#OUTPUT
#Enter dictionary: {'a': 10, 'b': 20, 'c': 30}
#Enter key to remove: b
#Updated dictionary: {'a': 10, 'c': 30}
