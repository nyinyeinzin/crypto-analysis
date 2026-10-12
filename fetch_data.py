import requests
import pandas as pd

coins = ["BTCUSDT", "ETHUSDT", "SOLUSDT"]
url = "https://api.binance.com/api/v3/klines"

for coin in coins:
    params = {"symbol": coin, "interval": "1d", "limit": 730}
    data = requests.get(url, params=params).json()
    df = pd.DataFrame(data).iloc[:, :6]
    df.columns = ["date", "open", "high", "low", "close", "volume"]
    df["date"] = pd.to_datetime(df["date"], unit="ms")
    df.to_csv(coin + ".csv", index=False)
    print(coin, len(df), "rows saved")
