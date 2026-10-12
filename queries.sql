SELECT coin, MAX(close) FROM prices GROUP BY coin;
select coin, count(date) from prices where close > open group by coin;
select coin, max((close - open) * 100.0 / open) from prices group by coin;