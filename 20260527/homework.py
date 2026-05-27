import pandas as pd
from common import factor
import numpy as np
facts=factor()
customers=pd.read_csv('data/raw/customers.csv')
customers_new = customers.loc[customers['segment']=='new']
customers_new.to_csv('customer_new.csv')
merged = facts.merge(customers_new,on='customer_id')
df = merged.pivot_table(
    values = 'line_revenue' ,
    index = 'city',
    aggfunc = ['sum','count','mean']
).round(2)
df.columns = ['revenue','cno','aov']
df=df.sort_values(by='aov')
df.to_csv('df.csv')