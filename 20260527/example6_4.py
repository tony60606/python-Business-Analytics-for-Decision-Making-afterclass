import pandas as pd
pd.set_option('display.max.columns',None)
orders=pd.read_csv('data/raw/orders.csv')
customers=pd.read_csv('data/raw/customers.csv')
order_items=pd.read_csv('data/raw/order_items.csv')
products=pd.read_csv('data/raw/products.csv')
print(f'orders 外觀:{orders.shape}')
print(f'customers 外觀:{customers.shape}')
print(f'order_items 外觀:{order_items.shape}')
print(f'products 外觀:{products.shape}')
print('======查看各資料表結構=========')
database=[orders,customers,order_items,products]
for x in database:
    print(x.info())
    print("="*30)

##示範A 最常用的二表合併(orders+customers)--begin

## 將顧客屬性 segment(顧客等級),city(地區),acquisition_channel(獲取來源) 合併到訂單
orders_with_customers=orders.merge(customers[['customer_id','segment','city','acquisition_channel']],on="customer_id")
##印出合併好的資料表,只看 order_id,customer_id,city,segment 等欄位,只看前五筆
print(orders_with_customers[['order_id','customer_id','city','segment']].head())

## 檢查合併好的資料表 orders_with_customers 與 orders 資料表的長度是否一致
print(f'order的筆數{len(orders)}筆\n'
      f'orders_with_customers的筆數{len(orders_with_customers)}筆\n'
      f'兩者筆數是否相同{len(orders)==len(orders_with_customers)}')

##示範A 最常用的二表合併(orders+customers)--end

##示範B 三表串接(orders+order_items+products)--begin
##從 品項層級算出每筆訂單,每個品項的營收,並帶出產品類別
## 主表 order_items 合併 orders('order_id','customer_id','order_date','status','payment_type')
## 與 products('product_id','category')
items_enriched=(order_items.merge(orders[['order_id','customer_id','order_date','status','payment_type']],on='order_id')).merge(products[['product_id','category']],on='product_id')
## 計算每個品項的營收
items_enriched['line_revenue']=(items_enriched['quantity']*items_enriched['unit_price']*(1-items_enriched['discount_rate'])).round(2)
(items_enriched[['order_id','customer_id','product_id','order_date','quantity','unit_price','discount_rate','line_revenue']]).sort_values(by='line_revenue',ascending=False,ignore_index=True).to_csv('temp3.csv')
##示範B 三表串接(orders+order_items+products)--end
