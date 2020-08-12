import pandas as pd
import yfinance as yf
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# import stock_prices.csv and read into a df
# NOTE: Come up with a dynamic way for the code to check when the last day data was gatherded, compare to current date, and then pull all prices for days missed since last run
# Above will likely require the index be set to the date to which the data is relevant
# 
df_stocks = pd.read_csv('stockProject\stock_prices.csv')

current_price = []
for tick in df_stocks.columns:
    current_price.append(yf.Ticker(tick).history(period='1d').Open.values[0])

df_stocks.loc[len(df_stocks.index)] = current_price