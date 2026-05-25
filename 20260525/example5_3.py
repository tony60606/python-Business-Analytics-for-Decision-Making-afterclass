## 找出高於平均的訂單
import pandas as pd
import numpy as np
from common import factor
facts=factor()
print(f'總記錄筆數:{len(facts)} 筆')
## 1.新增以 payment_type 分組的平均 欄位,名稱為 payment_avg
facts['payment_avg'] = facts.groupby(['payment_type'])['line_revenue'].transform('mean').round(2)
##方便檢視,更改欄位順序--begin
# a.取得目前欄位名稱,轉成列表指定給cols變數
cols = facts.columns.to_list()
print(cols)
# b.移除 line_revenue 欄位
cols.remove('line_revenue')
# c.取得 payment_avg 欄位的索引值
ind = cols.index('payment_type')
# d.插入 line_revenue 到 idx 的位置
cols.insert(ind,'line_revenue')
print(cols)
##方便檢視,更改欄位順序--end

# 以新的欄位順序且依 payment_type 欄位排序 輸出到 temp1.csv
facts[cols].sort_values(by=['payment_type'],ignore_index=True).to_csv('temp1.csv')
## 2.新增 vs_avg 欄位計算每筆訂單相差分組平均多少
facts['vs_avg'] = (facts['line_revenue']-facts['payment_avg']).round(2)
## 新增 vs_avg 到 cols 列表
cols.append('vs_avg')
# 以新的欄位順序依 payment_type 欄位排序 輸出到 temp2.csv
facts[cols].sort_values(by=['payment_type'],ignore_index=True).to_csv('temp2.csv')
## 3.篩選出高於分組平均的訂單(可能是大客戶或行銷熱點)
vip = facts[facts['vs_avg']>0]
# 以新的欄位順序依 payment_type 欄位排序 輸出到 temp3.csv
vip[cols].sort_values(by=['payment_type'],ignore_index=True).to_csv('temp3.csv')

#計算符合條件的總記錄筆數
print(f'符合條件的紀錄比數：{len(vip)}筆')