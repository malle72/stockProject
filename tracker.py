import pandas as pd
import yfinance as yf
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from datetime import date

# import stock_prices.csv and read into a df
# NOTE: Come up with a dynamic way for the code to check when the last day data was gatherded, compare to current date, and then pull all prices for days missed since last run
# Above will likely require the index be set to the date to which the data is relevant
# 
df_stocks = pd.read_csv('stockProject/stock_prices.csv')
df_stocks.set_index('date',drop=True,inplace=True)
df_stocks.index = pd.to_datetime(df_stocks.index)
""" print(df_stocks) """
""" filler = []
counter = 1
for item in df_stocks.columns:
    filler.append(counter)
    counter+=1

df_stocks.loc[0]=filler """
""" print(df_stocks) """
current_price = []
for tick in df_stocks.columns:
    current_price.append(yf.Ticker(tick).history(period='1d').Open.values[0])

df_stocks.loc[len(df_stocks.index)] = current_price 

# section of code dealing with index as date
# pulls indexes into list; replace unwanted element with suitable replacement
# set index equal to modified list

as_list = df_stocks.index.tolist()
idx = as_list.index(df_stocks.index.max())
as_list[idx]=date.today().isoformat()
df_stocks.index._data=np.array(as_list)

df_stocks.to_csv('stockProject/stock_prices.csv')
