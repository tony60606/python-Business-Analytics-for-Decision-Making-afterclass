import pandas as pd
from common import factor
facts=factor()
#針對payment_type欄位分群,不產生索引欄,統計下列資訊
# (訂單數=order_id,計數),(不重覆顧客數=customer_id,累計不重覆),(總營收=line_revenue,加總)
by_payment = facts.groupby(['payment_type'],as_index=False).agg(
    訂單數 = ('order_id','count') ,
    不重覆顧客數 = ('customer_id','nunique') ,
    總營收 = ('line_revenue','sum')
)
by_payment = by_payment.sort_values('總營收',ascending=False)
##輸出為temp6.csv
by_payment.to_csv('temp6.csv')