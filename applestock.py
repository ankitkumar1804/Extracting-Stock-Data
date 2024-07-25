import yfinance as yf
import pandas as pd
import matplotlib_inline
import json
apple=yf.Ticker("AAPL")
with open('apple.json') as json_file:
    apple_info = json.load(json_file)
    print("Type:", type(apple_info))
#print(apple_info)
print(apple_info['country'])
apple_share_price_data = apple.history(period="max")
#print(apple_share_price_data)
#print(apple.info)
#print(apple_share_price_data.head(100))
apple_share_price_data.reset_index(inplace=True)
#print(apple_share_price_data)

z= apple_share_price_data.plot(x='Date', y='Open')
#print(z)
print(apple.dividends)
print(apple.dividends.plot)