# Create a list of 20 numbers
numbers = [1, 5, 3, 7, 5, 9, 5, 2, 8, 5,
           4, 6, 5, 10, 11, 5, 12, 13, 5, 14]

print("Original List:", numbers)

# Take input from user
num = int(input("Enter number to delete: "))

# Check if number is in list
if num in numbers:
    
    # Remove first occurrence index
    first = numbers.index(num)
    
    # Remove all occurrences
    while num in numbers:
        numbers.remove(num)
    
    # Insert first occurrence back
    numbers.insert(first, num)

    print("Updated List:", numbers)

else:
    print("Number not found")
