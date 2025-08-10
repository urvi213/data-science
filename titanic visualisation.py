import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

titanic = pd.read_csv(r"C:\Users\user\Desktop\current coding\data science\titanic.csv")

ages = titanic["Age"]
bins = np.arange(0,101,10)
plt.hist(ages,bins=bins)
plt.xlabel("ages")
plt.ylabel("frequency")
plt.show()

pclassmean = titanic.groupby("Pclass")["Fare"].mean()
#print(pclassmean)
plt.bar(pclassmean.index,pclassmean)
plt.xticks([1,2,3])
plt.show()

categories = ["died","survived"]
distribution = titanic["Survived"].value_counts()
plt.pie(distribution,labels=categories,autopct="%1.2f%%")
plt.show()

data = titanic.groupby("Pclass").sum()[["Siblings/Spouses Aboard","Parents/Children Aboard"]]
#print(data)
plt.stackplot(data.index,data["Siblings/Spouses Aboard"],data["Parents/Children Aboard"],labels=["Siblings/Spouses Aboard","Parents/Children Aboard"])
plt.xticks([1,2,3])
plt.legend()
plt.show()