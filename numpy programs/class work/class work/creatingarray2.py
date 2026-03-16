#creating an array of five elements
import numpy as np
n1= np.array([1,2,3,4,5])
print("Array of five elements :")
print(n1)
print("------------------------------")
print("After multiply each emlements by 10 :")
print(n1*10)

#Zeros array
array1= np.zeros([3,4])
print("zeros array of order(3,4)")
print(array1)
#zeros array
array2 = np.zeros((5,3),dtype=int)
print("zeros array of order(5,3)")
print(array2)





#OUTPUT---------

#Array of five elements :
#[1 2 3 4 5]
#------------------------------
#After multiply each emlements by 10 :
#[10 20 30 40 50]
