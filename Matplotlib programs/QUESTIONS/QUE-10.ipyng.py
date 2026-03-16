#QUE-10 Develop a Bubble Chart showing population vs area of cities, where bubble size represents GDP.

import matplotlib.pyplot as plt

cities = ["A","B","C","D","E"]

population = [20,30,15,25,10]
area = [300,500,200,400,150]
gdp = [1000,2000,800,1500,600]

plt.scatter(area, population, s=gdp)

plt.title("Population vs Area (Bubble Size = GDP)")
plt.xlabel("Area")
plt.ylabel("Population")

plt.show()