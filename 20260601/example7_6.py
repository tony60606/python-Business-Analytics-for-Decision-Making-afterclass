import pandas as pd
import sqlite3 as sql
pd.set_option('display.max.columns',None)
customers=pd.read_csv('data/raw/customers.csv')
## 1.找出 2024年6月後註冊的台北或高雄vip客戶 利用 sql 語法
with sql.connect('data/raw/course.db') as conn:
    #將 sql 語法以多行字串表示
    query='''
    SELECT * 
    FROM customers
    WHERE signup_date >= 2024-06-01
    AND city IN ('Taipei','Kaohsiung')
    AND segment = 'vip'
    '''
    df=pd.read_sql_query(query,conn)
    print(df)
print("="*30)

## 2.找出 2024年6月後註冊的台北或高雄vip客戶 利用 dataframe.query方法
q_str=("signup_date >= '2024-06-01' and city in ['Taipei','Kaohsiung'] and segment == 'vip'")
df=customers.query(q_str).sort_values(by='signup_date')
print(df)