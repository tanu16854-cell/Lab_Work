# Program to assign grades based on marks

# Taking input
marks = float(input("Enter your marks: "))

# Checking grade
if marks >= 90:
    print("Grade: A")
elif marks >= 75:
    print("Grade: B")
elif marks >= 50:
    print("Grade: C")
else:
    print("Grade: Fail")
