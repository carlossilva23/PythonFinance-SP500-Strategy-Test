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
            if (buy_signal == True) and (cash > 1000):
                shares = 1000 // price
                holdings[symbol] = shares
                remaining = 1000 - (shares * price)
                cash += remaining
                log_trade(trade_log, date, symbol, "Buy", price, shares, cash, holdings)
            elif (sell_signal == True) and (holdings[symbol] > 0):
                cash += (holdings[symbol] * ticker.loc[date, 'Close'])
                holdings[symbol] = 0
                


            def log_trade(trade_log, date, symbol, action, price, shares, cash, holdings):
                trade_log['Date'] = date
                trade_log['Ticker'] = symbol
                trade_log['Action'] = action
                trade_log['Price'] = price
                trade_log['Shares'] = shares
                trade_log['Cash After'] = cash
                total_holdings = 0
                for shares in holdings.values(): 
                    total_holdings += shares
                trade_log['Total Holdings'] = total_holdings
            
        # portfolio value appends (updated)
    
