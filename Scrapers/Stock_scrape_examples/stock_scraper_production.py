# import packages
import pandas as pd
import yfinance as yf # pip install yfinance
import datetime
import time
import requests
import io

# demo list of random stock tickers, will be populated with list of mentioned tickers from comments and submissions
tickers_list = ["aapl", "goog", "amzn", "BAC", "BA"] # example list

# define the paramaters of the search
start = datetime.datetime(2020,12,6)  # start time (first comment/submission date)
end = datetime.datetime(2022,2,6)   # end time (last comment/submission date)
interval = "60m"    # how often do we want prices (every hour)

# download and import all ticker data into a pd dataframe
df = pd.DataFrame(yf.download(tickers_list, start = start, end= end, interval=interval, group_by='tickers', index=False))

# export df to a csv in the Data folder
df.to_csv("Data/ticker_test.csv")