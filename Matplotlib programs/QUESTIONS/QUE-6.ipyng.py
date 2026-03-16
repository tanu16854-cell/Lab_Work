#QUE-6 Draw a Pie Chart to represent the market share of five smartphone brands.
import matplotlib.pyplot as plt

brands = ["Apple","Samsung","Xiaomi","Oppo","Vivo"]
share = [30,25,20,15,10]

plt.pie(share, labels=brands, autopct='%1.1f%%')

plt.title("Smartphone Market Share")

plt.show()