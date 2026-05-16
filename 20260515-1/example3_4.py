import pandas as pd
# 步驟 1：讀取 orders
orders = pd.read_csv("data/raw/orders.csv")
# 步驟 2：轉換⽇期
orders["order_date"] = pd.to_datetime(orders["order_date"])
completed_2025 = orders.loc[
(orders["order_date"].dt.year == 2025) & (orders["status"] == "completed")]
completed_2025["order_month"] = completed_2025["order_date"].dt.to_period("M")
monthly_counts = completed_2025.groupby("order_month").size()
print(monthly_counts)

### 練習 依照年份與付款方式分組計算總數
orders['year'] = orders['order_date'].dt.year
payment = orders.groupby(['year','payment_type']).size()
print(payment)