#QUE-8 Plot a Histogram to visualize the distribution of marks obtained by 100 students.

import matplotlib.pyplot as plt
import numpy as np

marks = np.random.randint(40,100,100)

plt.hist(marks, bins=10, color="purple")

plt.title("Distribution of Marks")
plt.xlabel("Marks")
plt.ylabel("Number of Students")

plt.show()