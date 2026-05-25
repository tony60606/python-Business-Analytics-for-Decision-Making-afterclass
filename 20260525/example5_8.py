import pandas as pd
from common import factor
facts=factor()
def lesson(df)->None:
    print('Lesson 4:Groupby , pivot , KPI table')
    #按日期分組,日期保留為欄位而非索引,加總營收
    daily = df.groupby(df['order_date'].dt.date,as_index=False)['line_revenue'].sum()
    print('Daily revenue sample:')
    #查看daily前五筆
    print(daily.head())
  

    #製作樞紐分析表,針對付款方式查看訂單數,平均客單價,營收總計
    by_payment= df.pivot_table(
        values = 'line_revenue' ,
        index = 'payment_type' ,
        aggfunc = ['count','mean','sum']
    ).round(2)
    print(by_payment)
    by_payment.to_csv('temp8.csv')

lesson(facts)