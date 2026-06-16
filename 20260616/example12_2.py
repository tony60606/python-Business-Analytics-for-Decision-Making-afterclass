import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import sqlite3 as sql

##各客群與不同裝置之平均營收對比


#中文字型設定為 'Microsoft JhengHei' ,Mac 請改為 'PingFang TC'
plt.rcParams['font.family'] ='Microsoft JhengHei'
#負值設定
plt.rcParams['axes.unicode_minus'] = False
# 連線至 SQLite 資料庫 'data/raw/course.db'---
conn= sql.connect('data/raw/course.db')
#  SQL 查詢 CTE ---
query = """
WITH 
-- Step 1: 計算每一筆明細的營收，並按訂單加總 (對應 order_revenue)
OrderRevenue AS (
    --查詢 order_id,line_revenue(SUM)二個欄位
    SELECT order_id,
            SUM(quantity*unit_price*(1-discount_rate)) AS line_revenue
    --資料來源 order_items 資料表
    FROM order_items
    --依order_id 分群
    GROUP BY order_id
),

-- 為每位客戶的連線紀錄依照時間 (session_start) 進行排序打上流水號 (rn)
CustomerDeviceRanked AS (
    --查詢 customer_id,device,rn(利用窗口函數 依 customer_id分群,依 session_start遞增排序)
    SELECT customer_id,device,
    ROW_NUMBER() OVER (PARTITION BY customer_id ORDER BY session_start ASC) AS rn
    --資料來源 sessions 資料表
    FROM sessions
),

-- 取出每位客戶的裝置紀錄 (rn = 1)，避免資料膨脹
CustomerFirstDevice AS (
    --查詢 customer_id,device 欄位
   SELECT customer_id,device
    
    --資料來源 CustomerDeviceRanked暫存表
    FROM CustomerDeviceRanked

    --篩選 rn=1
    WHERE rn=1
)

-- 主查詢 - 串聯所有資料，並計算平均營收

--查詢 c.segment,cd.device,line_revenue(AVG(orv.line_revenue))
SELECT c.segment,cd.device,
        AVG(orv.line_revenue) AS line_revenue
--資料來源 orders資料表 別名 o
FROM orders o
-- 篩選已完成訂單，並 Inner Join 訂單營收

--INNER JOIN OrderRevenue 依 order_id 別名為 orv 
INNER JOIN OrderRevenue orv on o.order_id = orv.order_id
-- Left Join customers 資料表 依 customer_id 別名為 c
LEFT JOIN customers c on o.customer_id = c.customer_id

-- Left Join CustomerFirstDevice 表取得裝置 依 customer_id 別名 cd
LEFT JOIN CustomerFirstDevice cd on o.customer_id = cd.customer_id

-- 篩選 o.status='completed'
WHERE o.status = 'completed'
--針對 c.segment與 cd.device 分群
GROUP BY c.segment,cd.device
"""

# --- 3. 執行 SQL 查詢並載入為 Pandas DataFrame ---
analysis_df = pd.read_sql_query(query,conn)

# 關閉資料庫連線
conn.close()

# 檢查一下結果
print(analysis_df.head().round(2))

# 設定圖表大小為 10,6
fig,ax=plt.subplots(figsize=(10,6))
# 繪製圖表 data=analysis_df,x="segment",y="line_revenue",hue="device",palette="muted",edgecolor="white"
ax = sns.barplot(data=analysis_df,x="segment",y="line_revenue",hue="device",palette="muted",edgecolor="white")

#加上資料表標籤
for container in ax.containers:
    ax.bar_label(container,fmt='%.0f',padding=3,fontsize=12,color='green')# fmt='%.0f' 將數值轉為整數，padding=3 讓數字稍微懸浮於柱體上方

plt.title("各客群與不同裝置之平均營收對比", fontsize=16, fontweight="bold", pad=20)
plt.xlabel("客群分類 (Segment)", fontsize=12, labelpad=10)
plt.ylabel("平均營收（元）", fontsize=12, labelpad=10)


#設定格線與圖例
plt.grid(axis="y", linestyle="--", alpha=0.4)
plt.legend(title="使用裝置", loc="upper left", bbox_to_anchor=(1, 1))

plt.tight_layout()
plt.show()