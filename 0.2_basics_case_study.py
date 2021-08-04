import pandas as pd

dataframe = pd.read_csv('weather_data.csv')
""" day  temperature  windspeed  event
0  1/1/2017           32          6   Rain
1  1/2/2017           35          7  Sunny
2  1/3/2017           28          2   Snow
3  1/4/2017           24          7   Snow
4  1/5/2017           32          4   Rain
5  1/6/2017           31          2  Sunny """

# dimensions of table
dataframe.shape
# (6, 4)

# top 5 rows
dataframe.head()

# bottom 5 rows
dataframe.tail()

# slice dataframe data
dataframe[1:4]
"""         day  temperature  windspeed  event
1  1/2/2017           35          7  Sunny
2  1/3/2017           28          2   Snow
3  1/4/2017           24          7   Snow """

dataframe.columns
# Index(['day', 'temperature', 'windspeed', 'event'], dtype='object')

# get column data, way 1
dataframe.day

# get column data, way 2
dataframe['day']

# get 2 column data, way 2
dataframe[['day','temperature']]

# get max temperature
dataframe['temperature'].max()
# 35

# get min temperature
dataframe['temperature'].min()
# 24

# basic stats info about data
dataframe.describe()

# select row that has maximum temperature
dataframe[dataframe['temperature'] == dataframe['temperature'].max()]

# find day in which has maximum temperature
dataframe['day'][dataframe['temperature'] == dataframe['temperature'].max()]
# 1    1/2/2017