import pandas as pd

list1 = [1,4,3,6,5,3,4]
series1 = pd.Series(list1,index=["a","b","c","d","e","f","g"]) # you can make the indexes whatever you want, otherwise defaults to startig wiht 0
print(series1,type(series1))
print(series1["a"])

print(series1.sum())
print(series1.median())
print(series1.mean())
print(series1.count()) # like len
print(series1.min())
print(series1.max())
print(series1.mode()) # mode returns a series, becuse there can be multiple modes
print(series1.sort_values())
print(series1.sort_values(ascending=False)) # defaults to True
print(series1.value_counts()) # every value becomes the index - the items are the amount each index occurs
