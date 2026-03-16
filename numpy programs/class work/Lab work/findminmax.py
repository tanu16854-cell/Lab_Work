#QUE-2 Create a 5×5 matrix with random integers between 1 and 100 and find min & max
import numpy as np

# Create random 5x5 matrix
matrix = np.random.randint(1, 101, (5,5))

print("Matrix:")
print(matrix)

# Find minimum and maximum
print("Min =", matrix.min())
print("Max =", matrix.max())



#OUTPUT
#Matrix:
#[[35 25 87 31 55]
# [35 26  3 37 94]
# [10 79 19 14 33]
# [65 78 80 40 19]
# [40 98  6 66 97]]
#Min = 3
#Max = 98
