#https://github.com/baderalotaibi1/seaborn-data.git
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

tips_dataset = sns.load_dataset('tips')
print(tips_dataset.head())
#Q2: Create a histogram, where the x-axis represents the tip column
sns.set_style('whitegrid')
sns.histplot(x='tip',data=tips_dataset,hue="day",element='step')
plt.title('histogram')
plt.show()
print("Q2.1 Write your top three findings:\n1- more tips was in saturday\n 2- highest tips was also in saturday\n 3- lowest tips was in friday\n  ")

#Q3: [Optional] Create a displot, where the x-axis represents the day column
sns.displot(data=tips_dataset,x='day',hue='sex',multiple="dodge",shrink=0.5,color='Set1',hue_order=['Female', 'Male'])
plt.title('displot')
plt.show()
print("Q3.1 Write your top three findings:\n1-The least day that customers come is friday \n 2- On Thursday, we notice that the proportion of Male and Female is similer \n 3-On Saturday and Sunday,male come more then Female\n  ")

#Q4: Create a ecdf plot, where the x-axis represents the tip column
sns.set_style('darkgrid')
sns.set(font_scale=1.25)
sns.ecdfplot(tips_dataset,x='tip',hue='time',palette='summer',linewidth=3)
plt.title('ecdf')
plt.show()
print("Q4.1 Write your top three findings:\n1- highest tips value was in diner\n 2- longest rate was in lunch \n 3- when the tip value increseses you have a biger chanse to get the tip in dinner  \n ")

#Q5: [Optional] Create a box plot, where the x-axis represents the day column and the y-axis represents the tip column
sns.set_style('whitegrid')
sns.boxplot(data=tips_dataset,x='day',y='tip',hue='sex',palette='Paired',hue_order= ['Female', 'Male'],linewidth=2.5)
plt.title('box plot')
plt.show()
print("Q5.1 Write your top three findings:\n1- highest tips value for male was in Thursday = 6.72$\n 2- highest tips value for Female was in Sunday = 5.22$ \n 3-lowest tips value for Male and Female was in saturday = 1$  \n ")

#Q6: Create a violin plot, where the x-axis represents the time column and the y-axis represents the tip column
sns.violinplot(data=tips_dataset,x='time',y='tip',hue='sex',split=True,inner="quartiles",palette='Pastel1',hue_order=['Female','Male'],linewidth=2)
plt.legend(loc='upper left')
plt.title('violin')
plt.show()
#Q7: [Optional] Create a swarm plot, where the x-axis represents the time column and the y-axis represents the total_bill column
sns.swarmplot(data=tips_dataset,x='time',y='total_bill',hue='size')
plt.title('swarm plot')
plt.show()
print("Q6.1 Write your top three findings:\n1- most bills are between 10 and 30$ \n 2- most expensive bills are caming from 4 people \n 3- most bills in general from 2 people  \n ")

#Q8: Create a correlation heatmap
plt.figure(figsize=(8,5))
sns.heatmap(data=tips_dataset.corr(),vmin=-1,vmax=1,annot=True,cmap='RdBu')
plt.title('heatmap')
plt.show()
