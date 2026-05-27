import pandas as pd
from common import factor
import numpy as np
facts=factor()
customers=pd.read_csv('data/raw/customers.csv')
print(f'合併前:facts {facts.shape[0]} 列,customers {customers.shape[0]} 列')
## 1.執行合併,on='customer_id how=left
merged=facts.merge(customers,on='customer_id',how='left')

## 2.檢查 1.列數變化 (left join 後列數應等於左表的列數)
print(f'合併後:merged {len(merged)} 列')

## 3.檢查 2.鍵值唯一性,True 安全,False 會造成列數膨脹
print(f' 右表 customer_id 欄位是否唯一? {customers['customer_id'].is_unique}')

## .sum().sum() 解說
df=pd.DataFrame({
    'order_id':['T01','T02','T03'],
    'amount':[100,np.nan,200],
    'customer_id':['C01','C02',np.nan]
})
s1=df.isna()
print('s1=',s1)
s2=s1.sum()
print('s2=',s2)
print('type(s2)=',type(s2))
print(s2.to_string(index=False))
s3=s2.sum()
print('s3=',s3)
## 4.檢查 3.空值率變化(如果空值大量增加,代表很多左表的鍵在右表找不到配對)
null_before=facts.isna().sum().sum()
null_after=merged.isna().sum().sum()
print(f'空值變化:前:{null_before}->後:{null_after}')
print('='*30)