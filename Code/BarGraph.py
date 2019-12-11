import pandas as pd
import matplotlib.pyplot as plt

#Reading the dataset into an object
a = pd.read_csv('https://github.com/siddarthkrishna10/Project_Zlatan/blob/master/Code/ZlatanStat_Sheet.csv')

#Plotting a bar graph for Market Value and Transfer Fee
a.plot(x='Club', y=['Market_Value', 'Transfer_Fee'], kind='bar')
plt.xlabel('Club')
plt.xticks(rotation=45)
plt.show()
