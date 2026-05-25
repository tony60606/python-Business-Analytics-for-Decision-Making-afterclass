import pandas as pd
from common import factor

pd.set_option("display.max.columns", None)
facts = factor()
customers = pd.read_csv("data/raw/customers.csv")
df = facts.merge(customers[["customer_id", "segment"]], on="customer_id", how="left")
'''
segment        growth      new      vip
payment_type                           
atm           4921.36  4981.28  5148.77
card          5074.73  4902.68  5096.46
cod           5112.98  5019.68  5059.42
wallet        4904.64  5005.09  5145.36
'''
##利用groupby完成樞紐分析表 如上圖
pivot_eq = df.groupby(['payment_type','segment'])['line_revenue'].agg('mean').round(2).unstack()
print(pivot_eq)
pivot_eq.to_csv('temp6.csv')