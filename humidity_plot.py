# Create a histogram of humidity data from the second week

import pandas as pd
import matplotlib.pyplot as plt

df1 = pd.read_csv("formatdata1.csv")
df2 = pd.read_csv("formatdata2.csv")

df2['Humidity'].hist(bins=10, alpha=0.5)
plt.suptitle('Histogram of Humidity')

plt.show()
