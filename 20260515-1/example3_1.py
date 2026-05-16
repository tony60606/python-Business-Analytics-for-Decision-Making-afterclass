import pandas as pd
orders = pd.read_csv("data/raw/orders.csv")
# 轉換前：order_date 是字串
print(orders["order_date"].dtype) # object（即字串）
# 轉換成 datetime
orders["order_date"] = pd.to_datetime(orders["order_date"])
print(orders["order_date"].dtype) # datetime64[ns]
# 轉換後可⽤ .dt 存取器提取⽇期元素
orders["order_year"] = orders["order_date"].dt.year # 年份
print(orders["order_year"].head())
print('='*30)
orders["order_month"] = orders["order_date"].dt.month # ⽉份（1~12）
print('='*30)
print(orders["order_month"].head())
print('='*30)
orders["order_dow"] = orders["order_date"].dt.dayofweek # 星期幾（0=週⼀）
print(orders["order_dow"].head())
print('='*30)
orders["order_week"] = orders["order_date"].dt.isocalendar().week # ISO 週次
print(orders["order_week"].head())
# 篩選 2025 年資料
orders_2025 = orders.loc[orders["order_year"] == 2025,['order_id','order_year']]
print('='*30)
print(orders_2025.head())
