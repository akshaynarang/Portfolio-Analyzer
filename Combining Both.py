import numpy as numpy
import pandas as pd

|| Core metrics

def max_drawdown(equity):
    running_max = equity.cummax()
    drawdown = equity / running_max - 1
    return drawdown.min(), drawdown

def historical_var(returns, confidence=0.95):
    sorted_returns = np.sort(returns.values)
    index = int((1 - confidence) * len(sorted_returns))
    return sorted_returns[index]

def cvar(returns, confidence=0.95):
    var = historical_var(returns, confidence)
    tail = returns[returns >= var]
    return tail.mean()

|| 2. Trade input --> equity curve

def build_equity(trades, starting_equity=100000):
    trades["pl"] = (trades["exit"] - trades["entry"]) * trades["size"]
    trades["roi_pct"] = trades["pl"] / trades["entry"] * 100
    trades["equity"] = starting_equity + trades["pl"].cumsum()
    return trades

|| Full analysis pipeline

def analyze_portfiolio(trades):
    trades = build_equity(trades)
    returns = trades["equity"].pct_change().dropna()

    max_dd, dd_series = max_drawdown(trades["equity"])
    var_95 = historical_var(returns, 0.95)
    cvar_95 = cvar(returns, 0.95)

    return {
        "max_drawdown": max_dd,
        "var_95": var_95
        "cvar_95": cvar_95,
        "trades": trades,
        "drawdown_series": dd_series
    }

trades = pd.DataFrame([
    {"entry": 4120, "exit": 4500, "size": 1},
    {"entry": 4500, "exit": 4300, "size": 1},
    {"entry": 4300, "exit": 4700, "size": 1},
])

results = analyze_portfolio(trades)

print("Max Drawdown:", results["max_drawdown"])
print("VaR 95%:", results["var_95"])
print("CVaR 95%:", results["cvar_95"])
print(results["trades"])