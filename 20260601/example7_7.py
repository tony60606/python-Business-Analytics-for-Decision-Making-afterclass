import pandas as pd
import sqlite3 as sql
## 從orders資料表 篩選 status='completed'
## 針對 payment_type 分群計數訂單筆數並遞減排序
## 訂單筆數的欄位名稱為 order_count
## 只顯示 payment_type,status,order_count 三個欄位
query='''
SELECT payment_type,status,COUNT(*) as order_count
FROM orders
WHERE status = 'completed'
GROUP BY payment_type
ORDER BY order_count DESC
'''
with sql.connect('data/raw/course.db') as conn:
    df=pd.read_sql_query(query,conn)
    print(df)