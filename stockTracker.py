import yfinance as yf
# import pandas as pd
# import time

ticker = "EVMN"
data = yf.download(ticker, start="2025-11-07", end="2025-11-08", interval="30m").tz_convert('America/New_York')
data['Time-EST'] = data.index.strftime("%I:%M %p")
data['% Change'] = (data['Close'] / data['Open']) * 100 - 100
data = data.round(2)

for index, row in data.iterrows():
    if (row['% Change'].item() > 1):
        print("Good time to buy! Change is ", row['% Change'].item(), "%")
    else:
        print("Don't Buy! Change is ", row['% Change'].item(), "%")

print(data[['Time-EST', 'Open', 'Close', '% Change']])
