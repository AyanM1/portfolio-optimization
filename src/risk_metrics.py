
# Risk metrics calculations
import numpy as np
import pandas as pd


def calculate_var(returns: 'pd.Series', confidence: float = 0.05) -> float:
    """
    Calculate Value at Risk (VaR) at the given confidence level.
    """
    return np.percentile(returns, 100 * confidence)

def calculate_sharpe_ratio(returns: 'pd.Series', risk_free_rate: float = 0.0) -> float:
    """
    Calculate the Sharpe Ratio of the returns.
    """
    excess_returns = returns - risk_free_rate
    return excess_returns.mean() / excess_returns.std()

def calculate_max_drawdown(prices: 'pd.Series') -> float:
    """
    Calculate the maximum drawdown from a series of prices.
    """
    cumulative = prices.cummax()
    drawdown = (prices - cumulative) / cumulative
    return drawdown.min()
