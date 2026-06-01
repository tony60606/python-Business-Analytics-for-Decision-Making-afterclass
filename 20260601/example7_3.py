import pandas as pd
import sqlite3 as sql
## 1.連線到 sqlite 資料庫
conn=sql.connect('data/raw/course.db')

## 2.用pandas 執行 sql 查詢,結果直接是 DataFrame
df=pd.read_sql_query('SELECT * FROM orders LIMIT 5',conn)
print(df)

## 3.關閉資料庫
conn.close
print('='*30)
## 4.好習慣,用with管理連線,確保資源自動關閉
with sql.connect('data/raw/course.db') as conn :
    df= pd.read_sql_query('SELECT * FROM orders LIMIT 5',conn)
    print(df)