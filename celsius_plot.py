# Purpose: Create Celsius plot comparing period 1 and period 2 (week 1 and week 2)

import pandas as pd
import matplotlib.pyplot as plt
df1 = pd.read_csv("formatdata1.csv") #baseline data is period 1 (older)
df2 = pd.read_csv("formatdata2.csv") #data for period 2 (more recent)
plt.figure(); df1.Celsius.plot(label = 'week 1 ');df2.Celsius.plot(label = 'week 2'); plt.legend(loc='best'); plt.suptitle('Celsius')
plt.show()
