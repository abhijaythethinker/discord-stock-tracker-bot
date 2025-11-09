import yfinance as yf
import time
def get_percent_changes(data):

    data['% Change'] = (data['Close'] / data['Open']) * 100 - 100
    data = data.round(2)
    data = data.iloc[-1]

    return data

ticker = "EVMN"
data = yf.download(ticker, period="1d", interval="30m").tz_convert('America/New_York')
data['Time-EST'] = data.index.strftime("%I:%M %p")
processed = get_percent_changes(data)
print(processed)

# print(data[['Time-EST', 'Open', 'Close', '% Change']])
