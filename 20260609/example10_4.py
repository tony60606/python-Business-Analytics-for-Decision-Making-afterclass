import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from common import factor
#設定中文字型
plt.rcParams['font.family']='Microsoft JhengHei'
facts=factor()
#將 facts 資料表依照「訂單日期 (order_date)」分群，並將「單項營收 (line_revenue)」加總。
#日期保持為一般欄位。
daily=facts.groupby(facts['order_date'].dt.date,as_index=False)['line_revenue'].sum()

#欄位重新命名為 'date' (日期) 與 'revenue' (營收)
daily.columns=['date','revenue']
# 建立畫布與座標軸：設定圖表大小為寬 12 英吋、高 5 英吋
fig,ax=plt.subplots(figsize=(12,5))
# 繪製第一條線（日營收）：X 軸日期、Y 軸營收 線寬 0.8 alpha=0.6 (半透明)，標籤設定為 '日營收'
ax.plot(daily['date'],daily['revenue'],linewidth=0.8,alpha=0.6,label='日營收')
#計算 7 日移動平均 (MA7),min_periods=1資料不足 7 天也能算出平均，避免產生 NaN (空值)
daily['MA7']=daily['revenue'].rolling(7,min_periods=1).mean()
#繪製第二條線（7日移動平均）：線寬2，顏色設為紅色，標籤為 '7日移動平均'
ax.plot(daily['date'],daily['MA7'],linewidth=2,color='red',label='7日移動平均')

#設定標題為 每日營收趨勢(含 MA7)
ax.set_title('每日營收趨勢(含MA7)')

#設定 x 標籤 日期
ax.set_xlabel('日期')

#設定 y 標籤 營收(TWD)
ax.set_ylabel('營收(TWD)')
#產生圖例
ax.legend()
#繪製圖表
plt.show()