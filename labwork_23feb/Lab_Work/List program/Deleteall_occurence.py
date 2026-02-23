# Remove all duplicate numbers except first occurrence

numbers = [1, 2, 3, 2, 4, 1, 5]

result = []

for num in numbers:
    if num not in result:
        result.append(num)

print("Updated List:", result)
