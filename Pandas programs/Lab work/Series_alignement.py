
'''
Q5: Series Alignment Dataset:
    #s1 = pd.Series([10, 20, 30], index=['A', 'B', 'C'])
    #s2 = pd.Series([5, 15, 25], index=['B', 'C', 'D'])
#Tasks:
    #Add both Series (s1 + s2) Observe NaN values Replace NaN with 0 and recompute
    '''
import pandas as pd
s1 = pd.Series([10, 20, 30], index=['A', 'B', 'C'])
s2 = pd.Series([5, 15, 25], index=['B', 'C', 'D'])

# Add Series
result = s1 + s2
print(result)

# Replace NaN with 0
result_filled = result.fillna(0)
print(result_filled)


'''
OUTPUT
A     NaN
B    25.0
C    45.0
D     NaN
dtype: float64
A     0.0
B    25.0
C    45.0
D     0.0
dtype: float64

'''
