import matplotlib.pyplot as plt
import pandas as pd
## 利用 pyplot 繪製圖表
## 設定中文字型為 微軟正黑
plt.rcParams['font.sans-serif'] =['Microsoft JhengHei','sans-serif']
## fig 是整張圖 ax 是繪圖區 figsize=(寬,高)
fig,ax=plt.subplots(figsize=(8,5))
#利用 bar 方法設定 x標籤與y值
ax.bar(['台積電', '聯發科', '鴻海', '廣達', '中華電'],[35678, 48725, 62310, 41589, 78234])
#設定圖表標題為 '各付款方式訂單數' 字型大小為 14
ax.set_title('個人股票持股數',fontsize=30)
#設定 x 軸標籤為 付款方式
ax.set_xlabel('股票名稱',color='red',fontsize=18)
#設定 y 軸標籤為 訂單數
ax.set_ylabel('持股數',color='blue',fontsize=18)
#顯示圖表
plt.show()