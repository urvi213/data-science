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