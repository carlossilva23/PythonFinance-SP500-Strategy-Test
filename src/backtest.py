import matplotlib.pyplot as plt
import yfinance as yf
import strategy_test

ticker = yf.download('EA', period='5y', auto_adjust=True)
strategy_test.calculate_short_MA(ticker)
strategy_test.calculate_long_MA(ticker)
strategy_test.crossover(ticker)

plt.plot(ticker['Close'], label='Price')
plt.plot(ticker['Short MA'], label='Short MA')
plt.plot(ticker['Long MA'], label='Long MA')

plt.xlabel("Date")
plt.ylabel("Stock Price")
plt.title("Stock Average Crossover")
plt.legend()
plt.grid(True)
plt.show()