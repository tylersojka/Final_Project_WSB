import pandas as pd

# create df from the list of top mentioned non word tickers from the comment and post datasets
ticker_list = pd.read_csv("../Data/non_word_tickers.csv")

# drop all tickers mentioned less than 100X
ticker_list = ticker_list[ticker_list["count"] >= 100]

# drop weird ticker named "0" 
ticker_list = ticker_list[ticker_list["0"] != "0"]

# rename column "0" to tickers
ticker_list['Tickers'] = ticker_list["0"]

# drop count and old column 0
ticker_list = ticker_list.drop(["count", "0"],1)

# read in the list of shorted tickers to combine with ticker list
shorted_list = pd.read_csv("../Data/shorted_tickers.csv")

# combine ticker list and the shorted list 
final_ticker_list = shorted_list.append(ticker_list)

# save to csv
final_ticker_list.to_csv("../Data/final_ticker_list.csv", index=False)