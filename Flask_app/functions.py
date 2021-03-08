import os
import pandas as pd
from flask import Flask, render_template, redirect
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import create_engine


engine = create_engine(os.getenv("postgres_uri"))


#-----------------------------------------------------------

def get_data():
    query = '''select * from mentions_and_price'''
    price_mentions_data = pd.read_sql(query, engine)
    price_mentions_data.rename(columns={'Unnamed: 1':"Ticker"}, inplace=True)
    # new_df = price_mentions_data.set_index('Ticker').sort_index().sort_values(by=['Ticker','date'])
    new_df = price_mentions_data.sort_values(by=['Ticker','date'])
    new_df['Volume'] = new_df['Volume'].fillna(value=0)
    new_df = new_df.fillna(method='ffill')
    
    return new_df