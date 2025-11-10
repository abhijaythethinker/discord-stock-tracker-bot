import yfinance as yf

def get_percent_changes(ticker):

    # ticker
    data = yf.download(ticker, period="1d", interval="30m", auto_adjust=False, progress=False).tz_convert('America/New_York')

    if data.empty:
        return None
    
    data['Time-EST'] = data.index.strftime("%I:%M %p")

    open_price = data.iloc[0]

    # calculate percent
    data['% Change'] = (data['Close'] / open_price['Open']) * 100 - 100
    data = data.round(2)

    latest = data.iloc[-1]

    open_price = float(open_price['Open'].iloc[0])
    close_price = float(latest['Close'].iloc[0])
    percent_change = float(latest['% Change'].iloc[0])
    time_str = str(latest['Time-EST'].iloc[0])

    message = (
        f"**{ticker} Stock Update**\n"
        f"Time: {time_str}\n"
        f"% Change: {percent_change:.2f}%\n"
        f"Open: ${open_price:.2f}\n"
        f"Close: ${close_price:.2f}\n"
    )
    return message

# result = get_percent_changes()
# print(result)
