import yfinance as yf

def get_percent_changes(ticker):

    # ticker
    data = yf.download(ticker, period="1d", interval="30m", auto_adjust=False, progress=False).tz_convert('America/New_York')

    if data.empty:
        return None
    
    data['Time-EST'] = data.index.strftime("%I:%M %p")

    data['% Change'] = (data['Close'] / data['Open']) * 100 - 100
    data = data.round(2)

    latest = data.iloc[-1]

    open_price = float(latest['Open'].iloc[0])
    close_price = float(latest['Close'].iloc[0])
    percent_change = float(latest['% Change'].iloc[0])
    time_str = str(latest['Time-EST'].iloc[0])

    message = (
        f"**{ticker} Stock Update**\n"
        f"Time: {time_str}\n"
        f"% Change: {percent_change}%\n"
        f"Open: ${open_price}\n"
        f"Close: ${close_price}\n"
    )
    return message

# result = get_percent_changes()
# print(result)
