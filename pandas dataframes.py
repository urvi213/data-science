import pandas as pd

dict1 = {"name":["urvi","seb","ren"],"age":[14,14,14],"nationality":["india","hong kong","pakistan"]}
dataframe1 = pd.DataFrame(dict1) # keys become column names
print(dataframe1)
print(type(dataframe1))

# comma seperated values
dataframe2 = pd.read_csv(r"C:\Users\user\Desktop\current coding\data science\titanic.csv")  #lowercase r stops it from interpretig some stuff as special
print(dataframe2)

# fetching records from top
print(dataframe2.head(n=3)) # defaults to first 5
# fetching from bottom
print(dataframe2.tail(n=3))

# info
dataframe2.info() # includes print

# statistical summary (only works for numerical columns)
print(dataframe2.describe())

# rows and columns
print(dataframe2.shape)
print(dataframe2.columns)
print(dataframe2.index)

# look at one column
print(dataframe2["Name"][3])

# operations
print(dataframe2["Age"].max()) # series.max() we get oldest person
print(dataframe2["Fare"].mean())

# multiple columns
print(dataframe2[["Name","Age","Sex"]])

# filtering rows
print(dataframe2[dataframe2["Age"]<18]) # argument is the condition
print(dataframe2[(dataframe2["Age"]<18) & (dataframe2["Sex"] == "female")]) # & for and, | for or

# slicing (index spaced)
print(dataframe2.iloc[500:505,2:5]) # starting row:ending row, starting column:ending column (ending index not included)

# conditional slicing
print(dataframe2.loc[dataframe2["Age"]>18,["Name","Age","Fare"]]) # rows given as a condition, columns fetched by names
print(dataframe2.loc[500:505,["Name","Age","Fare"]]) # here rows are given by index (includes ending index)

# changing values
dataframe2.loc[0:2,["Name"]] = ["Urvi","Urja","Aanya"]
print(dataframe2.head())

# adding more columns
dataframe2["Discounted Fare"] = dataframe2["Fare"]/2
print(dataframe2.head())

# creating a csv file
dataframe2.to_csv("updated titanic.csv")

# renaming rows or columns
dataframe2.rename(columns={"Sex":"Gender","Fare":"Ticket"},inplace=True) # inplace means storing in original dataframe
print(dataframe2)

# sorting
print(dataframe2.sort_values("Age",ascending=True))

# replacing (every occurence of one value changes to something else)
dataframe2["Gender"].replace({"male":"m","female":"f"},inplace=True)
print(dataframe2)

# grouping, then aggregation function (min, max, sum ,median, mean)
pclass_min = dataframe2.groupby("Pclass").min() # pclass is now the index
print(pclass_min)
pclass = dataframe2.groupby(["Pclass","Gender"])[["Age","Ticket"]].mean() # both pclass and gender become indexes
print(pclass)

# aggregation function
print(dataframe2.agg({"Age":["mean","min","max"], "Name":["count"], "Ticket":"median"}))

# operations on text data
dataframe2["Last Name"] = dataframe2["Name"].str.split().str.get(-1) # getting last names, .str() manipulates specifically text data
print(dataframe2)
