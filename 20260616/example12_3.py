import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker 
from common import factor

#設定中文字型為 'Microsoft JhengHei'
plt.rcParams['font.family'] = 'Microsoft JhengHei'
#解決不同字型負號問題
plt.rcParams['axes.unicode_minus'] = False
# 讀取 customers.csv 為 customers dataframe
facts = factor()
customers = pd.read_csv('data/raw/customers.csv')
#依customer_id合併 customers dataframe
facts=facts.merge(customers,on='customer_id')
# 將order_date欄位由字串轉為日期格式
facts['order_date'] = pd.to_datetime(facts['order_date'])
# 利用 strftime 轉為年-月 '%Y-%m'
facts['order_month'] = facts['order_date'].dt.strftime('%Y-%m')

# 製作分群資料,依　['order_month', 'segment']分群,加總['line_revenue'],unstack('segment')
monthly = facts.groupby(['order_month', 'segment'])['line_revenue'].sum().unstack('segment')
print(monthly)

# 圖表寬 10,6 回傳 fig,ax
fig,ax=plt.subplots(figsize=(10,6))
# # 繪製折線圖
lines = ax.plot(
  monthly.index ,# x軸 monthly.index
  monthly ,# monthly dataframe 針對每個欄位畫一條折線
  marker = 'o' ,#標記為圓形
  markersize = 6 ,#大小6
  linewidth = 2#折線粗細 2
)
#  設定標題 '各客群月營收趨勢', fontsize=16, fontweight='bold', pad=20
ax.set_title('各客群月營收趨勢', fontsize=16, fontweight='bold', pad=20)
# 設定 xlabel '月份', fontsize=12, labelpad=10
ax.set_xlabel('月份', fontsize=12, labelpad=10)
# 設定 ylabel '總營收(元)', fontsize=12, labelpad=10
ax.set_ylabel('總營收(元)', fontsize=12, labelpad=10)

ax.yaxis.set_major_formatter(ticker.StrMethodFormatter('{x:,.0f}'))

# 設定圖例 monthly.columns, title='客群', loc='upper left', bbox_to_anchor=(1.02, 1)
plt.legend(monthly.columns, title='客群', loc='upper left', bbox_to_anchor=(1.02, 1))
# 加上資料標籤 
for i,column in enumerate (monthly.columns) :
    line = lines[i] 
    x_values = monthly.index
    y_values = monthly[column]
    for x,y in zip (x_values,y_values) :
        ax.text (x,y*1.02,f'{int(y):,}',color=line.get_color(),ha='center',va='bottom',fontsize=8,fontweight='bold')

# 加上 Y 軸格線
ax.grid(axis='y', linestyle='--', alpha=0.5)
ax.tick_params(axis='x', rotation=30)
# # 自動調整版面並顯示
plt.tight_layout()
plt.show()