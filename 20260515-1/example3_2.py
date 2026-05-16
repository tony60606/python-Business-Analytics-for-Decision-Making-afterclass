import pandas as pd
#篩選 2025 年完成訂單
# 步驟 1：讀取 orders
orders = pd.read_csv("data/raw/orders.csv")
# 步驟 2：轉換⽇期
orders["order_date"] = pd.to_datetime(orders["order_date"])
# 步驟 3：篩選
completed_2025 = orders.loc[
(orders["order_date"].dt.year == 2025) & (orders["status"] == "completed")
]
print(completed_2025[['order_date','status']].head(20))
print("="*30)
print(f"2025 年完成訂單數：{len(completed_2025):,}")
print("="*30)
## 篩選 2025 上半年的退款訂單,查看 order_id,order_date,status,只看前30筆記錄
refunded = orders.loc[(orders['order_date'].dt.year==2025)&(orders['order_date'].dt.month <= 6)&(orders['status']=='refunded'),['order_id','order_date','status']].head(30)
print(f'上半年度退款\n{refunded}')