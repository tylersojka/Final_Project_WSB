# r/WallStreetBets Ticker Mentions Frequency Analysis


![](Images/team%20(2).jpg)

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

- Reddit post and comment dataset
  - Pushshift API and pmaw python library. According to reddits API rules "Clients connecting via OAuth2 may make up to 60 requests per minute." This, however, was far to limiting for what we hoped accomplish. We needed another option to obtain mass amounts of post and comment data which lead us to Pushshift. 
  
    Pushshift is a big-data storage and analytics project started and maintained by Jason Baumgartner (/u/Stuck_In_the_Matrix). Most people know it for its copy of reddit comments and submissions. Essentially, Pushshift is an enormous database of comment and post objects, gathered in near real time as they appear on reddit. Pushshift provides an API to access this database, however, it too was even too slow for what we needed. 
    
    [PMAW](https://pypi.org/project/pmaw/) is self described as "an ultra minimalist wrapper for the Pushshift API which uses multithreading to retrieve Reddit comments and submissions. General usage is through the PushshiftAPI class which provides methods for interacting with different Pushshift endpoints." We obtained a set of posts, totaling ~800k posts, in about 2 days of run time. The comment dataset, based on the entire comment tree from each of the posts was then started. After about 5 days of running, the script was still not done. Lucky for us though, a member of reddit posted the exact dataset we were after, minus 3 days. 
    
    This dataset was pulled down from [kaggle](https://www.kaggle.com/mattpodolak/rwallstreetbets-posts-and-comments?select=wallstreetbets_posts.csv). The dataset contains all posts and comments from r/WallStreetBets from December 6, 2020 - February 6, 2021. The post dataset is roughly 700k rows and 80 columns, many of which will be dropped due to near 100% null values. The comment dataset is similar in width, but over 8 million rows. The row count, however, includes an extremely high percentage of "deleted" comments, comments that were deleted for whatever reason, but a placeholder of "deleted" was left behind for Pushshift to consume. After dropping these essentially null rows, we should be left with roughly half the original length. 
- Daily / Hourly stock prices
  -  Stock prices at open, close, etc. for specified stock tickers from the comment frequency analysis will be pulled from Yahoo Finance using the [yfinance](https://pypi.org/project/yfinance/) python library. yfinance provides a reliable, threaded, and Pythonic way to download historical market data from Yahoo! finance.
- Stock ticker list
  - A list of the most shorted stock tickers were scraped from [marketwatch](https://www.marketwatch.com/tools/screener/short-interest). These were selected because we needed to narrow down our stock ticker list to speed up the ETL process.
  - A longer list of all stock tickers was assembled from different sources. 

​
## Technology

1. Create and maintain database with Postgres via AWS.

2. ETL process will be carried out through Pandas Python and PySpark. 

3. Comment frequency analysis will be done in Python. 

4. Data Visualizations will be designed in Python's Matplotlib and JavaScript's Plotly.

5. A webapp will be hosted through Heroku.
​
## Communication

The group collaborates through Trello, Slack, and Zoom and Google Slides. 

## Presentation Boards 

[Slides](https://docs.google.com/presentation/d/1CnO_A2UGeZOWkdU0uxEbxQvIrU6RGEWmLszjNCRB4ic/edit#slide=id.gbcecd73ff9_0_5)


