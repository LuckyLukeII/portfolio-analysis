import yfinance as yf
import pandas as pd

def load_prices(tickers, start, end, save=True):
    data=yf.download(tickers, start=start, end=end)['Close'].ffill()
    if save:
        data.to_csv('data/raw/prices.csv')
    return data