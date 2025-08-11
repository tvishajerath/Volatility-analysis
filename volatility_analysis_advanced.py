import yfinance as yf
import pandas as pd
import matplotlib.pyplot as plt

# Multiple stocks
tickers = ["AAPL", "MSFT", "GOOGL"]
start_date = "2023-01-01"
end_date = "2023-12-31"

# Download data
data = yf.download(tickers, start=start_date, end=end_date)['Adj Close']

# Calculate daily returns
returns = data.pct_change()

# Calculate annualized volatility
volatility = returns.std() * (252**0.5)
print("Annualized Volatility (%):")
print((volatility * 100).round(2))

# Plot volatility comparison
plt.figure(figsize=(8, 5))
volatility.plot(kind='bar', title="Annualized Volatility Comparison (%)")
plt.ylabel("Volatility (%)")
plt.grid(axis='y')
plt.savefig("charts/multi_stock_volatility.png")  # Save for GitHub
plt.show()
