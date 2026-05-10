import pandas as pd
#1.讀取"data/raw/orders.csv"檔並指定給orders
orders = pd.read_csv('data/raw/orders.csv')
#2.基本檢視
#2_1.查看orders資料型態
print(orders.dtypes)
#2_2.查看orders的形狀
print(orders.shape)
#2_3.查看orders的欄位名稱
print(orders.columns)
#2_4.查看orders的列索引名稱
print(orders.index)
#3.取出 status 欄位資料,並指定給 status_col 變數
status_col = orders['status']
#4.查看 status_col 的資料型態
print(status_col.dtypes)
#5.印出 status_col 
print(status_col)
#6.取出 order_id,customer_id,status 三個欄位,並指定給 subset 變數
subset = orders[['order_id','customer_id','status']]
#7.查看 subset 資料型態
print(subset.dtypes)
#8.印出 subset
print(subset)