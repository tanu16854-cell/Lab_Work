# Program to count occurrence of an element in tuple

t = tuple(map(int, input("Enter tuple values: ").split()))
x = int(input("Enter element to count: "))

count = 0

for num in t:
    if num == x:
        count += 1

print("Occurrence:", count)


#Output
#Enter tuple values: 1 2 2 3 2
#Enter element to count: 2
#Occurrence: 3
