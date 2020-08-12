import pandas as pd
import yfinance as yf
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

df_stocks = pd.read_csv('stockProject/constituents_csv.csv')

df_stocks.drop(columns=['Name','Sector'],axis=1,inplace=True)
df_stocks.set_index('Symbol')
df_stocks = df_stocks.transpose()
df_stocks.columns=df_stocks.iloc[0].values
df_stocks.drop(index='Symbol',inplace=True)
df_stocks=df_stocks.rename(columns={'BRK.B':'BRK-B','BF.B':'BFB'})

df_stocks.to_csv('stockProject/stock_prices.csv')