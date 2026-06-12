import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

#設定中文字型為  'Microsoft JhengHei' 
plt.rcParams['font.family'] = 'Microsoft JhengHei'
#修正負值問題
plt.rcParams['axes.unicode_minus']=False
# 讀取order_items.csv
items = pd.read_csv('data/raw/order_items.csv')

# 計算每一列明細的營收 (公式：數量 * 單價 * (1 - 折扣))
items["line_revenue"] = items['quantity']*items['unit_price']*(1-items['discount_rate'])

# 選擇三個欄位 ["line_revenue", "quantity", "unit_price"]
cols = items[["line_revenue", "quantity", "unit_price"]]
print(cols) 

# 計算相關矩陣
corr = cols.corr()

# --- 4. 繪製熱力圖 ---
# 設定圖表大小 6,5
plt.figure(figsize=(6,5))
#繪製熱力圖
sns.heatmap(
            data=corr,
            annot=True,  #顯示資料標籤
            fmt='.2f' ,  #格式為小數二位
            cmap='RdBu_r',  #熱力圖色彩為紅藍漸層 RdBu_r
            vmin = -1 ,  #最小值為 -1
            vmax = 1 , #最大值為 1
            center= 0 , #置中
            annot_kws={'size':15}  # 放大格內數字
)

#設定圖表標題為 "unit_price 與 line_revenue 高度正相關（合理）"
plt.title('unit_price 與 line_revenue 高度正相關（合理）')
#顯示圖表
plt.show()

'''
line_revenue 與 unit_price 相關係數高達0.77,表示高度正相關,line_revenue 與 quantity 相關係數為0.55,表示正相關
因營收的公式有單價與數量，因此兩者的多寡對於營收的影響成正相關屬合理現象
quantity 與 unit_price 相關係數為0.00,表示幾乎無關,商品單價與購買數量幾乎無線性關係
'''