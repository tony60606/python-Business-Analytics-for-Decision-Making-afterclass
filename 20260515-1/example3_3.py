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
completed_2025["order_month"] = completed_2025["order_date"].dt.to_period("M")
# to_period("M") 會產⽣如 2025-01, 2025-02 的⽉份標記
print(completed_2025["order_month"])

##產生一個 order_m_d欄位 顯示格式為 ?月?日
completed_2025['order_m_d'] = completed_2025["order_date"].dt.strftime('%m月%d日')
completed_2025["order_week"] = completed_2025["order_date"].dt.day_of_week
completed_2025['iso'] = completed_2025["order_date"].dt.isocalendar().week
completed_2025.to_csv('ok.csv')