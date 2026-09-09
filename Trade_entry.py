trade_journal.py

def log_trade(date, symbol, direction, entry, exit_price, percent_return, result, notes=""):
    trade_entry = {
        "date": date,
        "symbol":symbol,
        "direction": direction,
        "entry": entry,
        "exit": exit_price,
        "percent_return": percent_return,
        "result": result,
        "notes": notes
    
    trade_journal.append(trade_entry)
    return trade_entry
