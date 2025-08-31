import pandas as pd
screen_time = pd.read_csv(r"C:\Users\user\Desktop\current coding\data science\Indian_Kids_Screen_Time.csv")
screen_time["Health_Impacts"].fillna(" ",inplace=True)
#print(screen_time.isnull().sum())

from sklearn.preprocessing import LabelEncoder
le = LabelEncoder()
screen_time["Exceeded_Recommended_Limit"] = le.fit_transform(screen_time["Exceeded_Recommended_Limit"])
print(screen_time["Exceeded_Recommended_Limit"])

import plotly.express as px
# what device has the highest averages?
# what age exceeds limits the most?
# whats the median average screen time for each age?
# what gender has the highest averages?
# what health impacts have higher ratio

device_sum_avgs = screen_time[["Primary_Device","Avg_Daily_Screen_Time_hr"]].groupby("Primary_Device").sum()
device_sum_avgs = device_sum_avgs.sort_values("Avg_Daily_Screen_Time_hr",ascending=True)
print(device_sum_avgs)
fig1 = px.bar(device_sum_avgs,"Avg_Daily_Screen_Time_hr",device_sum_avgs.index)
fig1.write_html("fig1.html",auto_open=True)

age_exceed = screen_time[["Age","Exceeded_Recommended_Limit"]].groupby("Age").sum()
print(age_exceed)
fig2 = px.bar(x=age_exceed.index,y=age_exceed["Exceeded_Recommended_Limit"])
fig2.write_html("fig2.html",auto_open=True)

median_avg_age = screen_time[["Age","Avg_Daily_Screen_Time_hr"]].groupby("Age").median()
print(median_avg_age)
fig3 = px.scatter(x=median_avg_age.index,y=median_avg_age["Avg_Daily_Screen_Time_hr"])
fig3.write_html("fig3.html",auto_open=True)

gender_avgs = screen_time[["Gender","Avg_Daily_Screen_Time_hr"]].groupby("Gender").mean()
print(gender_avgs)
fig4 = px.bar(gender_avgs,gender_avgs.index,"Avg_Daily_Screen_Time_hr",)
fig4.write_html("Fig4.html",auto_open=True)

health_ratio = screen_time[["Health_Impacts","Educational_to_Recreational_Ratio"]].groupby("Health_Impacts").mean()
print(health_ratio)
from sklearn.preprocessing import MinMaxScaler
mms = MinMaxScaler()
health_ratio["Educational_to_Recreational_Ratio"] = mms.fit_transform(health_ratio[["Educational_to_Recreational_Ratio"]])
print(health_ratio)
fig5 = px.scatter(health_ratio,health_ratio.index,health_ratio["Educational_to_Recreational_Ratio"])
fig5.write_html("Fig5.html",auto_open=True)