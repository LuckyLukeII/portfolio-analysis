import pandas as pd
import scipy.stats as stats

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
    ratio=CAGR(df)/abs(Max_Drawdown(df))
    return ratio

def Beta(df,benchmark='SPY'):
    returns=df.pct_change()
    b=returns.cov()[benchmark]/returns[benchmark].var()
    return b

def Jensen(df,risk=0.04,benchmark='SPY'):
    yr_bench=df[benchmark].pct_change().mean()*252
    Alpha=df.pct_change().mean()*252-(risk+Beta(df)*(yr_bench-risk))
    return Alpha

def VaR(df,confidence=0.95):
    var=df.pct_change().quantile(1-confidence)
    return var

def parametric_VaR(df,confidence=0.95):
    returns=df.pct_change().mean()
    std=df.pct_change().std()
    z=stats.norm.ppf(1-confidence)
    Pvar=returns-(std*z)
    return Pvar