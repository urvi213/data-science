import matplotlib.pyplot as plt
import numpy as np
import random

# https://matplotlib.org/2.1.2/api/_as_gen/matplotlib.pyplot.plot.html

# line plot
x_values = np.arange(1,11)
y_values = 2*x_values+3
plt.figure(figsize=(5,3)) # values given in inches
plt.plot(x_values,y_values,"b--*",markersize=10,label="line1") # makes line plot 
#plt.axis((-10,10,0,30)) # controls range for axes - start x, end x, start y , end y
plt.xticks(ticks=x_values,labels=["I","II","III","IV","V","VI","VII","VIII","IX","X"],rotation=45)
plt.yticks(ticks=y_values,labels=y_values)
plt.title("line plot y=2x+3")
plt.xlabel("x values")
plt.ylabel("y values")
plt.legend()
plt.show()

# multiple graphs on a single plot
x_values = np.arange(1,10,0.1)
plt.plot(x_values,x_values**2,"b-",label="x squared")
plt.plot(x_values,x_values**3,"g--",label="x cubed")
plt.legend()
plt.show()

# bar plot
plt.bar([0,1,2,3,4],[10,5,30,45,15])
plt.show()
subjects = ["english","maths","history","chemistry","music"]
plt.bar([1,3,5,7,9],[100,80,50,70,60],label="studentA")
plt.bar([2,4,6,8,10],[70,80,60,100,40],label="studentB",color="green")
plt.xticks(ticks=np.arange(1,10,2)+0.5,labels=subjects)
plt.legend()
plt.show()

# histogram
ages = np.random.randint(10,51,50)
print(ages)
bins = np.arange(10,51,10) # intervals
plt.hist(ages,bins=bins,rwidth=0.75,color="g")
plt.show()

# scatter graph
x_values2 = np.random.randint(1,11,15)
y_values2 = np.random.randint(1,21,15)
plt.scatter(x_values2,y_values2,marker="*",s=6)
plt.show()

# pie charts
categories = ["blue","red","yellow","green","pink"]
distribution = [24,30,42,13,65] # if they arent already percentages it will calculate
plt.pie(distribution,labels=categories,autopct="%1.2f%%",startangle=180,colors=categories,shadow=True)
plt.show() 

# stack plot
days = ["mon","tue","wed","thu","fri"]
activities = {"eating":np.random.randint(0,4,5),"guitar":np.random.randint(0,2,5),"walking":np.random.randint(0,1,5),"reading":np.random.randint(0,2,5),"schoolwork":np.random.randint(0,4,5)}
print(activities)
plt.stackplot(days,activities.values(),labels=activities.keys())
plt.legend()
plt.show()

# sub plots (multiple graphs per window/figure)
plt.figure()
plt.subplot(3,2,2)
plt.stackplot(days,activities.values(),labels=activities.keys())
plt.subplot(3,2,5)
plt.pie(distribution,labels=categories,autopct="%1.2f%%",startangle=180,colors=categories,shadow=True)
plt.show()
