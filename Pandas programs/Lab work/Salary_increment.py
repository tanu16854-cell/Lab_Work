
'''#Q2: Salary Increment Logic
Dataset:

    #salary = [25000, 32000, 28000, 40000, 50000]
    #emp = ['A', 'B', 'C', 'D', 'E']
    #s = pd.Series(salary, index=emp)

#Tasks:

    #Increase salary by 10% where salary < 30000 Decrease salary by 5% where salary> 45000 Find total salary expense after changes

'''
import pandas as pd
salary = [25000, 32000, 28000, 40000, 50000]
emp = ['A', 'B', 'C', 'D', 'E']

s = pd.Series(salary, index=emp)

# Increase salary by 10% where < 30000
s[s < 30000] = s[s < 30000] * 1.10

# Decrease salary by 5% where > 45000
s[s > 45000] = s[s > 45000] * 0.95

# Total salary expense
print("Total Salary:", s.sum())
print(s)


'''
OUTPUT

A    27500.0
B    32000.0
C    30800.0
D    40000.0
E    47500.0
dtype: float64
Total Salary: 177800.0
'''
