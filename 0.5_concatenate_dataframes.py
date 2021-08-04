import pandas as pd
from pandas.core.frame import DataFrame

india_weather = pd.DataFrame({
    "city": ["mumbai","delhi","banglore"],
    "temperature": [32,45,30],
    "humidity": [80, 60, 78]
})

""" 
city  temperature  humidity
0    mumbai           32        80
1     delhi           45        60
2  banglore           30        78 
"""

us_weather = pd.DataFrame({
    "city": ["new york","chicago","orlando"],
    "temperature": [21,14,35],
    "humidity": [68, 65, 75]
})

""" 
city  temperature  humidity
0  new york           21        68
1   chicago           14        65
2   orlando           35        75 
"""

dataframe = pd.concat([india_weather,us_weather])
"""        
city  temperature  humidity
0    mumbai           32        80
1     delhi           45        60
2  banglore           30        78
0  new york           21        68
1   chicago           14        65
2   orlando           35        75 
"""
# indices are not continous

# concat dataframes with continous indices
dataframe = pd.concat([india_weather,us_weather],ignore_index=True)
""" 
city  temperature  humidity
0    mumbai           32        80
1     delhi           45        60
2  banglore           30        78
3  new york           21        68
4   chicago           14        65
5   orlando           35        75 """

# concat dataframes based on row wise
dataframe = pd.concat([india_weather,us_weather],axis=1)
""" 
    city  temperature  humidity      city  temperature  humidity
0    mumbai           32        80  new york           21        68
1     delhi           45        60   chicago           14        65
2  banglore           30        78   orlando           35        75 """


