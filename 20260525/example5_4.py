import pandas as pd
from common import factor
pd.set_option('display.max.columns',None)
facts=factor()
##製作樞紐分析表,查看付款⽅式的訂單數、平均客單價、營收總計
pivot=facts.pivot_table (
    values = 'line_revenue' ,
    index = 'payment_type' ,
    aggfunc = ['count','mean','sum']
)
print(pivot.round(2))
## 儲存為 temp4.csv 
pivot.to_csv('temp4.csv')