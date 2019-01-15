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

mpl.style.use('ggplot') # optional: for ggplot-like style

df_japan = df_can.loc[['Japan'], years].transpose()

df_japan.plot(kind='box', figsize=(8, 6))

plt.title('Box plot of Japanese Immigrants from 1980 - 2013')
plt.ylabel('Number of Immigrants')

plt.savefig("BoxPlot.png")