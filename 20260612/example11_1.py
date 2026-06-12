import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from common import factor
facts=factor()
#設定 中文字型為微軟正黑
plt.rcParams['font.family'] = ['Microsoft JhengHei']
#設定圖表大小為 10inch,6inch
plt.figure(figsize=(10,6))
#利用sns繪製直方圖, data=facts,x='line_revenue', 加上密度線, bins=30, color='pink'
ax=sns.histplot(data=facts,x='line_revenue',kde=True, bins=30, color='pink')
print(ax.lines)
#設定密度線的色彩 blue,線寬 2 線條樣式 -.
if ax.lines :
    ax.lines[0].set_color('brown')
    ax.lines[0].set_linewidth(2)
    ax.lines[0].set_linestyle('-.')
    
#y軸標籤 '訂單筆數'
plt.ylabel('訂單比數')
#圖表標題 '訂單營收密度分布'
plt.title('訂單營收密度分布')
#x軸標籤 '營收(元)'
plt.xlabel('營收(元)')
#顯示圖表
plt.show()