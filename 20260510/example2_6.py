import pandas as pd
pd.set_option("display.max.columns", None)
# pd.set_option('display.max_rows', None)
orders = pd.read_csv("data/raw/orders.csv")
# and 邏輯運算子 & 位元運算子
print(10>8 and 10<8) # False
print(10>8 & 10<8) # False
print(5 and 8) # 
print(9 and 0) # 
print(0 and 8) # 
print(5 & 8) # 
print(9 & 0) # 
print(0 & 8) # 
print("="*30)
# 1.⽤布林條件選列，指定欄位名稱選欄
completed = orders.loc[orders["status"] == "completed", ["order_id","customer_id"]]
# 等同於 SQL: SELECT order_id, customer_id FROM orders WHERE status = 'completed'
# 1_1.查看 status 為 refuned ,欄位為 order_id 與 status 並指定為 refuned 變數
refunded = orders.loc[orders['status']=='refunded',['order_id','status']]
print("="*30)
# 2：選前 5 列的指定欄位
df1=orders.loc[0:4, ["order_id", "status"]]
print(df1)
print(orders[['order_id','status']].head())
# 注意：loc 的 0:4 包含第 4 列（共 5 列）
# 2_1 查看 2:4 列的 customer_id 與 payment_type 欄位
df2 = orders.loc[2:4,['customer_id','payment_type']]
# 3：複合條件
card_completed = orders.loc[
    (orders["status"] == "completed") & (orders["payment_type"] == "card"),:] # 冒號表⽰「所有欄位」
print(card_completed)

# ===== iloc 範例 =====
# 4：⽤位置選取前 5 列、前 3 欄
print(orders.iloc[0:5, 0:3])
# 注意：iloc 的 0:5 不含第 5 列（共 5 列）
print('='*30)
# 4_1 查看 4-9 列 1-3 欄
print(orders.iloc[4:9,1:3])
# 5：選取特定列與欄
print(orders.iloc[[0, 10, 100], [0, 2, 4]])
# 第 0、10、100 列的第 0、2、4 欄