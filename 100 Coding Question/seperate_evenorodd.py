# Program to separate even and odd numbers

numbers = list(map(int, input("Enter numbers: ").split()))

even = []
odd = []

for num in numbers:
    if num % 2 == 0:
        even.append(num)
    else:
        odd.append(num)

print("Even numbers:", even)
print("Odd numbers:", odd)

# Output
#Enter numbers: 1 2 3 4 5
#Even numbers: [2, 4]
#Odd numbers: [1, 3, 5]
