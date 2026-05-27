import pandas as pd
orders=pd.read_csv('data/raw/orders.csv')
order_items=pd.read_csv('data/raw/order_items.csv')
try:
    assert orders['order_id'].is_unique,'錯誤order_id有重覆'
    # assert order_items['order_id'].is_unique,'錯誤order_id有重覆'
except AssertionError as e:
    print(f'有發生錯誤:{e}')