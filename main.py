import pandas as pd
import requests as req
import matplotlib.pyplot as mat
import seaborn as sns


df = pd.read_csv("Data.csv")
# print(df)

mat.figure(figsize=(10,6))

s1 = sns.scatterplot(data=df,x='Date',y='Temperature')
print(s1)

mat.title('first data')
mat.yscale('Temperature')
mat.xscale('Date')

mat.tight_layout()
mat.show()