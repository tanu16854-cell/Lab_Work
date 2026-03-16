#QUE-13 Generate a Box Plot to show the salary distribution of employees in three different departments.
import matplotlib.pyplot as plt

dept1 = [30,35,40,45,50]
dept2 = [25,30,35,40,45]
dept3 = [20,25,30,35,40]

plt.boxplot([dept1,dept2,dept3], labels=["HR","IT","Sales"])

plt.title("Salary Distribution")
plt.ylabel("Salary")

plt.show()