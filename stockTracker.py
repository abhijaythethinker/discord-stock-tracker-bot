import yfinance as yf

ticker = yf.Ticker("SPY")
spy_price = ticker.history(period='1d', interval='30m')

print(spy_price)

