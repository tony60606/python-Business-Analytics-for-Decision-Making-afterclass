import pandas as pd

## 1.建立 df_sales DataFrame 銷售表
df_sales = pd.DataFrame(
    {
        "分店": ["台北店", "台北店", "台中店", "台中店"],
        "商品": ["蘋果", "香蕉", "蘋果", "香蕉"],
        "銷售量": [100, 150, 80, 120],
    }
)
# 轉 df_sales 為 df_sales.csv
df_sales.to_csv("df_sales.csv")
## 2.建立 df_inventory DataFrame 庫存表
df_inventory = pd.DataFrame(
    {
        "分店": ["台北店", "台北店", "台中店", "台中店"],
        "商品": ["蘋果", "香蕉", "蘋果", "香蕉"],
        "庫存量": [500, 300, 200, 450],
    }
)
# 轉 df_right為right.csv
df_inventory.to_csv("df_inventory.csv")

# 使用列表 ["分店", "商品"] 作為多欄位合併鍵
merged_df=df_sales.merge(df_inventory,on=['分店','商品'])
print('merged_df=',merged_df,sep='\n')


