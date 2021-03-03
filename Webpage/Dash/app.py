import os

import dash
import pandas as pd
import dash_core_components as dcc
import dash_html_components as html
import plotly.express as px
import dash_bootstrap_components as dbc
from dash.dependencies import Input, Output, State

test= ['test']
external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

server = app.server


df = pd.DataFrame(pd.read_csv('wsb_test_stock.csv'))

tickers = df['stock'].unique


tickers = df['stock'].unique()


app.layout =  html.Div([
    dcc.Dropdown(
        id='ticker_value',
        options=[{'label': i, 'value': i} for i in tickers],
        value='Choose a ticker'
        ),

    dcc.Graph(id='stock-graphic')
])


@app.callback(
Output('stock-graphic', 'figure'),
Input('ticker_value', 'value'),
)
def update_graph(ticker_value):
    df[df['stock'] == ticker_value]
    fig = px.scatter(x=df[df['stock'] == ticker_value]['mentions'],
                      y=df[df['stock'] == ticker_value]['price'])
    fig.update_xaxes(title='Mentions')

    fig.update_yaxes(title='Price')

    return fig

if __name__ == '__main__':
    app.run_server(debug=True)