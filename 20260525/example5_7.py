import pandas as pd
from common import factor
import numpy as np
facts=factor()
daily_kpi=(

# 第 1 步：按⽇期分組
# facts["order_date"] 是 datetime 型別（如 2024-01-15 08:30:00）
# .dt.date 去掉時分秒，只保留⽇期（2024-01-15），再依此分組
facts.groupby(facts['order_date'].dt.date)


#第 2 步：對每個⽇期分組同時計算兩個指標
# revenue = 當⽇所有品項⾦額加總（sum）
# order_count = 當⽇訂單筆數（count）
.agg(
    revenue = ('line_revenue','sum'),
    order_count = ('order_id','count')
    )


# 第 3 步：新增 aov 欄位（平均訂單⾦額）
# .assign() 不改動既有欄位，只新增欄位
# lambda x 中的 x 就是「前兩步的結果 DataFrame」
.assign(aov=lambda x : x['revenue'] / x['order_count']).round(2)

)
#針對aov排高排到底
daily_kpi=daily_kpi.sort_values(by=['aov'],ascending=False,ignore_index=True)
daily_kpi.to_csv("temp7.csv")