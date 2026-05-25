import pandas as pd
from common import factor
pd.set_option('display.max.columns',None)
facts=factor()
by_payment_dist=facts.groupby('payment_type',as_index=False).agg(
    平均客單價=('line_revenue','mean'),
    中位數=('line_revenue','median'),
    P90= ('line_revenue' , lambda x :x.quantile(0.9)) ,
    標準差=('line_revenue','std')
).round(2)
print(by_payment_dist.sort_values("P90",ascending=False))
