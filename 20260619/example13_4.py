import pandas as pd
import numpy as np
#宣告 run_data_quality_audit 函式,並傳入 orders, order_items, sessions, events, customers 等參數
def run_data_quality_audit(orders, order_items, sessions, events, customers):
    """
    執行六大自動化資料品質檢查
    輸入參數為 5 個 Pandas DataFrame：orders, order_items, sessions, events, customers
    """
    print("="*50)
    print(" 開始執行全自動資料品質健檢報告")
    print("="*50)

    # ---------------------------------------------------------
    # 檢查一：主鍵唯一性檢查 (Primary Key Uniqueness)
    # 目的：防止笛卡兒積，確保 orders 表裡的訂單 ID 都是獨一無二的。
    # ---------------------------------------------------------
    print("\n[1/6] 執行：主鍵唯一性檢查...")
    try:
        # 計算 orders 表中，order_id 欄位重複的數量
        dup_count=orders['order_id'].duplicated().sum()
        print(f'order_id重複筆數為:{dup_count}筆')

        # 顯示重覆數量
        if dup_count > 0 :
            dup_count1 = orders[orders['order_id'].duplicated(keep=False)] 

        print()
        # 如果有重覆,把所有重複的資料列全部抓出來 keep=False
            # 排序後印出前 10 筆
        print('重覆的 order_id 記錄如下:')
        print(dup_count1)

    except Exception as e:
        print('檢查失敗')
          

    # ---------------------------------------------------------
    # 檢查二：參照完整性（Referential Integrity）
    # 目的：檢查子表 (order_items) 裡面的訂單，是不是都能在母表 (orders) 
    # ---------------------------------------------------------

    print("\n[2/6] 執行：參照完整性檢查...")
    try:
        # 找出 order_items 裡面的 order_id，有哪些「不存在」(~) 於 orders 的 order_id 清單中
        orphan_items=orders[~order_items['order_id'].isin(orders['order_id'])]

        # 顯示孤兒數量
        print(f'孤兒筆數為{len(orphan_items)}筆') 

        print()

        # 顯示孤兒項目
        print(f'孤兒筆數為:\n{orphan_items}')
        
        
    except Exception as e:
        print(f'檢查失敗:{e}')

    # ---------------------------------------------------------
    # 檢查三：值域範圍檢查 (Value Range Check)
    # 目的：檢查數值型欄位是否符合常理（例如：價格不能是負的）。
    # ---------------------------------------------------------
    print("\n[3/6] 執行：值域範圍檢查...")
    try:
        # #檢查所有單價,折扣,數量 值是否合乎常理
        # assert (order_items['unit_price']>=0).all(),'發現負數的 unit_price'
        # assert (order_items['discount_rate']>=0).all(),'發現負數的 discount_rate'
        # assert (order_items['discount_rate']<=1).all(),'發現超過 100% 的 discount_rate'
        # assert (order_items['quantity']>0).all(),'發現數量為0 或是 負的'
        # 建立一個字典，用來收集所有的錯誤報告
        # 格式為 { '錯誤類型名稱': 異常的 DataFrame }
        error_reports = {}

        # 1. 檢查 unit_price (反向思考：找出小於 0 的壞資料)
        bad_price=order_items['unit_price'] < 0
        if bad_price.any() :
            error_reports['發現負數的 unit_price'] = order_items[bad_price]
           
        # 2. 檢查 discount_rate (找出小於 0 或 大於 1 的壞資料)
        # 注意：在 Pandas 中，多重條件要用 () 括起來，並使用 | (OR) 運算符
        bad_discount = (order_items['discount_rate'] < 0) | (order_items['discount_rate'] > 1)
        if bad_discount.any() :
            error_reports['發現異常的 discount_rate'] = order_items[bad_discount]

        # 3. 檢查 quantity (找出小於等於 0 的壞資料)
        bad_quantity = order_items['quantity'] <= 0
        if bad_quantity.any() :
            error_reports['發現數量異常'] = order_items[bad_quantity]
        # 如果 error_reports 裡面沒有任何東西 (長度為0)，代表全部過關 否則 顯示錯誤
        if not error_reports:
            print('檢查通過')
        else:
            print(f'檢查失敗,共發現{len(error_reports)}種異常')
            # 遍歷字典，把每一種錯誤的明細印出來
            for key,value in error_reports.items() :
                print(f'{key}共{len(value)}筆異常')
                print(value)

    except Exception as e:
        print(f'檢查失敗:{e}')

    # ---------------------------------------------------------
    # 檢查四：空值率報告 (Null Value Report)
    # 目的：掃描所有資料表，揪出哪些欄位有遺失值，並計算遺失比例。
    # ---------------------------------------------------------
    print("\n[4/6] 執行：空值率報告掃描...")
    try:
        # 定義一個專門產生空值報告的小函式 null_report,傳入 df,table_name
        def test(): 
            # 取得該資料表的總列數
            total = None

            # 計算每個欄位的空值總數
            null_counts = None
            print(f'===table_name 資料表 空值率==')
            print(null_counts)
            print()
            print("="*30)
            

            # 算出空值率的百分比，並四捨五入到小數第二位
            null_pct = (null_counts / total * 100).round(2) 
            
            # 把結果組成一個漂亮的新 DataFrame,欄位名稱分別為 'table','column','null_count','null_pct'
            


            # 過濾掉那些完全沒有空值 (null_count == 0) 的欄位，只回傳有問題的
            return None

        # 將手上的五張表打包成字典，方便用迴圈一次處理
        
        # tables = {
        #     "sessions": sessions, 
        #     "events": events, 
        #     "orders": orders, 
        #     "order_items": order_items, 
        #     "customers": customers
        # }
        
        # 使用 List Comprehension 對每張表呼叫 null_report，然後用 pd.concat 垂直合併起來
        full_report = None
        
        ## 如果 full_report > 0 印出空值結果 否則顯示 無空值
        
            
    except Exception as e:
         print(f"  檢查失敗: {e}")
          
    

    # ---------------------------------------------------------
    # 檢查五：類別有效性檢查 (Categorical Validity)
    # 目的：檢查字串欄位是否只包含「官方規定的選項」，防止拼字錯誤（如把 purchase 打成 purchas）。
    # ---------------------------------------------------------
    print("\n[5/6] 執行：類別有效性檢查...")
    try:
        # 定義欄位名稱集合 (Set)
        valid_event_types = None
        
        # 把資料表裡實際出現的事件名稱抽出來，去掉空值後轉成集合
        actual_types = None 
        
        # 利用集合的「差集(-)」運算：如果實際資料裡有官方沒規定的東西，就會被抓出來
        invalid = None 
        
        # 若有無效的資料顯示警告文字 否則 顯示 全數通過
        
    except Exception as e:
         print(f" 檢查失敗: {e}")
        
        

    # ---------------------------------------------------------
    # 檢查六：跨欄位邏輯檢查 (Cross-field Logical Check)
    # 目的：揪出「商業邏輯上的矛盾」（例如：退貨的訂單，不應該還有營業額進帳）。
    # ---------------------------------------------------------
    print("\n[6/6] 執行：跨欄位邏輯檢查...")
    try:
        # 第一步：把 orders 表，和「產生了營收(revenue > 0)」的 events 表結合在一起
        # 使用 inner merge，只保留兩邊都有的 order_id
        
        
        # 第二步：從剛剛合併出來「有營收」的資料中，找出訂單狀態竟然是 "cancelled" (已取消) 的
        
        
        #計算幽靈訂單數
        count = None

        #印出幽靈訂單數
        print(f" 已取消卻仍紀錄有營收的幽靈訂單數：count") 
        if count > 0:
            print(" 警告：發現商業邏輯矛盾的資料，請通知資料工程師查修！")
            # print(cancelled_with_rev[['order_id','status','revenue']])
    except Exception as e:
         print(f"   檢查失敗: {e}")

    print("\n" + "="*50)
    print(" 全自動健檢執行完畢！ ")
    print("="*50)


# 讀取了五個 DataFrame (orders, order_items, sessions, events, customers)
orders=pd.read_csv('data/raw/orders.csv')

order_items=pd.read_csv('data/raw/order_items.csv')
sessions=pd.read_csv('data/raw/sessions.csv')
events=pd.read_csv('data/raw/events.csv')
customers=pd.read_csv('data/raw/customers.csv')
sessions['campaign']=sessions['campaign'].str.replace(' ','').replace('none',np.nan)
run_data_quality_audit(orders, order_items, sessions, events, customers)