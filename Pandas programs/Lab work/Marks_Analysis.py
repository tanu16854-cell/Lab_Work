'''
Q1: Marks Analysis with Conditions
Dataset:
    import pandas as pd
    marks = [45, 67, 89, 34, 90, 55, 72]
    subjects = ['Math', 'Physics', 'Chemistry', 'English', 'CS', 'Biology', 'History']
    s = pd.Series(marks, index=subjects)
Tasks:
    Find subjects with marks > 70 Replace marks < 40 with "Fail" Count how many subjects scored above average
'''
import pandas as pd

marks = [45, 67, 89, 34, 90, 55, 72]
subjects = ['Math', 'Physics', 'Chemistry', 'English', 'CS', 'Biology', 'History']

s = pd.Series(marks, index=subjects)

# Subjects with marks > 70
print(s[s > 70])

# Replace marks < 40 with "Fail"
s1 = s.copy()
s1[s1 < 40] = "Fail"
print(s1)

# Count subjects above average
avg = s.mean()
count = (s > avg).sum()
print("Count above average:", count)

'''
#OUTPUT
#Chemistry    89
#CS           90
#History      72
#dtype: int64
'''
