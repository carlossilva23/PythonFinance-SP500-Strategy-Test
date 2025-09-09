import pandas as pd

# ticker_data is a dictionary of dataframes ticker symbol: dataframe
portfolio_value = pd.DataFrame(columns =['Date', 'Portfolio Value'])
trade_log = pd.DataFrame(columns = ['Date', 'Ticker', 'Action', 'Price', 'Shares', 'Cash After', 
                                    'Total Holdings', 'Portfolio Value'])
cash = 11,000

def initialize_portfolio(ticker_data): 
    holdings = {}
    for ticker in ticker_data.keys(): 
        holdings[ticker] = 0
    
def simulate_portfolio(ticker_data): 
    control = next(iter(ticker_data.values()))
    dates = control.index

    for date in dates: 
        for ticker in ticker_data.items(): 
            # if ticker[buy signal] == true and cash > 1000
                # shares = 1000 // price
                # holdings[ticker] = shares
                # remaining = 1000 (shares * price)
                # cash += remaining
                # trade_log[date] = date
                # trade_log[action] = buy
                # trade_log[ticker] = ticker
                # append all trade_log values 
            # else if ticker[sell signal] == true and holdings[ticker] > 0
                # cash += (holdings[ticker] * price)
                # holdings[ticker] = 0
                # trade_log append 
        # portfolio value appends (updated)
    
