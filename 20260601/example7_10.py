import pandas as pd
import sqlite3 as sql
pd.set_option('display.max.columns',None)
pd.set_option('display.max.rows',None)
##合併 orders,order_itmes,products 三個資料表
## on 分別為 order_id 與 product_id
## 需計算營收欄位 line_revenue

query="""
SELECT o.order_id,o.status,oi.order_id,oi.product_id,p.product_id,oi.quantity,oi.unit_price,oi.discount_rate,oi.quantity*oi.unit_price*(1-oi.discount_rate) as line_revenue
FROM orders o
JOIN order_items oi on o.order_id = oi.order_id 
INNER JOIN products p on oi.product_id = p.product_id
WHERE o.status = 'completed'
LIMIT 10
"""
with sql.connect('data/raw/course.db') as conn:
    df=pd.read_sql_query(query,conn)
    print(df)