# Program to find symmetric difference

set1 = set(map(int, input("Enter set1: ").split()))
set2 = set(map(int, input("Enter set2: ").split()))

result = set1 ^ set2

print("Symmetric difference:", result)


#Output
#Enter set1: 1 2 3
#Enter set2: 2 3 4
#Symmetric difference: {1, 4}
