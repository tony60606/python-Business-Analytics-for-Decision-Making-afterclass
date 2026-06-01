import pandas as pd
import sqlite3 as sql

##查看資料庫有那些資料表
with sql.connect('data/raw/course.db') as conn :
    df = pd.read_sql_query("SELECT name FROM sqlite_master WHERE type ='table'",conn)
    print(df)