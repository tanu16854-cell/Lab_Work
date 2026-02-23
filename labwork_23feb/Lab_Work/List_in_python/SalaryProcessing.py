# Salary Processing System
# This program:
# 1. Removes salaries below minimum wage
# 2. Adds 5% bonus to employees with salary > 50,000
# 3. Sorts salaries in descending order
# 4. Displays top 3 highest salaries

#List of employee salaries
salaries = [25000, 60000, 45000, 80000, 30000, 52000, 15000]
#--------------------------------------------
# Define minimum wage
min_wage = 20000
#------------------------------------------
#Remove salaries below minimum wage
valid_salaries = []

for sal in salaries:
    if sal >= min_wage:
        valid_salaries.append(sal)

print("Valid Salaries:", valid_salaries)
print("--------------------------------------")
#----------------------------------------------
#Add 5% bonus for salaries > 50,000
updated_salaries = []

for sal in valid_salaries:
    if sal > 50000:
        bonus = sal * 0.05
        sal = sal + bonus
    updated_salaries.append(sal)

print("Salaries After Bonus:", updated_salaries)
print("--------------------------------------")
#--------------------------------------------
#Sort salaries in descending order
updated_salaries.sort(reverse=True)

print("Sorted Salaries (High to Low):", updated_salaries)
print("--------------------------------------")
#----------------------------------------------------
#Display top 3 highest salaries
top_3 = updated_salaries[:3]

print("Top 3 Highest Salaries:", top_3)
print("--------------------------------------")
