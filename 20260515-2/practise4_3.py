import pandas as pd
import numpy as np
sessions=pd.read_csv('data/raw/sessions.csv')
mobile=pd.read_csv('data/raw/Automobile.csv')

def column_health_report(df,table_name=''):
    report=pd.DataFrame({
        '欄位名稱' : df.columns ,
        '資料型態' : df.dtypes.values ,
        '非空值' : df.notna().sum().values ,
        '空值' : df.isna().sum().values ,
        '缺失率' : (df.isna().sum()/len(df)*100).round(2).values ,
        '非重複值' : df.nunique().values
    })
    ##標註風險等級
    report['風險']='低'
    report.loc[report['缺失率']>10,'風險']='中'
    report.loc[report['缺失率']>30,'風險']='高'
    print(f'\n=={table_name} 欄位健康報告 =====')
    print(report.to_string(index=False))
    report.to_csv('health.csv')
    return report
health=column_health_report(sessions,'sessions')
print("="*30)
# 1.查看 mobile 工作表的欄位名稱
print(mobile.columns)
# 2.將欄位名稱有 -(減號) 全改為 _(底線) 
mobile.columns = mobile.columns.str.replace('-','_')
# 3.查看 mobile 工作表的欄位名稱
print(mobile.columns)
print("="*30)

# 4.將 mobile 工作表的 ? 全部轉為 NaN 值
mobile = mobile.replace('?',np.nan)
# 5.將 mobile 輸出為 mobile1.csv
mobile.to_csv('mobile1.csv')
# 6.查看資料結構
print(mobile.info())
# 7.將 price,horsepower,peak_rpm 更為類型為int
mobile[['price','horsepower','peak_rpm']] = mobile[['price','horsepower','peak_rpm']].astype('Int64')
# 8.查看資料結構
print(mobile.info())
print("===========更改結構後--=====================")

# 9.呼叫 column_health_report 函式
column_health_report(mobile,table_name='資料報表')