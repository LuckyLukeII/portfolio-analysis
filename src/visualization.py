import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import sys
sys.path.append('..')
from src.metrics import Rolling_Sharpe, Drawdown

def normalized_prizes(df,tickers):
    df_normalized=100*df/df.iloc[0]

    fig,ax=plt.subplots(figsize=(12,6))
    fig.suptitle("Normalized prizes",fontsize=14,fontweight="bold")

    for ticker in tickers:
        ax.plot(df_normalized.index,df_normalized[ticker],label=ticker)

    handles,labels=ax.get_legend_handles_labels()
    fig.legend(handles,labels,bbox_to_anchor=(1.05,0.5),loc="center left")
    fig.supylabel("Normalized prizes")
    ax.tick_params(axis="x",rotation=30)
    ax.grid(True,alpha=0.3)
    return fig

def correlation(df):
    corr=df.corr()
    fig,ax=plt.subplots(figsize=(8,6))
    sns.heatmap(corr,annot=True,fmt=".2f",cmap="coolwarm",ax=ax)
    ax.set_title("Correlation Matrix",fontsize=14,fontweight="bold")
    return fig

def rolling_volatility(df,tickers):
    returns=df.pct_change()
    rolling_vol=returns.rolling(30).std()*(252**0.5)

    fig,ax=plt.subplots(figsize=(12,6))
    fig.suptitle("Rolling Volatility (30 days)",fontsize=14,fontweight="bold")

    for ticker in tickers:
        ax.plot(rolling_vol.index,rolling_vol[ticker],label=ticker)

    handles,labels=ax.get_legend_handles_labels()
    fig.legend(handles,labels,bbox_to_anchor=(1.05, 0.5),loc="center left")
    fig.supylabel("Annualized Volatility")
    ax.tick_params(axis="x",rotation=30)
    ax.grid(True,alpha=0.3)
    return fig

def returns(df,tickers):
    returns=df.pct_change()

    fig,axes=plt.subplots(1,5,figsize=(18,4))
    fig.suptitle("Daily Returns Distribution",fontsize=14,fontweight="bold")

    for ticker,ax in zip(tickers,axes):
        ax.hist(returns[ticker].dropna(),bins=50)
        ax.set_title(ticker)
        ax.xaxis.set_major_formatter(plt.FuncFormatter(lambda x, _: f'{x:.1%}'))
        ax.tick_params(axis="x",rotation=30)
    return fig

def rolling_sharpe_graph(df,tickers):
    Rsharpe=Rolling_Sharpe(df)
    
    fig,ax=plt.subplots(figsize=(12,6))
    fig.suptitle("Rolling Sharpe (60 days)",fontsize=14,fontweight="bold")

    for ticker in tickers:
        ax.plot(Rsharpe.index,Rsharpe[ticker],label=ticker)

    handles,labels=ax.get_legend_handles_labels()
    fig.legend(handles,labels,bbox_to_anchor=(1.05, 0.5),loc="center left")
    fig.supylabel("Sharpe")
    ax.tick_params(axis="x",rotation=30)
    ax.grid(True,alpha=0.3)
    return fig

def drawdown_graph(df,tickers):
    drawdown=Drawdown(df)

    fig,ax=plt.subplots(figsize=(12,6))
    fig.suptitle("Drawdown",fontsize=14,fontweight="bold")

    for ticker in tickers:
        ax.plot(drawdown.index,drawdown[ticker],label=ticker)

    handles,labels=ax.get_legend_handles_labels()
    fig.legend(handles,labels,bbox_to_anchor=(1.05, 0.5),loc="center left")
    fig.supylabel("Drawdown")
    ax.tick_params(axis="x",rotation=30)
    ax.grid(True,alpha=0.3)
    return fig