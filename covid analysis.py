import pandas as pd

covid = pd.read_csv(r"C:\Users\user\Desktop\current coding\data science\covid_data.csv")
covid = covid[["Province_State","Country_Region","Confirmed","Recovered","Deaths","Active"]]
print(covid.isnull().sum())
covid["Province_State"].fillna(" ",inplace=True)
print(covid.isnull().sum())

import plotly.express as px

# top 10 most affected countries
country_sums = covid.groupby("Country_Region").sum()
#print(country_sums)
most_affected_countries = country_sums.sort_values("Confirmed",ascending=False).head(n=10)
print(most_affected_countries)

fig1 = px.scatter(most_affected_countries,x=most_affected_countries.index,y="Confirmed",size="Confirmed",size_max=120,title="Countries With Most Confirmed Cases",color=most_affected_countries.index)
fig1.write_html("covid analysis.html",auto_open=True)

# top 10 deaths
most_deaths = country_sums.sort_values("Deaths",ascending=False).head(n=10)
fig2 = px.bar(most_deaths,"Deaths",most_deaths.index,height=1000,color_continuous_scale=px.colors.sequential.Viridis,color="Deaths")
fig2.write_html("covid analysis 2.html",auto_open=True)