#QUE-1 Create a Line Chart to display the monthly sales of a company for 12 months.

import matplotlib.pyplot as plt

months = ["Jan","Feb","Mar","Apr","May","Jun","Jul","Aug","Sep","Oct","Nov","Dec"]
sales = [120,150,170,160,180,200,210,220,190,230,240,260]

plt.plot(months, sales, marker='o', color='blue')

plt.title("Monthly Sales of Company")
plt.xlabel("Months")
plt.ylabel("Sales")

plt.show()