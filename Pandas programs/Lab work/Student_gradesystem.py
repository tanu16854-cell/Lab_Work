'''
#Q4: Student Grades System Dataset:

    #marks = [95, 82, 67, 58, 73, 49, 88]
    #students = ['S1','S2','S3','S4','S5','S6','S7']
    #s = pd.Series(marks, index=students)

#Tasks:
    #Assign grades using apply() =90 → A =75 → B =60 → C <60 → D Count number of students in each grade
'''

import pandas as pd
marks = [95, 82, 67, 58, 73, 49, 88]
students = ['S1','S2','S3','S4','S5','S6','S7']

s = pd.Series(marks, index=students)

def grade(x):
    if x >= 90:
        return 'A'
    elif x >= 75:
        return 'B'
    elif x >= 60:
        return 'C'
    else:
        return 'D'

grades = s.apply(grade)
print(grades)

# Count each grade
print(grades.value_counts())

'''
OUTPUT
S1    A
S2    B
S3    C
S4    D
S5    C
S6    D
S7    B
dtype: str
B    2
C    2
D    2
A    1
Name: count, dtype: int64

'''
