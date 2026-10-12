import sqlite3
import pandas as pd

conn = sqlite3.connect("crypto.db")
df = pd.read_sql("SELECT coin, date, close FROM prices ORDER BY date", conn)

# daily change in percent, for each coin
df["daily_change"] = df.groupby("coin")["close"].pct_change() * 100

summary = df.groupby("coin").agg(
    risk=("daily_change", "std"),
    avg_day=("daily_change", "mean"),
)

first = df.groupby("coin")["close"].first()
last = df.groupby("coin")["close"].last()
summary["total_return"] = (last / first - 1) * 100

print(summary.round(2))