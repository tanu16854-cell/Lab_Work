#QUE-3 Create a Bar Chart to show the number of students enrolled in different courses such as Python, Java, Data Science, and Web Development.

import matplotlib.pyplot as plt

courses = ["Python","Java","Data Science","Web Dev"]
students = [120,90,70,100]

plt.bar(courses, students, color="green")

plt.title("Students Enrolled in Courses")
plt.xlabel("Courses")
plt.ylabel("Number of Students")

plt.show()