import pandas as pd
pd.set_option('display.max.columns',None)
## 1.建立 df_left DataFrame
df_left=pd.DataFrame({
    '員工編號':[101,102,103,104,105],
    '員工姓名':['小明','小華','小強','小玲','小志']
})
#轉 df_left為left.csv
df_left.to_csv('left.csv')
## 2.建立 df_right DataFrame
df_right=pd.DataFrame({
    '持卡人姓名':['小明', '小華', '小強', '大牛', '美美'],
    '門禁卡號':['CARD_A', 'CARD_B', 'CARD_C', 'CARD_D', 'CARD_E']
})
#轉 df_right為right.csv
df_right.to_csv('right.csv')

# m1=pd.merge(df_left,df_right,on='員工姓名',how='inner') #KeyError
m1=pd.merge(df_left,df_right,left_on='員工姓名',right_on='持卡人姓名',how='inner').drop(columns=['持卡人姓名'])
print(m1)
print(m1)