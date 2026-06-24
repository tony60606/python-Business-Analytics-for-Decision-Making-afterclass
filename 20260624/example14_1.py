import pandas as pd
order_items=pd.read_csv('data/raw/order_items.csv')
events=pd.read_csv('data/raw/events.csv')
oi=order_items.copy()
oi['calc_rev']=(
    oi['quantity']*oi['unit_price']*(1-oi['discount_rate'])
)
print(len(oi['calc_rev']))


oi_sum=oi.groupby('order_id')['calc_rev'].sum()
print(len(oi_sum))


purchase_rev=(
    events[events['event_type']=='purchase'].groupby('order_id')['revenue'].sum()
   )
print(purchase_rev.info())
print(purchase_rev)
print(len(purchase_rev))


comparison=pd.DataFrame({
    'calc':oi_sum,
    'actual':purchase_rev
}
).fillna(0)
print(comparison)

mismatch=(
    (abs(comparison['calc']-comparison['actual'])>1).sum()
)
print(f'營收不一致的訂單數:{mismatch}')
