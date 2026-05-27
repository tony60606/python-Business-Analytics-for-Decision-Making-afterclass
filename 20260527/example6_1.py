from common import factor
import pandas as pd
facts=factor()
##利用groupby
facts['week']=facts['order_date'].dt.to_period('W')
df=facts.groupby('week',as_index=False).agg(
    revenue = ('line_revenue','sum') ,
    order = ('order_id','count')
).assign(aov = lambda x : x['revenue']/x['order']).round(2)
df.to_csv('temp1.csv')
print('='*50)
##利用pivot_table
df2 = facts.pivot_table(
    values = 'line_revenue' ,
    index = 'week' ,
    aggfunc = ['sum','count','mean']
    ).round(2)
df2.columns = ['revenue','order','aov']
df2.to_csv('temp2.csv')