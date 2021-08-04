import pandas as pd
import numpy as np
from pandas.core import indexing

# create custom index
dataframe = pd.DataFrame([1,2,3,4,5,6,7,8,9,19], index=[49,48,47,46,45, 1, 2, 3, 4, 5])
"""
     0
49   1
48   2
47   3
46   4
45   5
1    6
2    7
3    8
4    9
5   19 """

""" 
2 ways of indexing

1. dataframe --> based on indexing
2. dataframe --> based on row
 
"""

dataframe.loc[45] # access based on index number
# Name: 45, dtype: int64

dataframe.iloc[4] # access based on row number
# Name: 45, dtype: int64

dataframe.loc[:2] # print until index 2
"""     
    0
49  1
48  2
47  3
46  4
45  5
1   6
2   7 """

dataframe.iloc[:2] # print upto 2 rows
"""     
    0
49  1
48  2 """

"""
.loc() --> uses index
.iloc() --> uses row no

.loc() & iloc() is same when default index is used
"""