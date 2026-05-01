import yfinance as yf
import pandas as pd
import os

def load_prices(tickers, start, end, save=True):
    data=yf.download(tickers, start=start, end=end)['Close'].ffill()
    if save:
        data.to_csv(os.path.join(os.path.dirname(__file__),'..','data','raw','prices.csv'))
    return data