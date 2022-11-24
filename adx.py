import yfinance as yf
import numpy as np

tickers = ["AMZN", "GOOG", "MFST"]
ohlcv_data = {}

for ticker in tickers:
    temp = yf.download(ticker, period='1mo', interval='5m')
    temp.dropna(how='any', inplace=True)
    ohlcv_data[ticker] = temp

def ADX(DP, n=20):
    df = DF.copy()
    df["upmove"] = df["High"] - df["High"].shift(1)
    df["downmove"] = df["Low"].shift(1) - df["Low"]
    df["+dm"] = np.where((df["upmove"] > df["downmove"]) & df["upmove"] > 0, df["upmove"], 0)
    df["-dm"] = np.where((df["downmove"] > df["upmove"]) & df["downmove"] > 0, df["downmove"], 0)