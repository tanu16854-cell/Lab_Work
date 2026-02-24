# Program to calculate BMI and category

# Taking input
weight = float(input("Enter weight (kg): "))
height = float(input("Enter height (m): "))

# BMI formula
bmi = weight / (height ** 2)

# Checking category
if bmi < 18.5:
    print("Underweight")
elif bmi < 25:
    print("Normal")
elif bmi < 30:
    print("Overweight")
else:
    print("Obese")

#OUTPUT
#Output
#Enter weight (kg): 60
#Enter height (m): 1.7
#Normal
