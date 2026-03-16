#QUE-7 Create an Exploded Pie Chart showing daily time spent on activities like study, sleep, exercise, and entertainment.

import matplotlib.pyplot as plt

activities = ["Study","Sleep","Exercise","Entertainment"]
time = [6,8,2,4]

explode = [0.1,0,0,0]

plt.pie(time, labels=activities, autopct='%1.1f%%', explode=explode)

plt.title("Daily Time Spent on Activities")

plt.show()