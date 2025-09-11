import pandas as pd

# ticker_data is a dictionary of dataframes ticker symbol: dataframe
portfolio_value = pd.DataFrame(columns =['Date', 'Portfolio Value'])
trade_log = []
cash = 11,000

def initialize_portfolio(ticker_data): 
    holdings = {}
    for ticker in ticker_data.keys(): 
        holdings[ticker] = 0
    return holdings
    
def simulate_portfolio(ticker_data, holdings): 
    control = next(iter(ticker_data.values()))
    dates = control.index

    for date in dates: 
        for symbol, ticker in ticker_data.items(): 
            buy_signal = ticker.loc[date, 'Buy Signal']
            sell_signal = ticker.loc[date, 'Sell Signal']
            price = ticker.loc[date, 'Close']
            if (sell_signal == True) and (holdings[symbol] > 0):
                shares = holdings[symbol]
                cash += (shares * price)
                holdings[symbol] = 0
                log_trade(trade_log, date, symbol, "Sell", price, shares, cash, holdings, ticker_data)
            elif (buy_signal == True) and (cash > 1000):
                shares = 1000 // price
                holdings[symbol] = shares
                remaining = 1000 - (shares * price)
                cash += remaining
                log_trade(trade_log, date, symbol, "Buy", price, shares, cash, holdings, ticker_data)
            
        
                
def log_trade(trade_log, date, symbol, action, price, shares, cash, holdings, ticker_data):
    total_holdings = 0
    for stock, holds in holdings.items(): 
        total_holdings += holds
    portfolio_value = cash + sum(holdings[stock] * ticker_data[stock].loc[date, "Close"])
    trade_log.append({
        "Date": date,
        "Ticker": symbol,
        "Action": action,
        "Price": price,
        "Shares": shares,
        "Cash": cash,
        "Holdings": total_holdings,
        "Portfolio Value": portfolio_value,
    })
                
    
