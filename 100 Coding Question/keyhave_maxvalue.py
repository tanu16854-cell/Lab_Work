# Find key having maximum value

d = eval(input("Enter dictionary: "))

max_key = max(d, key=d.get)

print("Key with maximum value:", max_key)

#Output
#Enter dictionary: {'a':10,'b':25,'c':15}
#Key with maximum value: b
