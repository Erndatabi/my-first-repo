import yfinance as yf
import pandas as pd

# 定義想睇嘅資產：標普500, 黃金, 美國十年期債息
assets = {
    'SPY': 'S&P 500 ETF',
    'GC=F': 'Gold Futures',
    '^TNX': 'US 10Y Treasury Yield'
}

print("正在抓取數據...")

# 抓取最近 5 日嘅收市價
data = yf.download(list(assets.keys()), period='5d')['Close']

# 重新命名等佢易睇啲
data.columns = [assets[col] for col in data.columns]

print("\n--- 最近 5 日跨資產數據 ---")
print(data)

# 儲存成 CSV 方便入 Excel 睇
data.to_csv('fund_data.csv')
print("\n成功！數據已儲存至 fund_data.csv")