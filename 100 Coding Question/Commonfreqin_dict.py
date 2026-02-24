# Count frequency using dictionary

lst = list(map(int, input("Enter elements: ").split()))

freq = {}

# Counting logic
for item in lst:
    if item in freq:
        freq[item] += 1
    else:
        freq[item] = 1

print("Frequency:", freq)

#Output
#Enter elements: 45
#Frequency: {45: 1}
