import pandas as pd
import sqlite3 as sql
query="""
-- 暫存表名稱 customer_rev
WITH customer_rev AS (
    --查詢 o.customer_id
    SELECT o.customer_id,
    --查詢 total_rev 欄位內容 單價*數量*折扣
    SUM(oi.quantity*oi.unit_price*(1-oi.discount_rate)) AS total_rev
    --從 orders 別名 o
    FROM orders o
    --以 order_id 欄位 結合 order_items 資料表 別名　oi
    JOIN order_items oi on o.order_id = oi.order_id
    --篩選 status='completed'
    WHERE status = 'completed'
    --針對customer_id 分群
    GROUP BY customer_id
),

--第二層 結合顧客資料並計算各自的排名 暫存表名稱 ranked_customers
ranked_customers AS (
    --查詢 c.customer_id,c.segment
    SELECT c.customer_id,
           c.segment,
    --針對total_rev 小數取二位
           ROUND(total_rev,2) AS total_rev ,
    --利用窗口函式RANK排名 欄位名稱 rank_in_segment 依 c.segment分群,cr.total_rev 遞減排序
           RANK() OVER (PARTITION BY c.segment ORDER BY cr.total_rev DESC) AS rank_in_segment
    --從 customer_rev 別名 cr
    FROM customer_rev cr
    --以 customer_id 欄位結合 customers 資料表 別名 c
   JOIN customers c on c.customer_id = cr.customer_id
)
   --主查詢 針對排名進行篩選
SELECT * FROM ranked_customers
   --每個客群只抓前三名
WHERE rank_in_segment <=3
   --針對segment,rank_in_segment排序
ORDER BY segment,rank_in_segment

"""
with sql.connect('data/raw/course.db') as conn:
    result=pd.read_sql_query(query,conn)
    print(result)