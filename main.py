import pandas as pd
import requests as req
import matplotlib.pyplot as mat
import seaborn as sns


df = pd.read_csv("Data.csv")

df['Date'] = pd.to_datetime(df['Date'])

print(df.head())
print(df.info())
print(df.describe())

df.fillna({
    'Precipitation':0,
    'WindSpeed':df['WindSpeed'].mean(),
    'Humidity':df['Humidity'].mean()
})