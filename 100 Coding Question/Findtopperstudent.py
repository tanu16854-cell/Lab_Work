# Find topper student

students = {}

n = int(input("Enter number of students: "))

# Input data
for i in range(n):
    name = input("Enter name: ")
    marks = int(input("Enter marks: "))
    students[name] = marks

# Find topper
topper = max(students, key=students.get)

print("Topper:", topper)

#OUTPUT
#Enter number of students: 2
#Enter name: Abhinav
#Enter marks: 95
#Enter name: tanu
#Enter marks: 89
#Topper: Abhinav
