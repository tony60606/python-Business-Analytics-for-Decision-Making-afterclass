import pandas as pd
import numpy as np
##記錄層級 統計每月的訂單記錄筆數
orders1=pd.read_csv('data/raw/orders1.csv')

#將 order_date 欄位轉為 datetime 格式,轉換為只保留『月份』的週期格式
orders1['order_date']=pd.to_datetime(orders1['order_date'])
orders1['order_month']=orders1['order_date'].dt.to_period('M')

#計算每月訂單筆數
monthly_counts=orders1.groupby('order_month').size()

#印出結果
print(monthly_counts)

##========時間層級==================

# 檢查起訖範圍
print("="*30)
print('訂單日期範圍:',orders1['order_date'].min(),"~",orders1['order_date'].max())

# 檢查是否有整天沒有記錄（斷層偵測）
# 1.找出資料中的第一天和最後一天，自動生成一個從 start 到 end 的連續日期清單
all_dates=pd.date_range(start=orders1['order_date'].min(),end=orders1['order_date'].max(),freq='D')

#抓出資料表的日期
existing_dates =orders1['order_date'].dt.normalize().unique()

#利用difference 方法比較與 all_dates 時間序列相差幾天
missing_dates = all_dates.difference(existing_dates)

print("="*30)
print(f"缺漏的⽇期共 {len(missing_dates)} 天,遺失的日期為:{missing_dates}：")