# r/WallStreetBets Ticker Mentions Frequency Analysis
​
## Project Overview
Given the sudden focus on the Reddit page r/WallStreetBets, the project seeks to analyze the variations in frequency of specific stock mentions compared to those stock's prices over time. <br /> <br />
**Minimum Viable Product**
<ol>
    <li> The body of Reddit comments will be analyzed for mentions of stock tickers. The frequency of mentions will be aggregated by day over the period of 1 December 2020 through 7 February 2021.</li>
    <li> Daily stock prices will be pulled for the most frequently mentioned tickers. Comment frequency will be compared to stock price trends over time.</li>
    <li> A ML model will use the comment frequency data to attempt to predict stock market price for the specific tickers and perform principle component analysis on the provided Reddit features and project-defined features. </li>
</ol> 
​
## Data Sources
- Reddit API--web scraping comments from r/WallStreetBets from 1 Dec 2020 thru 7 Feb 2021: https://pypi.org/project/pmaw/
- InterStock Data API--pulling stock prices at open, close, etc. for specified stock tickers from the comment frequency analysis
​
## Technology
1. Create and maintain database with Postgres via AWS.
2. ETL process will be carried out through Pandas Python and PySpark. 
3. Comment frequency analysis will be done in Python. 
4. Data Visualizations will be designed in Python's Matplotlib and JavaScript's Plotly.
5. A webapp will be hosted through Heroku.
​
## Communication
The group will collaborate through Trello and Zoom. 
