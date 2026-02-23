#dictionary example
student = {}
# to insert an element
student['name'] = 'Tanu Rana'
# to insert element
student['rollno'] = 1056
student['Hindi'] = 42
print("Dictionary is : ")
print(student)
print("--------------------------")
#----------------------------
#insert another student
student['english']= 56
student['hindi']=90
print("Updated dictionary is : ")
print(student)
print("---------------------------")
#using loop
for key in student:
    print(key,":",student(key))
# to retunr all keys
print("key are",student.key())
# to return all values 
print("values are",student.values())
print(student.get,(name))
