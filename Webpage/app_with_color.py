import os

import dash
import pandas as pd
import dash_core_components as dcc
import dash_html_components as html
import plotly.express as px
import dash_bootstrap_components as dbc
from dash.dependencies import Input, Output, State

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

server = app.server

colors = {
    'background': '#111111',
    'text': '#7FDBFF'
}

df = pd.DataFrame(pd.read_csv('tickers_mentions_total_2.csv'))

tickers = df['stocks'].unique


tickers = df['stocks'].unique()

app.layout =  html.Div(style={'backgroundColor': colors['background']}, children=[
    html.H1(
        children='WSB Final Project',
        style={
            'textAlign': 'center',
            'color': colors['text']
        }
    ),

    html.Div(children='A project that looks at stock price and mentions from the subreddit WallStreetBets.', style={
        'textAlign': 'center',
        'color': colors['text']
    }),

    dcc.Graph(id='stock-graphic'),

    dcc.Dropdown(
        id='ticker_value',
        options=[{'label': i, 'value': i} for i in tickers],
        value='Choose a ticker',
        searchable = True
        )
])


@app.callback(
Output('stock-graphic', 'figure'),
Input('ticker_value', 'value'),
Input('day--slider', 'value'))
def update_graph(ticker_value):
    df[df['stocks'] == ticker_value] 
    fig = px.scatter(x=df[df['stocks'] == ticker_value]['mentions'],
                      y=df[df['stocks'] == ticker_value]['price']
    )
    fig.update_xaxes(title='Mentions')

    fig.update_layout(
    plot_bgcolor=colors['background'],
    paper_bgcolor=colors['background'],
    font_color=colors['text'])



    fig.update_yaxes(title='Price')

    return fig

if __name__ == '__main__':
    app.run_server(debug=True)