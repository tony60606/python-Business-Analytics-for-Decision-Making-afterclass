import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

#設定中文字型為  'Microsoft JhengHei' 
plt.rcParams['font.family'] = 'Microsoft JhengHei'
#修正負值問題
plt.rcParams['axes.unicode_minus'] = False
# 讀取order_items.csv
items = pd.read_csv('data/raw/order_items.csv')

# 計算每一列明細的營收 (公式：數量 * 單價 * (1 - 折扣))
items["line_revenue"] = items['quantity']*items['unit_price']*(1-items['discount_rate'])

# 選擇三個欄位 ["line_revenue", "quantity", "unit_price"]
cols = ["line_revenue", "quantity", "unit_price"] 

# 計算相關矩陣
corr = items[cols].corr()

# --- 4. 繪製熱力圖 ---
# 設定圖表大小 6,5
plt.figure(figsize=(6,5))
#繪製熱力圖
sns.heatmap(data = corr ,
            annot= True ,  #顯示資料標籤
            fmt='.2f' ,#格式為小數二位
            cmap='RdBu_r'  , #熱力圖色彩為紅藍漸層 RdBu_r
            vmin= -1 ,  #最小值為 -1
            vmax= 1 ,#最大值為 1
            center= 0 , #置中
            annot_kws={'size' : 15,'color' : 'purple'}  # 放大格內數字

)
#設定圖表標題為 "unit_price 與 line_revenue 高度正相關（合理）"
plt.title('unit_price 與 line_revenue 高度正相關（合理）')
#顯示圖表
plt.show()