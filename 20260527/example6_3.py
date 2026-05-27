import pandas as pd
## 1.建立 df_left DataFrame
df_left=pd.DataFrame({
    '員工編號':[101,102,103,104,105],
    '員工姓名':['小明','小華','小強','小玲','小志']
})
#轉 df_left為left.csv
df_left.to_csv('left.csv')
## 2.建立 df_right DataFrame
df_right=pd.DataFrame({
    '員工姓名':['小明', '小華', '小強', '大牛', '美美'],
    '門禁卡號':['CARD_A', 'CARD_B', 'CARD_C', 'CARD_D', 'CARD_E']
})
#轉 df_right為right.csv
df_right.to_csv('right.csv')

## inner 內部 交集 預設
m1=df_left.merge(df_right,on='員工姓名',how='inner')
print("m1=",m1,sep='\n')
print('='*30)
## left 左外部連接 左邊一個不能少,右表沒對上就補 NaN
m2=df_left.merge(df_right,on='員工姓名',how='left')
print("m2=",m2,sep='\n')

print('='*30)
## right 右外部連接 右邊一個不能少,左表沒對上就補 NaN
m3=df_left.merge(df_right,on='員工姓名',how='right')
print("m3=",m3,sep='\n')

print('='*30)
## outer 全外部連接 聯集 二邊一個不能少,沒對上各自補 NaN
m4=df_left.merge(df_right,on='員工姓名',how='outer')
print("m4=",m4,sep='\n')

print('='*30)
## left_anti 只留下存在於左表,但右表找不到的人,即沒有申請門禁卡的人
m5=df_left.merge(df_right,on='員工姓名',how='left_anti')
print("m5=",m5,sep='\n')
