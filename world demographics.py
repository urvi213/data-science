import pandas as pd

demographics = pd.read_csv(r"C:\Users\user\Desktop\current coding\data science\wdi_wide.csv")

demographics.drop(columns=["Intermediate Region"],inplace=True)
demographics[["Region","Subregion"]] = demographics[["Region","Subregion"]].fillna("NA")
demographics.fillna(0,inplace=True)
#demographics.info()

# country vs population, physicians+male/female life expectancies, tertiary education female/male+women in parliament, gni, internet use

countrycolumns = ["Population","Physicians per 1000","Life expectancy, female","Life expectancy, male","Tertiary education, female","Tertiary education, male","Women in national parliament","GNI","Internet use"]

choice = input("check countries or regions: ")

import matplotlib.pyplot as plt

if choice == "countries":

    for column in countrycolumns:
        plt.figure(figsize=(15,5))
        
        demographics = demographics[demographics[column]!=0]
        top10 = demographics.sort_values(column,ascending=False).head(n=20)
        plt.subplot(1,2,1)
        plt.bar(x=top10["Country Name"],height=top10[column])
        plt.title(f"Top 10 Countries in terms of {column}")
        plt.xticks(rotation=45)
        plt.ylabel(column)

        bottom10 = demographics.sort_values(column,ascending=True).head(n=20)
        plt.subplot(1,2,2)
        plt.bar(x=bottom10["Country Name"],height=bottom10[column])
        plt.title(f"Bottom 10 Countries in terms of {column}")
        plt.xticks(rotation=45)
        plt.ylabel(column)
        plt.show()

elif choice == "regions":
    regions = demographics.drop(columns=["Country Name","Subregion","High Income Economy"]).groupby("Region").mean()
    regions.drop("NA",inplace=True)
    for column in countrycolumns:
        plt.figure()

        sortedregions = regions.sort_values(column,ascending=False)
        plt.bar(x=sortedregions.index,height=sortedregions[column])
        plt.title(f"Regions in terms of {column}")
        plt.xticks(rotation=45)
        plt.ylabel(column)
        plt.show()

subregionsum = demographics.groupby("Subregion").sum()
subregionsum.drop("NA",inplace=True)
plt.bar(x=subregionsum.index,height=subregionsum["International tourism"])
plt.xticks(rotation=60)
plt.ylabel("Number of International Tourists")
plt.title("Subregions in terms of International Tourism")
plt.show()

import numpy as np

regions = demographics.groupby("Region")
valuecounts = regions["High Income Economy"].value_counts()
unstacked = valuecounts.drop("NA").unstack()
xarray = np.arange(len(unstacked))
WIDTH = 0.35
plt.bar(x=xarray-WIDTH/2,height=unstacked["Yes"],width=WIDTH,label="High Income")
plt.bar(x=xarray+WIDTH/2,height=unstacked["No"],width=WIDTH,label="Low Income")
plt.title("High/Low income economies in Each Region")
plt.xticks(rotation=60,ticks=xarray,labels=unstacked.index)
plt.legend()
plt.show()
