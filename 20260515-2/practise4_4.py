import pandas as pd

items = pd.read_csv("data/raw/order_items.csv")
orders = pd.read_csv("data/raw/orders.csv")
items["line_revenue"] = (
    items["quantity"] * items["unit_price"] * (1 - items["discount_rate"])
)
items.to_csv("temp1.csv")
facts = (
    items.groupby("order_id",as_index=False)["line_revenue"]
    .sum()
    .merge(orders, on="order_id", how="left")
    .query('status=="completed"')
)
facts.to_csv("temp4.csv")
# 將 facts 的 order_date 欄位轉成日期時間
facts['order_date']=pd.to_datetime(facts['order_date'])

##單一聚合
daily_rev=facts.groupby(facts['order_date'].dt.date)['line_revenue'].sum()
print(daily_rev)
##多重聚合 以 payment_type 分群,組合計算 line_revenue 分別求 count,mean,sum,median,max,min
by_payment = facts.groupby(['payment_type'])['line_revenue'].agg(
    訂單數 = 'count' ,
    平均客單價 = 'mean' ,
    總金額 = 'sum' ,
    中位數 = 'median' ,
    最大數 = 'max' ,
    最小數 = 'min'
)
#只看小數一位
by_payment=by_payment.round(1)
#輸出為temp5.csv 
by_payment.to_csv('temp5.csv')