import yfinance as yf
import pandas as pd
import matplotlib_inline
import json
amd=yf.Ticker("AMD")
with open('amd.json') as json_file:
    amd_info = json.load(json_file)
    print("Type:", type(amd_info))
#print(amd_info)
print(amd_info['country'])
print(amd_info['sector'])
amd_share_price_data=amd.history(period='max')
#print(amd_share_price_data)
x=amd_share_price_data.head(1)
print(x.Volume)