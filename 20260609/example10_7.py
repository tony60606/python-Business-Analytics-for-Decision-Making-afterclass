import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from common import factor
facts=factor()
plt.rcParams['font.family']='Microsoft JhengHei'
fig,axes=plt.subplots(1,3,figsize=(15,4))
# 分別用 10,30,50 個 bin 繪製,觀察差異
for ax , b in zip (axes,[10,30,50]) :
    #資料為line_revenue
    ax.hist(facts['line_revenue'] ,
            #bins 分別為 10,30,50
            bins = b ,
            #框色彩為白色
            edgecolor = 'White' ,
            #alpha=0.7
            alpha = 0.7 ,
            color = 'Green'
    )
    #標題為 bins=10,30,50
    ax.set_title(f'bins={b}')
    #x標籤為 營收(元)
    ax.set_xlabel('營收(元)')
    #y軸標籤為 訂單數
    ax.set_ylabel('訂單數')
#顯示圖表
plt.tight_layout()
plt.show()