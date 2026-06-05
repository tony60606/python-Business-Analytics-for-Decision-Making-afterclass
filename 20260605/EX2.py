import pandas as pd
import sqlite3 as sql
data = {
    'order_date': ['10/01', '10/01', '10/02', '10/03'],
    'payment_type': ['Cash', 'Card', 'Cash', 'Card'],
    'revenue': [100, 200, 150, 300]
}
df = pd.DataFrame(data)
with sql.connect('temp.db') as conn:
    df.to_sql('orders',conn,index=False,if_exists='replace')
    print('資料庫寫入成功')
## 1_1.pandas 操作 transfom('sum') 分組
df['分組總和'] = df.groupby('payment_type')['revenue'].transform('sum')
print(df)
## 1_2 sql PARTITION BY 分組
query1 = '''
SELECT
order_date,payment_type,revenue,
SUM(revenue) OVER (PARTITION BY payment_type) AS sum1
FROM orders
'''
print("="*30)
with sql.connect('temp.db') as conn:
    data=pd.read_sql_query(query1,conn)
    print(data)

## 1_3 pandas 操作 cumsum() 累加
df=df.sort_values(by='order_date')
df['累加'] = df['revenue'].cumsum()
##排序日期
print(df)
## 1_4 sql ORDER BY 累加
query2 = '''
SELECT
order_date,payment_type,revenue,
SUM(revenue) OVER (ORDER BY order_date ROWS BETWEEN UNBOUNDED PRECEDING AND CURRENT ROW) AS sum2
FROM orders
'''
print("="*30)
with sql.connect('temp.db') as conn:
    data=pd.read_sql_query(query2,conn)
    print(data)

## 1_5 pandas 分組 累加
df['分組累加'] = df.groupby('payment_type')['revenue'].cumsum()
print(df)
## 1_6 PARTION BY ORDER BY
query3 = '''
SELECT
order_date,payment_type,revenue,
SUM(revenue) OVER (PARTITION BY payment_type ORDER BY order_date) AS sum3
FROM orders
ORDER BY order_date,sum3
'''
print("="*30)
with sql.connect('temp.db') as conn:
    data=pd.read_sql_query(query3,conn)
    print(data)