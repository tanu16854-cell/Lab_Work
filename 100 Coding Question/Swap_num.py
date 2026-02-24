# Swap two numbers without using third variable

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

# Swapping
a = a + b
b = a - b
a = a - b

print("After swapping:")
print("a =", a)
print("b =", b)
