#QUE-8 Create a 3×3 matrix and calculate the transpose of the matrix.
import numpy as np

matrix = np.array([[1,2,3],
                   [4,5,6],
                   [7,8,9]])

transpose = matrix.T

print(transpose)

#Output

#[[1 4 7]
# [2 5 8]
# [3 6 9]]
