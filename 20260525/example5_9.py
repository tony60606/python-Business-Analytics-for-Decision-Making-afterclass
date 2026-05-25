import pandas as pd
from common import factor
facts=factor()
## 1. 以 groupby 求 付款方式績效表 即看 總營收 訂單數 客單價
payment_kpi=(
    facts.groupby('payment_type',as_index=False).agg(
        revenue=('line_revenue','sum'),
        orders=('order_id','count')
    )
    .assign(aov=lambda x:x['revenue']/x['orders']).round(2)
)
print(payment_kpi)
print("="*30)
## 2. 以 pivot_table 求 付款方式績效表 即看 總營收 訂單數 客單價
payment_kpi2=facts.pivot_table(
    index='payment_type',
    values='line_revenue',
    aggfunc=['sum','count','mean']
).round(2)
payment_kpi2.columns=['revenue','orders','aov']
print(payment_kpi2)