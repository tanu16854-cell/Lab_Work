'''
Q8: Chained Operations
Dataset:
    data = [5, None, 15, 25, None, 35, 45]
Tasks:
    Fill missing values with median Filter values greater than 20 Sort in descending order Reset index
'''

import pandas as pd

data = [5, None, 15, 25, None, 35, 45]
s = pd.Series(data)

result = (
    s.fillna(s.median())      # fill missing
     .loc[lambda x: x > 20]   # filter > 20
     .sort_values(ascending=False)  # sort
     .reset_index(drop=True)  # reset index
)

print(result)

'''
OUTPUT

0    45.0
1    35.0
2    25.0
3    25.0
4    25.0
dtype: float64
'''
