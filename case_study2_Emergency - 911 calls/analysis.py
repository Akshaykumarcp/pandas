import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sb

dataset = pd.read_csv('dataset/100_1381403_bundle_archive/911.csv')

# info of dataset
dataset.info()

# frequently asked questions

# top 5 zip codes
dataset['zip'].value_counts().head(5)

# top 5 townships (twp) for 911 calls
dataset['twp'].value_counts().head(5)

# unique title columns
len(dataset['title'].unique())
#OR
dataset['title'].nunique()

#create new features

# in title column, seperate reason/department. Create "Reason" as seperate column
x = dataset['title'].iloc[0]
x.split(':')[0]

dataset["Reason"] = dataset['title'].apply(lambda title: title.split(':')[0])

# common reason for 911 call based on reason column

dataset['Reason'].value_counts()

#seaborn to create countplot of 911 calls by reason

sb.countplot(data=dataset,x=dataset['Reason'])

# data type of objects in "timeStamp" column
type('timeStamp')

# convert str to datetime
dataset['timeStamp'] = pd.to_datetime(dataset['timeStamp'])
type('timeStamp')
dataset.info()

#grab specific value from datetime
# create 3 new columns from datetime

#example
time = dataset['timeStamp'].iloc[0]
time.hour
time.month
time.dayofweek


dataset['hour'] = dataset['timeStamp'].apply(lambda time:time.hour)
dataset['month'] = dataset['timeStamp'].apply(lambda time:time.month)
dataset['dayOfWeek'] = dataset['timeStamp'].apply(lambda time:time.dayofweek)

#map day of the week from int to strings of actual day
dayOfMap = {0:'Mon',1:'Tue',2:'Wed',3:'Thu',4:'Fri',5:'Sat',6:'Sun'}

dataset['dayOfWeek'] = dataset['dayOfWeek'].map(dayOfMap)

# seaborn to create countplot of dayOfWeek with hue based on Reason column

sb.countplot(data=dataset,x='dayOfWeek',hue='Reason')
#legend is inside figure
plt.legend(bbox_to_anchor=(1.05,1),loc=2,borderaxespad=0.)

sb.countplot(data=dataset,x='month',hue='Reason')
#legend is inside figure
plt.legend(bbox_to_anchor=(1.05,1),loc=2,borderaxespad=0.)

dataset['timeStamp'].plot()

#create new "date" column from "timeStamp" column
dataset['date'] = dataset['timeStamp'].apply(lambda date:date.date())

# groupby by date column with count() aggrefate and plot based on counts of 911 calls
dataset.groupby('date').count()
dataset.groupby('date').count()['lat'] # for each colummn
dataset.groupby('date').count()['lat'].plot()
plt.tight_layout() #if x-axis is conjusted

dataset[dataset['Reason']=='Traffic'].groupby('date').count()['lat'].plot()

dataset[dataset['Reason']=='Fire'].groupby('date').count()['lat'].plot()

# seaborn heatborn, restructure the dataframe has, columns becomes
# hours and index becomes dayOfWeek using unstack method (makes in matrix form)
# advanced level

dayHour = dataset.groupby(by=['dayOfWeek','hour']).count()['Reason'].unstack()

sb.heatmap(dayHour)

# create clustermap for dayHour
sb.clustermap(dayHour)

dataset.groupby(by=['dayOfWeek','month']).count()['Reason'].unstack()

#911 emergency calls hourly
sb.countplot(x='hour',data=dataset)

# 911 emergency calls weekdays
sb.countplot(x='dayOfWeek',data=dataset)

dataset['Reason'].value_counts()
sb.countplot(data=dataset,x='Reason')