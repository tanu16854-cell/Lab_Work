#QUE-2 Plot a Multiple Line Chart showing the sales of three products (Product A, B, and C) for six months.

import matplotlib.pyplot as plt

months = ["Jan","Feb","Mar","Apr","May","Jun"]

productA = [50,60,70,80,90,100]
productB = [40,50,60,70,80,90]
productC = [30,40,50,60,70,80]

plt.plot(months, productA, marker='o', label="Product A")
plt.plot(months, productB, marker='s', label="Product B")
plt.plot(months, productC, marker='^', label="Product C")

plt.title("Sales of Products")
plt.xlabel("Months")
plt.ylabel("Sales")

plt.legend()
plt.show()