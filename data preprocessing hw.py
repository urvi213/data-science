import pandas as pd

screen_time = pd.read_csv(r"Indian_Kids_Screen_Time.csv")
#print(demographics)

print(screen_time.isnull().sum())

from sklearn.impute import SimpleImputer
si = SimpleImputer(missing_values=pd.NA,strategy="most_frequent")
screen_time[["Health_Impacts"]] = si.fit_transform(screen_time[["Health_Impacts"]])
print(screen_time.isnull().sum())

X = screen_time[["Age","Gender","Avg_Daily_Screen_Time_hr","Primary_Device","Educational_to_Recreational_Ratio","Health_Impacts","Urban_or_Rural"]]
y = screen_time["Exceeded_Recommended_Limit"]
print(X)
print(y)

# encoding
encoded_X = pd.get_dummies(X,columns=["Gender","Primary_Device","Health_Impacts","Urban_or_Rural"],dtype=int)
print(encoded_X)
from sklearn.preprocessing import LabelEncoder
le = LabelEncoder()
encoded_y = le.fit_transform(y)
print(encoded_y)

# # scaling
# from sklearn.preprocessing import MinMaxScaler
# mms = MinMaxScaler()
# encoded_X[["Age"]] = mms.fit_transform(encoded_X[["Age"]])
# print(encoded_X[["Age"]])

# split into train and test set
from sklearn.model_selection import train_test_split
Xtrain, Xtest, ytrain, ytest = train_test_split(encoded_X,encoded_y,test_size=0.1)
print(Xtrain)
print(Xtest)
print(ytrain)
print(ytest)
