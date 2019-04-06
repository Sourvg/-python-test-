 adj_close_px = aapl['Adj Close']
moving_avg = adj_close_px.rolling(window=40).mean()
print(moving_avg[52:])
