#QUE-5 Create a Stacked Bar Chart showing the number of male and female students in four departments.

import matplotlib.pyplot as plt

dept = ["CSE","ECE","ME","CE"]
male = [60,50,40,30]
female = [40,30,20,25]

plt.bar(dept, male, label="Male")
plt.bar(dept, female, bottom=male, label="Female")

plt.title("Male and Female Students in Departments")
plt.xlabel("Departments")
plt.ylabel("Number of Students")

plt.legend()
plt.show()