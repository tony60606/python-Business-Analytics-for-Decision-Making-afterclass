import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from common import factor
from matplotlib.colors import LinearSegmentedColormap
plt.rcParams['font.family']='Microsoft JhengHei'
#seaborn 熱力圖 管道*客群交叉分析
fact=factor()
customers=pd.read_csv('data/raw/customers.csv')
#合併customers資料表, on='customer_id' how='left'
facts=fact.merge(customers,on='customer_id',how='left')
#產生樞紐分析表
cross=facts.pivot_table(
    #計算欄位 line_revenue
    values = 'line_revenue',
    #列 acquisition_channel
    index = 'acquisition_channel' ,
    #欄 segment
    columns = 'segment' ,
    #聚合函式 平均
    aggfunc = 'mean'
)


#印出樞紐分析表
print(cross)

#產生圖表
fig,ax=plt.subplots(figsize=(12,5))

# 假設我們希望：低數值=藍色，中數值=綠色，高數值=紅色
# my_colors = ["#0000FF", "#00FF00", "#FF0000"] 

# 使用 from_list 方法將這串顏色變成漸層色盤，命名為 'my_RGB'
# custom_cmap = LinearSegmentedColormap.from_list('my_RGB', my_colors)

#繪製熱力圖 
sns.heatmap(cross,annot=True,fmt=',.0f',cmap='YlOrRd',ax=ax)
#標題 管道*客群 平均訂單營收
ax.set_title('管道*客群 平均訂單營收',fontsize=20)
#顯示圖表
plt.show()

