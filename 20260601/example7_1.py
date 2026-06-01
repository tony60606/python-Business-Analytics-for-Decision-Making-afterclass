import pandas as pd
from common import factor
orders=pd.read_csv('data/raw/orders.csv')
order_rev=pd.read_csv('data/raw/order_items.csv')
##錯誤的粒度--begin
wrong=orders.merge(order_rev,on='order_id')
print(f'orders 記錄筆數:{len(orders)}')
print(f'order_rev 記錄筆數:{len(order_rev)}')
print(f'wrong 記錄筆數:{len(wrong)}')
wrong.to_csv('temp1.csv')
wrong_count=wrong.groupby('payment_type')['order_id'].count()
print(wrong_count)
##錯誤的粒度--end


order_rev['line_revenue']=(
    order_rev['quantity']*order_rev['unit_price']*
    (1-order_rev['discount_rate'])
)
print('='*30)
order_rev=order_rev.groupby('order_id',as_index=False)['line_revenue'].sum()
facts=order_rev.merge(orders,on='order_id')
print(f'facts 記錄筆數:{len(facts)}')


##在此正確的粒度上做分析
correct_count=facts.groupby('payment_type')['order_id'].count()
print(correct_count)