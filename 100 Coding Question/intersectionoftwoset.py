# Program to find intersection of two sets

set1 = set(map(int, input("Enter set1: ").split()))
set2 = set(map(int, input("Enter set2: ").split()))

result = set1 & set2

print("Intersection:", result)


#Output
#Enter set1: 1 2 3
#Enter set2: 2 3 4
#Intersection: {2, 3}
