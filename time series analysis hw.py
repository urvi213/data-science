import pandas as pd
import matplotlib.pyplot as plt

weatherdata = pd.read_csv(r"C:\Users\user\Desktop\current coding\data science\worldwide_weather_2025.csv")
weatherdata.drop(columns=["weathercode"],inplace=True)
weatherdata.dropna(inplace=True)
weatherdata["time"] = pd.to_datetime(weatherdata["time"])
weatherdata["month"] = weatherdata["time"].dt.month
print(weatherdata)

# average precipitation monthly
for city in ["Berlin","Paris","London","Johannesburg"]:
    citydata = weatherdata[weatherdata["city"]==city]
    citydata = citydata[["temperature_2m_max","temperature_2m_min","precipitation_sum","month"]].groupby("month").mean()
    plt.bar(x=citydata.index,height=citydata["precipitation_sum"])
    plt.ylabel("average precipitation")
    plt.xlabel("month")
    plt.title(f"{city}'s average precipitation monthly")
    plt.show()

# top mean max temperature
temp = weatherdata[["temperature_2m_max","city"]].groupby("city").mean()
top10 = temp.sort_values("temperature_2m_max",ascending=False).head(n=10)
plt.bar(x=top10.index,height=top10["temperature_2m_max"])
plt.ylabel("average max temperature")
plt.xlabel("city")
plt.title("top ten city's average max temperatures")
plt.show()

# line plot - max, min, precipitation
for city in ["New_York","Seoul","Singapore","Tokyo"]:
    cityvalues = weatherdata[weatherdata["city"]==city]
    x = cityvalues["time"]
    plt.plot(x,cityvalues["temperature_2m_max"],label="max temperature")
    plt.plot(x,cityvalues["temperature_2m_min"],label="min temperature")
    plt.plot(x,cityvalues["precipitation_sum"],label="precipitation sum")
    plt.title(f"{city}'s weather data january to august")
    plt.legend()
    plt.show()