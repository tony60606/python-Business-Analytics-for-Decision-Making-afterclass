import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from common import factor

# 1. 取得資料,目標欄位 line_revenue
facts = factor()
data = facts['line_revenue']

# 2. 分別計算 q1,q2,a3,iqr
q1 = data.quantile(0.25)
q2 = data.median()
q3 = data.quantile(0.75)
iqr = q3-q1

# 計算理論邊界 lower_bound,upper_bound
lower_bound = q1-1.5*iqr
upper_bound = q3+1.5*iqr

# 計算實際的鬚線端點 (落在邊界內的最小值與最大值)
lower_whisker =data[data>=lower_bound].min()
upper_whisker = data[data<=upper_bound].max()

# 3. 開始繪圖 
 #設定中文字型為 'Microsoft JhengHei'
plt.rcParams['font.family']='Microsoft JhengHei'

#設定畫布大小為10inch 5inch
plt.figure(figsize=(10,5))
# sns.boxplot 畫出箱型圖，data=facts, y='line_revenue', color='lightblue' 並取得 axes 物件以便後續操作
ax=sns.boxplot(data=facts, y='line_revenue', color='lightblue')
#標題 '訂單營收箱形圖'
plt.title('訂單營收箱形圖')
#y軸標籤 '營收(元)'
plt.ylabel('營收(元)')
# 4. 將統計數值標註到圖表上
# 設定 X 軸的偏移量 (offset)，讓文字出現在箱子的右側，避免重疊
x_offset = 0.4
# 將需要標註的點位建立成字典，方便用迴圈處理
annotations = {
    f'Upper Whisker: {upper_whisker:,.0f}': upper_whisker,
    f'Q3: {q3:,.0f}': q3,
    f'Median: {q2:,.0f}': q2,
    f'Q1: {q1:,.0f}': q1,
    f'Lower Whisker: {lower_whisker:,.0f}': lower_whisker
}

# 逐一將文字畫上圖表
for text,y_pos in annotations.items() :
    ax.text(x_offset,y_pos,text,verticalalignment='center',color='green',fontweight='bold',fontsize=14)

# 以圖例形式將 iqr 放在右上角
ax.text(0.9,0.9,f'IQR={iqr:,.0f}',transform=ax.transAxes,horizontalalignment='right',verticalalignment='top')
#
plt.tight_layout()
plt.show()