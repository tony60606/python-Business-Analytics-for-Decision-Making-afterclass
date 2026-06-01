import pandas as pd
import sqlite3 as sql
pd.set_option('display.max.columns',None)


## 1.SELECT 選取欄位,查看 orders 資料表的前 10 筆記錄 只看 order_id,customer_id,status 三個欄位
## a. 利用 with 開啟資料庫 並利用 sql 語法查詢
with sql.connect('data/raw/course.db') as conn:
    df= pd.read_sql_query("SELECT order_id,customer_id,status FROM orders LIMIT 10",conn)
    print(df)
print("="*30)
## b.利用 dataframe 方法查詢
orders=pd.read_csv('data/raw/orders.csv')
df=orders[['order_id','customer_id','status']].head(10)
print(df)

## 2.WHERE 條件篩選 查看 orders 資料表 status=='completed' 且 payment_type='card' 的記錄
# 只看 order_id,customer_id,payment_type,status 欄位,前五筆

print("="*30)
## a.sql 語法
with sql.connect('data/raw/course.db') as conn:
    df=pd.read_sql_query('''
    SELECT order_id,customer_id,status 
    FROM orders
    WHERE status = 'completed'
    AND payment_type = 'card' 
    LIMIT 10''',conn)
    print(df)
print("="*30)

## b.利用 dataframe loc 或 query 方法查詢篩選
df=orders.loc[(orders['status']=='completed')&(orders['payment_type']=='card')].head(10)
print(df)
print("="*30)
print('利用 query 方法')
result= orders.query("status == 'completed' and payment_type == 'card'")[['order_id','customer_id','payment_type','status']].head(10)
print(result)