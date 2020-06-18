from alpha_vantage.timeseries import TimeSeries
import pandas as pd
from sklearn import preprocessing
import numpy as np

def save_data(symbol):
    API_KEY = 'DTJYUMAWMLMQYLRB'

    ts = TimeSeries(key=API_KEY, output_format='pandas')
    # Get json object with the intraday data and another with  the call's metadata
    data, meta_data = ts.get_daily(symbol, outputsize='full')
    data.to_csv(f'./{symbol}_daily.csv')

def load_data(symbol):
    data = pd.read_csv(f'./{symbol}_daily.csv')
    return data
