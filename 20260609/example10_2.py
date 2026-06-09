import matplotlib.pyplot as plt
import pandas as pd
from common import factor
## 設定中文字型為 微軟正黑
plt.rcParams['font.family'] = 'Microsoft JhengHei'
customers=pd.read_csv('data/raw/customers.csv')
fact=factor()
facts=fact.merge(customers,on='customer_id',how='left')
#印出 line_revenue 欄位摘要
print(facts[['line_revenue']])
#印出分組-客群來源的平均營收,遞減排序
print(facts.groupby('acquisition_channel')['line_revenue'].mean().sort_values(ascending=False))
print("="*30)


# payment_counts變數 依 payment_type 欄位分類 計數 order_id欄位 依 card,atm,cod,wallet順序,空值補0 ,型態設為整數
payment_counts = facts.groupby('payment_type')['order_id'].count().reindex(['card','atm','cod','wallet']).fillna(0).astype(int)
print("="*30)
print('payment_counts')
## 利用 pyplot 繪製圖表

## fig 是整張圖 ax 是繪圖區 figsize=(寬,高)
fig,ax=plt.subplots(figsize=(8,5))
#利用 bar 方法設定 x標籤(payment_counts.index)與y值(payment_counts.values)
ax.bar(payment_counts.index.tolist(),payment_counts.values.tolist())

#設定圖表標題為 '各付款方式訂單數' 字型大小為 14
ax.set_title('各付款方式訂單數',fontsize=18)

#設定 x 軸標籤為 付款方式
ax.set_xlabel('付款方式',fontsize=14)

#設定 y 軸標籤為 訂單數
ax.set_ylabel('訂單數',fontsize=14)

#為資料加上資料標籤
for i,v in enumerate(payment_counts.values.tolist()) :
    ax.text(i,v+max(1,int(v*0.01)),f'{v:,}',ha='center')

#儲存圖表名稱為payment.png
plt.savefig('payment.png')

#顯示圖表
plt.show()
