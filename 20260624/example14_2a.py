import pandas as pd
import numpy as np

# 1. 準備測試資料
df_users = pd.DataFrame({'id': [1, 2, np.nan], 'name': ['Alice', 'Bob', 'Charlie']})
df_orders = pd.DataFrame({'order_id': [101, np.nan], 'price': [100, 200]})

# 把這兩張表收納到一個字典（Dictionary）裡
tables = {
    "用戶表": df_users,
    "訂單表": df_orders
}

# 2. 定義 null_report 函式（計算每張表有幾個空值）
def null_report(df, table_name):
    # 計算每欄的缺失值總數
    null_counts = df.isnull().sum()
    
    # 建立一個簡單的報告 DataFrame
    report = pd.DataFrame({
        '資料表': table_name,
        '欄位名稱': null_counts.index,
        '缺失值數量': null_counts.values
    })
    return report

# 3. 執行核心程式碼
full_report = pd.concat([null_report(df, name) for name, df in tables.items()],ignore_index=True)
   

# 4. 列印結果
print(full_report)