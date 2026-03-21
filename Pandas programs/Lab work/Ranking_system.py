'''
Q6: Ranking System Dataset:
    scores = [88, 92, 79, 93, 85]
    players = ['P1','P2','P3','P4','P5']
    s = pd.Series(scores, index=players)
#Tasks:
    Rank players based on scores Display top 3 players Find player with lowest score
    '''
import pandas as pd

scores = [88, 92, 79, 93, 85]
players = ['P1','P2','P3','P4','P5']

s = pd.Series(scores, index=players)

# Rank players
ranks = s.rank(ascending=False)
print(ranks)

# Top 3 players
print(s.sort_values(ascending=False).head(3))

# Lowest score
print("Lowest:", s.idxmin(), s.min())

'''
OUTPUT
P1    3.0
P2    2.0
P3    5.0
P4    1.0
P5    4.0
dtype: float64
P4    93
P2    92
P1    88
dtype: int64
Lowest: P3 79

'''

