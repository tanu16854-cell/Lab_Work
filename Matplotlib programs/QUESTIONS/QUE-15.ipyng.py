#QUE-15 Create Subplots in a single figure that display four charts: Line Chart, Bar Chart, Pie Chart, and Scatter Plot.

import matplotlib.pyplot as plt

plt.figure(figsize=(10,8))

# Line
plt.subplot(2,2,1)
plt.plot([1,2,3],[10,20,30])
plt.title("Line Chart")

# Bar
plt.subplot(2,2,2)
plt.bar(["A","B","C"],[5,7,9])
plt.title("Bar Chart")

# Pie
plt.subplot(2,2,3)
plt.pie([30,40,30])
plt.title("Pie Chart")

# Scatter
plt.subplot(2,2,4)
plt.scatter([1,2,3],[4,5,6])
plt.title("Scatter Plot")

plt.show()