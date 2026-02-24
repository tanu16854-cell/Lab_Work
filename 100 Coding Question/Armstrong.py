# Program to check Armstrong number

num = int(input("Enter a number: "))
original = num

# Count digits
count = len(str(num))
sum_power = 0

# Calculate sum of powers
while num > 0:
    digit = num % 10
    sum_power += digit ** count
    num = num // 10

# Check condition
if sum_power == original:
    print("Armstrong Number")
else:
    print("Not an Armstrong Number")

#OUTPUT
#Enter a number: 153
#Armstrong Number
