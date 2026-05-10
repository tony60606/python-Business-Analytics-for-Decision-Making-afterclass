#載入pandas套件
import pandas as pd
#轉換CSV
orders = pd.read_csv("data/raw/orders.csv")
order_items = pd.read_csv("data/raw/order_items.csv")
sessions = pd.read_csv("data/raw/sessions.csv")
events = pd.read_csv("data/raw/events.csv")
#計算revenue
#合併報表
a_merge =  pd.merge(order_items,orders,on="order_id",how="left")
#篩選 => status為completed的資料 ，並複製存另一個記憶體(不覆蓋原檔)
a_completed = a_merge[a_merge["status"]=="completed"].copy()
#轉換成CSV
a_completed.to_csv("a_completed.csv")
#新增欄位
a_completed['a_revenue'] = a_completed["quantity"]*a_completed["unit_price"]*(1-a_completed['discount_rate'])
a_completed.to_csv('a_copmpleted_2.csv')
total_a_revenue = a_completed["a_revenue"].sum()
print(total_a_revenue)

#session數-有purchase事件
b_merge = pd.merge(events,sessions,on="session_id",how="left")
b_purchase = b_merge[b_merge["event_type"]=="purchase"].copy()
b_purchase.to_csv('b_purchase.csv')
count_b_purchase = b_purchase["session_id"].count()
#總session數
count_b_total = sessions["session_id"].count()
CVR = count_b_purchase / count_b_total
print(CVR)

#AOV
count_a_completed = a_completed["order_id"].nunique()
AOV = total_a_revenue / count_a_completed
print(AOV)

#RefundRate
count_order_refunded = orders[orders["status"]=="refunded"]["order_id"].count()
count_order_total = orders['order_id'].count()
RefundRate = count_order_refunded / count_order_total
print(RefundRate)