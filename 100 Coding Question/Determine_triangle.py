# Program to determine triangle type

# Taking input
a = float(input("Enter side 1: "))
b = float(input("Enter side 2: "))
c = float(input("Enter side 3: "))

# Checking triangle type
if a == b == c:
    print("Equilateral Triangle")
elif a == b or b == c or a == c:
    print("Isosceles Triangle")
else:
    print("Scalene Triangle")

# Output
#Enter side 1: 5
#Enter side 2: 5
#Enter side 3: 5
#Equilateral Triangle
