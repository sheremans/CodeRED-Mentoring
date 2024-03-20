import pandas as pd

file_path = "/Users/anastasiasheremet/Desktop/python/mieszkania_mac_linux (1).csv"
df = pd.read_csv(file_path)

print(df.head())
dfy = df.groupby(df['Rok'])['Wartosc'].mean()
print(dfy)

