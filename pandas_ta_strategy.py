import pandas as pd
import pandas_ta as ta
import yfinance
# import talib
import vectorbt as vbt
import matplotlib.pyplot as plt
import numpy as np

# Write a script to generate
# - a buy signal for the stock (with order price, and timestamp) when the 50 DMA price of the stock crosses over the 200 DMA price of the stock from below and
# - a sell signal (with order price and timestamp) when 50 DMA  price of the stock crosses down 200 DMA price of the stock from above
#
# Once done, use eDMA in place of DMAs

df = pd.DataFrame()
df = df.ta.ticker("INFY.NS", period="5y")
df.ta.cores = 0

myStrategy = ta.Strategy(
    name="SMA200 SMA50 crossover",
    ta = [
        {"kind": "sma", "length": 200},
        {"kind": "sma", "length": 50}
    ]
)
df.ta.strategy(myStrategy)
df.ta.tsignals(df.SMA_50 > df.SMA_200, append=True)

plt.figure(figsize=(20,10))
plt.tick_params(axis='both', labelsize=14)
df.Close.plot(color='k',label="Close Price")
df.SMA_50.plot(color='b',label="SMA_50")
df.SMA_200.plot(color='g', label="SMA_200")
plt.plot(df[df.TS_Entries == 1].index,
         df["SMA_50"][df['TS_Entries'] == 1],
         '^',markersize=15,color='g',alpha=0.7,label='buy')
plt.plot(df[df.TS_Exits == 1].index,
         df["SMA_50"][df["TS_Exits"]==1],
         'v',markersize=15,color='r',alpha=0.7,label='sell')

plt.ylabel('Price',fontsize=16)
plt.xlabel('Date',fontsize=16)
plt.legend()
plt.grid
plt.show()


# Manually calculate signals: substitue tsignals and plot
# df["Signal"] = 0.0
# df["Signal"] = np.where(df["SMA_50"] > df["SMA_200"], 1.0, 0.0)
# df["Position"] = df["Signal"].diff()
# # plot 'buy' signals
# plt.plot(df[df['Position'] == 1].index,
#          df["SMA_50"][df['Position'] == 1],
#          '^', markersize = 15, color = 'g', alpha = 0.7, label = 'buy')
# # plot 'sell' signals
# plt.plot(df[df['Position'] == -1].index,
#          df["SMA_50"][df['Position'] == -1],
#          'v', markersize = 15, color = 'r', alpha = 0.7, label = 'sell')
