# Program to check if all elements in tuple are unique

t = tuple(map(int, input("Enter tuple values: ").split()))

unique = True

for i in range(len(t)):
    for j in range(i + 1, len(t)):
        if t[i] == t[j]:
            unique = False
            break

if unique:
    print("All elements are unique")
else:
    print("Duplicates found")


#Output
#Enter tuple values: 1 2 3 4
#All elements are unique
