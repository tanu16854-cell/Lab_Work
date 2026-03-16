#QUE-9 Generate a NumPy array of 10 random numbers between 0 and 1 and normalize the array between 0 and 1.
import numpy as np

arr = np.random.rand(10)

normalized = (arr - arr.min()) / (arr.max() - arr.min())

print("Original Array:")
print(arr)
print("------------------------------------")
print("Normalized Array:")
print(normalized)




#OUTPUT
#Original Array:
#[0.12307502 0.76353994 0.15144241 0.00871674 0.71861725 0.52854336
# 0.02202263 0.55408032 0.35016515 0.70997798]
#------------------------------------
#Normalized Array:
#[0.1515034  1.         0.1890849  0.         0.94048581 0.68867335
# 0.01762783 0.72250507 0.45235549 0.9290404 ]

