# Program to check even or odd without using %

# Taking input
num = int(input("Enter a number: "))

# Logic: If (num // 2) * 2 == num → Even
if (num // 2) * 2 == num:
    print("Even Number")
else:
    print("Odd Number")


#OUTPUT
#Enter a number: 2
#Even Number
