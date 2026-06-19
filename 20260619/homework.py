import pandas as pd
import numpy as np
order_items = pd.read_csv('data/raw/order_items.csv')
events=pd.read_csv('data/raw/events.csv')
order_items['line_revenue'] = round(order_items['quantity']*order_items['unit_price']*(1-order_items['discount_rate']),2)
order_items2=order_items.groupby('order_id',as_index=False)['line_revenue'].sum().round(2)
print(order_items2)
order_items2.to_csv('temp3.csv')

merged = order_items2.merge(events,on='order_id')
merged['dif'] = merged['line_revenue'] - merged['revenue']
merged.to_csv('temp4.csv')

bad_data = (merged['dif'] > 1) | (merged['dif'] < -1)
if bad_data.any() :
    print(f'異常筆數共有{bad_data.sum()}筆')
    print(merged[bad_data])
else :
    print('資料完全正確')