# Program to find difference of two sets

set1 = set(map(int, input("Enter set1: ").split()))
set2 = set(map(int, input("Enter set2: ").split()))

result = set1 - set2

print("Difference:", result)


#Output
#Enter set1: 1 2 3
#Enter set2: 2 3 4
#Difference: {1}
