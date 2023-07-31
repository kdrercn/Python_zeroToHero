import pandas as pd
df = pd.read_csv("nba.csv")

# İlk 10 kayıt
result = df.head(10)

# Toplam kayıt
# result = df.count()["Name"]
result = len(df.index)

# Tüm oyuncuların toplam maaş ort
result = df["Salary"].mean()

# En yüksek maaş alan oyuncu ve ne kadar aldığı
# maxSalary = df.sort_values("Salary", ascending = False)
# result = maxSalary.head(1)[["Name","Salary"]]
result = df[df["Salary"]==df["Salary"].max()]["Name"].iloc[0]

# Yaşı 20-25 arası olan oyuncuların ismi ve takımları
result = df[(df["Age"] >= 20) & (df["Age"] <= 25)][["Name","Team"]]

# John Holland'ın takımı
result = df[df["Name"] == "John Holland"]["Team"].iloc[0]

# Takımlara göre ortalama maaş bilgisi
result = df.groupby("Team").mean()["Salary"]

# Kaç farklı takım mevcut
result = df.nunique()["Team"] # tekil bilgi sayısı gelir

# Her takımda kaç oyuncu var
result = df.groupby("Team")["Name"].count()

# İsminde "and" geçen kayıtlar
df.dropna(inplace = True)
result = df[df["Name"].str.contains("and")]



print(result)