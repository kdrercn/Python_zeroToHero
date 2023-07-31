import pandas as pd
df = pd.read_csv("imdb.csv")

result = df

result = df.head()
result = df.head(10)
result = df.tail()
result = df.tail(10)

result = df["Movie_Title"]
result = df["Movie_Title"].head()
result = df[["Movie_Title","Rating"]].head()
result = df[["Movie_Title","Rating"]].head(7)
result = df[5:15][["Movie_Title","Rating"]].head()
result = df[df["Rating"] > 8.0][["Movie_Title","Rating"]].head(50)
result = df.query("YR_Released >= 2014 & YR_Released <= 2015")["Movie_Title"]
result = df[(df["Num_Reviews"] > 100000) | ((df["Rating"] > 8.0) & (df["Rating"] <= 9.0))][["Num_Reviews","Rating"]]








print(result)