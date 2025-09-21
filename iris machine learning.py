import pandas as pd

irisdata = pd.read_csv(r"C:\Users\user\Desktop\current coding\data science\iris.csv")
X = irisdata[["sepal_length","sepal_width","petal_length","petal_width"]]
y = irisdata["species"]

from sklearn.preprocessing import LabelEncoder
le = LabelEncoder()
y = le.fit_transform(y)

from sklearn.model_selection import train_test_split
Xtrain, Xtest, ytrain, ytest = train_test_split(X,y,test_size=0.25,random_state=20) # fix random_state to ensure model uses same data each time

from sklearn.ensemble import RandomForestClassifier
rfc = RandomForestClassifier()
rfc.fit(Xtrain,ytrain) # let it learn
trainprediction = rfc.predict(Xtrain)
testprediction = rfc.predict(Xtest)

print(trainprediction,"\n")
print(testprediction)

from sklearn.metrics import classification_report
print(classification_report(ytrain,trainprediction)) # f1-score - decimal showing accuracy
print(classification_report(ytest,testprediction))

import matplotlib.pyplot as plt

plt.scatter(pd.Series(ytest).index,ytest)
plt.scatter(pd.Series(ytest).index,testprediction)
plt.show()