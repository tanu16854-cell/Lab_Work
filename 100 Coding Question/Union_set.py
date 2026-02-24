# Union of two sets

set1 = set(map(int, input("Enter set1: ").split()))
set2 = set(map(int, input("Enter set2: ").split()))

result = set1.union(set2)

print("Union:", result)

#OUTPUT
#Enter set1: 23
#Enter set2: 34
#Union: {34, 23}
