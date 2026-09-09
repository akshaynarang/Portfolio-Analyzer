def max_drawdown (series):
    running_max = series.cummax()
    drwadown = series / running_max - 1
    max_dd = drawdown.min()
    return max_dd, max_drawdown
import numpy as np
import pandas pd

def historical_var(returns, confidence=0.95)
    # returns = daily returns as a pd.Series
    sorted_returns = np.sort(returns)
    index = int((1 - confidence) * len(sorted_returns))
    var = sorted_returns[index]
    return var

def cvar(returns, confidence=0.95):
    var = historical(returns, confidence)
    tail_losses = returns[returns <= var]
    return tail_losses.mean()

df["returns"] = df["equity"].pct_change().dropna()

max_dd, dd_series = max_drawdown(df["equity"])
var_95 = historical_var(df["returns"], confidence=0.95)
cvar_95 = cvar(df["returns"], confidence=0.95)