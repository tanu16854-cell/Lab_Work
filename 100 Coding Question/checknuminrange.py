# Program to check number in range

# Taking input
num = int(input("Enter a number: "))
start = int(input("Enter start range: "))
end = int(input("Enter end range: "))

# Checking condition
if start <= num <= end:
    print("Number is within range")
else:
    print("Number is outside range")

#OUTPUT
#Enter a number: 10
#Enter start range: 5
#Enter end range: 15
#Number is within range
