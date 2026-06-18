#Importing all the important libraries needed
import pandas as pd
import requests as req
import matplotlib.pyplot as mat
import seaborn as sns


df = pd.read_csv("Data.csv") #dataframe(df) for pandas to read the csv data

df['Date'] = pd.to_datetime(df['Date'])
 
#printing the dataframe(df) functions like heading and infomatics
print(df.head())
print(df.info())
print(df.describe())

#telling the df to take the avg of the windspeed and humidity
df = df.fillna({
    'Precipitation': 0,
    'WindSpeed': df['WindSpeed'].mean(),
    'Humidity': df['Humidity'].mean()
})

# Date column se month ka number (1, 2, 3...) extract karke naye integer column mein save karna
df['Month'] = df['Date'].dt.month
# Date column se day ka number (1 se 31) extract karna takis plotting ke liye clean X-axis mil sake
df['Day'] = df['Date'].dt.day



#Displaying the average temp and humidity
avg_temp = df['Temperature'].mean()
avg_humidity = df['Humidity'].mean()
print("----------------------------------------------------------------------------------------------------")
print (f'the average humidity is {avg_humidity:.2f}% and the average tmeperature is {avg_temp:.2f}C')
print("----------------------------------------------------------------------------------------------------")

# jo df h uske jo value h usko validate krta h
condition_count = df['Condition'].value_counts
print(condition_count)

def temp():
    fig,ax1 = mat.subplots(figsize =(15,6))#Makes the canvas for matplot

    #Plots the df in the canvas
    ax1.plot(df['Date'],df['Temperature'],color='red',marker='o',linewidth = 2.5,label = 'temp(C)')
    # x and y label for canvas
    ax1.set_xlabel('Date',fontsize = 12)
    ax1.set_ylabel('Temperature',fontsize = 12)

    # jo axis p color hota h usko define krte h

    ax1.tick_params(axis='y', labelcolor='crimson')
    ax1.grid(True, linestyle=':', alpha=0.6)

    mat.title('Daily Temperature Analysis') # Graph ka main heading
    mat.show() # Graph ko screen par display karne ke liye

def hum():
    fig,ax1 = mat.subplots(figsize =(15,6))#Makes the canvas for matplot

    #Plots the df in the canvas
    ax1.plot(df['Date'],df['Humidity'],color='blue',marker='o',linewidth = 2.5,label = 'temp(C)')
    # x and y label for canvas
    ax1.set_xlabel('Date',fontsize = 12)
    ax1.set_ylabel('Humidity',fontsize = 12)

    # jo axis p color hota h usko define krte h

    ax1.tick_params(axis='y', labelcolor='crimson')
    ax1.grid(True, linestyle=':', alpha=0.6)

    mat.title('Daily Humidity Analysis') # Graph ka main heading
    mat.show() # Graph ko screen par display karne ke liye

def tempvhum():
    fig, ax1 = mat.subplots(figsize=(15, 6))
    ax1.scatter(df['Temperature'],df['Humidity'],color='Purple',marker = '|',s=50,alpha = 0.8)
    ax1.set_xlabel('Temperature (°C)', fontsize=12)
    ax1.set_ylabel('Humidity (%)', fontsize=12)
    ax1.tick_params(axis='both',color='black')
    ax1.grid(True, linestyle=':', alpha=0.6)
    mat.title('Temperature vs Humidity Relationship (Scatter Plot)', fontsize=14, fontweight='bold')
    mat.show()


