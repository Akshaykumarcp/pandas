from pandas_datareader import data,wb
import pandas as pd
import numpy as np
import datetime
import seaborn as sb

#get data using pandas_datareader

start = datetime.datetime(2006,1,1)
end = datetime.datetime(2016,1,1)

#various banks, yahoo is the finance
BAC = data.DataReader('BAC','yahoo',start,end) # bank of america
C = data.DataReader('C','yahoo',start,end) # citigroup
GS = data.DataReader('GS','yahoo',start,end) #goldman sachs
JPM = data.DataReader('JPM','yahoo',start,end) #JP morgan
MS = data.DataReader('MS','yahoo',start,end) #morgan stanley
WFC = data.DataReader('WFC','yahoo',start,end) #wells fargo

# list of ticker symbols as strings in alphabetical order.
tickers = ['BAC','C','GS','JPM','MS','WFC']

#concat all dataframes
bank_stocks = pd.concat([BAC,C,GS,JPM,MS,WFC],axis=1,keys=tickers)
#created multi-level indices
bank_stocks.head()

#set column name levels
bank_stocks.columns.names = ['Bank Ticker','Stock Info']

bank_stocks.head()

#EDA


# max close price for each bank stock thorughout the period
#hint
bank_stocks['BAC']['Close'].max()

for tick in tickers:
    print(tick,bank_stocks[tick]['Close'].max())

#OR

bank_stocks.xs(key='Close',axis=1,level='Stock Info').max()

# create dataframe "returns" which'll have returns of each bank stocks. returns are defined by an formula

returns = pd.DataFrame()

for tick in tickers:
    returns[tick+'Return'] = bank_stocks[tick]['Close'].pct_change()

# pairplot for returns
sb.pairplot(returns[1:]) # 0th index has Nan value, so start from 1st index
# find which bank crashed (that has steeper line)

# what date each bank had best and worst single day returns.
# should notice that all the banks share the same day for the worst drop,
# find out the reason ?

returns.idxmin()
returns.idxmax()
# google for date so that reason are finding out

# S.D of returns and classify riskiest
#more S.D - high risk

returns.std()
"""
BACReturn    0.036647
CReturn      0.038672 - highest
GSReturn     0.025390 
JPMReturn    0.027667
MSReturn     0.037819

"""

returns.ix['2015-01-01':'2015-12-31'].std()

#distplot using seaborn for 2015 returns
sb.distplot(returns.ix['2015-01-01':'2015-12-31']['MSReturn'],color='green',bins=50)

# visualization

import matplotlib.pyplot as plt

#line plot for entire index
for tick in tickers:
    bank_stocks[tick]['Close'].plot(label=tick,figsize=(12,4))
plt.legend()

# OR

bank_stocks.xs(key='Close',axis=1,level='Stock Info').plot()

# moving averages in 2008
# plot rolling 30 day average against the Close Price for Bank of america stock for 2008
BAC['Close'].ix['2008-01-01':'2009-01-01'].rolling(window=30).mean().plot(label='30 day ')
BAC['Close'].ix['2008-01-01':'2009-01-01'].plot(labels='BAC close')

# heatmap for cor between stock close price
sb.heatmap(bank_stocks.xs(key='Close',axis=1,level="Stock Info").corr(),annot=True)

#cluster map
sb.clustermap(bank_stocks.xs(key='Close',axis=1,level="Stock Info").corr(),annot=True)

