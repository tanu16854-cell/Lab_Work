#Q9:Sales Performance
    #sales = [200, 450, 300, 150, 500, 700, 100]
    #days = ['Mon','Tue','Wed','Thu','Fri','Sat','Sun']
    #s = pd.Series(sales, index=days)
#Tasks:
    #Find best and worst sales day Calculate total and average sales Apply 20% bonus on days where sales > 400 Sort sales in descending order

import pandas as pd

sales = [200, 450, 300, 150, 500, 700, 100]
days = ['Mon','Tue','Wed','Thu','Fri','Sat','Sun']

s = pd.Series(sales, index=days)

# Best and worst day
print("Best day:", s.idxmax(), s.max())
print("Worst day:", s.idxmin(), s.min())

# Total and average
print("Total:", s.sum())
print("Average:", s.mean())

# 20% bonus where sales > 400
s_bonus = s.copy()
s_bonus[s_bonus > 400] *= 1.20
print(s_bonus)

# Sort descending
print(s.sort_values(ascending=False))


'''OUTPUT
Best day: Sat 700
Worst day: Sun 100
Total: 2400
Average: 342.85714285714283
Mon    200
Tue    540
Wed    300
Thu    150
Fri    600
Sat    840
Sun    100
dtype: int64
Sat    700
Fri    500
Tue    450
Wed    300
Mon    200
Thu    150
Sun    100
dtype: int64

'''
