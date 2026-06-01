import pandas as pd
import sqlite3 as sql
pd.set_option('display.max.columns',None)
pd.set_option('display.max.rows',None)
query = '''
SELECT c.segment,SUM(oi.quantity*oi.unit_price*(1-oi.discount_rate))/COUNT(DISTINCT o.order_id) as aov
FROM order_items oi
JOIN orders o on oi.order_id = o.order_id
INNER JOIN customers c on o.customer_id = c.customer_id
WHERE o.status = 'completed'
GROUP BY c.segment
ORDER BY c.segment
'''
with sql.connect('data/raw/course.db') as conn:
    df=pd.read_sql_query(query,conn).round(0)
    df.to_csv('homework.csv')
    print(df)