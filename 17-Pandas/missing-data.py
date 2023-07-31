import pandas as pd
import numpy as np

data = np.random.randint(10,100,15).reshape(5,3)

df = pd.DataFrame(data, index = ["a","c","e","f","h"],columns = ["column1","column2","column3"])

df = df.reindex(["a","b","c","d","e","f","g","h"])

newColumn = [np.nan,30,np.nan,51,np.nan,30,np.nan,10]
df["column4"] = newColumn

result = df
result = df.drop("column1", axis = 1)

result = df.isnull()
result = df.notnull()
result = df.isnull().sum()
result = df[df["column1"].notnull()]["column1"]

result = df.dropna() # axis = 0 
result = df.dropna(axis = 1) 
result = df.dropna(how = "any") # nan varsa almaz
result = df.dropna(how = "all") # hepsi nansa almaz
result = df.dropna(subset = ["column1","column2"]) # column 1 ve 2deki nan olmayanları alır
result = df.dropna(subset = ["column1","column2"], how = "all") 
result = df.dropna(thresh = 3) # en az 3 nan olmayan değer varsa alır

result = df.fillna(value = "no input")
result = df.fillna(value = 1)

result = df.sum()
result = df.sum().sum()
result = df.size
result = df.isnull().sum()
result = df.isnull().sum().sum()

def ort(df):
    toplam = df.sum().sum()
    adet = df.size - df.isnull().sum().sum()
    return toplam/adet

result = df.fillna(value = ort(df))


print(result)
