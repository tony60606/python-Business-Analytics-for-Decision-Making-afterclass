import pandas as pd
import time
df=pd.read_csv("data/raw/order_items.csv")
#1.利用for loop計算--begin
start_time=time.perf_counter()
revenus = [] 
for i in range(len(df)) :
    rev=df.iloc[i]["quantity"]*df.iloc[i]['unit_price']*(1-df.iloc[i]['discount_rate'])
    revenus.append(rev)
print(f'總金額={sum(revenus):.2f}')
end_time=time.perf_counter()
ex_time=end_time-start_time
print(f'花費時間：{ex_time:4f}秒')
#1.利用for loop計算--end

#2.利用dataframe向量化處理方式--begin
start_time2=time.perf_counter()
df['revenue_total']=df['quantity']*df['unit_price']*(1-df['discount_rate'])
print(f'總金額：{df["revenue_total"].sum():.2f}')
end_time2=time.perf_counter()
ex_time2=end_time2-start_time2
print(f'花費時間：{ex_time2:4f}秒')
#2.利用dataframe向量化處理方式--end