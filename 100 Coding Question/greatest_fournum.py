# Program to find greatest of four numbers

# Taking input
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
c = int(input("Enter third number: "))
d = int(input("Enter fourth number: "))

# Finding greatest
greatest = a

if b > greatest:
    greatest = b
if c > greatest:
    greatest = c
if d > greatest:
    greatest = d

# Display result
print("Greatest number is:", greatest)

#OUTPUT
#Enter first number: 10
#Enter second number: 25
#Enter third number: 7
#Enter fourth number: 18
#Greatest number is: 25
