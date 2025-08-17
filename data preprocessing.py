import pandas as pd

data = pd.read_csv(r"C:\Users\user\Desktop\current coding\data science\dataset.csv")
#print(data)
print("")

# checking for missing values (missing values are NaN)
#print(data.isnull().sum())
# removing missing values
# data.dropna(inplace=True) # removes rows with NaN

# replacing the value
#print(data["Age"].replace(pd.NA,data["Age"].mean()))
# data.loc[data["Age"].isnull(),"Age"] = data["Age"].mean()
# data.loc[data["Salary"].isnull(),"Salary"] = data["Salary"].mean()
#print(data)

# replace automatically
from sklearn.impute import SimpleImputer
si = SimpleImputer(missing_values=pd.NA,strategy="mean")
data[["Age","Salary"]] = si.fit_transform(data[["Age","Salary"]])
#print(data)

# seperating features (X) and target (y)
X = data[["Country","Age","Salary"]]
y = data["Purchased"]
print(X)
print(y)

# encoding categorical data
# encoding features
encoded_countries = pd.get_dummies(X,columns=["Country"],dtype=int)
print(encoded_countries)
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import OneHotEncoder
ct = ColumnTransformer(transformers=[("encoder",OneHotEncoder(),[0])],remainder="passthrough")
sk_encoded_countries = ct.fit_transform(X)
print(sk_encoded_countries)

france = X[X["Country"]=="France"]
print(france)
encoded_france = pd.get_dummies(france,columns=["Country"],dtype=int)
print(encoded_france)
sk_encoded_france = ct.transform(france) # not fit_transform because the model has already learnt
print(sk_encoded_france) # creates features for other 2 countries even if it doesnt find them

# encoding target
from sklearn.preprocessing import LabelEncoder
le = LabelEncoder()
encoded_target = le.fit_transform(y) # encodes values alphabetically
print(encoded_target)
le_encoded_countries = le.fit_transform(X["Country"])
print(le_encoded_countries)

# scaling data
# standard scaler
from sklearn.preprocessing import StandardScaler
ss = StandardScaler()
print(ss.fit_transform(encoded_countries[["Age","Salary"]])) # mean is 0 with deviation of 1
# min max scaling
from sklearn.preprocessing import MinMaxScaler
mms = MinMaxScaler()
encoded_countries[["Age","Salary"]] = mms.fit_transform(encoded_countries[["Age","Salary"]]) # between 0 and 1
print(encoded_countries)

# splitting into training and test set
from sklearn.model_selection import train_test_split
Xtrain, Xtest, ytrain, ytest = train_test_split(encoded_countries,encoded_target,test_size=0.2,random_state=20) # each integer in random_state has its own combination
print(Xtrain)
print(Xtest)
print(ytrain)
print(ytest)
