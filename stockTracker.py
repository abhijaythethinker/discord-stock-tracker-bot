import yfinance as yf
import time

def get_percent_changes(data):

    data['% Change'] = (data['Close'] / data['Open']) * 100 - 100
    data = data.round(2)

    for _, row in data.iterrows():
        if (row['% Change'].item() > 1):
            print(row['Time-EST'].item(), ": Good time to buy! Change is ", row['% Change'].item(), "%")
        else:
            print(row['Time-EST'].item(), ":Don't Buy! Change is ", row['% Change'].item(), "%")

    return data

ticker = "EVMN"
data = yf.download(ticker, period="1d", interval="30m").tz_convert('America/New_York')
data['Time-EST'] = data.index.strftime("%I:%M %p")
processed = get_percent_changes(data)


data = data.round(2)

print(data[['Time-EST', 'Open', 'Close', '% Change']])
