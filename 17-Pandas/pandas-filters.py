import pandas as pd
import numpy as np

data = np.random.randint(10,100,75).reshape(15,5)
df = pd.DataFrame(data, columns = ["Column1","Column2","Column3","Column4","Column5"])

result = df
result = df.columns

result = df.head(10) # paranteze bir şey yazmazsan ilk 5 satır
result = df.tail(10)

result = df["Column1"].head()
result = df.Column1.head()
result = df[["Column1","Column2"]].head()
result = df[5:15][["Column1","Column2"]].head()

result = df > 50
result = df[df > 50]
result = df[df % 2 == 0]
result = df[df["Column1"] > 50][["Column1","Column2"]]
result = df[(df["Column1"] > 50) & (df["Column1"] <= 70)]






print(result)