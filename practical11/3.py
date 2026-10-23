#pandas installation and series data frame

import pandas as pd

data={
    "Name": ["Aditya","Om","Rohit"],
    "Age": [20,21,22],
    "Marks": [90,80,70]
}

df = pd.DataFrame(data)

print(df)

print("\nDataFrame Info:")
print(df["Name"])
print(df.iloc[0])
print(df.shape)
print(df.columns)
print(df.dtypes)
print(df[df["Marks"]>80])
df["Grade"]=["A","B","C"]
print(df)