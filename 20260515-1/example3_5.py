import pandas as pd
# 0.設定欄位為全部顯示
pd.set_option('display.max.columns',None)
# 1.讀入 sessions.csv 檔 指定給 sessions 變數
sessions=pd.read_csv("data/raw/sessions.csv")
# 2.將前 10 筆記錄 轉為 名稱為 temp1.csv--看長相
temp1 =sessions.head(10)
temp1.to_csv("temp1.csv")
# 3.將後 10 筆記錄 轉為 名稱為 temp2.csv
temp2 =sessions.tail(10)
temp2.to_csv("temp2.csv")

# 4.查看 DataFrame的資訊--看欄位結構
print(sessions.info())
print("="*30)

# 5.查看 DataFrame的摘要(文字欄位)--看數值分布
print(sessions.describe())
print("="*30)
# 5-1.讀入order_items.csv 指定給 oitems變數--看數值分布
oitems = pd.read_csv('data/raw/order_items.csv')
# 5-2.查看 DataFrame的摘要(數值欄位)--看數值分布
print(oitems.describe())
print("="*30)
'''
偏態（Skewness）：平均數與中位數差距⼤，且分布不對稱。
離群值（Outliers）：極端值遠離其他數據點，可能是錯誤或特殊情況。
集中趨勢（Central Tendency）：數據集中在某個值附近，平均數、中位數、眾數是衡量集中趨勢的指標。
平均數（Mean）：所有數值的總和除以數量，受極端值影響⼤。
中位數（Median）：將數值排序後的中間值，對偏態分布更穩健。
眾數（Mode）：出現頻率最⾼的值，適⽤於類別型資料。
'''

# 6-1.查看 campaign 欄位的類別分布
campaign = sessions['campaign'].value_counts()
print(campaign)
print("="*30)
# 6-2.查看 device 欄位的類別分布,以百分比方式顯式
device = (sessions['device'].value_counts(normalize=True)*100).map(lambda x:f'{x:.2f}%')
print(device)