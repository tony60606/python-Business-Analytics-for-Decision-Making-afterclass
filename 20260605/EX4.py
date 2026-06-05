import pandas as pd
import sqlite3 as sql

## 1. 建立 course.db 連線
conn=sql.connect('data/raw/course.db')
query1="""
--建立 daily 暫存表
WITH daily AS (
    SELECT
    --查詢日期欄位(字串前10個字) 別名為 d
    substr(order_date,1,10) AS d ,
    --計算每日營收(品項層級加總的日層級)
    ROUND(SUM(CAST(oi.quantity AS REAL)*CAST(oi.unit_price AS REAL)*(1-CAST(oi.discount_rate AS REAL))),2) AS rev
    FROM orders o
    --以 order_id 欄位結合 order_items資料表
    JOIN order_items oi on o.order_id = oi.order_id
    --篩選已完成的訂單
    WHERE o.status = 'completed'
    --按日期分組,每天一列,有日期 d 和 營收 rev 二欄
    GROUP BY substr(order_date,1,10)
)
    --主查詢層
    SELECT 
        --查詢 d 欄位
        d,
        --查詢 當日營收,四捨五入到小數二位 別名 rev
        rev,
        --查詢累計營收,從第一天到當天,每日營收加總,小數二位 別名 running_rev
        ROUND(SUM(rev) OVER (ORDER BY d ROWS BETWEEN UNBOUNDED PRECEDING AND CURRENT ROW),2) AS running_rev ,
        --查詢 七日移動平均 ma7 ,小數二位 別名 ma7
        ROUND(AVG(rev) OVER (ORDER BY d ROWS BETWEEN 6 PRECEDING AND CURRENT ROW),2) AS ma7
    --從 daily 暫存表
    FROM daily
    --依 d 欄位排序
    ORDER BY d
    --只看前 10 筆記錄
    LIMIT 10
"""
print(pd.read_sql_query(query1,conn))
## 求各付款方式平均每筆訂單的客單價,由高至低
query2="""
--產生 order_rev 暫存表
  WITH order_rev AS ( 
        --查詢 order_id與加總order_id之營收,欄名為revenue
        SELECT order_id ,
        ROUND(
        SUM(
        CAST(quantity AS REAL)*CAST(unit_price AS REAL)*(1-CAST(discount_rate AS REAL))
        )
        ,2) AS revenue 
        --從 order_items資料表
        FROM order_items 
        --依 order_id分群
        GROUP BY order_id
    )
--主查詢層
    --查詢訂單主檔之付款方式,及付款方式筆數orders,及平均客單價avg_revenue
    SELECT o.payment_type,COUNT(r.order_id) AS order_count,AVG(r.revenue) AS avg_revenue
    --從order_rev 暫存表取得資料 別名為 r
    FROM order_rev r
    --結合orders依order_id 欄位
    JOIN orders o on o.order_id = r.order_id
    --篩選已完成的訂單
    WHERE o.status = 'completed'
    --依 payment_type分組
    GROUP BY o.payment_type
    --依 平均客單價遞減排序
    ORDER BY avg_revenue DESC
"""
print("="*30)
print(pd.read_sql_query(query2,conn))

## 找出累積消費金額最高的前10名vip客戶(金雞母)

query3="""
--產生 customer_rev 暫存表
WITH customer_rev AS (
        --查詢 customer_id與加總customer_id之營收,欄名為 total_rev
    SELECT o.customer_id,
        ROUND(
        SUM(
        CAST(oi.quantity AS REAL)*CAST(oi.unit_price AS REAL)*(1-CAST(oi.discount_rate AS REAL))
        )
        ,2) AS total_rev
        --從 orders資料表
        FROM orders o
        -- 依 order_id 欄位 結合 order_items資料表
        JOIN order_items oi on o.order_id = oi.order_id
        --篩選已完成的訂單
        WHERE o.status = 'completed'
        --依 customer_id分群
        GROUP BY o.customer_id
)
--主查詢層
    --查詢 customer_id欄位,總營收欄位 total_rev ,排序欄位 revenue_rank
    SELECT customer_id,total_rev,
        --窗口函數 RANK 依 total_rev 遞減排序
    RANK() OVER (ORDER BY total_rev DESC) AS revenue_rank
    --從 customer_rev 暫存表 
    FROM customer_rev
    --查看最前10筆
    LIMIT 10
"""

print("="*30)
print(pd.read_sql_query(query3,conn))