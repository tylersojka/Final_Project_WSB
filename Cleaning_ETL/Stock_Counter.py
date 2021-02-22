
#import dependencies

import boto3
import pandas as pd
import re

#Connect to boto3 client
client = boto3.client('s3')

#Create S3 bucket path variable.
path = "s3://wsb-final-project-bucket/kaggle_wsb_posts_12:6-2:6.csv"

#Read in data.
df = pd.read_csv(path)


#Create title dataframe as a series.
title_df = pd.Series(df['title'])

#Download tickers csv.
tickers = pd.read_csv("https://media.githubusercontent.com/media/tylersojka/Final_Project_WSB/main/Data/tickers.csv", header=None)

#Regex out commas and 0's in Tickers csv.
tickers = tickers.replace(',','', regex=True)
tickers = tickers.replace('0', '', regex=True)


#Create title_df
titles_df = df['title']

#Create variables to track tickers and the number of mentions.
ticker_names = []
ticker_counts = []

#Get list of tickers for the for loop
tickers_list = tickers[0].to_list()

#Iterate through tickers and readd the submissions for mentions of tickers. Regex searching for Ticker Name with whitespace on either side.
for ticker in tickers_list:
    count = titles_df.str.contains(rf"\s({ticker})\s", flags=re.IGNORECASE, regex=True).sum()
    ticker_names.append(ticker)
    ticker_counts.append(count)


#Make new dataframe with ticker names
stocks_df3 = pd.DataFrame(ticker_names, columns=['Ticker Name'])


#Add the count to the dataframe.
stocks_df3['Ticker Count'] = ticker_counts

#Save as new csv
stocks_df3.to_csv(path_or_buf='/Users/gregfinin/Project/stocks_df_final.csv',index=False)

#Check data to see top mentions.
stocks_df3.sort_values(by='Ticker Count', ascending=False)






