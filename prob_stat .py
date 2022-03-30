# -*- coding: utf-8 -*-
"""Prob_Stat.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/18vU2CK9Cop45bcRIk6Mhvv1JeymEnbhO
"""

pip install stemgraphic

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import stemgraphic

from google.colab import files
uploaded = files.upload()

# ! Import dataset
df  = pd.read_csv("./SolarPrediction.csv")

# ! Clean not used data 

del df["UNIXTime"]
del df["Pressure"]
del df["WindDirection(Degrees)"]
del df["Speed"]
del df["TimeSunRise"]
del df["TimeSunSet"]
df = df.drop(df.index[3500:],axis=0)
df.info()

print(df["Radiation"].describe())
print(df["Temperature"].describe())
print(df["Humidity"].describe())

# ! For the reason that Data(Date) and Time are use for categorize another data
# ? we will only calculate avg, median, mode and standard deviation of the remaining three 
# ! Finding Mean(xbar) of each column
avg_radiation_wpm2 = df["Radiation"].mean()
avg_Temperature_Fahrenheit = df["Temperature"].mean()
avg_Relative_Humidity_percentage = df["Humidity"].mean()

print("Mean of radiation is : %.5f w/m^2" %avg_radiation_wpm2)
print("Mean of temperature is : %.5f °F" % avg_Temperature_Fahrenheit)
print("Mean of humidity is : %.5f "% avg_Relative_Humidity_percentage + "%" )\

# ! Finding Mode of each column
mode_radiation_wpm2 = df["Radiation"].mode()
mode_Temperature_Fahrenheit = df["Temperature"].mode()
mode_Relative_Humidity_percentage = df["Humidity"].mode()

print("Mode of radiation is : %.5f w/m^2" %mode_radiation_wpm2)
print("Mode of temperature is : %.5f °F" % mode_Temperature_Fahrenheit)
print("Mode of humidity is : %.5f "% mode_Relative_Humidity_percentage + "%" )

# ! Finding Median(x tilde) of each column

med_radiation_wpm2 = df["Radiation"].median()
med_Temperature_Fahrenheit = df["Temperature"].median()
med_Relative_Humidity_percentage = df["Humidity"].median()

print("Med of radiation is : %.5f w/m^2" %med_radiation_wpm2)
print("Med of temperature is : %.5f °F" % med_Temperature_Fahrenheit)
print("Med of humidity is : %.5f "% med_Relative_Humidity_percentage + "%" )

# ! Finding SD of each column
# ? ddof in parameter is Delta Degree of Freedom which the divisor use. (N-ddof)

SD_radiation_wpm2 = df["Radiation"].std(ddof=1)
SD_Temperature_Fahrenheit = df["Temperature"].std(ddof=1)
SD_Relative_Humidity_percentage = df["Humidity"].std(ddof=1)

print("SD of radiation is : %.5f w/m^2" %SD_radiation_wpm2)
print("SD of temperature is : %.5f °F" % SD_Temperature_Fahrenheit)
print("SD of humidity is : %.5f "% SD_Relative_Humidity_percentage + "%" )

df['Radiation'].hist()
plt.title("Histogram of radiation")
plt.xlabel("Radiation(w/m^2)")
plt.ylabel("Frequency of data")

df['Temperature'].hist()
plt.title("Histogram of temperature")
plt.xlabel("Temperature(°F)")
plt.ylabel("Frequency of data")

df['Humidity'].hist()
plt.title("Histogram of humidity")
plt.xlabel("Humidity(%)")
plt.ylabel("Frequency of data")

stemgraphic.stem_graphic(df['Radiation'],scale = 10,display=3500)

stemgraphic.stem_graphic(df['Temperature'],scale = 10,display=3500)

stemgraphic.stem_graphic(df['Humidity'],scale = 10,display=3500)

df_low=df[df['Radiation'] <= 660]
print(df_low['Temperature'].median())
df_low.info()
plt.scatter(df_low['Temperature'],df_low['Humidity'])
plt.title("Scatter plot between low radiation")
plt.xlabel("Temperature(°F)")
plt.ylabel("Humidity(%)")
plt.show()

df_medium=df[df['Radiation'] > 660 ]
df_medium=df_medium[df_medium['Radiation'] <= 1320 ]
print(df_medium['Temperature'].median())
df_medium.info()
plt.scatter(df_medium['Temperature'],df_medium['Humidity'])
plt.title("Scatter plot between medium radiation")
plt.xlabel("Temperature(°F)")
plt.ylabel("Humidity(%)")
plt.show()

df_high=df[df['Radiation'] > 1320 ]
print(df_high['Temperature'].median())
df_high.info()
plt.scatter(df_high['Temperature'],df_high['Humidity'])
plt.title("Scatter plot between high radiation")
plt.xlabel("Temperature(°F)")
plt.ylabel("Humidity(%)")
plt.show()

plt.boxplot(df['Radiation'])
plt.title("Box plot of Radiation")
plt.ylabel("Radiation(w/m^2)")
plt.show()

rad_outlier = df[df['Radiation'] > 1349.6125]
rad_outlier.info()

rad_no_outlier = df[df['Radiation'] <= 1349.6125]
rad_no_outlier.info()

plt.boxplot(df['Temperature'])
plt.title("Box plot of Temperature")
plt.ylabel("Temperature(°F)")
plt.show()

Temp_High_outlier = df[df['Temperature'] > 76.5]
Temp_High_outlier.info()
Temp_Low_outlier = df[df['Temperature'] < 32.5]
Temp_Low_outlier.info()

plt.boxplot(df['Humidity'])
plt.title("Box plot of Humidity")
plt.ylabel("Humidity(%)")
plt.show()

Humi_High_outlier = df[df['Humidity'] > 143.5]
Humi_High_outlier.info()
Humi_Low_outlier = df[df['Humidity'] < 3.5]
Humi_Low_outlier.info()

count, bins_count = np.histogram(df['Radiation'], bins=10)

pdf = count / sum(count)
cdf = np.cumsum(pdf)
plt.plot(bins_count[1:], pdf, color="red", label="PDF")
plt.plot(bins_count[1:], cdf, label="CDF")
# plt.ylabel('Y numbers')
plt.xlabel('Radiation(w/m^2)')
plt.title("Radiation PDF and CDF")
plt.legend()

count, bins_count = np.histogram(df['Temperature'], bins=10)

pdf = count / sum(count)
cdf = np.cumsum(pdf)
plt.plot(bins_count[1:], pdf, color="red", label="PDF")
plt.plot(bins_count[1:], cdf, label="CDF")
# plt.ylabel('Y numbers')
plt.xlabel('Temperature(°F)')
plt.title("Temperature PDF and CDF")
plt.legend()

count, bins_count = np.histogram(df['Humidity'], bins=10)

pdf = count / sum(count)
cdf = np.cumsum(pdf)
plt.plot(bins_count[1:], pdf, color="red", label="PDF")
plt.plot(bins_count[1:], cdf, label="CDF")
# plt.ylabel('Y numbers')
plt.xlabel('Humidity(%)')
plt.title("Humidity PDF and CDF")
plt.legend()