import pandas as pd
sessions=pd.read_csv('data/raw/sessions.csv')
## 7.將 sessions 工作表 的 device 欄位 強制轉為數值欄位,若無法轉換則填入 NaN
sessions['device']=pd.to_numeric(sessions['device'],errors='coerce')
## 8.字串清理,利用.str 存取器
## 8-1 將 sessions 的 campaign 欄位的內容 去頭尾空白,輸出為 temp1.csv
temp1 = sessions['campaign'].str.strip()
temp1.to_csv('temp1.csv')
## 8-2 將 campaign 欄位的內容 去除所有空白,輸出為 temp2.csv
temp2 = sessions['campaign'].str.replace(' ','')
temp2.to_csv('temp2.csv')
## 8-3 查詢 campaign 欄位是否有包含 retarget 的值 ,輸出為 temp3.csv
temp3 = sessions['campaign'].str.contains('retarget')
temp3.to_csv('temp3.csv')
## 8-4 查詢 符合 campaign 為 retarget 的記錄,只看 campaign 與 device　二欄位,前五筆
campaign = sessions.loc[sessions['campaign']=='retarget',['campaign','device']].head()
print(campaign)
## 8-5 檢查 campaign 欄位是否有異常的類別 利用 unique 方法
unique_campaign = sessions['campaign'].unique()
print(unique_campaign)