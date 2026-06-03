import pandas as pd
import sqlite3 as sql
'''
Common Table Expression 語法
-- 宣告區 (定義變數)
WITH 暫存表名稱 AS (
    SELECT ... (你的複雜查詢)
)
-- 執行區 (使用變數)
SELECT ... 
FROM 暫存表名稱;
===========================
等同於python 這麼寫
# 宣告區
temp_table = fetch_data_and_calculate()

# 執行區
result = process(temp_table)
'''
#================================================
##利用子查詢
query1="""
SELECT
    c.segment,
    COUNT(*) AS orders,
    ROUND(AVG(oi.revenue),2) AS avg_revenue
FROM (
    SELECT 
        order_id,
        SUM(quantity*unit_price*(1-discount_rate)) AS revenue
        FROM order_items
        GROUP BY order_id
) oi
JOIN orders o ON o.order_id=oi.order_id
JOIN customers c ON o.customer_id=c.customer_id
WHERE o.status='completed'
GROUP BY c.segment
ORDER BY avg_revenue DESC
"""

##以CTE取代
query2="""
-- 宣告區 (定義變數)
WITH order_revenue AS (
SELECT
    order_id,
    ROUND(SUM(quantity*unit_price*(1-discount_rate)),2) AS revenue
    FROM order_items
    GROUP BY order_id
)
-- 執行區 (使用變數)
SELECT c.segment,COUNT(*) AS orders,ROUND(AVG(r.revenue),2) AS aov
FROM order_revenue r
JOIN orders o ON o.order_id=r.order_id
JOIN customers c ON o.customer_id=c.customer_id
WHERE o.status='completed'
GROUP BY c.segment
ORDER BY aov DESC
 --直接呼叫剛才做好的 CTE 暫存表 並給它代號 r

"""
with sql.connect('data/raw/course.db') as conn:
    df1=pd.read_sql_query(query1,conn)
    print(df1)
    print("="*40)
    df2=pd.read_sql_query(query2,conn)
    print(df2)