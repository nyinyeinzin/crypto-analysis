import sqlite3
import pandas as pd
import matplotlib.pyplot as plt

conn = sqlite3.connect("crypto.db")
df = pd.read_sql("SELECT coin, date, close FROM prices ORDER BY date", conn)
df["date"] = pd.to_datetime(df["date"])

# turn each coin's price into "growth since day 1" (starts at 100)
df["growth"] = df.groupby("coin")["close"].transform(lambda x: x / x.iloc[0] * 100)

for coin, data in df.groupby("coin"):
    plt.plot(data["date"], data["growth"], label=coin)

plt.title("BTC vs ETH vs SOL: growth of 100 over 2 years")
plt.ylabel("Value (start = 100)")
plt.legend()
plt.savefig("growth_chart.png")
print("chart saved")