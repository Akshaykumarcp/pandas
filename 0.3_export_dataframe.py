import pandas as pd

dataframe = pd.read_csv('weather_data.csv')
""" day  temperature  windspeed  event
0  1/1/2017           32          6   Rain
1  1/2/2017           35          7  Sunny
2  1/3/2017           28          2   Snow
3  1/4/2017           24          7   Snow
4  1/5/2017           32          4   Rain
5  1/6/2017           31          2  Sunny """

# export dataframe with index
dataframe.to_csv("dataframe_with_index.csv")

# export dataframe without index
dataframe.to_csv("dataframe_without_index.csv",index=False)









