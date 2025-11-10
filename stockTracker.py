import yfinance as yf
def get_percent_changes():

    ticker = "EVMN"
    data = yf.download(ticker, period="1d", interval="30m", auto_adjust=False, progress=False).tz_convert('America/New_York')

    if data.empty:
        return None
    
    data['Time-EST'] = data.index.strftime("%I:%M %p")

    data['% Change'] = (data['Close'] / data['Open']) * 100 - 100
    data = data.round(2)

    latest = data.iloc[-1]

    return latest

result = get_percent_changes()
print(result)
