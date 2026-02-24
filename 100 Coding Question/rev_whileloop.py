# Program to reverse a number using while loop

num = int(input("Enter a number: "))
reverse = 0

# Loop until number becomes 0
while num != 0:
    digit = num % 10
    reverse = reverse * 10 + digit
    num = num // 10

print("Reversed number:", reverse)

#OUTPUT
#Enter a number: 1234
#Reversed number: 4321
