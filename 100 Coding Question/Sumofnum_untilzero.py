# Program to sum numbers until user enters 0

total = 0

while True:
    num = int(input("Enter a number (0 to stop): "))
    
    if num == 0:
        break
    
    total += num

print("Total sum:", total)
#OUTPUT
#Enter a number: 5
#Enter a number: 3
#Enter a number: 0
#Total sum: 8
