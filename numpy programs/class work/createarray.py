import numpy as np
print("-------------Created array using numpy----------------")
#First array(int)
n1=np.array([45,78,90])
print("Array 1 :")
print(n1)
print("---------------------------------")

#Second array(float)

n2=np.array([2.4,4.5,6.7])
print("Array 2 :")
print(n2)
print("---------------------------")

#Third array(string)

n3=np.array([2.4,4.5,6.7,'hello'])
print("Array 3 :")
print(n3)
print("--------------------------------")

#multiply each element by 1

print("After multiply by 3 :")
print(n1*3)
print("-----------------------------------")

#Element greater than 70

print("Elements > 70 :")
print(n1>70)
print("-----------------------------------")

#2d array

matrix1 =np.array([[34,56,67],[56,67,86]])
print("2d array :")
print(matrix1)
print("-----------------------------------")
#3d array

matrix2 =np.array([[34,56,67],[56,67,86],[56,78,98]])
print("3d array :")
print(matrix2)
print("-----------------------------------")
#output
#-------------Created array using numpy----------------
#Array 1 :
#[45 78 90]
#---------------------------------
#Array 2 :
#[2.4 4.5 6.7]
#---------------------------
#Array 3 :
#['2.4' '4.5' '6.7' 'hello']
#--------------------------------
#After multiply by 3 :
#[135 234 270]
#-----------------------------------
#Elements > 70 :
#[False  True  True]
#-----------------------------------
#2d array :
#[[34 56 67]
 #[56 67 86]]
#-----------------------------------
#3d array :
#[[34 56 67]
 #[56 67 86]
 #[56 78 98]]
#----------------------------------


