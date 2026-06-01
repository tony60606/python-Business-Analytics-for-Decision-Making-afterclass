import pandas as pd
from common import factor
import numpy as np
facts=factor()
customers=pd.read_csv('data/raw/customers.csv')
facts=facts.merge(customers,on='customer_id',how='left')
## 管道*客群的平均客價交叉表
cross=facts.pivot_table(
     values = 'line_revenue' ,##針對營收欄位做計算
     index = 'acquisition_channel' , ##列 客戶來源管道
     columns = 'segment' ,## 欄 客群
     aggfunc = 'mean' ,## 平均客單價
     margins = True ## 加上欄/列 合計

).round(0)
print(cross)