# Program to check subset

set1 = set(map(int, input("Enter set1: ").split()))
set2 = set(map(int, input("Enter set2: ").split()))

if set1.issubset(set2):
    print("set1 is subset of set2")
else:
    print("set1 is NOT subset of set2")

#Output
#Enter set1: 1 2
#Enter set2: 1 2 3
#set1 is subset of set2
