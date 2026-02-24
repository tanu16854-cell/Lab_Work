# Program to count digits in a number

num = int(input("Enter a number: "))
count = 0

# Handle zero case
if num == 0:
    count = 1
else:
    num = abs(num)
    while num > 0:
        count += 1
        num = num // 10

print("Total digits:", count)
#OUTPUT
#Enter a number: 56789
#Total digits: 5
