import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import sqlite3 as sql

# 1. 建立與'data/raw/course.db'資料庫的連線
db_path = 'data/raw/course.db'
conn = sql.connect(db_path)

# 2.  SQL CTE 查詢 暫存表
query = """
--  計算單品實際營收，並直接按 order_id 聚合為「單筆訂單總金額」
WITH OrderTotals AS (
    --查看 order_id,與 line_revenue(需SUM計算) 欄位
    SELECT order_id,
    SUM(quantity*unit_price*(1-discount_rate)) AS line_revenue
    --來源資料表 order_items
    FROM order_items
    --依 order_id 分群
    GROUP BY order_id
),

-- 關聯訂單主表，過濾已完成訂單，並按 customer_id 聚合計算指標
CustomerMetrics AS (
    --查詢 o.customer_id,total_spent(SUM),order_count(COUNT)
    SELECT o.customer_id,
        -- 加總該顧客的所有訂單金額(ot.line_revenue) 欄位名稱 total_spent
            SUM(ot.line_revenue) AS total_spent ,
        -- 計算不重複的訂單數 (等同 nunique) 欄位名稱 order_count
            COUNT(DISTINCT ot.order_id) AS order_count
    --來源資料表 orders 別名 o
    FROM orders o
    --依上方 OrderTotals 資料表 別名 ot 依 o.order_id=ot.order_id 結合
    JOIN OrderTotals ot on o.order_id = ot.order_id
    --篩選 o.status='completed'
    WHERE o.status = 'completed'
    --依 o.customer_id 分群
    GROUP BY o.customer_id
)

--  最後合併顧客主表，取得 segment 等標籤
--查詢 cm.customer_id,cm.total_spent,cm.order_count,c.segment,c.city,c.acquisition_channel
 SELECT cm.customer_id,cm.total_spent,cm.order_count,c.segment,c.city,c.acquisition_channel
--來源資料表 CustomerMetrics 別名 cm
FROM CustomerMetrics cm
--依 cm.customer_id = c.customer_id 結合 customers資料表
JOIN customers c on cm.customer_id = c.customer_id

"""

# 3. 執行 SQL 並直接將結果轉換為 Pandas DataFrame
df_final = pd.read_sql_query(query,conn)

# 4. 關閉資料庫連線 (好習慣)
conn.close()

# 顯示前幾筆資料驗證結果
print(df_final.head())


# 3. 資料視覺化 (Data Visualization)

# 設定 Seaborn 背景樣式為白色網格 (whitegrid)
sns.set_theme(style='whitegrid')

#設定中文字型為 'Microsoft JhengHei'
plt.rcParams['font.sans-serif'] = 'Microsoft JhengHei'

# 建立畫布 figsize=(10, 6)
plt.figure(figsize=(10, 6))

# 繪製散佈圖 (Scatter Plot)
ax =sns.scatterplot(data=df_final,
    x='order_count',#x='order_count'
    y='total_spent',#y='total_spent'
    hue='segment',# 依據segment分群改變顏色
    style='segment',# 依據segment分群改變形狀 (讓辨識度更高)
    palette='hsv',# 使用鮮豔的色票 (bright 或 hsv)
    s=100,# 設定點的大小 100
    alpha=0.7,# 些微的透明度，避免點重疊時看不清
    edgecolor='White',   
    linewidth=1,# 白邊讓點看起來更有立體感
)


# 圖表標題 '顧客分群消費行為分析：總消費金額 vs 訂單數量'
plt.title('顧客分群消費行為分析：總消費金額 vs 訂單數量')
# x 軸標籤 '訂單數量 (次)'
plt.xlabel('訂單數量 (次)')
# y 軸標籤 '總消費金額 (元)'
plt.ylabel('總消費金額 (元)')
# 調整圖例位置，將其移至圖表右側，避免擋住數據
plt.legend(title='顧客分群', bbox_to_anchor=(1.05, 1), loc='upper left', fontsize=11, title_fontsize=12)

# 自動優化整體佈局
plt.tight_layout()

# 顯示圖表
plt.show()