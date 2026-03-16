#QUE-5 Create a NumPy array of numbers from 1 to 25 and reshape it into a 5×5 matrix. Extract the middle 3×3 sub-matrix.
import numpy as np

arr = np.arange(1,26).reshape(5,5)

middle = arr[1:4,1:4]

print(middle)

#Output

#[[ 7  8  9]
# [12 13 14]
# [17 18 19]]
