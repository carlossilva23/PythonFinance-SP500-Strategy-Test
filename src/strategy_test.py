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
    ticker_data['Prev Bool'] = ticker_data['Switch'].shift(1)
    

def date_tracker(ticker_data): 
    buy_signal = ticker_data[(ticker_data['Prev Bool'] == True) & (ticker_data['Switch'] == False)]
    sell_signal = ticker_data[(ticker_data['Prev Bool'] == False) & (ticker_data['Switch'] == True)]
    print(buy_signal.index)
    print(sell_signal.index)


def main(): 
    ticker = yf.download('PNW', period='1y', auto_adjust=True)
    calculate_short_MA(ticker)
    calculate_long_MA(ticker)
    crossover(ticker)
    date_tracker(ticker)
main()


