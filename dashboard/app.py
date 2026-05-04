import streamlit as st
import pandas as pd
import sys
sys.path.append('..')
import os
sys.path.insert(0,os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import matplotlib.pyplot as plt
from src.data_loader import load_prices
from src.metrics import CAGR, YR_Volatility, Sharpe, Sortino, Max_Drawdown, Calmar_Ratio, Beta, Jensen, VaR, parametric_VaR
from src.visualization import normalized_prizes, correlation, rolling_volatility, returns, drawdown_graph, rolling_sharpe_graph
from src.optimization import optimize_max_sharpe, optimize_min_volatility, optimize_risk, portfolio_performance

st.title('Portfolio Analysis Dashboard')
st.sidebar.header('Settings')

selected=st.sidebar.multiselect(
    'Select tickers',
    ['QQQ','GLD','TLT','MSFT','AAPL','AMZN','BTC-USD'],
    default=['QQQ','GLD','TLT','MSFT']
)
tickers=["SPY"]+selected

start=st.sidebar.date_input('Start date',value=pd.to_datetime('2020-01-01'))
end=st.sidebar.date_input('End date',value=pd.to_datetime('2024-12-31'))

@st.cache_data
def get_data(tickers,start,end):
    return load_prices(tickers,str(start),str(end),save=False)

df=get_data(tickers,start,end)

st.header('Price Data')
fig=normalized_prizes(df,tickers)
st.pyplot(fig)


st.header("Metrics")
metrics=pd.DataFrame({
    'CAGR':CAGR(df),
    'Volatility':YR_Volatility(df),
    'Sharpe':Sharpe(df),
    'Sortino':Sortino(df),
    'Max Drawdown':Max_Drawdown(df),
    'Calmar Ratio':Calmar_Ratio(df),
    'Beta':Beta(df),
    'Alpha':Jensen(df),
    'VaR':VaR(df),
    'Parametric VaR':parametric_VaR(df)
})
st.dataframe(metrics.round(4))


st.header('Correlation')
fig=correlation(df)
st.pyplot(fig)


st.header('Rolling Volatility')
fig=rolling_volatility(df,tickers)
st.pyplot(fig)


st.header('Daily Returns Distribution')
fig=returns(df,tickers)
st.pyplot(fig)


st.header('Drawdown')
fig=drawdown_graph(df,tickers)
st.pyplot(fig)


st.header('Rolling Sharpe')
fig=rolling_sharpe_graph(df,tickers)
st.pyplot(fig)


st.header("Optimization")
tab1,tab2,tab3=st.tabs(['Max Sharpe','Min Volatility','Efficient Risk 15%'])
with tab1:
    Msharpe=optimize_max_sharpe(df)
    return_Msharpe,volatility_Msharpe,sharpe_Msharpe=portfolio_performance(df,Msharpe)
    Msharpe={k:v for k,v in Msharpe.items() if v>0}
    col1,col2,col3=st.columns(3)
    col1.metric("Expected Return",f"{return_Msharpe:.2%}")
    col2.metric("Volatility",f"{volatility_Msharpe:.2%}")
    col3.metric("Sharpe Ratio",f"{sharpe_Msharpe:.2f}")
    fig,ax=plt.subplots(figsize=(12,6))
    ax.pie(Msharpe.values(),labels=Msharpe.keys(),autopct='%1.1f%%')
    st.pyplot(fig)
with tab2:
    minvol=optimize_min_volatility(df)
    return_minvol,volatility_minvol,sharpe_minvol=portfolio_performance(df,minvol)
    minvol={k:v for k,v in minvol.items() if v>0}
    col1,col2,col3=st.columns(3)
    col1.metric("Expected Return",f"{return_minvol:.2%}")
    col2.metric("Volatility",f"{volatility_minvol:.2%}")
    col3.metric("Sharpe Ratio",f"{sharpe_minvol:.2f}")
    fig,ax=plt.subplots(figsize=(12,6))
    ax.pie(minvol.values(),labels=minvol.keys(),autopct='%1.1f%%')
    ax.set_title('Min Volatility')
    st.pyplot(fig)
with tab3:
    Optrisk=optimize_risk(df)
    return_Optrisk,volatility_Optrisk,sharpe_Optrisk=portfolio_performance(df,Optrisk)
    Optrisk={k:v for k,v in Optrisk.items() if v>0}
    col1,col2,col3=st.columns(3)
    col1.metric("Expected Return",f"{return_Optrisk:.2%}")
    col2.metric("Volatility",f"{volatility_Optrisk:.2%}")
    col3.metric("Sharpe Ratio",f"{sharpe_Optrisk:.2f}")
    fig,ax=plt.subplots(figsize=(12,6))
    ax.pie(Optrisk.values(),labels=Optrisk.keys(),autopct='%1.1f%%')
    ax.set_title('Optimal Risk at 15%')
    st.pyplot(fig)