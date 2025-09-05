import yfinance as yf

portfolio =['EA', 'GRMN', 'GIS', 'VLO', 'GS', 'BSX', 'UBER', 'FSLR', 'ECL', 'IRM', 'PNW']

def fetch_stock(ticker):
    stock_data = yf.download((ticker), start='2020-01-01', end='2025-01-01', auto_adjust=True)
    stock_data.dropna(inplace=True)
    return stock_data

def main(): 
    for stock in portfolio: 
        data = fetch_stock(stock)
        print(data)

main()