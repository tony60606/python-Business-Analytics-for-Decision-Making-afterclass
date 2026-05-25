import pandas as pd
from common import factor
pd.set_option('display.max.columns',None)
facts=factor()
customers=pd.read_csv('data/raw/customers.csv')
'''
segment        growth      new      vip      All
payment_type                                    
atm           4921.36  4981.28  5148.77  4979.96
card          5074.73  4902.68  5096.46  4974.20
cod           5112.98  5019.68  5059.42  5052.66
wallet        4904.64  5005.09  5145.36  4987.98
All           5014.23  4949.50  5112.48  4985.64
'''
df=facts.merge(customers[['customer_id','segment']],on='customer_id',how='left')
##產生如上的樞紐分析表
pivot2=df.pivot_table (
    values = 'line_revenue' ,
    index = 'payment_type' ,
    columns = 'segment' ,
    aggfunc = ['mean','std'] ,
    margins = True
).round(2)
print(pivot2)
pivot2.to_csv('temp5.csv')
