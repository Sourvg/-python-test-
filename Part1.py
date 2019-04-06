1- # Lets define a function for moving average with rolling window

# Sklearn has seperate function to calculate this: [ DataFrame.rolling(window).mean() ].

def moving_average(series, n):
    """
        Calculate average of last n observations
        
        n - rolling window
    """
    return np.average(series[-n:])

'''
# We can also imlement this user-defined function. But, first we need to isolate both 'Date' and 'Close' columns
under consideration. After that, we need to resample according to week , using:

df.resample('W')

function. Then We will pass the 'Close' column as the 'series' argument to the custom built function.
And, n = rolling window size.


But: We are not doing that here to maintain simplicity in code.
"\n# We can also imlement this user-defined function. But, first we need to isolate both 'Date' and 'Close' columns\nunder consideration. After that, we need to resample according to week , using:\n\ndf.resample('W')\n\nfunction. Then We will pass the 'Close' column as the 'series' argument to the custom built function.\nAnd, n = rolling window size.\n\n\nBut: We are not doing that here to maintain simplicity in code.\n\n"
Let us calculate moving averages (closing price) for weeks = [4,16,28,40,52].
weeks = [4, 16, 28, 40, 52]
def indexing(stock):
    stock.index = stock['Date']
    return stock
    indexing(TCS)
indexing(INFY)
indexing(NIFTY)

def plot_time_series(stock, weeks = [4, 16, 28, 40, 52]):
    
    dummy = pd.DataFrame()
    # First Resampling into Weeks format to calculate for weeks
    dummy['Close'] = stock['Close'].resample('W').mean() 
     
    for i in range(len(weeks)):
        m_a = dummy['Close'].rolling(weeks[i]).mean() # M.A using inbuilt function
        dummy[" Mov.AVG for " + str(weeks[i])+ " Weeks"] = m_a
        print('Calculated Moving Averages: for {0} weeks: \n\n {1}' .format(weeks[i], dummy['Close']))
    dummy.plot(title="Moving Averages for {} \n\n" .format(stock.name))
    Table With Calculated Moving Average + plot for Moving averages for weeks = [4,16,28,40,52]
    plot_time_series(TCS)
    plot_time_series(INFY)
    plot_time_series(NIFTY)
    
    2- TCS = TCS.asfreq('D', method ='pad')        # pad-ffill : forward-fill
INFY = INFY.asfreq('D', method ='pad')
NIFTY = NIFTY.asfreq('D', method ='pad')


TCS.name = 'TCS'
INFY.name = 'INFY'
NIFTY.name = 'NIFTY_IT'
def plot_roll_win(stock, win = [10, 75]):
    
    dummy = pd.DataFrame()
    
    dummy['Close'] = stock['Close']
     
    for i in range(len(win)):
        m_a = dummy['Close'].rolling(win[i]).mean() # M.A using predefined function
        dummy[" Mov.AVG for " + str(win[i])+ " Roll Window"] = m_a
        print('Calculated Moving Averages: for {0} weeks: \n\n {1}' .format(win[i], dummy['Close']))
    dummy.plot(title="Moving Averages for {} \n\n" .format(stock.name))
plot_roll_win(TCS)
plot_roll_win(INFY)
plot_roll_win(NIFTY)

3. volume shocks:

def volume_shocks(stock):
    """
    'Volume' - Vol_t
    'Volume next day - vol_t+1
    
    """
    stock["vol_t+1"] = stock.Volume.shift(1)  #next rows value
    
    stock["volume_shock"] = ((abs(stock["vol_t+1"] - stock["Volume"])/stock["Volume"]*100)  > 10).astype(int)
    
    return stock
    volume_shocks(TCS)
volume_shocks(INFY)
volume_shocks(NIFTY)

Volume shock direction:

def direction_fun(stock):
    
    # considerng only shock - 1 valued rows.
    # 0 - negative and 1- positive
    if stock["volume_shock"] == 0:
        pass
    else:
        if (stock["vol_t+1"] - stock["Volume"]) < 0:
            return 0
        else:
            return 1
            def vol_shock_direction(stock):
    stock['VOL_SHOCK_DIR'] = 'Nan'
    stock['VOL_SHOCK_DIR'] = stock.apply(direction_fun, axis=1)
    return stock
    vol_shock_direction(TCS)
vol_shock_direction(INFY)
vol_shock_direction(NIFTY)

Price shocks:

def price_shocks(stock):
    """
    'ClosePrice' - Close_t
    'Close Price next day - vol_t+1
    
    """
    stock["price_t+1"] = stock.Close.shift(1)  #next rows value
    
    stock["price_shock"] = (abs((stock["price_t+1"] - stock["Close"])/stock["Close"]*100)  > 2).astype(int)
    
    stock["price_black_swan"] = stock['price_shock'] # Since both had same data anad info/
    
    return stock
    price_shocks(TCS)
price_shocks(INFY)
price_shocks(NIFTY)

Price Shock Direction and Black Swan shock direction (both same):
def direction_fun_price(stock):
    
    # considerng only shock - 1 valued rows.
    # 0 - negative and 1- positive
    if stock["price_shock"] == 0:
        pass
    else:
        if (stock["price_t+1"] - stock["Close"]) < 0:
            return 0
        else:
            return 1
            def price_shock_direction(stock):
    stock['PRICE_SHOCK_DIR'] = 'Nan'
    stock['PRICE_SHOCK_DIR'] = stock.apply(direction_fun_price, axis=1)
    return stock
    vol_shock_direction(TCS)
vol_shock_direction(INFY)
vol_shock_direction(NIFTY)

Price Shock w/o volume shocks:

def price_shock_wo_vol_shock(stock):
    
    stock["not_vol_shock"]  = (~(stock["volume_shock"].astype(bool))).astype(int)
    stock["price_shock_w/0_vol_shock"] = stock["not_vol_shock"] & stock["price_shock"]
    
    return stock
    price_shock_wo_vol_shock(TCS)
price_shock_wo_vol_shock(INFY)
price_shock_wo_vol_shock(NIFTY)




    
