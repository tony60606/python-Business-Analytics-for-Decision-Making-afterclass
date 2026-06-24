import pandas as pd


# 讀取了五個 DataFrame (orders, order_items, sessions, events, customers)
orders=pd.read_csv('data/raw/orders.csv')
order_items=pd.read_csv('data/raw/order_items.csv')
sessions=pd.read_csv('data/raw/sessions.csv')
events=pd.read_csv('data/raw/events.csv')
customers=pd.read_csv('data/raw/customers.csv')

duplicate_orders = orders["order_id"].duplicated().sum()
print(f'主鍵重覆數量:{duplicate_orders}')

orphan_items = (~order_items["order_id"].isin(orders["order_id"])).sum()
print(f'孤兒訂單數:{orphan_items}')

null_report = orders.isna().sum().sort_values(ascending=False).head()
print(f'orders資料表的空值欄位計數:\n{null_report}')

print("選擇偏誤檢查")
#選擇偏誤檢查 (Selection Bias Check)
# Selection bias check: compare traffic composition and conversion by device.
purchase_sessions = set(events.loc[events["event_type"] == "purchase",
"session_id"].tolist())
tmp = sessions.copy()
tmp["converted"] = tmp["session_id"].isin(purchase_sessions).astype(int)
print("device mix:")
print((tmp["device"].value_counts(normalize=True) * 100).round(2))
print("conversion by device:")
print(tmp.groupby("device")
["converted"].mean().sort_values(ascending=False).round(4))


print("="*30)
#時間邏輯與資料洩漏檢查 
# Time leakage check: purchase must happen after session_start.
starts = sessions[["session_id", "session_start"]].copy()
starts["session_start"] = pd.to_datetime(starts["session_start"])
purchases = events.loc[events["event_type"] == "purchase", ["session_id",
"event_time"]].copy()
purchases["event_time"] = pd.to_datetime(purchases["event_time"])
merged = purchases.merge(starts, on="session_id", how="left")
#統計有幾筆資料的「購買時間」竟然早於「工作階段開始時間」。
leakage_count = (merged["event_time"] < merged["session_start"]).sum()
print("time leakage rows (purchase before session_start):", int(leakage_count))