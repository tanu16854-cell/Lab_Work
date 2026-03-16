#QUE-11 Plot an Area Chart showing the yearly profit growth of a company over 6 years.

import matplotlib.pyplot as plt

years = [2019,2020,2021,2022,2023,2024]
profit = [10,15,20,25,30,35]

plt.fill_between(years, profit, color="skyblue")

plt.title("Yearly Profit Growth")
plt.xlabel("Year")
plt.ylabel("Profit")

plt.show()