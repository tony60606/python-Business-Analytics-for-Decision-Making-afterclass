import pandas as pd
import sqlite3 as sql
# 1. 建立 10 筆測試資料 (模擬 A、B 兩個部門在 5 個月內的業績)
data = {
    'Dept': ['A', 'A', 'A', 'A', 'A', 'B', 'B', 'B', 'B', 'B'],
    'Month': [1, 2, 3, 4, 5, 1, 2, 3, 4, 5],
    'Sales': [100, 150, 150, 200, 300, 80, 90, 90, 120, 150]
}
# 2. 將 data 轉為 dataframe
data = pd.DataFrame(data)

# 3.建立 sales_report 資料庫,並將DataFrame 寫入變成資料表
db_name = 'sales_report.db'
with sql.connect(db_name) as conn :
    data.to_sql('salestable',conn,index=False,if_exists='replace')
#4.窗口函式應用
query="""
-- 1. 排序函數 (依部門分組,按業績由高到低排序)    
SELECT Dept,Month,Sales,
RANK() OVER (PARTITION BY Dept ORDER BY Month) AS sql_row_number
   

-- 2. 偏移函數 (依部門分組,按月份由小到大排序)

  

-- 3. 聚合函式 ()
   
FROM salestable
ORDER BY Dept,Month
"""
result_df=pd.read_sql_query(query,conn)
print(result_df.to_string(index=False))
conn.close()



