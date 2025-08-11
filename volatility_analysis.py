import yfinance as yf
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Parameters
ticker = "AAPL"  # Stock ticker
start_date = "2023-01-01"
end_date = "2024-01-01"
window = 20  # Rolling window size in days

# Fetch data
data = yf.download(ticker, start=start_date, end=end_date)

# Calculate daily returns
data['Daily Return'] = data['Adj Close'].pct_change()

# Calculate rolling volatility
data['Volatility'] = data['Daily Return'].rolling(window).std() * np.sqrt(window)

# Plot Closing Price
plt.figure(figsize=(12, 6))
plt.subplot(2, 1, 1)
plt.plot(data['Adj Close'], label=f"{ticker} Closing Price")
plt.title(f"{ticker} Stock Price")
plt.legend()

# Plot Volatility
plt.subplot(2, 1, 2)
plt.plot(data['Volatility'], label="Rolling Volatility", color='red')
plt.title(f"{ticker} {window}-Day Rolling Volatility")
plt.legend()

plt.tight_layout()
plt.show()
