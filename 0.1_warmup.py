import pandas as pd

dataframe = pd.read_csv('nyc_weather.csv')

# find maximum temperature
dataframe['Temperature'].max()
# 50

# find on which day did it rain
dataframe['EST'][dataframe["Events"] == "Rain"]
""" 0      1/1/2016
1      1/2/2016
2      1/3/2016
3      1/4/2016
4      1/5/2016
5      1/6/2016
6      1/7/2016
7      1/8/2016
8      1/9/2016
9     1/10/2016
10    1/11/2016
11    1/12/2016
12    1/13/2016
13    1/14/2016
14    1/15/2016
15    1/16/2016
16    1/17/2016
17    1/18/2016
18    1/19/2016
19    1/20/2016
20    1/21/2016
21    1/22/2016
22    1/23/2016
23    1/24/2016
24    1/25/2016
25    1/26/2016
26    1/27/2016
27    1/28/2016
28    1/29/2016
29    1/30/2016
30    1/31/2016
Name: EST, dtype: object """

# find average wind speed
dataframe['WindSpeedMPH'].mean()
# 6.892857142857143

