#QUE-3 Create array 1–10 and replace even numbers with 0

import numpy as np

arr = np.arange(1,11)

arr[arr % 2 == 0] = 0

print(arr)

#OUTPUT
#[1 0 3 0 5 0 7 0 9 0]
