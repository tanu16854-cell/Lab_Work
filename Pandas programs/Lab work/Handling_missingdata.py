'''#Q3: Handling Missing Data Smartly
Dataset:

    #data = [10, None, 30, None, 50, 60, None]
    #s = pd.Series(data)

#Tasks:
    #Fill missing values with mean Count missing values before and after filling Drop remaining nulls (if any)
'''
import pandas as pd
data = [10, None, 30, None, 50, 60, None]
s = pd.Series(data)

# Count missing before
print("Missing before:", s.isnull().sum())

# Fill with mean
s = s.fillna(s.mean())

# Count after
print("Missing after:", s.isnull().sum())

# Drop remaining nulls
s = s.dropna()

print(s)


'''
OUTPUT
Missing before: 3
Missing after: 0
0    10.0
1    37.5
2    30.0
3    37.5
4    50.0
5    60.0
6    37.5
dtype: float64
'''
