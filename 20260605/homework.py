import pandas as pd
import sqlite3 as sql
conn=sql.connect('data/raw/course.db')
query ='''
WITH customer_rev AS (
    SELECT 
    o.customer_id,
    o.order_id,
    ROUND(SUM(oi.quantity*oi.unit_price*(1-oi.discount_rate)),2) AS revenue
    FROM orders o
    JOIN order_items oi on o.order_id = oi.order_id 
    WHERE o.status = 'completed'
    GROUP BY o.customer_id
) 
SELECT c.customer_id,c.segment,cr.revenue,
RANK() OVER (PARTITION BY segment ORDER BY revenue DESC) AS Rank_rev
FROM customer_rev cr
JOIN customers c on c.customer_id = cr.customer_id
ORDER BY Rank_rev,c.segment
LIMIT 30
'''
print(pd.read_sql_query(query,conn))