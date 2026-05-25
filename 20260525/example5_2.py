import pandas as pd
import random
from common import factor
pd.set_option('display.max.columns',None)
'''
order_id payment_type  line_revenue
      1         card           100
      2          atm           200
      3         card           300
      4          atm           400
      5          atm           600

'''
## 1.以data字典建立上述欄位資料
data = {
    'order_id' : list(range(1,6)) ,
    'payment_type' : ['card','atm','card','atm','atm'] ,
    'line_revenue' : random.sample(range(100,600),5)
}
## 2.將 data 字典轉名稱為 df 的DataFrame
df = pd.DataFrame(data)
## 3.印出 df 
print(df)
print('='*30)
## 4.用 agg 計算各付款方式的平均金額 指定給 result 變數
result = df.groupby(['payment_type'])['line_revenue'].agg('mean').round(2)
## 5.印出結果
print(result)
print('='*30)
## 6.用 transform 計算各付款方式的平均金額
df['result2']= df.groupby(['payment_type'])['line_revenue'].transform('mean').round(2)
## 7.印出結果
print(df)
print('='*30)
## 8.印出結果,針對 payment_type 排序,將相同分類印在一起
print(df.sort_values(by=['payment_type'],ignore_index=True))
