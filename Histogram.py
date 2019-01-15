import numpy as np
import pandas as pd
import matplotlib as mpl
import matplotlib.pyplot as plt


df_can = pd.read_excel("Canada.xlsx",
                        sheet_name="Canada by Citizenship",
                        skiprows=range(20),
                        skipfooter=2)
                        
df_can.drop(['AREA', 'REG', 'DEV', 'Type', 'Coverage'], axis=1, inplace=True)
df_can.rename(columns={'OdName':'Country', 'AreaName':'Continent','RegName':'Region'}, inplace=True)
all(isinstance(column, str) for column in df_can.columns)
df_can.columns = list(map(str, df_can.columns))
df_can.set_index('Country', inplace=True)
df_can['Total'] = df_can.sum(axis=1)

years = list(map(str, range(1980, 2014)))

count, bin_edges = np.histogram(df_can['2013'])

df_can['2013'].plot(kind='hist', figsize=(8, 5), xticks=bin_edges)

plt.title('Histogram of Immigration from 195 Countries in 2013') # add a title to the histogram
plt.ylabel('Number of Countries') # add y-label
plt.xlabel('Number of Immigrants') # add x-label

plt.savefig("Immigrants_Histogram.png")