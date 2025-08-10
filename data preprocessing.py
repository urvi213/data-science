import pandas as pd

data = pd.read_csv(r"C:\Users\user\Desktop\current coding\data science\dataset.csv")
print(data)
print("")

# checking for missing values (missing values are NaN)
print(data.isnull().sum())
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