import pandas as pd
import sqlite3 as sql
# 1. 建立 10 筆測試資料 (模擬 A、B 兩個部門在 5 個月內的業績)
data = {
    'Dept': ['A', 'A', 'A', 'A', 'A', 'B', 'B', 'B', 'B', 'B'],
    'Month': [1, 2, 3, 4, 5, 1, 2, 3, 4, 5],
    'Sales': [100, 150, 150, 200, 300, 80, 90, 90, 120, 150]
}
# 2. 將 data 轉為 dataframe
df=pd.DataFrame(data)

# 3.建立 sales_report 資料庫,並將DataFrame 寫入變成資料表
db_name='sales_report.db'
with sql.connect(db_name) as conn:
    df.to_sql('salestable',conn,index=False,if_exists='replace')
    print('資料庫建立成功')

query='''
SELECT Dept,Month,Sales,
ROW_NUMBER () OVER (PARTITION BY Dept ORDER BY Sales DESC) AS sql_row_number ,
RANK () OVER (PARTITION BY Dept ORDER BY Sales DESC) AS sql_rank ,
LAG(Sales,2) OVER (PARTITION BY Dept ORDER BY Month) AS sql_lag ,
LEAD(Sales,3) OVER (PARTITION BY Dept ORDER BY Month) AS sql_lead ,
SUM(Sales) OVER (PARTITION BY Dept ORDER BY Month) AS sql_sum1 ,
SUM(Sales) OVER (PARTITION BY Dept ORDER BY Month ROWS BETWEEN 1 PRECEDING AND 1 FOLLOWING) AS sql_sum2 ,
SUM(Sales) OVER (ORDER BY Month) AS sql_sum3 ,
SUM(Sales) OVER (PARTITION BY Dept) AS sql_sum4 ,
ROUND(AVG(Sales) OVER (PARTITION BY Dept ORDER BY Month),2) AS sql_avg1 ,
ROUND(AVG(Sales) OVER (PARTITION BY Dept ORDER BY Month ROWS BETWEEN 1 PRECEDING AND CURRENT ROW),2) AS sql_avg2 ,
ROUND(AVG(Sales) OVER (PARTITION BY Dept ORDER BY Month ROWS BETWEEN 6 PRECEDING AND CURRENT ROW),2) AS sql_avg3 

FROM salestable
ORDER BY Dept,Month
'''
result_df=pd.read_sql_query(query,conn)
print(result_df.to_string(index=False))
conn.close()