import pandas as pd
orders=pd.read_csv('data/raw/orders.csv')
def lesson02(orders) -> None:
    import numpy as np
    # print("Lesson 2: NumPy + pandas basics")
    # NumPy 向量化⽰範
    arr = np.array([1, 3, 5, 7, 9])
    # print("Vectorized result:", arr * 2 + 1)
    # 每個元素乘 2 再加 1 → [3, 7, 11, 15, 19]
    # 重點：不需要寫迴圈
    # pandas 條件篩選 + 欄位選取
    # 這⼀⾏等於 SQL:
    # SELECT order_id, customer_id FROM orders WHERE status='completed' LIMIT 5
    print(orders.loc[
    orders["status"] == "completed", # 條件：狀態為 completed
    ["order_id", "customer_id",'status'] # 欄位：只取這三欄
    ].head(5)) # 只看前 5 筆
    print('='*30)
    #篩選出 20列到300列間 符合 status == refunded, 只取這兩欄 order_id, status ,只看前三筆
    print(orders.iloc[20:300].loc[orders['status']=='refunded',['order_id','status']].head(3))

lesson02(orders)