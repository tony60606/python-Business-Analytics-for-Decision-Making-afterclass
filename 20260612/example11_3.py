import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# 1. 讀取原始資料
order_items = pd.read_csv('data/raw/order_items.csv')
products = pd.read_csv('data/raw/products.csv')

# 2. 計算每個商品明細的實際營收 (扣除折扣)
order_items['line_revenue'] = order_items['quantity']*order_items['unit_price']*(1-order_items['discount_rate'])

# 3. 按 order_id 彙總，計算每筆「整張訂單」的總營收,並reset_index() 改成一般欄位,而不是索引
order_revenue = order_items.groupby('order_id')['line_revenue'].sum().reset_index()
print(order_revenue)
 

# 4. 設立黃金交叉點，擷取 VIP 訂單 ID
vip_threshold = 13681
vip_order_ids = order_revenue[order_revenue['line_revenue']>vip_threshold]['order_id']

print(vip_order_ids)

# 5. 取出這些 VIP 訂單的購買明細，並與 products 資料表關聯 (Join) 以取得分類資訊
vip_items = order_items[order_items['order_id'].isin(vip_order_ids)].merge(products,on='product_id',how='left')


# ----- 開始進行商業分析 -----

print(f"  VIP 訂單共：{len(vip_order_ids)} 筆")
print("-" * 40)

# 維度 A：購買次數 (VIP 訂單中最常出現的商品分類)
print("A. VIP 訂單中最常購買的商品分類 (按頻率次數)：")
#印出結果
print(vip_items['category'].value_counts())
print("-" * 40)

# 維度 B：營收貢獻 (真正撐起破萬訂單的商品分類)
print("B VIP 訂單中貢獻最多營收的商品分類 (按總金額)：")
#印出結果
print(vip_items.groupby('category')['line_revenue'].sum().sort_values(ascending=False))
# ---------------------------------------------------------
# 準備繪圖用資料
# ---------------------------------------------------------
# 整理維度 A (頻次) 資料，並轉為 DataFrame 方便 Seaborn 繪圖
#依商品分類計數
freq_data = vip_items['category'].value_counts().reset_index()
#設定欄位為 ['category', 'frequency']
freq_data.columns=['category', 'frequency']

# 整理維度 B (營收) 資料，並轉為 DataFrame 方便 Seaborn 繪圖
#依商品分類加總營收,並重設索引為DataFrame
rev_data = vip_items.groupby('category')['line_revenue'].sum().reset_index()
#依營收遞減排序
rev_data = rev_data.sort_values(by='line_revenue',ascending=False)


# ---------------------------------------------------------
# 步驟七：繪製 Subplots 子圖表
# ---------------------------------------------------------
# 1. 設定中文字型
plt.rcParams['font.family'] = 'Microsoft JhengHei'
# 2. 建立畫布：1 列 2 欄，設定總寬度 14, 高度 6
fig,axes=plt.subplots(1,2,figsize=(14,6))
# 3. 繪製子圖 1 (左邊)：購買頻率次數
# 使用 ax=axes[0] 指定畫在第一個位置，套用藍色漸層 (Blues_r)
#data=freq_data, x='category', y='frequency', ax=axes[0], palette='Blues_r'
sns.barplot(data=freq_data, x='category', y='frequency', ax=axes[0], palette='Blues_r')
#設定圖表標題 'VIP 訂單商品分類 - 購買頻次' 字型大小 14 
axes[0].set_title('VIP 訂單商品分類 - 購買頻次',fontsize=14)
#設定x軸標籤 '商品分類'
axes[0].set_xlabel('商品分類')
#設定 y 軸標籤 '購買次數'
axes[0].set_ylabel('購買次數')
# 將 x 軸刻度旋轉 45
axes[0].tick_params(axis='x',rotation=45)

#為長條圖加上資料標籤
for i,v in enumerate (freq_data['frequency']) :
    y_pos=v+1
    axes[0].text(i,y_pos,f'{v:.0f}',ha='center',va='bottom',fontsize=10)

# 4. 繪製子圖 2 (右邊)：營收貢獻
# 使用 ax=axes[1] 指定畫在第二個位置，套用紅色漸層 (Red_r)
#data=rev_data, x='category', y='line_revenue', ax=axes[1], palette='Red_r'
sns.barplot(data=rev_data, x='category', y='line_revenue', ax=axes[1], palette='Oranges_r')
#設定圖表標題 'VIP 訂單商品分類 - 營收貢獻' fontsize=14
axes[1].set_title('VIP 訂單商品分類 - 營收貢獻',fontsize=14)
#設定x軸標籤 '商品分類'
axes[1].set_xlabel('商品分類')
#設定 y 軸標籤 '總營收貢獻 (元)'
axes[1].set_ylabel('總營收貢獻 (元)')
# 將 x 軸刻度旋轉 45
axes[1].tick_params(axis='x',rotation=45)


#為長條圖加上資料標籤
for i,v in enumerate (rev_data['line_revenue']) :
    y_pos=v+1
    axes[1].text(i,y_pos,f'{v:.0f}',ha='center',va='bottom',fontsize=10)

# 5. 自動調整子圖之間的間距，並顯示
plt.tight_layout()
plt.show()