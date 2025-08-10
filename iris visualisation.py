import pandas as pd
import matplotlib.pyplot as plt

iris = pd.read_csv(r"C:\Users\user\Desktop\current coding\data science\iris.csv")

plt.subplot(2,2,1)
plt.scatter(iris["petal_length"],iris["petal_width"],s=2)
plt.subplot(2,2,2)
plt.scatter(iris["petal_length"],iris["sepal_width"],s=2)
plt.subplot(2,2,3)
plt.scatter(iris["sepal_length"],iris["sepal_width"],s=2)
plt.subplot(2,2,4)
plt.scatter(iris["petal_width"],iris["sepal_width"],s=2)

plt.show()

plt.pie(iris["species"].value_counts(),labels=iris["species"].value_counts().index)
plt.show()