import pandas as pd
## 唯一性
# --- 1. 建立資料 左表
print("左表：order order_id 1001 出現了 2 次")
orders = pd.DataFrame({
    'order_id': [1001, 1002],
    'amount': [500, 500]
})
print(orders, "\n")

# --- 2. 建立資料 右表
print("右表：order_items order_id 1001 出現了 3 次")
order_items = pd.DataFrame({
    'order_id': [1001, 1001, 1001],
    'product': ['A', 'B', 'C']
})
print(order_items, "\n")

# --- 2. 執行一般的 Merge 
print("合併結果：笛卡兒積大爆炸")

#合併 order_items how='inner'
merged=orders.merge(order_items,on='order_id')
# 驗證營收被高估
print(f'錯誤的總營收被算成了:\n{merged['amount'].sum()}')


try:
    merged_2=orders.merge(order_items,on='order_id',how='inner',validate='1:m')
    #validate='1:m' # 強制規定：左表的主鍵必須是唯一的 (1)，右表可以有多個 (m)

except Exception as e:
    print('成功攔截錯誤')
    print(f'merge error:{e}')