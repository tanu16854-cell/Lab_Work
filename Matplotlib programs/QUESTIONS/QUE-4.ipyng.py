#QUE-4 Generate a Horizontal Bar Chart to visualize the population of five different cities.

import matplotlib.pyplot as plt

cities = ["Delhi","Mumbai","Kolkata","Chennai","Bangalore"]
population = [30,20,15,12,14]

plt.barh(cities, population, color="orange")

plt.title("Population of Cities")
plt.xlabel("Population (Millions)")
plt.ylabel("Cities")

plt.show()