import yfinance as yf

# assume that ticker_data is a pandas df returned from a yfinance.download() call
def calculate_short_MA(ticker_data): 
    shortMA = ticker_data['Close'].rolling(window=25).mean()
    ticker_data['Short MA'] = shortMA
    
def calculate_long_MA(ticker_data): 
    longMA = ticker_data['Close'].rolling(window=100).mean()
    ticker_data['Long MA'] = longMA

def crossover(ticker_data): 
    switch_signal = ticker_data['Short MA'] > ticker_data['Long MA']
    ticker_data['Switch'] = switch_signal
    

def date_tracker(ticker_data): 
    buy_signal = (ticker_data['Switch'].diff() == 1)
    sell_signal = (ticker_data['Switch'].diff() == -1)
    buy_dates = ticker_data.loc[buy_signal]
    sell_dates = ticker_data.loc[sell_signal]
    print(buy_dates.index)
    print(sell_dates.index)



def main(): 
    ticker = yf.download('PNW', period='5y', auto_adjust=True)
    calculate_short_MA(ticker)
    calculate_long_MA(ticker)
    crossover(ticker)
    date_tracker(ticker)
main()


