import yfinance as yf

portfolio =['EA', 'GRMN', 'GIS', 'VLO', 'GS', 'BSX', 'UBER', 'FSLR', 'ECL', 'IRM', 'PNW']

for stocks in portfolio: 
    ticker = yf.download((stocks), period='1mo', auto_adjust=True)

