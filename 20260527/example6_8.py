import pandas as pd
from common import factor
import numpy as np
pd.set_option('display.max.columns',None)
facts=factor()
## axis=0 縱向堆疊(預設)
## 1.讀入 orders.csv 轉為 DataFrame
orders=pd.read_csv('data/raw/orders.csv')
## 2.更改 order_date 欄位資料型態為 datetime
orders['order_date']=pd.to_datetime(orders['order_date'])
## 3.查找2025年一月份的訂單資料
jan=orders.loc[orders['order_date'].dt.strftime('%Y-%m')=='2025-01']
## 查看2025年一月前五筆
print(jan.head())
print("="*30)
## 4.查找2025年二月份的訂單資料
feb=orders.loc[orders['order_date'].dt.strftime('%Y-%m')=='2025-02']
## 查看二月前五筆
print(feb.head())

print("="*30)
## 5.把一月和二月的訂單資料合在一起
combined=pd.concat([jan,feb],axis=0)
combined2=pd.concat([jan,feb],axis=1)
print(combined)
## 6.將combined資料表輸出為 temp1.csv
combined.to_csv("temp4.csv")
combined.to_csv("temp5.csv")

print("="*30)
## 查看 未合併與合併後的列數
print(f'一月:{len(jan)} 列,二月:{len(feb)} 列,合併一,二月:{len(combined)} 列')


## axis=1 橫向合併 ,將二個同長度的DataFrame左右併在一起
stats_a=facts.groupby('payment_type')['line_revenue'].mean().rename('avg_rev')
print("="*30)
print(stats_a)
stats_b=facts.groupby('payment_type')['line_revenue'].sum().rename('total_rev')
print("="*30)
print(stats_b)
side_by_side=pd.concat([stats_a,stats_b],axis=1)
print("="*30)
print(side_by_side.round(2))
side_by_side.to_csv('temp6.csv')
