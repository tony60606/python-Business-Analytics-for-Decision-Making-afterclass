import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from common import factor
plt.rcParams['font.family']='Microsoft JhengHei'
facts=factor()
customers=pd.read_csv('data/raw/customers.csv')
#合併customer資料表
figdata=facts.merge(customers,on='customer_id',how='left')
## seaborn 箱形圖 比較各客群的客單價分佈 寬 8 inch 高 5 inch
fig,ax=plt.subplots(figsize=(8,5))
#繪製箱形圖 data=figdata,x='segment',y='line_revenue',ax=ax,order=['new','growth','vip']
sns.boxplot(data=figdata,x='segment',y='line_revenue',ax=ax,order=['new','growth','vip'])
#標題 各客群客單價分佈
ax.set_title('各客群客單價分佈')
#x軸標籤 客群
ax.set_xlabel('客群')
#y軸標籤 訂單營收(TWD)
ax.set_ylabel('訂單營收(TWD)')
#顯示圖表
plt.show()
