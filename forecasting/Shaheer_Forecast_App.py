import pandas as pd
import streamlit as st
import yfinance as yf
from plotly import graph_objs as go

from datetime import datetime

start = '2015-01-01'
today = datetime.today().strftime("%Y-%m-%d")

st.title("Stock Prediction App")

stocks = ("AAPL","GOOG","MSFT","TSLA","META")
selected_stock = st.selectbox("Select dataset for prediction", stocks)

n_years = st.slider("Days of prediction: ", 1, 90)

@st.cache_data
def load_data(ticker):
    data = yf.download(ticker, start, today)
    data.reset_index(inplace=True)
    return data

data_load_state = st.text("Loading data...")
data = load_data(selected_stock)
data_load_state.text("Data load completed...")

st.subheader("Raw data")
st.write(data.head())

def plot_data():
    fig = go.Figure()
    fig.add_trace(go.Scatter(x=data['Date'], y=data['Open'], name='Open', line=dict(color='blue')))
    fig.add_trace(go.Scatter(x=data['Date'], y=data['Close'], name='Close', line=dict(color='red')))
    fig.layout.update(title_text="Stock Price Data", xaxis_rangeslider_visible=True, yaxis_title='Price in USD')
    st.plotly_chart(fig)

plot_data()