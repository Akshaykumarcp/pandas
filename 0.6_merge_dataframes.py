import pandas as pd

temperature_df = pd.DataFrame({
                                "city": ["mumbai","delhi","banglore", 'hyderabad'],
                                "temperature": [32,45,30,40]})
""" 
        city  temperature
0     mumbai           32
1      delhi           45
2   banglore           30
3  hyderabad           40 """

humidity_df = pd.DataFrame({
                            "city": ["delhi","mumbai","banglore"],
                            "humidity": [68, 65, 75]})
""" 
       city  humidity
0     delhi        68
1    mumbai        65
2  banglore        75 """

# merge dataframes based on city

city_dataframe = pd.merge(temperature_df,humidity_df,on='city')
"""        
city            temperature  humidity
0    mumbai           32        65
1     delhi           45        68
2  banglore           30        75 """

# outer join (for including hyderabad)
city_dataframe = pd.merge(temperature_df,humidity_df,on='city',how='outer')
"""         
        city  temperature  humidity
0     mumbai           32      65.0
1      delhi           45      68.0
2   banglore           30      75.0
3  hyderabad           40       NaN """


