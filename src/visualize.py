import matplotlib.pyplot as plt
import yfinance as yf
import calculate_data

ticker = yf.download('EA', period='5y', auto_adjust=True)
calculate_data.calculate_short_MA(ticker)
calculate_data.calculate_long_MA(ticker)
calculate_data.crossover(ticker)

plt.plot(ticker['Close'], label='Price')
plt.plot(ticker['Short MA'], label='Short MA')
plt.plot(ticker['Long MA'], label='Long MA')

plt.xlabel("Date")
plt.ylabel("Stock Price")
plt.title("Stock Average Crossover")
plt.legend()
plt.grid(True)
plt.show()