# Portfolio Analysis
### A quantitative analysis tool for financial protfolios built with Python

This project provides a comprehensive quantitative analysis of a financial portfolio, including historical price data, risk metrics, correlation analysis, and portfolio optimization using Modern Portfolio Theory.

[Live Dashboard](https://portfolio-analysis-luckylukeii.streamlit.app/)

[Dashboard Screenshot](reports/screenshot.png)

## Tech Stack
- Python 3.14
- Pandas · NumPy · SciPy
- yfinance
- matplotlib · seaborn · plotly
- PyPortfolioOpt
- Streamlit
- pytest

## Installation

- git clone https://github.com/LuckyLukeII/portfolio-analysis.git
- cd portfolio-analysis
- python -m venv venv
- venv\Scripts\activate
- pip install -r requirements.txt

## Project Structure

```
portfolio-analysis/
├── data/               # Raw price data downloaded from Yahoo Finance
├── notebooks/          # Jupyter notebooks for analysis
├── src/
│   ├── data_loader.py  # Download and clean price data
│   ├── metrics.py      # Financial metrics calculation
│   ├── optimization.py # Portfolio optimization (MPT)
│   └── visualization.py# Chart functions
├── tests/              # Unit tests with pytest
├── dashboard/          # Streamlit web app
└── reports/            # Screenshots and outputs
```

## Metrics

| Metric | Description |
|--------|-------------|
| CAGR | Compound Annual Growth Rate |
| Annualized Volatility | Standard deviation of returns, annualized |
| Sharpe Ratio | Risk-adjusted return vs risk-free rate |
| Sortino Ratio | Like Sharpe, but penalizes only downside volatility |
| Maximum Drawdown | Worst peak-to-trough loss |
| Calmar Ratio | CAGR divided by Maximum Drawdown |
| Beta | Sensitivity to market movements (benchmark: SPY) |
| Jensen's Alpha | Excess return over CAPM prediction |
| Historical VaR | Worst loss at 95% confidence (historical) |
| Parametric VaR | Worst loss at 95% confidence (normal distribution) |

## Results

| Ticker | CAGR | Volatility | Sharpe | Sortino | Max Drawdown | Calmar Ratio | Beta | Alpha | VaR | Parametric VaR |
|--------|------|------------|--------|---------|--------------|--------------|------|-------|-----|----------------|
| AAPL | 28.25% | 31.69% | 0.82 | 1.16 | -31.43% | 0.90 | 1.19 | 12.06% | -3.01% | 3.40% |
| MSFT | 22.59% | 30.51% | 0.69 | 0.96 | -37.15% | 0.61 | 1.19 | 7.21% | -2.86% | 3.26% |
| QQQ | 19.75% | 25.65% | 0.68 | 0.89 | -35.12% | 0.56 | 1.14 | 4.13% | -2.58% | 2.74% |
| SPY | 14.34% | 21.00% | 0.55 | 0.68 | -33.72% | 0.43 | 1.00 | 0.00% | -1.93% | 2.24% |
| TLT | -6.16% | 17.97% | -0.49 | -0.77 | -48.35% | -0.13 | -0.13 | -7.26% | -1.73% | 1.84% |