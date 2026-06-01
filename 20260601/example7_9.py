import pandas as pd
import sqlite3 as sql
pd.set_option('display.max.columns',None)
## 等同 pandas: orders.merge(customers, on="customer_id", how="inner")
query="""
SELECT o.order_id,o.customer_id,c.customer_id,o.status,c.city,c.segment
FROM orders o
JOIN customers c 
ON o.customer_id = c.customer_id 
WHERE c.segment = 'vip'
AND o.status = 'completed'
AND c.city IN ('Taipei','Kaohsiung')
LIMIT 10
"""
with sql.connect('data/raw/course.db') as conn:
    df=pd.read_sql_query(query,conn)
    print(df)