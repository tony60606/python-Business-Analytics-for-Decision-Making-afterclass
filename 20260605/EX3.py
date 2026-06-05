import pandas as pd
import sqlite3 as sql
data = {
    'id': range(1, 11),
    'date': [f'10/{i:02d}' for i in range(1, 11)],
    'revenue': [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
}
df = pd.DataFrame(data)
print(df)

with sql.connect('temp2.db') as conn:
    df.to_sql('sales',conn,index=False,if_exists='replace')
    print('資料庫寫入成功')

## 1. 累計總和 (從第一列到當前列)
query1='''
SELECT id,date,revenue,
SUM(revenue) OVER (ORDER BY date ROWS BETWEEN UNBOUNDED PRECEDING AND CURRENT ROW) AS sum1
FROM sales
'''

print("="*30)
df_sql1=pd.read_sql_query(query1,conn)
print(df_sql1)
## 2. 7 日移動總和,從往前 6列到當前列
query2='''
SELECT id,date,revenue,
SUM(revenue) OVER (ORDER BY date ROWS BETWEEN 6 PRECEDING AND CURRENT ROW) AS sum2
FROM sales
'''
print("="*30)
df_sql2=pd.read_sql_query(query2,conn)
print(df_sql2)
## 3. 前一列+當前+後一列 前後三列總和
query3='''
SELECT id,date,revenue,
SUM(revenue) OVER (ORDER BY date ROWS BETWEEN 1 PRECEDING AND 1 FOLLOWING) AS sum3
FROM sales
'''
print("="*30)
df_sql2=pd.read_sql_query(query3,conn)
print(df_sql2)
## 4. 全域計算
query4='''
SELECT id,date,revenue,
SUM(revenue) OVER (ORDER BY date ROWS BETWEEN UNBOUNDED PRECEDING AND UNBOUNDED FOLLOWING) AS sum4
FROM sales
'''
print("="*30)
df_sql2=pd.read_sql_query(query4,conn)
print(df_sql2)