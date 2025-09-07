import pandas as pd

demographics = pd.read_csv(r"C:\Users\user\Desktop\current coding\data science\wdi_wide.csv")

demographics.drop(columns=["Intermediate Region"],inplace=True)
demographics[["Region","Subregion"]] = demographics[["Region","Subregion"]].fillna("NA")
demographics.fillna(0,inplace=True)

# country vs population, physicians+male/female life expectancies, tertiary education female/male+women in parliament, gni, internet use

countrycolumns = ["Population","Physicians per 1000","Life expectancy, female","Life expectancy, male","Tertiary education, female","Tertiary education, male","Women in national parliament","GNI","Internet use"]

import matplotlib.pyplot as plt

for column in countrycolumns:

    top10 = demographics.sort_values(column,ascending=False).head(n=20)

    plt.bar(x=top10["Country Name"],height=top10[column])
    plt.title(f"Top 10 Countries in terms of {column}")
    plt.xticks(rotation=45)
    plt.ylabel(column)
    plt.show()

    # bottom10 = demographics.sort_values(column,ascending=True).head(n=20)

    # plt.bar(x=top10["Country Name"],height=bottom10[column])
    # plt.title(f"Bottom 10 Countries in terms of {column}")
    # plt.xticks(rotation=45)
    # plt.ylabel(column)
    # plt.show()