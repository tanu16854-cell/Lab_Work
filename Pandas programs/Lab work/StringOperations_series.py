'''
Q7: String Operations in Series
#Dataset:
    #names = ['anuj', 'rahul', 'sneha', 'kiran', 'amit']
    #s = pd.Series(names)
#Tasks:
    #Convert all names to uppercase Find names containing letter 'a' Replace 'anuj' with 'Anuj Kumar'
    '''
import pandas as pd
names = ['anuj', 'rahul', 'sneha', 'kiran', 'amit']
s = pd.Series(names)

# Uppercase
print(s.str.upper())

# Names containing 'a'
print(s[s.str.contains('a')])

# Replace
s = s.replace('anuj', 'Anuj Kumar')
print(s)
names = ['anuj', 'rahul', 'sneha', 'kiran', 'amit']
s = pd.Series(names)

# Uppercase
print(s.str.upper())

# Names containing 'a'
print(s[s.str.contains('a')])

# Replace
s = s.replace('anuj', 'Anuj Kumar')
print(s)
'''
OUTPUT
0     ANUJ
1    RAHUL
2    SNEHA
3    KIRAN
4     AMIT
dtype: str
0     anuj
1    rahul
2    sneha
3    kiran
4     amit
dtype: str
0    Anuj Kumar
1         rahul
2         sneha
3         kiran
4          amit
dtype: str
0     ANUJ
1    RAHUL
2    SNEHA
3    KIRAN
4     AMIT
dtype: str
0     anuj
1    rahul
2    sneha
3    kiran
4     amit
dtype: str
0    Anuj Kumar
1         rahul
2         sneha
3         kiran
4          amit
dtype: str
'''
