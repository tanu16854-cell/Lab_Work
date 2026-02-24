# Check if key exists

d = eval(input("Enter dictionary: "))
key = input("Enter key: ")

if key in d:
    print("Key exists")
else:
    print("Key does not exist")
#OUTPUT
#Enter dictionary: {'a': 10, 'b': 20, 'c': 30}
#Enter key: b
#Key exists
