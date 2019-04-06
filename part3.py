import pandas as pd
from pandas import datetime
import numpy as np

import seaborn as sns

import matplotlib
import matplotlib.pyplot as plt
%matplotlib inline
path = 'E:/GitHub_Project_upload/done/python-test/'

TCS = pd.read_csv(path + 'tcs_stock.csv', parse_dates=['Date'])

INFY = pd.read_csv(path + 'infy_stock.csv', parse_dates=['Date'])

NIFTY = pd.read_csv(path + 'nifty_it_index.csv', parse_dates=['Date'])


stocks = [TCS, INFY, NIFTY]


TCS.name = 'TCS'
INFY.name = 'INFY'
NIFTY.name = 'NIFTY_IT'
TCS["Date"] = pd.to_datetime(TCS["Date"])
INFY["Date"] = pd.to_datetime(INFY["Date"])
NIFTY["Date"] = pd.to_datetime(NIFTY["Date"])
# data extraction


def features_build(df):
    df['Date'] = pd.to_datetime(df['Date'])
    df['Year'] = df['Date'].dt.year
    df['Month'] = df.Date.dt.month
    df['Day'] = df.Date.dt.day
    df['WeekOfYear'] = df.Date.dt.weekofyear
    
    
    
for i in range(len(stocks)):
    # print(stocks[i])
    features_build(stocks[i])

TCS.shape
