import pandas as pd

time_data = pd.read_csv(r"C:\Users\user\Desktop\current coding\data science\WHO-COVID-19-global-data.csv")
#time_data.info()

time_data["DateReported"] = pd.to_datetime(time_data["DateReported"]) # changes dates (strings) into datatype you can work with
time_data = time_data[["DateReported","Country","New_cases","Cumulative_cases","New_deaths","Cumulative_deaths"]]
time_data["Year"] = time_data["DateReported"].dt.year
time_data["Month"] = time_data["DateReported"].dt.month
time_data["Day"] = time_data["DateReported"].dt.day
print(time_data)

import plotly.graph_objects as go

# daily cumulative cases
day_sums = time_data.groupby("DateReported").sum()
print(day_sums)
fig1 = go.Figure()
fig1.add_trace(
    go.Scatter(x=day_sums.index,y=day_sums["Cumulative_cases"],fill="tonexty",fillcolor="green",line_color="green"))
fig1.add_trace(
    go.Scatter(x=day_sums.index,y=day_sums["Cumulative_deaths"]))
fig1.update_layout(title="Daily Sum of Cumulative Cases/Deaths")
#fig1.write_html("fig1.html",auto_open=True)

fig2 = go.Figure(
    data=[go.Scatter(x=day_sums.index,y=day_sums["New_cases"]),
          go.Scatter(x=day_sums.index,y=day_sums["New_deaths"])]
    )
#fig2.write_html("fig2.html",auto_open=True)

# monthly cases
month_sums = time_data[["New_cases","Cumulative_cases","New_deaths","Cumulative_deaths","Year","Month"]].groupby(["Year","Month"]).sum()
print(month_sums)

# hw

#print(month_sums.iloc[0:12])

hw1 = go.Figure(
    data=[
        go.Bar(name="2020 new cases",x=month_sums.loc[2020].index,y=month_sums["New_cases"]),
        go.Bar(name="2020 new deaths",x=month_sums.loc[2020].index,y=month_sums["New_deaths"])
    ])
hw1.write_html("hw1.html",auto_open=True)

print(month_sums.loc[2020])


hw2 = go.Figure(
    data=[
        go.Bar(name="2021 new cases",x=month_sums.loc[2021].index,y=month_sums["New_cases"]),
        go.Bar(name="2021 new deaths",x=month_sums.loc[2021].index,y=month_sums["New_deaths"])
    ])
hw2.write_html("hw2.html",auto_open=True)
