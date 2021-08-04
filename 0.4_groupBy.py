import pandas as pd

dataframe = pd.read_csv('weather_data_cities.csv')
"""          
day      city  temperature  windspeed   event
0   1/1/2017  new york           32          6    Rain
1   1/2/2017  new york           36          7   Sunny
2   1/3/2017  new york           28         12    Snow
3   1/4/2017  new york           33          7   Sunny
4   1/1/2017    mumbai           90          5   Sunny
5   1/2/2017    mumbai           85         12     Fog
6   1/3/2017    mumbai           87         15     Fog
7   1/4/2017    mumbai           92          5    Rain
8   1/1/2017     paris           45         20   Sunny
9   1/2/2017     paris           50         13  Cloudy
10  1/3/2017     paris           54          8  Cloudy
11  1/4/2017     paris           42         10  Cloudy 
"""

# OPERATOR --> group by

group_by_city = dataframe.groupby('city')
# groups based on city column values

for city, city_df in group_by_city:
    print(city)
    print(city_df)

""" 
mumbai
        day    city  temperature  windspeed  event
4  1/1/2017  mumbai           90          5  Sunny
5  1/2/2017  mumbai           85         12    Fog
6  1/3/2017  mumbai           87         15    Fog
7  1/4/2017  mumbai           92          5   Rain
new york
        day      city  temperature  windspeed  event
0  1/1/2017  new york           32          6   Rain
1  1/2/2017  new york           36          7  Sunny
2  1/3/2017  new york           28         12   Snow
3  1/4/2017  new york           33          7  Sunny
paris
         day   city  temperature  windspeed   event
8   1/1/2017  paris           45         20   Sunny
9   1/2/2017  paris           50         13  Cloudy
10  1/3/2017  paris           54          8  Cloudy
11  1/4/2017  paris           42         10  Cloudy 
"""

# indices are intact in groupby

# find specific group
group_by_city.get_group('mumbai')
""" 
day    city  temperature  windspeed  event
4  1/1/2017  mumbai           90          5  Sunny
5  1/2/2017  mumbai           85         12    Fog
6  1/3/2017  mumbai           87         15    Fog
7  1/4/2017  mumbai           92          5   Rain """

# find max temperature in each cities
group_by_city.max()
"""                
city        day         temperature  windspeed  event

mumbai    1/4/2017           92         15      Sunny
new york  1/4/2017           36         12      Sunny
paris     1/4/2017           54         20      Sunny """

# average 
group_by_city.mean()
"""  city         temperature  windspeed
mumbai          88.50       9.25
new york        32.25       8.00
paris           47.75      12.75 """

# describe
group_by_city.describe()
""" temperature                                             ... windspeed
               count   mean       std   min    25%   50%    75%  ...      mean       std  min   25%   50%    75%   max      
city                                                             ...
mumbai           4.0  88.50  3.109126  85.0  86.50  88.5  90.50  ...      9.25  5.057997  5.0  5.00   8.5  12.75  15.0      
new york         4.0  32.25  3.304038  28.0  31.00  32.5  33.75  ...      8.00  2.708013  6.0  6.75   7.0   8.25  12.0      
paris            4.0  47.75  5.315073  42.0  44.25  47.5  51.00  ...     12.75  5.251984  8.0  9.50  11.5  14.75  20.0 """
