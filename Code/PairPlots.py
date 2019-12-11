import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

#Reading the dataset into an object
b = pd.read_csv('https://github.com/siddarthkrishna10/Project_Zlatan/blob/master/Datasets/Zlatan_ClubComp.csv')
c = pd.read_csv('https://github.com/siddarthkrishna10/Project_Zlatan/blob/master/Datasets/ZlatanStat_Sheet.csv')

#Dropping Malmö row from the dataframe object c
c = c.drop([0])

#Plotting a pairplot for Appearances vs Goals and Minutes Played using Seaborn
b1 = sns.pairplot(b, y_vars=['Appearances'], x_vars=['Goals', 'Minutes_Played'], hue="Country")

#Converting Minutes_Played column from non-null object to a integar type
c['Minutes_Played'] = pd.to_numeric(c['Minutes_Played'])

#Calculating the Minutes Per Game
c['Minutes_PerGame'] = round(c['Minutes_Played']/c['Appearances'])

#Plotting for Appearances vs Minutes Per Game using Seaborn
cc3 = sns.pairplot(c, y_vars=['Appearances'], x_vars=['Minutes_PerGame'], hue="Club")

#Calculating the Goals Per Game and Minutes Per Goal
b['Goals_PerGame'] = round(b['Goals']/b['Appearances'], 2)
b['Minutes_PerGoal'] = round(b['Minutes_Played']/b['Goals'])

#Taking only Zlatan's league stats into consideration
bb1 = b[b['Competition_Type'] == 'League']

#Plotting using seaborn for Appearances vs Goals Per Game and Minutes Per goal
bb2 = sns.pairplot(bb1, y_vars=['Appearances'], x_vars=['Goals_PerGame', 'Minutes_PerGoal'], hue="Club")
plt.show()
