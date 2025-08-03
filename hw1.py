import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

titanic = pd.read_csv(r"C:\Users\44750\OneDrive\Desktop\coding stuff urvi\data science\titanic.csv")

a = 0
b = 0
c = 0
x_values = np.arange(0,51,0.1)

choice = input("what sort of expression do you want to to evaluate?\n1) Linear (ax+b)\n2) Quadratic (ax^2+bx+c)\n")
print("")
if choice == "1":
    a = int(input("a? "))
    b = int(input("b? "))
    y_values = a*x_values+b
elif choice == "2":
    a = int(input("a? "))
    b = int(input("b? "))
    c = int(input("c? "))
    y_values = a*x_values**2+b*x_values+c

plt.figure(figsize=(5,3))
plt.plot(x_values,y_values)
plt.show()


pclass_values = titanic["Pclass"].value_counts()

plt.bar(pclass_values.index,pclass_values)
plt.xticks(ticks=np.arange(1,4,1))
plt.show()

sex_values = titanic["Sex"].value_counts()
plt.bar(sex_values.index,sex_values)
plt.show()