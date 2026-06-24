import numpy as np # 匯入 numpy
from common import factor
facts=factor()
x_bar = facts["line_revenue"].mean() # 算出「樣本平均值」：也就是目前手中這些訂單的平均營收。
print(f'{x_bar=:.2f}')
s = facts["line_revenue"].std() # 算出「樣本標準差」：用來衡量這些訂單金額的波動程度（大家都買差不多金額，還是有人買 10 元有人買 1 萬元？）。
print(f'{s=:.2f}')
n = len(facts) # 樣本量
print(f'{n=}')
se = s / np.sqrt(n) # 標準誤
print(f'{se=:.2f}')
z_star = 1.96 # 95% 信賴區間的 z 臨界值
ci_lower = x_bar - z_star * se # 信賴區間下界
ci_upper = x_bar + z_star * se # 信賴區間上界
print(f"樣本平均營收：{x_bar:.1f} 元") # 印出點估計
print(f"95% 信賴區間：[{ci_lower:.1f}, {ci_upper:.1f}]") # 印出區間估計