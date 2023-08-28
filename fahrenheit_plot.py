#Purpose: Create scatter plot of humidity for period 1. Can replace df1 to df2 to display second period data

import pandas as pd
import matplotlib.pyplot as plt
df1 = pd.read_csv("formatdata1.csv")
df2 = pd.read_csv("formatdata2.csv")
plt.scatter(df1.index.values, df1['Fahrenheit']); plt.suptitle('Fahrenheit & Humidity')
plt.scatter(df1.index.values, df1['Humidity']);
plt.show()