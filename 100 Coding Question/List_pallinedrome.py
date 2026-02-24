# Check list palindrome

lst = list(map(int, input("Enter elements: ").split()))

# Compare with reverse
if lst == lst[::-1]:
    print("Palindrome List")
else:
    print("Not Palindrome")
#OUTPUT
#Enter elements: 121
#Palindrome List
