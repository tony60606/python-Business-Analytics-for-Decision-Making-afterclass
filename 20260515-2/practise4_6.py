import pandas as pd
from common import factor
#設定查看所有欄位
pd.set_option('display.max.columns',None)
facts=factor()
customers=pd.read_csv('data/raw/customers.csv')
#將facts合併customers資料表,但只合併 customer_id,segment二欄位,以customer_id為合併索引欄位
#且以左邊資料表為依據
df = facts.merge(customers[['customer_id','segment']],on='customer_id',how='left')
df.to_csv('temp7.csv')
'''
依 payment_type 及 segment 二欄位分組
計算 
    訂單數=('order_id','count')
    平均客單價=('line_revenue','mean')
    營收總計=('line_revenue','sum')
結果指定給 by_payment_segment 變數,取小數2位
'''
by_payment_segment=(df.groupby(['payment_type','segment']).agg(
    訂單數 = ('order_id','count'),
    平均客單價= ('line_revenue','mean'),
    營業總計 = ('line_revenue','sum')
)).round(2)
print(by_payment_segment)
by_payment_segment.to_csv('temp8.csv')
