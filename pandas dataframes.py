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