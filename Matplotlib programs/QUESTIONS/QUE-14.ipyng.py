# QUE-14 Create a Violin Plot to visualize the distribution of exam scores in different classes.
import matplotlib.pyplot as plt

class1 = [60,65,70,75,80]
class2 = [55,60,65,70,75]
class3 = [50,55,60,65,70]

plt.violinplot([class1,class2,class3])

plt.title("Exam Score Distribution")

plt.show()