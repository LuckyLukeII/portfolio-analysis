import pandas as pd
import numpy as np

def CAGR(df):
    years=(df.index[-1]-df.index[0]).days/365.25
    cagr=(df.iloc[-1]/df.iloc[0])**(1/years)-1
    return cagr

def YR_Volatility(df):
    returns=df.pct_change()
    yr_vol=returns.std()*(252**0.5)
    return yr_vol

def Sharpe(df,risk=0.04):
    yr_vol=YR_Volatility(df)
    sharpe=(df.pct_change().mean()*252-risk)/yr_vol
    return sharpe

def Sortino(df,risk=0.04):
    returns=df.pct_change()
    yr_vol=returns[returns<0].std()*(252**0.5)
    sortino=(returns.mean()*252-risk)/yr_vol
    return sortino

def Max_Drawdown(df):
    Cmax=df.cummax()
    drawdown=(df-Cmax)/Cmax
    return drawdown.min()

def Calmar_Ratio(df):
    return CAGR(df)/abs(Max_Drawdown(df))