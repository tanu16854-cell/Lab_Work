#QUE-12 Create a Step Chart to display electricity consumption during different time intervals in a day.

import matplotlib.pyplot as plt

time = [0,4,8,12,16,20,24]
consumption = [2,3,5,6,7,5,3]

plt.step(time, consumption)

plt.title("Electricity Consumption During Day")
plt.xlabel("Time (Hours)")
plt.ylabel("Consumption")

plt.show()