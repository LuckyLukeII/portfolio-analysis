import pandas as pd
from pypfopt import expected_returns, risk_models, EfficientFrontier

def optimize_max_sharpe(df):
    Exp_Returns=expected_returns.mean_historical_return(df)
    Cov_matrix=risk_models.CovarianceShrinkage(df).ledoit_wolf()
    ef=EfficientFrontier(Exp_Returns, Cov_matrix)
    ef.max_sharpe(risk_free_rate=0.04)
    weights=ef.clean_weights(0.01)
    return weights

def optimize_min_volatility(df):
    Exp_Returns=expected_returns.mean_historical_return(df)
    Cov_matrix=risk_models.CovarianceShrinkage(df).ledoit_wolf()
    ef=EfficientFrontier(Exp_Returns, Cov_matrix)
    ef.min_volatility()
    weights=ef.clean_weights(0.01)
    return weights

def optimize_risk(df):
    Exp_Returns=expected_returns.mean_historical_return(df)
    Cov_matrix=risk_models.CovarianceShrinkage(df).ledoit_wolf()
    ef=EfficientFrontier(Exp_Returns, Cov_matrix)
    ef.efficient_risk(target_volatility=0.15)
    weights=ef.clean_weights(0.01)
    return weights

def portfolio_performance(df,weights,risk=0.04):
    Exp_Returns=expected_returns.mean_historical_return(df)
    Cov_matrix=risk_models.CovarianceShrinkage(df).ledoit_wolf()
    ef=EfficientFrontier(Exp_Returns,Cov_matrix)
    ef.set_weights(weights)
    return ef.portfolio_performance(risk_free_rate=risk,verbose=True)