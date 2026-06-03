import pandas as pd
import sqlite3 as sql
## 不使用子查詢
query1="""
SELECT 
c.segment ,
SUM(oi.quantity*oi.unit_price*(1-oi.discount_rate)) as revenur ,
ROUND(SUM(oi.quantity*oi.unit_price*(1-oi.discount_rate))/COUNT(DISTINCT o.order_id),2) as aov
FROM orders o
JOIN order_items oi on o.order_id = oi.order_id
INNER JOIN customers c on c.customer_id = o.customer_id
WHERE o.status = 'completed'
GROUP BY c.segment
ORDER BY aov
"""

##利用子查詢
query2="""
SELECT c.segment ,
    ROUND(AVG(oi.revenue),2) AS aov
FROM (
    SELECT
        order_id,
        SUM(quantity*unit_price*(1-discount_rate)) AS revenue
    FROM order_items
    GROUP BY order_id
) oi
JOIN orders o on o.order_id = oi.order_id 
INNER JOIN customers c on o.customer_id = c.customer_id
WHERE o.status = 'completed'
GROUP BY c.segment
ORDER BY aov
"""
with sql.connect('data/raw/course.db') as conn:
    df=pd.read_sql_query(query1,conn)
    print(df)
    print("="*30)
    df2=pd.read_sql_query(query2,conn)
    print(df2)