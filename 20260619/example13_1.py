import pandas as pd
import numpy as np
##計算空值佔的比率
sessions=pd.read_csv('data/raw/sessions.csv')
##印出 sessions 的欄位結構
print(sessions.info())
#campaign 欄位,刪除空白,並以np.nan取代none值+
#1.印出campaign欄位內容
print(sessions['campaign'])
print("="*30)
#2.刪除空白,並以np.nan取代none值
sessions['campaign']=sessions['campaign'].str.replace(' ','').replace('none',np.nan)
print(sessions['campaign'])

##利用 pivot_table 分組計算 source 及 campaign 欄位的非空數及空值數
result=sessions.pivot_table(
    index='traffic_source',
    values=['campaign'],
    aggfunc=['size','count',lambda x:x.isna().sum()]
)
#設定欄位名稱為 ['總筆數(含NaN)', '有效資料數(不含NaN)', 'NaN值數量']
result.columns=['總筆數(含NaN)', '有效資料數(不含NaN)', 'NaN值數量']
#將結果輸出為 temp1.csv
result.to_csv('temp1.csv')
print('='*30)
print(result)
#==========================================
#計算空值佔比
result1=sessions.groupby('traffic_source')['campaign'].apply(lambda x:x.isna().mean()).round(2)*100

#印出百分比
print(result1.map(lambda x:f'{x:.0f}%'))
#==========================================

##處理空值 設定二個條件
#1 (sessions['campaign'].isnull()) & (sessions['traffic_source'].isin(['direct','seo'])),
#2 (sessions['campaign'].isnull()) & (sessions['traffic_source'].isin(['sem','email','social']))
conditions=[
    (sessions['campaign'].isnull()) & (sessions['traffic_source'].isin(['direct','seo'])),
    (sessions['campaign'].isnull()) & (sessions['traffic_source'].isin(['sem','email','social']))
]
# 對應條件的填補值 ['Organic', 'Untracked_Bug']
choices = ['Organic', 'Untracked_Bug']

# 執行條件替換，依據 conditions 替換為 choices 的內容 如果都不符合就保持原本的 campaign 值
sessions['campaign']=np.select(conditions,choices,default=sessions['campaign'])
print(sessions['campaign'])
sessions['campaign'].to_csv('temp2.csv')