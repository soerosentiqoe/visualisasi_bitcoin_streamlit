import streamlit as st
import pandas as  pd
import datetime
import plotly.graph_objects as go
from PIL import Image

st.write("""
#Cryptocurency Dashboard Appliaction
Visually show data on Crypto
""")
image=Image.open("D:/python/web/cryptodashboard/download.jpg")
st.image(image,use_column_width=True)
st.sidebar.header("user Input")

def get_input():
    start_date=st.sidebar.text_input("start date","2020-01-01")
    end_date=st.sidebar.text_input("start date","2022-01-01")
    crypto_symbol=st.sidebar.text_input("Crypto Simbol","BTC")
    return start_date,end_date,crypto_symbol

def get_crypto_name(symbol):
    symbol=symbol.upper()
    if symbol =="BTC":
        return "Bitcoin"
    elif symbol =="ETH":
        return "Ethereum"
    elif symbol =="DOGE":
        return "Dogecoin"
    else:
        return "None"

def get_data(symbol,start,end):
    symbol=symbol.upper()
    if symbol=="BTC":
        df =pd.read_csv("D:/python/web/cryptodashboard/BTC-USD.csv")
    elif symbol=="DOGE":
        df =pd.read_csv("D:/python/web/cryptodashboard/DOGE-USD.csv")
    elif symbol=="ETH":
        df =pd.read_csv("D:/python/web/cryptodashboard/ETH-USD.csv")
    else:
        df=pd.DataFrame(columns=["Date","Close","Open","Volume","Adj Close"])
    start=pd.to_datetime(start)
    end=pd.to_datetime(end)

    df=df.set_index(pd.DatetimeIndex(df['Date'].values))

    return df.loc[start:end]

start,end,symbol=get_input()
df=get_data(symbol,start,end)
crypto_name=get_crypto_name(symbol)

fig = go.Figure(
    data=[go.Candlestick(
        x=df.index,
        open=df["Open"],
        high=df["High"],
        low=df["Low"],
        close=df["Close"],
        increasing_line_color='green',
        decreasing_line_color='red'
    )]
)

st.header(crypto_name+" Data ")
st.write(df)
st.header(crypto_name +" data statistic")
st.write(df.describe())
st.header(crypto_name +" close Price")
st.line_chart(df['Close'])
st.header(crypto_name +" Volume")
st.bar_chart(df.describe())
st.header(crypto_name +" candle stick")
st.plotly_chart(fig)

