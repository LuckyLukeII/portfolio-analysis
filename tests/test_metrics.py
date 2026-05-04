import pandas as pd
import numpy as np
import sys
sys.path.append('..')
import pytest
from src.metrics import CAGR, YR_Volatility, Sharpe, Max_Drawdown

dates=pd.date_range('2020-01-01',periods=100)
df=pd.DataFrame({
    'SPY':np.linspace(100,120,100),
    'QQQ':np.linspace(100,130,100)
},index=dates)

def test_CAGR():
    result=CAGR(df)
    years=(df.index[-1]-df.index[0]).days/365.25
    expected=(120/100)**(1/years)-1
    assert result['SPY']==pytest.approx(expected,rel=0.01)

def test_Max_Drawdown():
    result=Max_Drawdown(df)
    assert result['SPY']<=0 and result['QQQ']<=0

def test_YR_Volatility():
    result=YR_Volatility(df)
    assert result['QQQ']>0 and result['SPY']>0

def test_Sharpe_0():
    returns=df.pct_change().dropna().mean()*252
    result=Sharpe(df,returns)
    assert result['SPY']==0 and result['QQQ']==0

def test_Correlation_Matrix():
    result=df.corr()
    assert (result==result.T).all().all() and (np.diag(result)==pytest.approx(1.0))