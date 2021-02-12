# r/WallStreetBets Ticker Mentions Frequency Analysis


![](https://github.com/alainacox/Final_Project_WSB/blob/main/team%20(2).jpg)

​
## Project Overview

So, I missed jumping onto the GameStop waggon--what's the next craze? Given the sudden focus on the Reddit page r/WallStreetBets, everyone is weighing in with their two cents about the next big stock or crypto to cash in on across social media. But why not go to the ridiculous source of these shenanigans? <br />
This project's aim is to analyze the variations in frequency of specific stock mentions on the Reddit sub r/WallStreetBets to gain insights and visualize on the behavior of high profile tickers like GME. Moreover, the project aims to create a model that can analyze the sub's page to predict which tickers will next be affected by the masterminds of r/WallStreetBets by analyzing such features as frequency of mentions, upvotes of comments, mentions by popular contributors, and others. <br /> 
While trying to predict trends in something as dynamic as stock prices from such volatile medium has obvious limitations, the team hopes to clarify the confusion of what happened on Reddit simultaneously with the stock prices through visualizations with Plotly. <br /> <br />
**Minimum Viable Product**
<ol>
    <li> The body of Reddit comments will be analyzed for mentions of stock tickers. The frequency of mentions will be aggregated by day over the period of 1 December 2020 through 7 February 2021.</li>
    <li> Daily stock prices will be pulled for the most frequently mentioned tickers. Comment frequency will be compared to stock price trends over time.</li>
    <li> A ML model will use the comment frequency data to attempt to predict stock market price for the specific tickers and perform principle component analysis on the provided Reddit features and project-defined features. </li>
</ol> 

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

