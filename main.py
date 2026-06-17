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

df['Month'] = df['Date'].dt.month
df['Day'] = df['Date'].dt.day

avg_temp = df['Temperature'].mean()
avg_humidity = df['Humidity'].mean()
print("----------------------------------------------------------------------------------------------------")
print (f'the average humidity is {avg_humidity:.2f} and the average tmeperature is {avg_temp:.2f}')
print("----------------------------------------------------------------------------------------------------")
