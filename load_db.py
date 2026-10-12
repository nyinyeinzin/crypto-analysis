import sqlite3
import pandas as pd

conn = sqlite3.connect("crypto.db")

for coin in ["BTC", "ETH", "SOL"]:
    df = pd.read_csv(coin + "USDT.csv")
    df["coin"] = coin
    df.to_sql("prices", conn, if_exists="append", index=False)

print(pd.read_sql("SELECT coin, COUNT(*) AS days FROM prices GROUP BY coin", conn))
conn.close()
